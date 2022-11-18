# Notes

This document is to help use this repository to reproduce the results in the paper: *Explainable Machine Learning Applications to Predict and Assess Complex Drought Impacts* and to share the fine-tuned models and the drought impact datasets.

```markdown
├── data
│		├──	data_samples
│		├──	full_datasets
├── docs
├── notebooks
├── saved_models
│		├── demo
│		├── national
│		├── state
├── scripts
```

## data

### data_samples

The features and drought impacts on fire and economy in California and Colorado, respectively, are under this directory. These data samples are also employed in a quick demonstration on Google Colab. You can use them to get familiar with the proposed explainable ML framework.

### full_datasets

The full datasets are not deposited in this folder due to their large size. Instead, an explaining document is under this directory with a publicly accessible link to a Google Drive folder.

## docs

The folder to hold this document.

## notebooks

Simple Jupyter Notebooks of implementing the scripts to train and test XGBoost models, as well as running the SHAP interpreter.

## saved_models

### demo

The two fine-tuned XGBoost models used in the demonstration are under this directory.

### national

The fine-tuned XGBoost models at the national level (ones were compared to the baselines in the paper) are under this directory.

*To-do: the model of drought impacts on agriculture needs to be saved using joblib, currently is in json.*

### state

The fine-tuned XGBoost models at the state level in California, Colorado, Kansas, New Mexico, and Texas (ones were used for thorough analyses and checking interpretability) are under this directory.

## scripts

Python files, including functions to process the datasets as machine-learning-ready and to train and test XGBoost models, are under this directory



**To be noticed: **

* Models saved by *joblib* require to be correctly loaded using the same version of libraries: *<u>xgboost==1.6.0,  joblib==1.1.0</u>* 

  And in order to reproduce the same predictions and interpretations from the saved models, I also suggested to keep these libraries in the same version following: 

  *<u>shap==0.40.0, scikit-learn==1.0.2, numpy==1.21.6</u>*

* To keep this repository concise and easily implemented, only the necessary scripts and datasets are displayed. Others, such as the exploratory analyses of features and the training and testing procedures of the baseline models, are not included. If having any questions or comments, you are welcome to have a discussion with the corresponding author.