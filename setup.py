from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of required libraries for our project
    '''
    requirment=[]
    with open(file_path) as file_obj:
        requirment=file_obj.readlines()
        requirment=[req.replace("\n","") for req  in requirment]

        if HYPEN_E_DOT in requirment:
            requirment.remove(HYPEN_E_DOT)

    return requirment

setup(
    name='Machine Learning Project WebAPP',
    version='0.0.1',
    author='Shubham Pandey',
    author_email='shubhampandey426@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)