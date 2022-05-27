import pandas as pd
userid=pd.read_csv("user_id.csv")

#print(userid.to_numpy())
print(len(userid))
for i in range(0,len(userid)):
    userid['user_id'][i] ="hello"



