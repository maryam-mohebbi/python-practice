import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from numpy import random
import os


donatation = pd.read_csv(os.path.join("zuwendungen-berlin.csv"))


group_by_name = donatation.groupby(['Politikbereich'], as_index=False)[
    'Betrag'].agg({'min': 'min', 'median': 'median', 'max': 'max'})
filter = group_by_name['Politikbereich'] == 'Wissenschaft'
a = (np.array(group_by_name[filter]))
print(a)
