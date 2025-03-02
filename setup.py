from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(filename:str)->List[str]:
    requirements = []
    with open(filename, "r") as f:
        requirements = f.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
   

    return requirements



setup(
    name="my_project",          # Name of the package
    version="1.0.0",            # Package version
    author = 'Abhinav',
    packages=find_packages(),   # Automatically finds Python packages . find_packages() automatically detects all directories that contain __init__.py.
    install_requires=get_requirements('requirements.txt')  # Dependencies

)
