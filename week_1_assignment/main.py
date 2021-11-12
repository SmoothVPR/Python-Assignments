#!/usr/bin/env python3

"""
Author:   Malik R Booker
Created:  November 11, 2021
Modified: November 12, 2021

Brief:
    - [x] Please import csv (or) openpyxl & Logging packages for this problem.
    - [x] Program should take any filename as per the format mentioned as input.
    - [x] Input month value from the file name where ex: January(expedia_report_monthly_january_2018.xlsx)
    - [x] Based on the month and year input values value print the values into a log file using a logger
"""

DAY     = 5
PROJECT = 1

import pandas as pd
import numpy as np

import pathlib
import sys

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

abrv_month_names = ( "Jan",
                     "Feb",
                     "Mar",
                     "Apr",
                     "May",
                     "Jun",
                     "Jul",
                     "Aug",
                     "Sep",
                     "Oct",
                     "Nov",
                     "Dec" )

def handle_command_line():
    argv = sys.argv
    argc = len(sys.argv)

    if argc != 2:
        __usage_error()

    if pathlib.Path(argv[1]).is_file():
        return argv[1]

    sys.stderr.write(f"File '{argv[1]}' does not exist.\n")
    sys.exit(1)

def __usage_error():
    sys.stderr.write( "Usage error.\n"
                      "\n"
                      "Example:\n"
                      f"  {sys.argv[0]} path/to/excel.xlsx\n" )

    sys.exit(1)

def display_assignment():
    sys.stdout.write( f"###############\n"
                      f"# Day: {DAY}      #\n"
                      f"# Project: {PROJECT}  #\n"
                      f"###############\n"
                      f"\n\n" )

def extract_month_from_file(file_path):
    for month in month_names:
        if month.upper() in file_path.upper():
            logger.log(f"Target month identified as {month}.")
            return month

    logger.log(f"Could not determine month from '{file_path}'.")
    logger.destroy()
    sys.exit(1)

def get_dataframe(file_path, sheet_name=0):
    logger.log(f"Loading excel spreadsheet '{file_path}'...")

    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        logger.log(f"Successfully loaded '{file_path}'.")

        return df
    except:
        logger.log(f"Failed to load spreadsheet '{file_path}'.")
        logger.destroy()

    sys.exit(1)

def parse_summary(df, target_month):
    logger.log(f"Attempting to parse Month of {target_month} in '{sheet_names[0]}'...")

    df = df.iloc[:12]       # clean up rows
    df = df[df.columns[:6]] # clean up columns

    # Clean up index column
    dt_format = "%Y-%m-%d %H:%M:%S"
    convert_dt_to_month = lambda x: datetime.strptime(str(x), dt_format).strftime("%B")
    df["Unnamed: 0"] = df["Unnamed: 0"].map(convert_dt_to_month)

    target_row = df.loc[df["Unnamed: 0"] == target_month]
    values = target_row.values.tolist()[0][1:]
    columns = df.columns[1:]

    # Clean up 'Calls Offered' column
    df["Calls Offered"] = df["Calls Offered"].astype(np.int64)

    result = []
    for column, value in zip(columns, values):
        # formatting by data type
        if df[column].dtype == np.int64:
            result.append(tuple([ column, f"{int(value):,}" ]))
        else:
            result.append(tuple([ column, f"{100 * value:.2f}%" ]))

    logger.log(f"Results for Summary Rolling MoM of {target_month}: {str(result)}")

def parse_voc_rolling(df, target_month):
    df, target_month
    logger.log(f"Attempting to parse Month of {target_month} in '{sheet_names[1]}'...")

    # result = []
    # for column, value in zip(columns, values):
        # result.append(tuple([ column, value ]))
    # logger.log(f"Results for VOC Rolling MoM of {target_month}: {str(result)}")

if __name__ == "__main__":
    file_path = handle_command_line()
    display_assignment()

    logger.init()
    target_month = extract_month_from_file(file_path)

    df_summary_rolling = get_dataframe(file_path, sheet_name=sheet_names[0])
    parse_summary(df_summary_rolling, target_month)

    df_voc_rolling     = get_dataframe(file_path, sheet_name=sheet_names[1])
    parse_voc_rolling(df_voc_rolling, target_month)

    # df_statements      = get_dataframe(file_path, sheet_name=2)

    logger.destroy()
