import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn import model_selection
from sklearn import metrics
import torch
import time
import joblib

'''
This Python file was to show the training and test process of the XGBoost models
For the baseline models, the process is similar, Hence, they are not shown repetitively
The required packages are xgboost, scikit-learn, pytorch (for checking GPU availablility)
'''
def define_hyperparameters(tuning = dict()):
    '''
    Define your own hyperparameters by editing this function
    
    return: the hyperparameter dictionary
    '''
    if len(tuning) == 0:
        # the hypyerparameters I tuned
        tuning['n_estimators'] = np.arange(100,600,100)
        tuning['gamma'] = np.arange(1,11,1)
        tuning['learning_rate'] = [0.01, 0.1, 0.2, 0.3]
        tuning['max_depth'] = np.arange(3,15,2)
        tuning['min_child_weight'] = [0,1,5,10]
        tuning['max_delta_step'] = [0,1,5,10]
        tuning['subsample'] = np.arange(0.5, 1,0.1)
        tuning['colsample_bytree'] = np.arange(0.5,1,0.1)
        tuning['lambda'] = np.arange(1,5,1)
        tuning['scale_pos_weight'] = np.arange(1,16,1)
    else:
        pass
    
    return tuning

def model_training(X_train, y_train, tuning_dict, search_type = "random", odir = None):
    '''
    nested cross validation training process, fine-tuning the hyperparameters
    X_train: the training dataset of the features
    y_train: the test dataset of the impacts
    search_type: how to conduct the cross validation.
                 two options: random, grid
                 
    return: the fine-tuned model
    '''
    
    start_time = time.time()
    gpu_status = torch.cuda.is_available()
    f2_score_list = []
    
    #setup the outer cv
    cv_outer = model_selection.StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    count = 1
    for TrainingIdx, TestingIdx in cv_outer.split(X_train,y_train):
        # split data for outer cv
        X_train_skf, X_test_skf = X_train.iloc[TrainingIdx, :], X_train.iloc[TestingIdx, :]
        y_train_skf, y_test_skf = y_train.iloc[TrainingIdx,:], y_train.iloc[TestingIdx,:]
        # set up the inner cv
        cv_inner = model_selection.StratifiedKFold(n_splits=3, shuffle=True, random_state=42)
        # define the model
        if gpu_status:
            # if gpu available, the study was trained on GPU
            clf_xgb = xgb.XGBClassifier(objective='binary:logistic',tree_method='gpu_hist',missing=1, seed=42)
            print("Using GPU to train XGBoost...")
        else:
            # if gpu not available
            # the tree_method can be change as demand
            clf_xgb = xgb.XGBClassifier(objective='binary:logistic',tree_method='hist',missing=1, seed=42)
            print("Using CPU to train XGBoost...")
        # define the F2 score
        ftwo_scorer = metrics.make_scorer(metrics.fbeta_score, beta=2)
        # define search
        if search_type == "random":
            search_model = model_selection.RandomizedSearchCV(clf_xgb, tuning_dict, scoring=ftwo_scorer, n_iter=300, cv=cv_inner,
                                               error_score='raise', verbose=2, refit=True)
        elif search_type == "grid":
            search_model = model_selection.GridSearchCV(clf_xgb, tuning_dict, scoring=ftwo_scorer, cv=cv_inner, 
                                                        error_score='raise', verbose=2, refit=True)
        else:
            raise ValueError("The search type should be either random or grid.")
        # execute search
        result = search_model.fit(X_train_skf, y_train_skf,verbose=2)
        # save the best model
        best_model = result.best_estimator_
        if odir != None:
            joblib.load(odir+"/best_model"+str(count)+".joblib",best_model)
            count += 1
        # predict on the cv test dataset
        y_pred_val = best_model.predict(X_test_skf)
        # save the f2 score
        f2_score = metrics.fbeta_score(y_test_skf, y_pred_val, average='micro', beta=2)
        f2_score_list.append(f2_score)
        
        
    
    print('F2 score: %.3f (%.3f)' % (np.mean(f2_score_list), np.std(f2_score_list)))
    end_time = time.time()
    print('The training process cost: %2.f hours'%((end_time-start_time)/3600))
    
    return best_model


def model_testing(model, X_test, y_test):
    '''
    check the performance of the fine-tuned model on the test dataset
    model: the saved fine-tuned model
    X_test: the test dataset of the features
    y_test: the test dataset of the impacts
    
    return: confusion matrix, F2 score, recall, precision on the test datasaet
    '''
    y_pred = model.predict(X_test)
    cm = metrics.confusion_matrix(X_test,y_test)
    f2_score = metrics.fbeta_score(y_test, y_pred, beta=2)
    recall = metrics.recall_score(y_test, y_pred)
    precision = metrics.precision_score(y_test, y_pred)
    
    print("The confusion matrix of the prediction is: ", cm)
    print("The F2 score of the XGBoost model on predicting drought impacts on fire in California is %.2f,\
    \nand the recall is %.2f, the precision is %.2f" %(f2_score,recall,precision))
    
    return cm, f2_score, recall, precision