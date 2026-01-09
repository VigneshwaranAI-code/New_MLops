 

from setuptools import setup, find_packages
from typing import List

def get_requirements()->List[str]:

    try:
        with open('requirements.txt') as file:
            lines = file.readlines()
            req_list = []

            for line in lines:
                requirements = line.strip("\n")
                
                if requirements and requirements != "-e .":
                    req_list.append(requirements)
    except FileNotFoundError:
        print("File not found")
    return req_list


      
setup(
    name="networksecurity",
    version="0.0.1",
    author="vigesh",
    author_email="1234456@gamil",
    packages=find_packages(),
    install_requires=get_requirements(),
)

 