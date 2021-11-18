#!/usr/bin/env python3

"""
Author:       Malik R Booker
Created:      November 17, 2021
Completed:    November 17, 2021
Modified:     November 17, 2021

Brief:
    - [x] import pandas as pd
          import numpy as np
    - [x] Read Salaries.csv as a dataframe called sal.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

import sys

from IPython.display import display
from pandas import DataFrame
# from typing import ...

DAY = 7

def excercise_a() -> DataFrame:
    """
    Read Salaries.csv as a dataframe called 'df'.
    """
    try:
        df = pd.DataFrame(pd.read_csv("./2_pandas_Salaries.csv"))
    except:
        sys.exit(1)

    return df

def excercise_b(df: DataFrame) -> None:
    """
    Check the head of the DataFrame.
    """
    display(df.head())

def excercise_c(df: DataFrame) -> None:
    """
    Use the .info() method to find out how many entries there are.
    """
    display(df.info())

def excercise_d(df: DataFrame) -> None:
    """
    What is the average BasePay?
    """
    print(f"The average BasePay is: ${df['BasePay'].mean():,.2f}\n")

def excercise_e(df: DataFrame) -> None:
    """
    What is the highest amount of OvertimePay in the dataset?
    """
    print(f"The highest amount of OvertimePay is: ${df['OvertimePay'].max():,.2f}\n")

def excercise_f(df: DataFrame) -> None:
    """
    What is the job title of  JOSEPH DRISCOLL ? Note: Use all caps, otherwise  
    you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll).
    """
    title = df.loc["JOSEPH DRISCOLL" == df['EmployeeName']]['JobTitle'].values[0]
    print(f"Joseph Driscoll's job title: {title}\n")

def excercise_g(df: DataFrame) -> None:
    """
    How much does JOSEPH DRISCOLL make (including benefits)?
    """
    amount = df.loc[df["EmployeeName"] == "Joseph Driscoll"]["TotalPayBenefits"].values[0]

    print(f"Joseph Driscoll's total pay benefits: ${amount:,.2f}\n")

def excercise_h(df: DataFrame) -> None:
    """
    What is the name of highest paid person (including benefits)?
    """
    print(f"The highest paid person is: {df.loc[df['TotalPayBenefits'] == df['TotalPayBenefits'].max()]['EmployeeName'].values[0]}\n")

def excercise_i(df: DataFrame) -> None:
    """
    What is the name of lowest paid person (including benefits)?
    Do you notice something strange about how much he or she is paid?
    """
    name, amount = df.loc[df["TotalPayBenefits"] == df["TotalPayBenefits"].min()][["EmployeeName", "TotalPayBenefits"]].values[0]

    print(f"The lowest paid person is: {name} who somehow gets paid ${amount}\n")

def excercise_j(df: DataFrame) -> None:
    """
    What was the average (mean) BasePay of all employees per year? (2011-2014)?
    """
    avg = df[df["Year"].between(2011, 2014)]["BasePay"].mean()

    print(f"average base pay is: ${avg:,.2f}\n")

def excercise_unique(df: DataFrame) -> None:
    """
    How many unique job titles are there?
    """
    print(f"There are ${len(df['JobTitle'].unique()):,} job titles\n")

def excercise_k(df: DataFrame) -> None:
    """
    What are the top 5 most common jobs?
    """
    print(f"The top 5 most common jobs:\n {df['JobTitle'].value_counts()[:5]}")

def excercise_l(df: DataFrame) -> None:
    """
    How many Job Titles were represented by only one person in 2013?
    (e.g. Job Titles with only one occurrence in 2013?)
    """

    group = df.groupby(by=["JobTitle"]).count().sort_values(by=["Id"], ascending=False)
    print(f"Job Titles with only one occurrence: {sum([x for x in group['Id'] if x == 1])}")

def excercise_m(df: DataFrame) -> None:
    """
    How many people have the word Chief in their job title? (This is pretty tricky)
    """
    amount = len([x for x in df['JobTitle'].to_numpy() if "chief " in x.lower()])

    print(f"Number of people with the word 'Chief' in their job title: {amount}")

def excercise_n(df: DataFrame) -> None:
    """
    Bonus: Is there a correlation between length of the Job Title string and Salary?
    """
    df["TitleLength"] = df["JobTitle"].apply(lambda x: len(x))

    corr = df[["TitleLength", "TotalPayBenefits"]].corr()
    corr.style.background_gradient(cmap='coolwarm')

    print(corr)

    sns.heatmap(corr)
    plt.show()

    plt.savefig("correlation.jpg")

if __name__ == "__main__":
    df = excercise_a()

    excercise_b(df)
    excercise_c(df)
    excercise_d(df)
    excercise_e(df)
    excercise_f(df)
    excercise_g(df)
    excercise_h(df)
    excercise_i(df)
    excercise_j(df)
    excercise_k(df)
    excercise_l(df)
    excercise_m(df)
    excercise_n(df)
