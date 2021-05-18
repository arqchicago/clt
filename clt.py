import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

# creating a skewed distribution with 1000 observations
random_data = 1000*np.random.gamma(1.95, 2.5, 1000)
random_data_df = pd.DataFrame(random_data, columns=['data'])
random_data_df = random_data_df.round(0)
print(random_data_df)

# visualizing the data distribution
fig, ax = plt.subplots()
plt.hist(random_data_df['data'], bins=100)
plt.title('original data distribution', fontsize=25)
ax.set_ylabel('Frequency')
ax.set_xlabel('data')
plt.savefig('output/orig_distribution.png')