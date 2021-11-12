#!/usr/bin/env python3

"""
Author:   Malik R Booker
Created:  November 11, 2021
Modified: November 11, 2021

Brief:
    - [x] Please import csv (or) openpyxl & Logging packages for this problem.
    - [x] Program should take any filename as per the format mentioned as input.
    - [x] Input month value from the file name where ex: January(expedia_report_monthly_january_2018.xlsx)
    - [ ] Based on the month and year input values value print the values into a log file using a logger
"""

DAY = 5
PROJECT = 1

import pandas as pd
# import numpy as np

import pathlib
import sys
# import os

from datetime import datetime
from logger import Logger

logger = Logger(f"{datetime.now().strftime('%Y-%m-%d')}_log.txt")

sheet_names = ( "Summary Rolling MoM",
               "VOC Rolling MoM",
               "Monthly Verbatim Statements" )

month_names = ( "January",
                "February",
                "March",
                "April",
                "May",
                "June",
                "July",
                "August",
                "September",
                "October",
                "November",
                "December" )

def display_assignment():
    print( "###############")
    print(f"# Day: {DAY}      #")
    print(f"# Project: {PROJECT}  #")
    print( "###############")
    print("")

def __usage_error():
    sys.stderr.write("Usage error.\n"
                     "\n"
                     "Example:\n"
                     f"  {sys.argv[0]} path/to/excel.xlsx\n")

    sys.exit(1)

def handle_command_line():
    argv = sys.argv
    argc = len(sys.argv)

    if argc != 2:
        __usage_error()

    if pathlib.Path(argv[1]).is_file():
        return argv[1]

    sys.stderr.write(f"File '{argv[1]}' does not exist.\n")
    sys.exit(1)

def extract_month_from_file(file_path):
    for month in month_names:
        if month.upper() in file_path.upper():
            logger.log(f"Target month idendified as {month}.")
            return month

    sys.stderr.write(f"Could not determine month from '{file_path}'.\n")
    sys.exit(1)

def main():
    ...

if __name__ == "__main__":
    display_assignment() # Display task

    file_path = handle_command_line()
    logger.init()

    target_month = extract_month_from_file(file_path)

    df_summary_rolling = pd.read_excel(file_path, sheet_name=sheet_names[0])
    df_voc_rolling     = pd.read_excel(file_path, sheet_name=sheet_names[1])
    df_statements      = pd.read_excel(file_path, sheet_name=sheet_names[1])

    logger.destroy()
