#!/bin/bash

# EVALUATE ALL MODELS EXCEPT POLYGLOT AND DACY MODELS 

# create and activate virtual environment
echo -e "[INFO:] Creating virtual environment 'env' and installing necessary requirements..." # user msg
python3.9 -m venv env
source ./env/bin/activate

pip install -r requirements/requirements.txt # install 

echo -e "[INFO:] Setup complete!" # user msg 

# evaluating models 
echo -e "[INFO:] Evaluating SpaCy models ..." # user msg
python3.9 src/fairness_models.py -m spacy

echo -e "[INFO:] Evaluating Scandi-NER ..." # user msg
python3.9 src/fairness_models.py -m scandi_ner

echo -e "[INFO:] Evaluating flair ..." # user msg
python3.9 src/fairness_flair.py

echo -e "[INFO:] Evaluating DaNLP BERT ..." # user msg
python3.9 src/fairness_models.py -m danlp 

# happy message ! 
echo -e "[INFO:] Evaluation of all models done! Results saved ..." # user msg

# deactivate virtual env 
deactivate
