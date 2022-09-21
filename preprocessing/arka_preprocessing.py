import pandas as pd
import os
from numpy import mean
from sklearn.datasets import make_classification
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.tree import DecisionTreeClassifier
from imblearn.pipeline import Pipeline
from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler

data=pd.read_csv(os.getcwd()+'\preprocessing\datafiles\data.csv')
data=data.drop(['Time'],axis=1)
data=data.drop(['Amount'],axis=1)
values=data.values

df=pd.DataFrame()

def get_dataframe():
    count1=0
    count0=0

    # example of evaluating a decision tree with random oversampling
    # define dataset
    #X, y = make_classification(n_samples=10000, weights=[0.99], flip_y=0)
    X=values[:,:-1]
    y=values[:,-1]
    for ys in y:
        if(ys==0):
            count0+=1
        elif(ys==1):
            count1+=1
    data=[{'0':count0,'1':count1}]
    df_count=pd.DataFrame(data)
    count1=0
    count0=0
    print(df_count)

    # define pipeline
    steps = [('over', RandomOverSampler()), ('model', DecisionTreeClassifier())]
    pipeline = Pipeline(steps=steps)
    # evaluate pipeline
    cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
    scores = cross_val_score(pipeline, X, y, scoring='f1_micro', cv=cv, n_jobs=-1)
    overscore = mean(scores)
    print('F1 Score: %.3f' % overscore)
    for ys in y:
        if(ys==0):
            count0+=1
        elif(ys==1):
            count1+=1
    dataover=[{'0':count0,'1':count1}]
    df_countover=pd.DataFrame(dataover)
    count1=0
    count0=0
    print(df_countover)



    # example of evaluating a decision tree with random undersampling
    
    # define datasetX=values[:,:-1]
    #X, y = make_classification(n_samples=10000, weights=[0.99], flip_y=0)
    X=values[:,:-1]
    y=values[:,-1]
    # define pipeline
    steps = [('under', RandomUnderSampler()), ('model', DecisionTreeClassifier())]
    pipeline = Pipeline(steps=steps)
    # evaluate pipeline
    cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
    scores = cross_val_score(pipeline, X, y, scoring='f1_micro', cv=cv, n_jobs=-1)
    underscore = mean(scores)
    print('F1 Score: %.3f' % underscore)
    for ys in y:
        if(ys==0):
            count0+=1
        elif(ys==1):
            count1+=1
    dataunder=[{'0':count0,'1':count1}]
    df_countunder=pd.DataFrame(dataunder)
    count1=0
    count0=0
    print(df_countunder)



    # example of evaluating a model with random oversampling and undersampling
    
    X=values[:,:-1]
    y=values[:,-1]
    
    #X, y = make_classification(n_samples=10000, weights=[0.99], flip_y=0)
    # define pipeline
    over = RandomOverSampler(sampling_strategy=0.1)
    under = RandomUnderSampler(sampling_strategy=0.5)
    steps = [('o', over), ('u', under), ('m', DecisionTreeClassifier())]
    pipeline = Pipeline(steps=steps)
    # evaluate pipeline
    cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
    scores = cross_val_score(pipeline, X, y, scoring='f1_micro', cv=cv, n_jobs=-1)
    combscore = mean(scores)
    print('F1 Score: %.3f' % combscore)
    for ys in y:
        if(ys==0):
            count0+=1
        elif(ys==1):
            count1+=1
    datacombo=[{'0':count0,'1':count1}]
    df_countcombo=pd.DataFrame(datacombo)
    count1=0
    count0=0
    print(df_countcombo)

    df['oversampling']=[overscore]
    df['undersampling']=[underscore]
    df['combination']=[combscore]

    print(df)

    return df,df_count,df_countover,df_countunder,df_countcombo


get_dataframe()