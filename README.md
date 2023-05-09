# Accuracy is not all you need: Fairness Metrics in Danish NER

This repository contains the code used to produce the results in the paper "Accuracy is Not All You Need" by Lassen et al. (forthcoming). It builds upon the work done in the code repository [Danish-NER-Bias](https://github.com/centre-for-humanities-computing/Danish-NER-bias).

**Add sentence about the purpose of the project** (preferably closely linked to the abstract)

For instructions on how to reproduce the results, please refer to the [Pipeline]() section.

## Project Structure 
The repository has the following structure: 
```

```

### Danish Language Models 
The following models are evaluated:
* [ScandiNER](https://huggingface.co/saattrupdan/nbailab-base-ner-scandi)
* [DaCy models](https://github.com/centre-for-humanities-computing/DaCy)
    * DaCY large (da_dacy_large_trf-0.1.0)
    * DaCy medium (da_dacy_medium_trf-0.1.0)
    * DaCY small (da_dacy_small_trf-0.1.0)
* [DaNLP BERT](https://danlp-alexandra.readthedocs.io/en/stable/docs/tasks/ner.html#bert)
* [Flair](https://github.com/flairNLP/flair)
* [Spacy models](https://spacy.io/models/da)
    * SpaCy large (da_core_news_lg-3.4.0)
    * SpaCy medium (da_core_news_md-3.4.0)
    * SpaCy small (da_core_news_sm-3.4.0)
* [Polyglot](https://polyglot.readthedocs.io/en/latest/NamedEntityRecognition.html)

## Pipeline 

## Acknowledgements
The name augmentation was performed using [augmenty](https://kennethenevoldsen.github.io/augmenty/). 