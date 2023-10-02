# graphicsCAT1

## Overview
This Python project is designed to process and manage data from the MASSIVE Dataset. It includes scripts and functions to perform various tasks related to data processing, such as generating Excel files, partitioning datasets, and generating translations.

## Project Structure
The project is organized into several Python scripts and a constants file. Here's an overview of the project structure:

question1.py: Contains code related to Question 1, which involves generating en-xx .xlsx files for different languages using English as a pivot language.

question_1_functions.py: Contains functions for handling JSONL files, merging dataframes, and generating Excel files.

question2.py: Contains code related to Question 2, which involves generating separate JSONL files for English (en), Swahili (sw), and German (de) in test, train, and dev sets, as well as generating translations.

question_2_functions.py: Contains functions for partitioning dataframes and generating translations.

main.py: The main entry point of the project, responsible for running specific tasks based on command-line flags.

constants.py: Contains constants related to directory paths and dataset filenames.

## Getting Started
## Dependencies
Before running the code, make sure you have the following dependencies installed:

Python 3.x
Pandas library
absl-py library
You can install these dependencies using pip:

## bash
Copy code
pip install pandas absl-py
Data Import
Ensure that the MASSIVE Dataset files (e.g., en-US.jsonl, sw-KE.jsonl, de-DE.jsonl) are available in the specified directory (./data) before running the code.

## Running the Code
You can execute different tasks using command-line flags. Here are some examples:

## To run Question 1 and generate en-xx .xlsx files:

python main.py --question1="Running Question 1"
## To run Question 2 and perform partitioning and translation tasks:
python main.py --question2="Running Question 2"
## To view available options:

python main.py --help
## Output
The code generates various output files, including Excel files (en-xx.xlsx), partitioned JSONL files, and a JSON file containing translations (all_translations.json).
