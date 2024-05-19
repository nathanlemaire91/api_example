FROM ubuntu:22.04
WORKDIR /app

CMD mkdir saved_models
CMD mkdir saved_data

CMD python setup.py install

CMD kaggle datasets download -d rashikrahmanpritom/heart-attack-analysis-prediction-dataset -p saved_data
CMD unzip saved_data/heart-attack-analysis-prediction-dataset.zip
CMD rm saved_data/heart-attack-analysis-prediction-dataset.zip

CMD uvicorn main:app --reload