# **How much is Berlin spending on each U-Bahn?**

# At the time this dataset was created, there were 9 metro lines in Berlin.

# Use the previously loaded data frame of spendings, filter for transportation (German 'Verkehr'), group by the specific Ubahn and sum up the spendings. At the end, print the Ubahn names ordered from most (first element) to least expensive (last element).

# *Note*: For the Ubahn grouping you are interested in the column 'Zweck' (eng. 'purpose'). This column contains a short description of what exactly the money was spent on. The Ubahn signs - *U1, U2... U9* - are hidden in these descriptions. You need to find a way to extract these signs so that you can group according to them. Sometimes there is more than one Ubahn listed in the description; it is fine if you just extract the first one.

import pandas as pd
import os

donatation = pd.read_csv(os.path.join("zuwendungen-berlin.csv"))
donatation['Uban'] = donatation['Zweck'].str.extract(r'(\bU ?[1-9]\b)')
donatation['Uban'] = donatation['Uban'].str.replace(' ', '', regex=False)
grouped_uban = donatation.groupby(['Uban'], as_index=False)[
    'Betrag'].agg({'sum'})
print(grouped_uban)
