import pandas as pd

# Todo : 1. Write a Pandas program to create and display a one-dimensional array-like object containing an array of data using Pandas module.

ds = pd.Series([2, 4, 6, 8, 10])
print(ds)

# Todo : 2.Write a Pandas program to convert a Panda module Series to Python list and it’s type.

ds = pd.Series([2, 4, 6, 8, 10])
print("Pandas Series and type")
print(ds)
print(type(ds))
print("Convert Pandas Series to Python list")
print(ds.tolist())
print(type(ds.tolist()))

# Todo : 3.Write a  Pandas program to convert Series of lists to one Series.

s = pd.Series([
    ['Red', 'Green', 'White'],
    ['Red', 'Black'],
    ['Yellow']])
print("Original Series of list")
print(s)
s = s.apply(pd.Series).stack().reset_index(drop=True)
print("One Series")
print(s)

# Todo : 4.Write a Pandas program to sort a given Series.
import pandas as pd
s = pd.Series(['100', '200', 'python', '300.12', '400'])
print("Original Data Series:")
print(s)
new_s = pd.Series(s).sort_values()
print(new_s)

# Todo : 5.Pandas program to add some data to an existing Series.
import pandas as pd
s = pd.Series(['100', '200', 'python', '300.12', '400'])
print("Original Data Series:")
print(s)
print("\nData Series after adding some data:")
new_s = pd.concat([s, pd.Series([500, "php"])], ignore_index=True)
print(new_s)

# Todo : 6.Write a Pandas program to calculate the number of characters in each word in a given series.
import pandas as pd
series1 = pd.Series(['Php', 'Python', 'Java', 'C#'])
print("Original Series:")
print(series1)
result = series1.map(lambda x: len(x))
print("\nNumber of characters in each word in the said series:")
print(result)

# Todo : 7.Write a Pandas program to get the items which are not common of two given series.
import pandas as pd
import numpy as np
sr1 = pd.Series([1, 2, 3, 4, 5])
sr2 = pd.Series([2, 4, 6, 8, 10])
print("Original Series:")
print("sr1:")
print(sr1)
print("sr2:")
print(sr2)
print("\nItems of a given series not present in another given series:")
sr11 = pd.Series(np.union1d(sr1, sr2))
sr22 = pd.Series(np.intersect1d(sr1, sr2))
result = sr11[~sr11.isin(sr22)]
print(result)


# Todo: 8.Write a  Pandas program to display most frequent value in a given series and replace everything else as ‘Other’ in the series.
import pandas as pd
import numpy as np
num_series = pd.Series(np.random.randint(1, 5, [15]))
print("Original Series:")
print(num_series)
print("Top 2 Freq:", num_series.value_counts())
result = num_series[~num_series.isin(num_series.value_counts().index[:1])] = 'Other'
print(num_series)


# Todo: 9.Write a Pandas program to find the positions of numbers that are multiples of 5 of a given series.
import pandas as pd
import numpy as np
num_series = pd.Series(np.random.randint(1, 10, 9))
print("Original Series:")
print(num_series)
result = np.where(num_series % 5==0)
print("Positions of numbers that are multiples of 5:")
print(result)


# Todo: 10.Write a Pandas program to get the positions of items of a given series in another given series.
import pandas as pd
series1 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
series2 = pd.Series([1, 3, 5, 7, 10])
print("Original Series:")
print(series1)
print(series2)
result = [pd.Index(series1).get_loc(i) for i in series2]
print("Positions of items of series2 in series1:")
print(result)


# Todo: 11.Write a Pandas program to calculate the number of characters in each word in a given series.
import pandas as pd
series1 = pd.Series(['Php', 'Python', 'Java', 'C#'])
print("Original Series:")
print(series1)
result = series1.map(lambda x: len(x))
print("\nNumber of characters in each word in the said series:")
print(result)


# Todo: 12.Write a  Pandas program to filter words from a given series that contain atleast two vowels.
import pandas as pd
from collections import Counter
color_series = pd.Series(['Red', 'Green', 'Orange', 'Pink', 'Yellow', 'White'])
print("Original Series:")
print(color_series)
print("\nFiltered words:")
result =color_series.map(lambda c: sum([Counter(c.lower()).get(i, 0) for i in list('aeiou')]) >= 2)
print(color_series[result])


# Todo: 13.Write a  Pandas program to replace missing white spaces in a given string with the least frequent character.
import pandas as pd
str1 = 'abc def abcdef icd'
print("Original series:")
print(str1)
ser = pd.Series(list(str1))
element_freq = ser.value_counts()
print(element_freq)
current_freq = element_freq.dropna().index[-1]
result = "".join(ser.replace(' ', current_freq))
print(result)


# Todo: 14.Check the equality of two given series
import pandas as pd
nums1 = pd.Series([1, 8, 7, 5, 6, 5, 3, 4, 7, 1])
nums2 = pd.Series([1, 8, 7, 5, 6, 5, 3, 4, 7, 1])
print("Original Series:")
print(nums1)
print(nums2)
print("Check 2 series are equal or not?")
print(nums1 == nums2)
