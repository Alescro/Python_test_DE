import os.path
from datetime import datetime
import pandas as pd
import json
import numpy as np
from pathlib import Path


class Config:

    def __init__(self):
        self.DRUGS_PATH = Path('resources/inputs/drugs.csv')
        self.CLINICAL_TRIALS_PATH = Path('resources/inputs/clinical_trials.csv')
        self.PUBMED_CSV_PATH = Path('resources/inputs/pubmed.csv')
        self.PUBMED_JSON_PATH = Path('resources/inputs/pubmed.json')
        self.NESTED_JSON_PATH = Path('resources/outputs/JSON_drugs_publications.json')

