"""
This file imports the MASSIVE Dataset and generates the necessary en-xx xlsxs
"""
import pandas as pd
import os
import question_1_functions
from constants import dataset_dir, english_dataset, processed_files_dir
from absl import flags

FLAGS = flags.FLAGS
flags.DEFINE_string("question1", "Running Question 1", "The question to run")


def generate_xlsx_file(file: str) -> None:
    """
    Processes a single jsonl file to merge it with an english DataFrame and creates an excel file
    :param file:
    """
    dataset_path = os.path.join(dataset_dir, file)
    df = question_1_functions.read_jsonl_file(dataset_path)
    lang_code = file.split('-')[1].split('.')[0]
    english_jsonl = pd.read_json(f"{dataset_dir}/{english_dataset}", lines=True)
    df = question_1_functions.merge_with_english(english_jsonl, df)
    df.to_excel(f'{processed_files_dir}/en-{lang_code}.xlsx')


def process_all_files(data_dir: str):
    """
    Generates en-xx excel files for all languages with English as the pivot
    """
    files = os.listdir(data_dir)
    for file_path in files:
        generate_xlsx_file(file_path)

