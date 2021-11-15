#!/usr/bin/env python3 

import pandas as pd

row = {'Calls Offered': '22,343', ' Abandon after 30s': '3.0    5%', 'FCR': '86.00%', 'DSAT ': '18.00%', 'CSAT ': '74.40%'}
df = pd.DataFrame(row, index=[0])

print(df)
