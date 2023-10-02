"""
This file contains functions to partition the datasets and combine the translations
"""
import pandas as pd
import os
from constants import partitioned_dir, processed_files_dir


def partition_df(df: pd.DataFrame, key: str) -> pd.DataFrame:
    """
    Partitions DataFrame based on the partition needed
    """
    return df[df["partition"] == key]


def generate_partitioned_jsonl(dfs: list[pd.DataFrame], df_names: list["str"], partitions: list["str"]):
    """
    Generates the partitioned datasets in jsonl format
    """
    for df, name in zip(dfs, df_names):
        for partition in partitions:
            partitioned_df = partition_df(df, partition)
            export_path = os.path.join(partitioned_dir, f'{name}-{partition}.jsonl')
            partitioned_df.to_json(export_path, orient="records", lines=True)


def generate_all_translations():
    """
    Generates all translations from en-xx for all train datasets
    """
    files = os.listdir(processed_files_dir)

    results = []
    for file in files:
        file_path = os.path.join(processed_files_dir, file)
        df = pd.read_excel(file_path)
        df = partition_df(df, "train")
        df = df[["id", "utterance"]]
        results.extend(list(df.to_dict(orient='index').values()))

    return results




