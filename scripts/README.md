# Final Scripts

This directory resides Python scripts for preprocessing, modeling, and inference.

1. `preprocess.py` contains the functions to preprocess raw training data from password protected .xlsx to dataframe that is usable in `BERTopic_topic_modeling.ipynb` and `Inference.ipynb`
2. `BERTopic_topic_modeling.ipynb` contains the Python scripts to train the BERTopic model for this task.
3. `Inference.ipynb` contains the Python scripts to classify new data using the trained BERTopic model.

For training a new BERTopic model, one can use `BERTopic_topic_modeling.ipynb` as a skeleton code to train a new model.

For inference, one can run `Inference.ipynb` with different data file path and password information with respect to the new data.

In any case, one does not need to run `preprocess.py` independently. The functions in this Python file is embedding in the other 2 notebooks.