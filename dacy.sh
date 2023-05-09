#!/bin/bash

# evaluate dacy 
python3.9 -m venv dacyenv
source ./dacyenv/bin/activate

# install requirements
echo -e "[INFO:] Installing necessary requirements in virtual environment..." # user msg

pip install -r requirements/requirements_dacy.txt

# run dacy
echo -e "[INFO:] Evaluating DaCy models ..." # user msg
python3.9 src/fairness_models.py -m dacy

# deactivate
deactivate