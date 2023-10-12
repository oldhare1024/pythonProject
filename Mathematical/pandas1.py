import pandas as pd

print(pd.__version__)
mydata = {
    'sites': ["Google", "Ruboob", "WiKi"],
    'number': [1, 2, 3]
}
myvar = pd.DataFrame(mydata)
print(myvar)
a = [1, 2, 3]
myvar2 = pd.Series(a)
print(myvar2)
print(myvar2[2])
myvar3 = pd.Series(mydata['sites'], index=["x", "y", "z"])
sites1 = {1: "Google", 2: "Runoob", 3: "Wiki"}
myvar4 = pd.Series(sites1, index=[1, 2], name="RUNOOB-Series-TEST")
print(myvar3)
print(myvar3['y'])
print(myvar3)
print(myvar4)
