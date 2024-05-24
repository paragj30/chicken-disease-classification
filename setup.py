from setuptools import find_packages,setup
from typing import List

__version__ = "0.0.0"
REPO_NAME = "Chicken-Disease-Classification-Projects"
AUTHOR_USER_NAME = "paragj30"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "paragj30@gmail.com"
HYPEN_E_DOT='-e .'

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [file.replace("\n","") for file in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name = REPO_NAME,
    version =__version__,
    author= AUTHOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    description="A small python package for Computer Vision app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages= find_packages(where="src"),
    install_requires = get_requirements('requirements.txt')    
)