# Select the Salary of the employee with EmployeeID 104.

import pandas as pd
import DataSet as ds

df = pd.DataFrame(ds.data)

emp = df['employeeid'] == 104

print(df.loc[emp,'salary'].values())