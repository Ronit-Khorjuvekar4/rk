# Retrieve the entire row of data for the employee named 'Eva'.

import pandas as pd
import DataSet as ds

df = pd.DataFrame(ds.data)

empname = df.loc[df['name'] == 'Eva',:]

print(empname)