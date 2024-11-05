import os 
from pathlib import Path

package_name = 'Text_Preprocessing_Toolkit'

list_of_files = [
  ".github/workflows/ci.yaml",
  "src/ __init__.py",
  f"src/{package_name}/__init__.py",
  f"src/{package_name}/tokenizer.py",
  f"src/{package_name}/lemmatizer.py",
  f"src/{package_name}/stopwords.py",
  f"src/{package_name}/normalizer.py",
  f"src/{package_name}/utils.py",
  "tests/unit/__init__.py",
  "tests/unit/test_tokenizer.py",
  "tests/unit/test_lemmatizer.py",
  "tests/unit/test_stopwords.py",
  "tests/unit/test_normalizer.py",
  "tests/integration/__init__.py",
  "tests/integration/integration_testing.py",
  "init_setup.sh",
  "requirements.txt",
  "requirements_dev.txt",
  "setup.py",
  "setup.cfg",
  "pyproject.toml",
  "tox.ini",
  "experiments/experiments.ipynb",


]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
#
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
          pass  