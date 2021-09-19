# -*- coding: utf-8 -*-
"""HW3-Pandas

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HXxCCa0gceXXx68MdH7eEPg4zRrjcsCh
"""

import pandas as pd

# read earthquake:
# a) count 'magType' (ml) & 'type' (explosion)
# b) calculate mean(mag) in (Alaska & distance < 100km)
# c) calculate mean(mag) in each quarter (q1:m1-m3, q2:m4-m6, q3:m7-m9, q4: m10-m12), the 'time' field stores the milliseconds from 1/1/1970, hint: timestamp.

df = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Data /earthquakes (1).csv')
df.head(n=2)

df.info()

# a)
len(df[(df['magType'] == 'ml') & (df['type'] == 'explosion')])

# b)
dk = df[(df['place'].str.contains('Alaska')) &~ (df['place'].str.contains('\d{3,}',regex = True))]
dk.mag.mean()

# c)