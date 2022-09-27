# Deep learning Project

## workflow

1.update your config.yaml
2.update secrets.yaml [Optional]
3.update params.yaml
4.update the entity
5.update the configuration manager in srs config
6.update the components
7.update the pipeline
8.Test run pipeline stage
9.Run tox for testing your package
10.Update the dvc.yaml
11.Run "Dvc repro" for running all the stages in pipeline

17/9/2022

Autocomplete the following information from the command line for    each stage information  yourself and    you can also specify
TabNine:: 

Tox - To create the environment and test everything
pytest - to check the testcase
Mypy - will check the error for eg( if you are passing wrong datatype to the function) ---it called linting of datatype
flake8 - It will check the standard code formatting eg: indentation  ---it is called code linting



MLFLOW_TRACKING_URI=https://dagshub.com/Mukesh-areo/CNN_claasaifier.mlflow \
MLFLOW_TRACKING_USERNAME=Mukesh-areo \
MLFLOW_TRACKING_PASSWORD=434cc55976d25211145784e69290bf348ce1e14a \
python script.py



# Project setups 

1. command
To create the folder structure use the following command
 ----Python template.py----

2. Then connect with the github
To connect the local repository with git use 
 ----git init-----

3. To create the Environment 
Use init_setup.sh file
----bash init-setup.sh ----

4. Activate the environment
---- conda activate ./env-----

5. Then run the Tox
------tox ----
or tox --recreate



