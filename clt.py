import pandas as pd
import numpy as np


# creating a skewed distribution with 1000 observations
random_data = 1000*np.random.gamma(1.95, 2.5, 1000)
random_data_df = pd.DataFrame(random_data, columns=['data'])
random_data_df = random_data_df.round(0)
print(random_data_df)

# visualizing the data distribution