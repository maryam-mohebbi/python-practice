# How much is each recipient of a spending receiving in total?

# Use the previously loaded data frame of spendings, group by recipient (column Name) and then sum all money received for each recipient. Print the names of the recipients that received in total 250 euros.

import pandas as pd
import os


donatation = pd.read_csv(os.path.join("zuwendungen-berlin.csv"))
group_by_name = donatation.groupby(['Name'])['Betrag'].agg(['sum'])
filter = group_by_name['sum'] == 250
result = group_by_name[filter]


print(result)
