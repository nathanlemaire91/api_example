import pandas as pd
import subprocess
from sklearn.ensemble import HistGradientBoostingClassifier
import pickle
import datetime
import os


DF_COLUMNS = ['age', 'sex', 'cp', 'trtbps', 'chol', 'fbs', 
                'restecg', 'thalachh', 'exng', 'oldpeak', 'slp', 'caa', 'thall']


def download_dataset_from_kaggle(dataset_name = 'rashikrahmanpritom/heart-attack-analysis-prediction-dataset'):
    subprocess.run(['kaggle', 'datasets', 'download', '-d', dataset_name, '-p', 'saved_data'])
    

def load_data(data_path = 'saved_data/heart.csv'):
    df = pd.read_csv(data_path)
    return df


def train_model(df_train):
    model = HistGradientBoostingClassifier(categorical_features=['sex'])
    X = df_train.drop(columns = ['output'])
    y = df_train['output']
    
    model.fit(X, y)
    print('Model score : {}'.format(model.score(X, y)))
    return model


def predict(model, df_pred):
    return model.predict(df_pred)


def save_model(model):
    path = datetime.datetime.now().strftime("%y-%m-%d_%H-%M")
    full_path = 'saved_models/heart_disease_{}.pkl'.format(path)
    with open(full_path, 'wb') as file:
        pickle.dump(model, file)
    

def load_model(model_date = None):
    if model_date is None:
        models = os.listdir('saved_models')
        latest_date = max([model_path[-18:-4] for model_path in models])
        model_path = 'heart_disease_{}.pkl'.format(latest_date)
    with open('saved_models/{}'.format(model_path), 'rb') as file:
        model = pickle.load(file)
    return model