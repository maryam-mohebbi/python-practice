import matplotlib.pyplot as plt
import seaborn as sns

iris_data = sns.load_dataset('iris')
fig, axs = plt.subplots(2, 2, figsize=(9, 6))
fig.subplots_adjust(hspace=0.35, wspace=0.35)

sns.boxplot(data=iris_data, x='species', y='sepal_length', ax=axs[0, 0])
sns.boxplot(data=iris_data, x='species', y='sepal_width',  ax=axs[0, 1])
sns.boxplot(data=iris_data, x='species', y='petal_length', ax=axs[1, 0])
sns.boxplot(data=iris_data, x='species', y='petal_width',  ax=axs[1, 1])
plt.show()

sns.pairplot(iris_data, hue='species', diag_kind='hist')
plt.show()
