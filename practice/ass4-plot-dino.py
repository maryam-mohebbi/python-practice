import matplotlib.pyplot as plt
import pandas as pd

df_read = pd.read_table("data/DatasaurusDozen.tsv")
dino_df = df_read.where(df_read['dataset'] == 'dino')
fig = plt.figure(figsize=(7, 7))  # make square frame for plot
plt.plot(dino_df['x'], dino_df['y'], '.', markersize=3.5)
plt.tick_params(left=False, right=False, labelleft=False,
                labelbottom=False, bottom=False)
plt.show()
