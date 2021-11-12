#!/usr/bin/env python3

"""
Author:    Malik R Booker
Created:   November 11, 2021
Completed: November 12, 2021
Modified:  November 12, 2021

Brief:
    - [x] Please import csv (or) openpyxl & Logging packages for this problem.
    - [x] Program should take any filename as per the format mentioned as input.
    - [x] Input month value from the file name where ex: January(expedia_report_monthly_january_2018.xlsx)
    - [x] Based on the month and year input values value print the values into a log file using a logger
"""

import pandas as pd
import numpy as np

import pathlib
import sys
import re

from datetime import datetime
from logger import Logger

DAY     = 5
PROJECT = 1

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

def extract_year_from_file(file_path):
    regex = "(?<=_)[0-9]{4}(?=\\.xlsx)"
    match = re.search(regex, file_path)
    
    if match != None:
        target_year = match.group(0)

        logger.log(f"Target year identified as {target_year}.")
        return target_year

    logger.log(f"Could not determine year from '{file_path}'.")
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

def parse_summary(df, target_month, target_year):
    logger.log(f"Attempting to parse {target_month} of {target_year} in '{sheet_names[0]}'...")

    # Slice dataframe to only include meaningful data
    df = df.iloc[:12]       # clean up rows
    df = df[df.columns[:6]] # clean up columns

    # Clean up index column
    df.rename(columns={'Unnamed: 0': 'index'}, inplace=True)

    # Clean up index datetime
    dt_format = "%Y-%m-%d %H:%M:%S"
    convert_dt_to_month = lambda x: datetime.strptime(str(x), dt_format).strftime("%b-%y")
    df["index"] = df["index"].map(convert_dt_to_month)

    # Clean up 'Calls Offered' column
    df["Calls Offered"] = df["Calls Offered"].astype(np.int64)

    # Format target_month & target_year to "%b-%y"
    target_dt = target_month[:3] + "-" + target_year[2:]
    target_row = df.loc[df["index"] == target_dt]

    values = target_row.values.tolist()[0][1:]
    columns = df.columns[1:]

    result = []
    for column, value in zip(columns, values):
        if df[column].dtype == np.int64:
            result.append(tuple([ column, f"{int(value):,}" ]))
        else:
            result.append(tuple([ column, f"{100 * value:.2f}%" ]))

    logger.log(f"Results for Summary Rolling MoM of {target_month} of {target_year}: {str(result)}")

def parse_voc(df, target_month, target_year):
    logger.log(f"Attempting to parse {target_month} of {target_year} in '{sheet_names[1]}'...")

    # Clean up index column
    df.rename(columns={'Unnamed: 0':'index'}, inplace=True)

    # Remove all 'Unnamed' columns
    for col in df.columns:
        if "Unnamed" in str(col):
            df.drop(col, axis=1, inplace=True)

    # Clean up column names and replace them
    dt_format = "%Y-%m-%d %H:%M:%S"
    columns = df.columns[1:]
    new_axis = [ "index" ]

    for column in columns:
        if type(column) == datetime:
            new_axis.append(datetime.strptime(str(column), dt_format).strftime("%b-%y"))
        else:
            new_axis.append(datetime.strptime(str(column) + str(target_year), "%B%Y").strftime("%b-%y"))

    df.set_axis(new_axis, axis=1, inplace=True)

    # Drop empty rows
    df.dropna(axis=0, inplace=True)

    # Select datetime in target column
    target_dt = target_month[:3] + "-" + target_year[2:]

    # Output formatting
    columns = [ "Base Size",
                "Promoters",
                "Passives",
                "Detractors",
                "Overall NPS %",
                "SAT with Agent %",
                "DSAT with Agent %" ]

    values = df[target_dt].values.tolist()

    result = []
    for column, value in zip(columns, values):
        if value > 1:
            if column == columns[0]: # Base Size
                result.append(tuple([ column, f"{int(value):,}" ]))
            elif column == columns[1]: # Promoters:
                result.append(tuple([ column, f"{'good' if value > 200 else 'bad'}" ]))
            else: # Passives & Detractors:
                result.append(tuple([ column, f"{'good' if value > 100 else 'bad'}" ]))
        else:
            result.append(tuple([ column, f"{100 * value:.2f}%" ]))

    logger.log(f"Results for VOC Rolling MoM of {target_month} of {target_year}: {str(result)}")

if __name__ == "__main__":
    file_path = handle_command_line()
    display_assignment()
    logger.init()

    target_month = extract_month_from_file(file_path)
    target_year = extract_year_from_file(file_path) 

    df_summary_rolling = get_dataframe(file_path, sheet_name=sheet_names[0])
    parse_summary(df_summary_rolling, target_month, target_year)

    df_voc_rolling = get_dataframe(file_path, sheet_name=sheet_names[1])
    parse_voc(df_voc_rolling, target_month, target_year)

    logger.destroy()
