import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('hubble.csv')
print(data.head())
data.set_index("distance", inplace=True)

data.plot()
plt.show()