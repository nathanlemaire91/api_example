from setuptools import setup, find_packages

setup(
    name='patient_heart_disease_prediction_project',
    version='0.1',
    packages=find_packages(include = ['api', 'model']),
    install_requires=
    [
        'anyio==3.7.1',
        'h11==0.12.0',
        'httpcore==0.13.7',
        'httpx==1.0.0b0',
        'kaggle==1.6.14',
        'pandas==2.2.2',
        'scikit-learn==1.4.2',
        'fastapi==0.111.0',
        'numpy==1.26.4'
    ],
    license='MIT'
)