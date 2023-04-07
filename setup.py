from setuptools import find_packages,setup
from typing import List

HYPEN_E_NOT ='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function return the list of requirements
    '''
    
    requirements =[]
    with open(file_path) as fil_obj:
        requirements=fil_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_NOT in requirements:
            requirements.remove(HYPEN_E_NOT)

    return requirements

setup(
name='mlpojects',
version='0.0.1',
author='purushoth',
author_email='haripurushoth185@gmail.com',
packages=find_packages(),
install_requires =get_requirements('requirements.txt')
    
)
