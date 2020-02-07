import pandas as pd

data = {
       'disease':['hi',2,5],
       'id':[10,9,8]}
df = pd.DataFrame(data)

a = df[(df.disease=='hi')].index.tolist()
b = df[(df.disease==3)].index.tolist()
if a:
    print("hi")

if b:
    print("b")