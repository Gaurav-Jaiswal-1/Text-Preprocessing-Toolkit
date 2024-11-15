
from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'


def get_requirements(file_path:str)->List[str]:
  requirements = []
  with open(file_path) as f:
    requirements = f.readlines()
    requirements = [req.replace("\n", "") for req in requirements]

    if HYPEN_E_DOT in requirements:
      requirements.remove(HYPEN_E_DOT)
  return requirements



with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.1"
REPO_NAME = "Text-Preprocessing-Toolkit"
PKG_NAME = "Text_Preprocessing_Toolkit"
AUTHOR_NAME = "Gaurav Jaiswal"
AUTHOR_EMAIL = "jaiswalagaurav863@gmail.com"




setup(
    name=PKG_NAME,
    version= __version__,
    author= AUTHOR_NAME,
    author_email= AUTHOR_EMAIL,
    description="Automate text preprocessing tasks like tokenization, lemmatization, stop word removal, and normalization.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=  "https://github.com/Gaurav-Jaiswal-1/Text-Preprocessing-Toolkit.git",
    project_urls={
      "Bug Tracker": "https://github.com/Gaurav-Jaiswal-1/Text-Preprocessing-Toolkit/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=get_requirements("./requirements.txt"),
    keywords= ['text preprocessing toolkit', 'automated text preprocessing' ]
    
    )

