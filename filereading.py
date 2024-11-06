import pandas as pd
df = pd.read_csv("C:\Users\User\Desktop\harsh31\pandas\Book1.csv")
#print(df.head())
ser = pd.Series(df['Name'])
print(ser)

# ser = pd.DataFrame(df[['name','rollno.']])
# print(ser)