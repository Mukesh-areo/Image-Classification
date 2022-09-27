from fileinput import filename
from msilib.schema import Component
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s: ')
package_name="deepClassifier"                                                    # "deepClassifier" is the name of the package 

list_of_files=[                                                                  # list of files that contain the DeepClassifier class
    ".github/workflows/.gitkeep",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/Component/__init__.py",
    f"src/{package_name}/utils/__init__.py",
    f"src/{package_name}/config/__init__.py",
    f"src/{package_name}/pipeline/__init__.py",
    f"src/{package_name}/entity/__init__.py",
    f"src/{package_name}/constants/__init__.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "configs/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "research/trials.ipynb"
]

for filepath in list_of_files:                                            
    filepath=Path(filepath)
    filedir, filename =os.path.split(filepath)
    if filedir !="":                                # check if file exists if not create it
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory:{filedir} for file:{filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'wb'):
            pass #create an empty file
            logging.info(f"Creating empty file:{filedir}")
    else:
        logging.info(f"{filename} already exist")