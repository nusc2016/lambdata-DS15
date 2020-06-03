from sklearn.model_selection import train_test_split
import pandas as pd

def enlarge(n):
    """
    Param n is a number
    Function will enlarge the number
    """
    return n * 100

# Split a dataframe into train, val, and test sets
def split(df):
    train1, val = train_test_split(df, train_size=0.85, test_size=0.15, random_state=42)
    train2, test = train_test_split(train1, train_size=0.8, test_size=0.2, random_state=42)
    return(train2, val, test)

# Assign datetime datatype to a column and then split into year, month, and day columns
def date_split(df, column):
    df['column'] = pd.to_datetime(df['column'], infer_datetime_format=True)
    df['year'] = df['column'].DateTimeIndex(df['column']).year
    df['month'] = df['column'].DateTimeIndex(df['column']).month
    df['day'] = df['column'].DateTimeIndex(df['column']).day
    return(df['year'],df['month'],df['day'])



# this code breaks our ability to import enlarge from other files, if left in the global scope:

if __name__ == "__main__":
#     # only run the code below IF this script is invoked from the command-line
#     # not if it is imported from another script
    print("HELLO")
    y = int(input("Please choose a number: "))
    print(y, enlarge(y))