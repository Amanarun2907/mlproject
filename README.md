## End to End Machine learning project 

## Step 1 :Setting virtual environment

pip install virtualenv

python -m venv .venv

.venv\Scripts\activate

## Step 2 : Create github repository and add a relation of github with local machine. and also make a README.md file in it.

## Step 3 : Make a .gitignore file in the github repository itself . 

## Step 3 : Make a requirements.txt file in the root directory.

## Step 4 : Make a setup.py file in the root directory.

from setuptools import find_packages,setup

from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:

    '''

    this function will return list of requirements

    '''

    requirements=[]

    with open(file_path) as file_obj:

        requirements=file_obj.readlines()

        requirements=[req.replace("\n","") for req in requirements]
        
        if HYPEN_E_DOT in requirements:

            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(

    name  = 'mlproject',

    version = '0.0.1',

    author = "AJ",

    author_email='aman.jain.23cse@bmu.edu.in',

    packages = find_packages(),

    install_requires= get_requirements('requirements.txt')

)

run it by python setup.py

## Step 5 : Make a src folder in the root directory and create an __init__.py file inside that folder. 




