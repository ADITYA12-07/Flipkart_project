from setuptools import find_namespace_packages, setup
from typing import List

def get_requirements() -> List[str]:
    
    """
    
    This function will return list of requirements
    
    """
    requirement_list:list[str] = []
    """
    Write a code to read get_requirements.txt file and append each get_requirements_list variable.
    
    """
    
    return requirement_list


setup(
    name= "flipkart",
    version = "0.0.1",
    author = "Aditya Pawar",
    author_email="pawarap12@gmail",
    packages=find_namespace_packages(),
    install_requires = get_requirements()
)