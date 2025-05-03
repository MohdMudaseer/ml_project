from setuptools import setup, find_packages
from typing import List

hyphen_e_dot = '-e .'

def getRequirements(filepath: str) -> List[str]:
    requirements = []
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]

        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)
    
    return requirements

setup(
    name='ML-Project',
    version='0.0.1',
    author="Mohd Mudaseer Mazharuddin",
    author_email="mudaseer2753@gmail.com",
    packages=find_packages(),
    install_requires=getRequirements('requirements.txt')
)
