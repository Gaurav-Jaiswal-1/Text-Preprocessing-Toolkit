#!/bin/bash

echo "Initializing project..."

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements_dev.txt

echo "Project initialized successfully!"
