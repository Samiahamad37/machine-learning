import pandas as pd
import numpy as np

data =  {
    "Name": ['samia', 'adam', 'hamad']


}
   

df = pd.DataFrame(data, index=[1, 2, 3])

print(df.loc[3])