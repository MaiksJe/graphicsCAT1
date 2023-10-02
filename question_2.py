"""
This file contains functions to partitions and generate translations for the files
"""
import pandas as pd
import question_2_functions
from constants import dataset_dir, english_dataset, swahili_dataset, german_dataset
from absl import flags


FLAGS = flags.FLAGS
flags.DEFINE_string("question2", "Running Question 2", "The question to run")


def partition_files():
    """
    Partitions English, Swahili, and German files into given partitions
    """
    english = pd.read_json(f"{dataset_dir}/{english_dataset}", lines=True)
    swahili = pd.read_json(f"{dataset_dir}/{swahili_dataset}", lines=True)
    german = pd.read_json(f"{dataset_dir}/{german_dataset}", lines=True)
    dfs = [english, swahili, german]
    names = ["english", "swahili", "german"]
    partitions = ["test", "train", "dev"]
    question_2_functions.generate_partitioned_jsonl(dfs, names, partitions)


def generate_translations():
    """
    Generates translations for all train sets and pretty prints the results
    """
    results = question_2_functions.generate_all_translations()
    hell = pd.DataFrame(results)
    hell.to_json('all_translations.json', orient='index', indent=4)
