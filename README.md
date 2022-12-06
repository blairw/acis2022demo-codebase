# acis2022demo-codebase

## What is this?

This is the demonstration codebase for the paper:

> **Wang B.**, 2022, 'Programming for Qualitative Data Analysis: Towards a YAML Workflow', presented at the Australasian Conference on Information Systems (ACIS), Melbourne (Australia), paper 30.

## First-time setup

Please place a clone of the wonderful https://github.com/0xabu/pdfannots project in the parent directory.

Please also place `fulltexts`, containing PDF files of the full-text documents, in the parent directory.

You will need to set up a Python virtual environment as per below:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade pandas
python3 -m pip install --upgrade pdfminer.six
python3 -m pip install --upgrade pyyaml
```

