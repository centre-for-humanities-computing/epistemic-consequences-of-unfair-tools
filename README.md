# Epistemic consequences of unfair tools

This repository contains the code used to produce the results in the paper ["Epistemic consequences of unfair tools" by Lassen et al. (2024)](https://doi.org/10.1093/llc/fqad091). It builds upon earlier work done in [Lassen et al. (2023)](10.18653/v1/2023.latechclfl-1.13) (for which see also the following repo: [Danish-NER-Bias](https://github.com/centre-for-humanities-computing/Danish-NER-bias)).

The project examines representational biases in Danish language models (see [list](https://github.com/centre-for-humanities-computing/epistemic-consequences-of-unfair-tools#danish-language-models)) used for Named Entity Recognition (NER) through the lens of intersectionality.

The experimental pipeline presented in this repository investigates differences in performance scores across all known Named Entity Recognition (NER) frameworks. This is achieved by applying a data augmentation technique, namely augmenting PERSON entities in the [DaNe](https://aclanthology.org/2020.lrec-1.565/) test set on gender-divided name lists for both majority and minority names. 

In the paper, these results are further analyzed by utilising fairness measures from the field of algorithmic fairness. The results show that only the models ScandiNER and DaCy large are compliant with the fairness measures in question.

For instructions on how to reproduce the results, please refer to the [Pipeline](https://github.com/centre-for-humanities-computing/epistemic-consequences-of-unfair-tools#pipeline) section.

## Project Structure 
The repository has the following directory structure:
| <div style="width:120px"></div>| Description |
|---------|:-----------|
| ```name_lists``` | Contains (raw) name lists used for data augmentation|
| ```requirements``` | Requirements file for all models, separate files for **Polyglot** and **DaCy** |
| ```results``` | Results from all model runs saved as CSV files|
| ```src```  | Scripts for extracting metrics for all models (```fairness_XX.py```). Also has helper modules for preprocessing name lists (```process_names```) and augmenting names + extracting metrics  (```evaluate_fns```).|
| ```tables``` | CSV files containing tables of all models with aggregated metrics (A: TP/FP/FN, B: Precision/Recall/F1) |
| ```results.md``` | Rmarkdown for producing tables in the paper |
| ```run-models.sh``` | Installs virtual environment and necessary requirements to run **SpaCy**, **DaNLP BERT**, **Flair** and **ScandiNER** models|
| ```run-dacy.sh``` | Installs virtual environment and necessary requirements to run **DaCy** models|
| ```run-polyglot.sh``` | Installs virtual environment and necessary requirements to run **Polyglot** model|

### Danish Language Models 
The following models are evaluated:
* [ScandiNER](https://huggingface.co/saattrupdan/nbailab-base-ner-scandi)
* [DaCy models](https://github.com/centre-for-humanities-computing/DaCy)
    * DaCy large (da_dacy_large_trf-0.1.0)
    * DaCy medium (da_dacy_medium_trf-0.1.0)
    * DaCy small (da_dacy_small_trf-0.1.0)
* [DaNLP BERT](https://danlp-alexandra.readthedocs.io/en/stable/docs/tasks/ner.html#bert)
* [Flair](https://github.com/flairNLP/flair)
* [Spacy models](https://spacy.io/models/da)
    * SpaCy large (da_core_news_lg-3.4.0)
    * SpaCy medium (da_core_news_md-3.4.0)
    * SpaCy small (da_core_news_sm-3.4.0)
* [Polyglot](https://polyglot.readthedocs.io/en/latest/NamedEntityRecognition.html)

## Pipeline 
The pipeline has been built on Ubuntu ([UCloud](https://cloud.sdu.dk/)). 

For models **SpaCy**, **DaNLP BERT**, **Flair** and **ScandiNER**, run: 
```
bash run-models.sh
```

For the three **DaCy** models, run: 
```
bash run-dacy.sh
```
The ```run-models.sh``` and ```run-dacy.sh``` scripts will install requirements and run models in environments called ```env``` and ```dacyenv```, respectively.

Finally, for **Polyglot**, run: 
```
sudo bash run-polyglot.sh
```
**NB! Notice that it is necessary to run Polyglot with sudo as the setup requires certain devtools that will not be installed otherwise. Run at own risk!**

The ```run-polyglot.sh``` script will both install devtools, packages and run the evaluation of the model in a seperately created environment called ```polyenv```. 

## Acknowledgements
The name augmentation was performed using the package [augmenty](https://kennethenevoldsen.github.io/augmenty/). 
