import pandas as pd
import os
file_name = "Student.txt"
df = pd.read_csv(file_name, sep="\t")
print("Students data:")
print(df)