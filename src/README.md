The src folder contains the following: 

| <div style="width:120px"></div>| Description |
|---------|:-----------|
| ```evaluate_fns``` | scripts used in evaluate pipeline in all fairness_XX.py scripts. Contains scripts to extract metrics TP/FP/FN/PRECISION/RECALL/F1 and to prepare data augmentation |
| ```process_names``` | scripts used to preprocess names before name augmentation e.g., filtering overlaps between majority and minority name lists|
| ```fairness_XX.py```  | Scripts for evaluating models. All models except polyglot and flair can be run with ```fairness_models.py``` (*NB. DaCy has dependency conflicts with the rest, and has to be run with seperate requirements. See ```run-dacy.sh```*) 
| ```stats-names.py``` | Get count of all first and last names used in name augmentation after filtering. Divided into gender and majority/minority |