import pandas as pd
import os


donatation = pd.read_csv(os.path.join("zuwendungen-berlin.csv"))
count = float(donatation.loc[:, 'Betrag'].count())
mean = float(donatation.loc[:, 'Betrag'].mean())
std = float(donatation.loc[:, 'Betrag'].std())
min = float(donatation.loc[:, 'Betrag'].min())
median = float(donatation.loc[:, 'Betrag'].median())
max = float(donatation.loc[:, 'Betrag'].max())
print(f'Count: {count} \nMean: {mean} \nStd: {std} \nMin: {min} \nMedian: {median} \nMax: {max}'
      )
