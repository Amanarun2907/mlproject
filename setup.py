## building our application as a package itself
from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .' ## this is used to ignore the -e . in requirements.txt file
def get_requirements(file_path:str)->List[str]: ## get_requirements function will return list of requirements
    '''
    this function will return list of requirements as there are many libraries which are required for our project and we do not write the name of each library in setup.py file manually
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    ## meatadata about the package
    name  = 'mlproject', ## name of the project or package 
    version = '0.0.1', ## version of the package
    author = "Aman Jain", ## Name of the author 
    author_email='aman.jain.23cse@bmu.edu.in',  ## email of the author 
    packages = find_packages(),
    install_requires= get_requirements('requirements.txt') ## list of dependencies that is necessary for our project
)