import pandas as pd

data = [['Google', 10.], ['Runoob', 12.], ['Wiki', 13.]]
df = pd.DataFrame(data, columns=['site', 'age'])
print(df)
data1=[{'a':1,'b':2},{'a':5,'b':10,'c':20}]
df2=pd.DataFrame(data1)
print(df2)
data2={
    'calories':[420,380,390],
    'duration':[50,40,45]
}
df3=pd.DataFrame(data2)
df4=pd.DataFrame(data2,index=['day1','day2','day3'])
print(df3.loc[0])
print(df3.loc[1])
print(df3.loc[[1,2]])
print(df4.loc['day2'])