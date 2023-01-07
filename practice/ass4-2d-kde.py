import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

mean = [0, 0]
cov = [[5, 2], [2, 2]]

# generate 5000 samples from distribution and transpose them
x, y = np.random.multivariate_normal(mean, cov, 5000).T
sns.jointplot(x=x, y=y, kind="kde")
plt.show()
