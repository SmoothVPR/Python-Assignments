#!/usr/bin/env python3

"""
Author:      VPR
Created:     November 18, 2021
Modified:    November 20, 2021

Brief:
    Weekend Assignment 2
"""

# import matplotlib.pyplot as plt
# import seaborn as sns
import pandas as pd
# import numpy as np

import pathlib
import sys
import os
import re

from datetime import datetime
from pandas import DataFrame
from typing import Tuple, NoReturn, Union

from modules.logging import Logger
from modules import full_state_names, abbr_state_names

logger = Logger(f"{datetime.now().strftime('%Y-%m-%d')}_log.txt")

def get_files(_dir) -> Union[NoReturn, Tuple[str, str]]:
    """
    Attempts to return a tuple of two strings (current_file, previous_file)

    Exits on any parsing or system error.
    """
    files = [x for x in os.listdir(_dir) if ".csv" in x]
    files.sort()

    current_file  = _dir + files[-1]
    previous_file = _dir + files[-2]

    return ( current_file, previous_file )

def get_dataframes(current_file: str, previous_file: str) -> Tuple[DataFrame, DataFrame]:
    """
    Attempts to return a tuple of two DataFrame ( df_curr, df_prev )  
    to the caller.

    Exits on any parsing or system error.
    """
    try:
        logger.log(f"Attempting to load '{current_file}'.")
        df_curr = pd.DataFrame(pd.read_csv(current_file))
        logger.log(f"Successfully loaded '{current_file}' into a DataFrame.")
    except:
        logger.err(f"Failed to load '{current_file}'.")
    try:
        logger.log(f"Attempting to load '{previous_file}'.")
        df_prev = pd.DataFrame(pd.read_csv(previous_file))
        logger.log(f"Successfully loaded '{previous_file}' into a DataFrame.")
    except:
        logger.err(f"Failed to load '{previous_file}'.")

    return ( df_curr, df_prev )

def assess_line_difference(df_curr, df_prev) -> Union[None, NoReturn]:
    """
    Asserts that the line count difference between the two DataFrame is
    no larger than 500 lines.

    Exits on failure.
    """
    result = abs(df_curr.shape[0] - df_prev.shape[0]) < 500

    if result is False:
        logger.err("Line count difference insufficient.")

def handle_nyl_list(current_file: str, operation: str="read") -> None:
    """
    File if processed once should be stored in the reference file 'NYL.lst'.
    If we are reprocessing the same file again an exception will be thrown,  
    saying that it was already processed and the program will exit.
    """
    NYL = "NYL.lst"

    if operation == "read":
        # if it doesnt exist, create it
        if not os.path.exists(NYL):
            with open(NYL, 'w') as f:
                f.write("")

        # read the NYL.lst file
        if not pathlib.Path(NYL).is_file():
            sys.exit(1)

        with open(NYL, 'r+') as f:
            file_list = f.read().split("\n")

            try:
                assert (current_file not in file_list)
            except AssertionError:
                logger.err("This file has already been processed.", exit_code=5)

    elif operation == "append":
        with open(NYL, 'a') as f:
            try:
                f.write(current_file)
                logger.log(f"'{current_file}' successfully processed.")
                logger.log(f"Adding '{current_file}' to '{NYL}'.")
            except Exception as ex:
                logger.err(f"{ex}")
    else:
        logger.err(f"Unknown operation requested.", exit_code=-1)

def get_cleaned_dataframe(df: DataFrame) -> DataFrame:
    """
    Attempts to return a more clean and universal dataset to the caller.

    Logs non-fatal errors and continues to run.
    Exits immediately on fatal errors.
    """
    df_new = df

    # Columns to change from
    bad_column_1 = 'Agent Writing Contract Start Date (Carrier appointment start date)'
    bad_column_2 = 'Agent Writing Contract Status (active)'
    bad_column_3 = 'Agent Writing Contract Status (cancelled)'

    # Columns to change to
    good_column_1 = 'Agent Writing Contract Start Date'
    good_column_2 = 'Agent Writing Contract Status'
    good_column_3 = good_column_2

    if bad_column_1 in df.columns:
        df_new[bad_column_1].rename(good_column_1)
        
    if bad_column_2 in df.columns:
        df_new[bad_column_2].rename(good_column_2)
        
    if bad_column_3 in df.columns:
        df_new[bad_column_3].rename(good_column_3)

    return df_new

def is_valid_phone_number(phone_number: str) -> bool:
    # 3 numbers followed by a '.', '-', or ' '
    regex = r"^([0-9]{3}[\.\- ]){2}[0-9]{4}$"
    match = re.match(regex, phone_number)
    
    if match:
        return True
    
    return False

def is_valid_state(state: str) -> bool:
    return state in [ *full_state_names, *abbr_state_names ]

def is_valid_email(email: str) -> bool:
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    match = re.match(regex, email)
    
    if match:
        return True
    
    return False

def parse_dataframe(df: DataFrame) -> None:
    """
    Parses the target date frame for the following features:
    - Valid phone number
    - Valid state
    - Valid email

    Iterates through each of the target columns and logs any dirty
    data with a warning using the logger.
    """

    # Parse phone numbers
    for i, phone_number in enumerate(df["Agency Phone Number"]):
        if not is_valid_phone_number(phone_number):
            logger.warn(f"Invalid phone number: '{phone_number}' found in row {i}.")

    # Parse states
    for i, state in enumerate(df["Agency State"]):
        if not is_valid_state(state):
            logger.warn(f"Invalid state: '{state}' found in row {i}.")

    # Parse email addresses
    for i, email in enumerate(df["Agent Email Address"]):
        if not is_valid_email(email):
            logger.warn(f"Invalid state: '{email}' found in row {i}.")

if __name__ == "__main__":
    # Set working directory to source file directory
    path = os.path.dirname(__file__)
    os.chdir(os.path.abspath(path))

    logger.init()

    resource_dir = "res/"
    current_file, previous_file = get_files(resource_dir)

    # Initial data processing and loading
    df_curr, df_prev = get_dataframes(current_file, previous_file)
    assess_line_difference(df_curr, df_prev)

    # Check if the file is has already been handled
    handle_nyl_list(current_file)

    # Clean up the data
    df_curr = get_cleaned_dataframe(df_curr)
    df_prev = get_cleaned_dataframe(df_curr)

    # Check the phone number, state, and email columns for dirty data
    parse_dataframe(df_curr)

    # Write after successful processing
    handle_nyl_list(current_file, operation="append")

    logger.destroy()
