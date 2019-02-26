import pandas as pd
import pylab as plt

# Create dataframe
file_name = "epochloss.csv"
df = pd.DataFrame.from_csv(file_name)
df.plot()
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.title('Epoch-Loss curve')
plt.show()
