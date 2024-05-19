FROM python:3.11
WORKDIR /app

COPY *.py /app

RUN mkdir saved_models
RUN mkdir saved_data

RUN python setup.py install

RUN kaggle datasets download -d rashikrahmanpritom/heart-attack-analysis-prediction-dataset -p saved_data
RUN unzip saved_data/heart-attack-analysis-prediction-dataset.zip -d saved_data
RUN rm saved_data/heart-attack-analysis-prediction-dataset.zip

CMD uvicorn main:app --port 80 --host 0.0.0.0