#!/usr/bin/env python3 

import pandas as pd

# Paste collected from logger
# Example:
# summary_row = {'Calls Offered': ['16,915'], ' Abandon after 30s': ['2.32%'], 'FCR': ['86.50%'], 'DSAT ': ['14.20%'], 'CSAT ': ['78.30%']} 
summary_row = {}

df_summary = pd.DataFrame(summary_row, index=[0])
print(df_summary)


# Paste collected from logger
# Example:
# voc_col = {'Jan-18': [('Base Size', ['425']), ('Promoters', ['256', 'good']), ('Passives', ['86', 'bad']), ('Detractors', ['86', 'bad']), ('Overall NPS %', ['39.70%']), ('SAT with Agent %', ['78.30%']), ('DSAT with Agent %', ['14.20%'])]}
voc_col = {}

voc_col = pd.DataFrame(voc_col)
print(voc_col)
