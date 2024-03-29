"""
Script containing the pipeline for extracting fairness metrics 
Used in all evaluate_XX.py scripts. 
"""

# utils
import pathlib
from typing import Optional

import dacy

# data wrangling
import pandas as pd

# model eval
import spacy

from spacy.training import Example

# import DaCyScorer
from evaluate_fns.wrapped_spacy_scorer import DaCyScorer


def filter_ents(doc, ents_to_keep):
    if ents_to_keep is None:
        return doc
    ents = [e for e in doc.ents if e.label_ in ents_to_keep]
    doc.ents = ents
    return doc


def eval_fairness_metrics(
    model_dict: dict,
    augmenters: list,
    dataset,
    outfolder: pathlib.Path,
    filename: str,
    ents_to_keep: Optional[list] = None,
):
    """
    Return CSV file of fairness metrics (FP, TP, FN & Precision/Recall) on NER task with different name augmentations.
    Fairness metrics will be calculated for all the ents you wish to include (ents_to_keep).

    Args:
        - model_dict : dictionary of models to be run
        - augmenters : list containing tuples of already loaded augmenters in the format: [(augmenter_obj, augmenter_name, n_repetitions)]
        - dataset : test dataset for model eval
        - ents_to_keep : entities to keep in the dataset for model evaluation in the format: ["PER", "LOC", "ORG", "MISC"]
        - outfolder : path where you wish to save the CSV file.
        - filename : additional unique identifier for filename: "{mdl}_{filename}_fairness.csv"

    Output:
        - .CSV file with fairness metrics in outfolder
    """

    # define output path
    outfolder.mkdir(parents=True, exist_ok=True)

    for mdl in model_dict:
        print(f"[INFO]: Scoring model '{mdl}'")

        # load model depending on model name (different pipelines) and load dataset
        if "dacy" in mdl:
            nlp = dacy.load(model_dict[mdl])
        elif "spacy" in mdl:
            nlp = spacy.load(model_dict[mdl])
            spacy.prefer_gpu()
        else:
            nlp = model_dict[mdl]

        examples = list(dataset(nlp))  # load dataset
        # filter dataset
        for e in examples:
            e.reference = filter_ents(e.reference, ents_to_keep=ents_to_keep)

        # begin evaluation
        i = 0
        scores = []

        for aug, nam, k in augmenters:
            print(f"\t Running augmenter: {nam} | Amount of times: {k}")

            # augment
            i += 1
            for n in range(k):
                # augment corpus
                augmented_corpus = [
                    e for example in examples for e in aug(nlp, example)
                ]

                # apply model to augmented corpus as a pipeline
                # notably faster than applying model to each example
                # as it can be batched
                _examples = ((e.x.text, e.y) for e in augmented_corpus)
                doc_tuples = nlp.pipe(_examples, as_tuples=True)
                augmented_corpus = [Example(x, y) for x, y in doc_tuples]

                # filter augmented corpus
                for e in augmented_corpus:
                    e.predicted = filter_ents(e.predicted, ents_to_keep=ents_to_keep)

                # initialize scorer
                scorer = DaCyScorer(nlp)

                # get scores_dict
                scores_dict, score_obj = scorer.score_spans_plus(
                    augmented_corpus, attr="ents"
                )

                # define values for dataframe
                score_vals = {
                    "model": mdl,
                    "augmenter": nam,
                    "i": i - 1,
                    "k": n,
                    "FP": score_obj.fp,
                    "TP": score_obj.tp,
                    "FN": score_obj.fn,
                    "precision": score_obj.precision,
                    "recall": score_obj.recall,
                    "F1_score": score_obj.fscore,
                    "ents_included": [ents_to_keep],
                }

                # create pandas dataframe
                scores_data = pd.DataFrame.from_records(score_vals, index=[0])

                # reorder columns
                scores_data = scores_data[
                    [
                        "ents_included",
                        "FP",
                        "TP",
                        "FN",
                        "precision",
                        "recall",
                        "F1_score",
                        "k",
                        "model",
                        "augmenter",
                        "i",
                    ]
                ]

                # append to list of dataframes
                scores.append(scores_data)

        # concatenate all dataframes (one per augmentation) into one file
        scores = pd.concat(scores)

        # save to csv
        scores.to_csv(f"{outfolder}/{mdl}_{filename}_fairness.csv")
