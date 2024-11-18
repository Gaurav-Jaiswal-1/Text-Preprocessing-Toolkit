from setuptools import setup, find_packages
from typing import List

# Constant for -e . in requirements (editable install)
HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    Function to read the requirements file and return a list of dependencies.
    Removes the editable install option if present.
    """
    requirements = []
    with open(file_path, "r") as f:
        requirements = f.readlines()
        # Strip newlines and remove editable install if it exists
        requirements = [req.strip() for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

# Read the long description from the README.md file
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Package details
__version__ = "0.0.1"
REPO_NAME = "Text-Preprocessing-Toolkit"
PKG_NAME = "Text_Preprocessing_Toolkit"
AUTHOR_NAME = "Gaurav Jaiswal"
AUTHOR_EMAIL = "jaiswalgaurav863@gmail.com"

setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="Automate text preprocessing tasks like tokenization, lemmatization, stop word removal, and normalization.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Gaurav-Jaiswal-1/Text-Preprocessing-Toolkit.git",
    project_urls={
        "Bug Tracker": "https://github.com/Gaurav-Jaiswal-1/Text-Preprocessing-Toolkit/issues",
        "Documentation": "https://github.com/Gaurav-Jaiswal-1/Text-Preprocessing-Toolkit/wiki",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=get_requirements("./requirements.txt"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Linguistic",
    ],
    keywords=['text preprocessing toolkit', 'automated text preprocessing'],
    python_requires=">=3.8",
    extras_require={
        "dev": [
            "pytest>=7.2.0",
            "pytest-cov>=4.0.0",
            "flake8>=6.0.0",
            "black>=23.1.0",
            "mypy>=0.991",
            "sphinx>=7.1.2",
            "sphinx-rtd-theme>=1.2.0",
        ]
    },
    include_package_data=True,  # Ensure any extra files like README.md are included
)
