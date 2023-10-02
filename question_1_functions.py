"""
This file contains all the functions for importing and merging the jsonl files to Dataframes
"""
import pandas as pd
import os
from constants import *


def build_file_path(file_name: str) -> str:
    """
    Builds relative file path to a file in the MASSIVE dataset
    :param file_name:
    :return filepath:
    """
    return os.path.join(dataset_dir, file_name)


def read_jsonl_file(path: str) -> pd.DataFrame:
    """
    Reads jsonl file at a filepath and generate a DataFrame
    :param path:
    :return DataFrame:
    """
    df = pd.read_json(path, lines=True)
    return df


def merge_with_english(english_df: pd.DataFrame, other_df: pd.DataFrame) -> pd.DataFrame:
    """
    Merges English DataFrame with another language's DataFrame
    :param english_df:
    :param other_df:
    :return merged DataFrame:
    """
    df = other_df.merge(english_df, on='id')
    df = df.rename(
        {
            "utt_x": "utt_translation",
            "annot_utt_x": "annot_utt_translation",
            "utt_y": "utterance",
            "annot_utt_y": "annot_utt",
            "partition_y": "partition",
        },
        axis=1,
    )
    return df[["id", "utterance", "utt_translation", "annot_utt_translation", "annot_utt", "partition", ]]
