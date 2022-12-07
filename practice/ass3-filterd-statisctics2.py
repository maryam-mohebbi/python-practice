import numpy as np
import pandas as pd
import os


donatation = pd.read_csv(os.path.join("zuwendungen-berlin.csv"))
group_by_name = donatation.groupby(['Politikbereich'], as_index=False)[
    'Betrag'].agg({'min': 'min', 'median': 'median', 'max': 'max'})
filter = group_by_name['Politikbereich'] == 'Wissenschaft'
output = np.delete((np.array(group_by_name[filter])), 0)
print(output)
