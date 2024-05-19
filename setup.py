from setuptools import setup, find_packages

setup(
    name='patient_heart_disease_prediction_project',
    version='0.1',
    packages=find_packages(include = ['api', 'model']),
    install_requires=
    [
        'kaggle',
        'pandas',
        'subprocess',
        'scikit-learn',
        'pickle',
        'datetime',
        'fastapi',
        'pydantic',
        'numpy'
    ],
    license='MIT'
)