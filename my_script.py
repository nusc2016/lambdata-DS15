import pandas

def enlarge(n):
    return n * 100

print("HELLO WORLD")

df = pandas.DataFrame({"state": ["CT", "CO", "CA", "TX"]})
print(df.head())

print("-----------------")
x = 5
print("NUMBER", x)
print("ENLARGED NUMBER", enlarge(x)) # invoking our function!!