#!/usr/bin/env python3

"""
Author:      VPR
Created:     November 18, 2021
Modified:    November 18, 2021

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

from datetime import datetime
from pandas import DataFrame
from typing import Tuple, NoReturn, Union

from modules.logging import Logger

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

def handle_nyl_list(current_file: str) -> None:
    """
    File if processed once should be stored in the reference file 'NYL.lst'.
    If we are reprocessing the same file again an exception will be thrown,  
    saying that it was already processed and the program will exit.
    """
    NYL = "NYL.lst"

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
            f.write(current_file)
        except AssertionError:
            logger.err("This file has already been processed.", exit_code=5)

def get_cleaned_dataframe(df: DataFrame) -> DataFrame:
    """
    Attempts to return a more clean and universal dataset to the caller.

    Logs non-fatal errors and continues to run.
    Exits immediately on fatal errors.
    """
    new_df = df

    return new_df

if __name__ == "__main__":
    path = os.path.dirname(__file__)
    os.chdir(os.path.abspath(path))

    logger.init()

    resource_dir = "res/"
    current_file, previous_file = get_files(resource_dir)

    df_curr, df_prev = get_dataframes(current_file, previous_file)
    assess_line_difference(df_curr, df_prev)

    # Check if the file is has already been handled
    handle_nyl_list(current_file)

    # Clean up the data
    df_curr = get_cleaned_dataframe(df_curr)
    df_prev = get_cleaned_dataframe(df_curr)

    logger.destroy()
