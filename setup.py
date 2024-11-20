from setuptools import setup, find_packages
from typing import List
import os

# Constant for editable install
HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """
    Reads the requirements file and returns a list of dependencies.
    Removes the editable install option if present.
    """
    requirements = []
    try:
        with open(file_path, "r") as f:
            requirements = f.readlines()
            # Strip newlines and remove editable install if it exists
            requirements = [req.strip() for req in requirements if req.strip()]
            if HYPHEN_E_DOT in requirements:
                requirements.remove(HYPHEN_E_DOT)
    except FileNotFoundError:
        print(f"Warning: {file_path} not found. Proceeding with empty requirements.")
    return requirements

# Read the long description from the README.md file
long_description = ""
if os.path.exists("README.md"):
    with open("README.md", "r", encoding="utf-8") as f:
        long_description = f.read()

# Package metadata
__version__ = "0.0.1"
REPO_NAME = "Text-Preprocessing-Toolkit"
PKG_NAME = "Text_Preprocessing_Toolkit"
AUTHOR_NAME = "Gaurav Jaiswal"
AUTHOR_EMAIL = "jaiswalgaurav863@gmail.com"
REQUIREMENTS_FILE = "requirements.txt"

setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="Automate text preprocessing tasks like tokenization, lemmatization, stop word removal, and normalization.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/Gaurav-Jaiswal-1/{REPO_NAME}.git",
    project_urls={
        "Bug Tracker": f"https://github.com/Gaurav-Jaiswal-1/{REPO_NAME}/issues",
        "Documentation": f"https://github.com/Gaurav-Jaiswal-1/{REPO_NAME}/wiki",
    },
    package_dir={"": "src"},  # Ensure the source code is under the `src` folder
    packages=find_packages(where="src"),
    install_requires=get_requirements(REQUIREMENTS_FILE),  # Dependencies from requirements.txt
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
    keywords=["text preprocessing toolkit", "automated text preprocessing"],
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
    include_package_data=True,  # Include additional files like README.md
)
