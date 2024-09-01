
"""
# this is the original python tutorial from 2013
# It had ~ 100 questions in one file.
# Later it was split into multiple jupyter notebooks
"""

# Python Test 100
## Group Pandas 1 Questions 1..21


import os,sys
import pandas as pd
import numpy as np
from IPython.display import display, Image

aa = np.array([range(10),range(10)])
print(aa)
print(aa.shape)

print(pd.__file__)
print(pd.__version__)
print(np.__file__)
print(np.__version__)

### -------------------- Question 1 --------------------
# Explain how to install/upgrade pandas module

#### Answer

""" 
#    pandas stands for "Panel Data"
#    http://pandas.pydata.org/
#    It is a python module which is great for  analytical calculations.
#    Original author - Wes McKinney
# 
#    Installation - it comes with Anaconda Python.
#    It is recommended to add these two channels:
#      conda config --add channels anaconda
#      conda config --add channels conda-forge
#
#    Updates happen when you update anaconda:
#      conda update conda
#      conda update anaconda
#    
#    To play with pandas I recommend to use function ddd() defined below
""" 

mydict = {} # empty dict
mydict["c1"] = [1,2,3]
mydict['c2'] = [4,5,6]
print(mydict)
print('-'*40)
aa = pd.DataFrame(  mydict , 
                    index = ['mama','papa','me'],
                    columns = ['c2','c1'])
display(aa)
print('-'*40)
print(aa.columns)

aa.index[1]

# --------------------------------------------------------------
def ddd(nrows=10):
    """
    # returns a simple pandas DataFrame - useful for quick tests
    # nrows is number of rows (divisible by 10), for example:
    #     df = ddd()
    #     df = ddd(100)
    #     df = ddd(10**6)   # million rows
    """
    n_aa = 10
    nn = int(nrows/n_aa)
    if nn < 1:
        nn = 1
    aa = pd.DataFrame({
          'ii':nn*[0,1,2,3,4,5,np.nan,7,8,9],
          'i1':nn*[6,5,4,3,2,1,0,-1,-2,-3],
          'i2':nn*[6,5,4,4,1,1,0,-1,-2,-3],
          'ff':nn*[0.0,1.0,2.0,np.NaN,4.0,5.0,6.0,7.0,8.0,9.0],
          'f1':nn*[0.0,1.01,2.002,3.0003,4.00004,5.000005,6.0000006,7.0,8.0,9.0],
          'f2':nn*[1.11,2.22,3.33,4.44,5.55,7.77,9.99,0.01,-0.01,-1.11],
          'ss':nn*['s0','s1','狗','汽车',np.nan,'s5','s6','s7','s8','s9'],
          's1':nn*list(np.array(['s0','s1','s2','s2',np.nan,'s5','s6','s7','s8','s9'],dtype=np.str)),
          's2':nn*['1.11','2.22','3.33','4.44','5.55','7.77','9.99','0.01','-0.01','-1.11'],
          'bb':nn*[True, False, True, False, np.nan, False, True,np.nan, False, True],
          'b1':nn*[True, False, True, False, True, False, True, True, False, True],
          'xx':nn*list(range(n_aa)),
          'yy':nn*[x*50 + 60 + np.random.randn() for x in range(n_aa)]
    })
    aa = aa[['ii','i1','i2','ff','f1','f2','ss','s1','s2','bb','b1','xx','yy']].copy()
    aa.index = range(len(aa))

    if 1 <= nrows < 10:
        aa = aa[:nrows+1]
        
    return aa

# --------------------------------------------------------------
aa = ddd()
display(aa.head(5).tail(2))
print("-"*40)
display(aa.tail(6).T.copy())

### -------------------- Question 2 --------------------

#    - Show how to test the type of the variable (is it an int? float? str?, list? dict? etc.) 
#    - Show how to test type of a column in a DataFrame 
#    - Show how to list types of all columns in a DataFrame


#### Answer

type({1:2,3:4})
aa = ddd()
aa['i1'].dtype

print("type of a python variable")

# -------------------------------------
def print_type(obj):
    if type(obj) == int:
        print("  int")
    elif type(obj) == float:
        print("  float")
    elif type(obj) == str:
        print("  str")
    else:
        print("  unknown type")

print_type(1)
print_type(1.1)
print_type('mama')
print_type([1,2,3])

print("type of pd.DataFrame column")
aa = ddd()
print("aa.f1.dtype    = ",aa.f1.dtype)
print("aa['f1'].dtype = ",aa['f1'].dtype)

print('-'*40)
print("types of all pd.DataFrame columns")
print(aa.dtypes)

### -------------------- Question 3 --------------------

#    Show how to take a value from a particular cell of a dataframe
#     - using df[col][row]                  # label based
#     - using df.loc [row_label, col_label] # label based
#     - using df.iloc[row_index, col_index] # indexes start with 0

#### Answer

aa = ddd()
aa.index = range(len(aa))
# aa.index = range(len(aa)-1,  -1,  -1)
print("aa['i2'][1]     =", aa['i2'][1]   )     # order: column(s), row(s)
print("aa.loc [1,'i2'] =", aa.loc [1,'i2'] )   # order: row(s), column(s)
print("aa.iloc[1,1]    =", aa.iloc[1, 1  ] )   # order: row(s), column(s)

aa = ddd()
mask = (aa.f1 >= 1.5) & (aa.f1 < 5)
print(mask)
aa[mask]
# aa[2:4]
# aa

aa=ddd()
N = len(aa)
aa.index = range(N-1,-1,-1)
aa.loc[2,'ii']

aa = [5,6,7,8,9,10,11,12]
bb = aa[:]
cc = aa
cc = aa
for ii in range(len(cc)):
    cc[ii] = pow(cc[ii],2)
print(id(aa))
print(id(cc))
print(id(bb))
print(aa)
print(cc)

x = 100000000
e = (1+1/x)**x
print(e)

# Note:
#   loc  - by labels
#   iloc - by integer numbers of rows/columns - count starts with 0
#   ix   - deprecated, can do both

aa = ddd()
aa = aa.loc[:,['ii','i1','i2']] # [rows,cols]
aa.index = range(len(aa))  # 0,1,...,5,6
aa.index = aa.index.map(lambda x: 'm' + str(x))
display(aa)
#     id  i1  i2
# m0   0   6   6
# m1   1   5   5
# m2   2   4   4
# m3   3   3   4
# m4   4   2   1
# m5   5   1  1
# m6 NaN   0   0
print('-'*40)
print(aa.loc['m2','i2'])  # 4
# aa.iloc['m2','i2'] # ERROR
print(aa.iloc[2,2])       # 4

### -------------------- Question 4 --------------------

#    Extract a row from a DataFrame into a regular python list

#### Answer

aa=ddd()
print(aa.loc[1,:].values.tolist())
print(aa.loc[1,:].tolist())
print(aa.iloc[len(aa)-1].tolist())

aa=ddd()
type(aa.i1.values)

### -------------------- Question 5 --------------------

#    - Show to find rows which has the same value in a particular column
#    - Show how to use value_counts()
#    - Show how to count number of times each unique value appears in group, and for multiple columns 
#    - What is np.unique - and how is it used?
#    - Write a procedure to extract duplicate rows (by one or more columns)

#### Answer

# duplicated() - create true/false mask
aa=ddd()
aa.duplicated(['i2'])

# value_counts()
# Returns pd.Series containing counts of unique values (excluding NaN)
# in descending order (the first element is the most frequently occuring).

aa['i2'].value_counts()

# Show how to count number of times each unique value appears in group, and for multiple columns

data = [
  ['amazon.com',  'correct',   'correct'  ], 
  ['amazon.com',  'incorrect', 'correct'  ], 
  ['walmart.com', 'incorrect', 'correct'  ], 
  ['walmart.com', 'incorrect', 'incorrect']
]

source = pd.DataFrame(data, columns=['domain', 'price', 'product'])

source.groupby('domain').apply(lambda x: x[['price','product']].apply(lambda y: y.value_counts())).fillna(0)

# np.unique is a Numpy function which shows unique values in a column,
# and where they were found first time.

aa=ddd()
np.unique(aa.i2)

# a procedure to extract duplicate rows (by one or more columns)

# --------------------------------------------------------------
def show_duplicates(df, cols=[], include_nulls=True):
    """
    # accepts a dataframe df and a column (or list of columns)
    # if list of columns is not provided - uses all df columns
    # returns a dataframe consisting of rows of df
    # which have duplicate values in "cols"
    # sorted by "cols" so that duplciates are next to each other
    # Note - doesn't change index values of rows
    """
    # ---------------------------------
    aa = df.copy()
    mycols = cols
    # ---------------------------------
    if len(mycols) <= 0:
        mycols = aa.columns.tolist()
    elif type(mycols) != list:
        mycols = list(mycols)
    # ---------------------------------
    if not include_nulls:
        mask = False
        for mycol in mycols:
            mask = mask | (aa[mycol] != aa[mycol])  # test for null values
        aa = aa[~mask]                              # remove rows with nulls in mycols
    if len(aa) <= 0:
        return aa[:0]
    # ---------------------------------
    # duplicated() method returns Boolean Series denoting duplicate rows
    mask = aa.duplicated(subset=mycols, keep='first').values \
         | aa.duplicated(subset=mycols, keep='first').values
    aa = aa[mask]
    if len(aa) <= 0:
        return aa[:0]
    # ---------------------------------
    # sorting to keep duplicates together
    # Attention - can not sort by nulls
    # bb contains mycols except for cols which are completely nulls
    bb = aa[mycols]
    bb = bb.dropna(how='all',axis=1)
    # sort aa by columns in bb (thus avoiding nulls)
    aa = aa.sort_values(by=bb.columns.tolist())
    # ---------------------------------
    # sorting skips nulls thus messing up the order. 
    # Let's put nulls at the end
    mask = False
    for mycol in mycols:
        mask = mask | (aa[mycol] != aa[mycol])  # test for null values
    aa1 = aa[~mask]
    aa2 = aa[mask]
    aa = aa1.append(aa2)

    return aa

# --------------------------------------------------------------
aa = ddd()
show_duplicates(df=aa, cols=['i2'], include_nulls=True)

### -------------------- Question 6 --------------------

#    - Show how to append dataframes
#    - Show how to append a list (or series) of data to a dataframe

#### Answer

# append two dataframes one on top of the other
aa1 = ddd(5)
aa2 = ddd(5)
aa = aa1.append(aa2)
aa.index = range(len(aa))
display(aa)

# append a series or list by converting it to a DataFrame
aa = ddd()
bb = aa.loc[1].tolist()   # take 2nd row as a list
dd = pd.DataFrame([bb], columns=aa.columns)

# now append list
aa = aa.append(dd)
display(aa)

# Note: alternatively you can make 1-column dataframe - and transpose it
# bb=DataFrame(ss)
# bb.index = aa.columns
# aa.append(bb.T)

### -------------------- Question 7 --------------------

#    Show how to remove duplicate rows (duplicate is defined as having same value in a list of columns)

#### Answer

aa = aa.drop_duplicates(['i2']) 
# or
aa = aa.drop_duplicates(['i2'], keep='last') 
display(aa)

### -------------------- Question 8 --------------------

#    Show how to use a mask using   &, |, ~, .isin(), .isnull()

#### Answer

aa=ddd()
mask = aa.f2.isnull()
display(aa[mask])
print('-'*40)
mask = aa.i1.isin([1,3,5])
display(aa[mask])
print('-'*40)
display(aa[~mask]) # shows the records where mask is False
print('-'*40)

# examples of masks based on more than one column
# mask = (aa.ii==1) & (aa.i2 == 4)
# mask = (aa.ii==1) | (aa.i2 == 4)

### -------------------- Question 9 --------------------

#    Give an example of using a map() function on a pandas DataFrame column

#### Answer

aa=ddd()
str(aa.yy)

aa=ddd()
display(aa.yy.dtype)
aa['yy'] = aa.yy.map(lambda crocodile : str(round(crocodile,2)) + "abc")
display(aa)

### -------------------- Question 10 --------------------

#    Give example using map with lambda for dataframe operations


#### Answer

aa = ddd()
aa['s2'] = aa.ss + '__' + aa.i1.map(lambda x: str(x))

# make a list of values in column 'yy' 
# rounded to 2 digits after dot
aa['zz'] = aa['yy'].map(lambda x: round(x,2))
display(aa)

### -------------------- Question 11 --------------------

#    Give example using groupby().sum()

#### Answer

aa = ddd()
cc = aa.groupby(['i2'], as_index=False).sum()
display(cc)
print("-"*40)

# note - groupby().sum() will usually remove all 
# string columns from the result. To avoid it, you can use agg()
# But be carefull to avoid mixing NaN with strings - causes error 

aa = ddd()
aa['ss'] = aa.ss.fillna('_') # this removes NaN
cc = aa.groupby('i2', as_index=False).agg({'i1':np.sum,'ss':np.max})
display(cc)

### -------------------- Question 12 --------------------

#    Give example using groupby().aggregate()

#### Answer

aa = ddd()
bb = aa.groupby('i2', as_index=True).aggregate({'yy':np.sum, 'xx':np.max}) 
display(bb)

### -------------------- Question 13 --------------------

#    Show how to sort a dataframe by a list of columns

#### Answer

cc = aa.sort_values(by=['i2','yy'])
display(cc)

### -------------------- Question 14 --------------------

#    Show how to delete some rows from dataframe - and reindex

#### Answer

aa = ddd()
aa = aa.drop([1,3,5]) # remove several rows 
display(aa)

# remove rows based on a mask
aa = ddd()
mask = aa['ii'].map(lambda x: x > 3) # True when aa.ii > 3
aa = aa[~mask]                       # take only where a.ii <= 3 or NaN
display(aa)
print('-'*40)
mask = aa['ii'].map(lambda x: x in (0,1,4))
aa = aa[~mask]
display(aa)

# after removing rows you may want to index rows sequentially
aa = ddd()
aa.reindex() # doesn't change index unless you provide it 
print('-0'*30)
aa.index = range(len(aa))
display(aa)
print('-1'*30)
# note - you can shift index
aa.index = range(100,100+len(aa))
display(aa)
print('-2'*30)
# you can even make all index values the same - although it is pointless
aa.index = [2]*len(aa)
display(aa)

### -------------------- Question 15 --------------------

#    Show how to add rows to a dataframe 
#    (add 2 dataframes together vertically - and reindex)

#### Answer

aa=ddd()
aa = aa.append(aa[2:4],ignore_index=True)
display(aa)

### -------------------- Question 16 --------------------

#    - Show how to write dataframe to csv file
#    - Show how to read it back

#### Answer

aa = ddd()
aa.to_csv('junk.csv', sep='|', header=True, index=False)
bb = pd.read_csv('junk.csv', sep='|')
display(bb)

### -------------------- Question 17 --------------------

#    - Show how to add columns to pandas DataFrame
#    - Show how to calculate column values from numeric/string values in other columns.
#    - Show how to delete one or more columns

#### Answer

aa = ddd()
aa['c4'] = None         # populate with same value
display(aa)
print('-0'*30)
col2=[1,2,3,4,5,6,7,8,9,0]
aa['c4'] = col2         # list becomes a column
display(aa)
print('-1'*30)
aa['c4'] = "-"
display(aa)
print('-2'*30)

# adding a column - and populating it using vectorized operation on columns
aa['c5']= 2*aa['i1'] + 3*aa['i2'] + 5
display(aa)
print('-3'*30)

# calculating column values from other columns:
aa['c4']= 2*aa['i1'] + 3*aa['i2'] + 5
aa['s2'] = aa.ss + '__' + aa.i1.map(lambda x: str(x))
display(aa)
print('-4'*30)

# Deleting one column
del aa['s1']
display(aa)
print('-5'*30)

# Deleting many columns
aa = aa.drop(['i1','i2','c4'], axis=1)
display(aa)

### -------------------- Question 18 --------------------

#    Show how to calculate a pandas DataFrame column 
#    as a linear combination of some other columns

#### Answer

aa = ddd()
aa['c4']= 2*aa['i1'] + 3*aa['i2'] + 5 
display(aa)

### -------------------- Question 19 --------------------

#    Show how to calculate a DataFrame column 
#    from several other columns while using str() and int().<br>
#    Hint - use map(lambda ..)

#### Answer

aa = ddd()
aa['s3'] = aa['yy'].map(lambda x: int(x)) 
aa['s4']= '>>>' + aa.s3.map(lambda x: str(x)) + '<<<'
display(aa)

### -------------------- Question 20 --------------------

#    Show how to define a mask using regex on one column, 
#    and numeric comparison on the other column

#### Answer

import re
aa = ddd()
mask = (aa.i2.map(lambda x: True if re.search(r'4',str(x)) else False)) & (aa.xx > 2)
display(mask)
display(aa[mask])

# more examples
# mask = ( df.a == 1) & (df.b == 2)
# mask = ( df.a == 1) | (df.b == 2)
# mask = ( df.a == 1) | df.b.isin([1,2,3])
# mask = ( df.a == 1) | df.b.map(lambda x: ......)
# mask = ( df.a == 1) | df.b.map(lambda x: ......)  |  df.c.map(lambda x: ......) 

### -------------------- Question 21 --------------------

#    String operations on columns
#    How to define a mask using a regular expression

aa = ddd()
mask = aa.ss.map(lambda x: True if re.search(r's[1,3]',str(x)) else False)
display(aa[mask])

# --------------------------------------------------------------
# Python Test 100
## Group Pandas 2 Questions 1..19

import os,sys
import pandas as pd
import numpy as np
from IPython.display import display

# --------------------------------------------------------------
def ddd(nrows=10):
    """
    # returns a simple pandas DataFrame - useful for quick tests
    # nrows is number of rows (divisible by 10), for example:
    #     df = ddd()
    #     df = ddd(100)
    #     df = ddd(10**6)   # million rows
    """
    n_aa = 10
    nn = int(nrows/n_aa)
    if nn < 1:
        nn = 1
    aa = pd.DataFrame({
          'ii':nn*[0,1,2,3,4,5,np.nan,7,8,9],
          'i1':nn*[6,5,4,3,2,1,0,-1,-2,-3],
          'i2':nn*[6,5,4,4,1,1,0,-1,-2,-3],
          'ff':nn*[0.0,1.0,2.0,np.NaN,4.0,5.0,6.0,7.0,8.0,9.0],
          'f1':nn*[0.0,1.01,2.002,3.0003,4.00004,5.000005,6.0000006,7.0,8.0,9.0],
          'f2':nn*[1.11,2.22,3.33,4.44,5.55,7.77,9.99,0.01,-0.01,-1.11],
          'ss':nn*['s0','s1','狗','汽车',np.nan,'s5','s6','s7','s8','s9'],
          's1':nn*list(np.array(['s0','s1','s2','s2',np.nan,'s5','s6','s7','s8','s9'],dtype=np.str)),
          's2':nn*['1.11','2.22','3.33','4.44','5.55','7.77','9.99','0.01','-0.01','-1.11'],
          'bb':nn*[True, False, True, False, np.nan, False, True,np.nan, False, True],
          'b1':nn*[True, False, True, False, True, False, True, True, False, True],
          'xx':nn*list(range(n_aa)),
          'yy':nn*[x*50 + 60 + np.random.randn() for x in range(n_aa)]
    })
    aa = aa[['ii','i1','i2','ff','f1','f2','ss','s1','s2','bb','b1','xx','yy']].copy()
    aa.index = range(len(aa))

    if 1 <= nrows < 10:
        aa = aa[:nrows+1]
        
    return aa

### -------------------- Question 2.1 --------------------

#    Changing the order of columns in a DataFrame.

#### Answer

aa = pd.DataFrame({
    'a' : [0,1,2],
    'b' : [0,2,4],
    'c' : [0,1,3]
})
display(aa)

col_list_ordered = ['b','c','a']    # When you reorder using these methods, 
                                    # the data in the columns also shift 
                                    # along with names 
aa = aa[col_list_ordered]
display(aa)

print('-'*40)

# or (notice double-brackets)
aa = aa[['c','b','a']]
display(aa)

aa.columns = ['b','a','c']    # Rename columns without changing 
                              # contents of the columns
display(aa)

### -------------------- Question 2.2 --------------------

#    Show how to check if a dataframe has a column with a particular name

#### Answer

aa = ddd()
display(aa.head())
if 'i2' in aa.columns:
    print("true")

### -------------------- Question 2.3 --------------------

#    Select rows of a pandas DataFrame which have null values 
#    (in any column)

#### Answer

mask = False
def rows_with_nulls(df):
    # mask=pd.Series(data = [False]*len(df), index = df.index)
    # mask = False
    global mask
    for col in df.columns:
        # print(mask)
        mask = mask | df[col].isnull()  # series with value=True 
                                        # for rows wirth null values
    return df.loc[mask,:].copy()

aa = ddd()
display(aa)
print('-' * 40)
bb = rows_with_nulls(aa)
display(bb)

### -------------------- Question 2.4 --------------------

#    Show how to substitute for null values 
#    - in a column 
#    - in the whole dataframe

#### Answer

# IN COLUMN
aa = ddd()
display(aa)
aa['ss'] = aa.ss.fillna('hello')
#          aa.ss.fillna(0)
#          aa.ss.fillna('-')
display(aa)
print('-'*40)

# IN ENTIRE DATAFRAME
aa = ddd()
aa.fillna(0, inplace=True)
display(aa)

### -------------------- Question 2.5 --------------------

#    Can an integer column in pandas DataFrame have a NaN value?

#### Answer

"""
#    No. Float column can.
#    If you insert a NaN value into integer column, 
#    the column type will silently be changed to float64
"""

aa = ddd()
display(aa)
print(aa.i1.dtype)
aa.loc[1,'i1'] = np.NaN
print(aa.i1.dtype)
display(aa)

### -------------------- Question 2.6 --------------------

#    Show how to convert value type of a column to int64 or float64 

#### Answer

aa = ddd()
display(aa)
print(aa.i1.dtype)
aa['i1'] = aa.i1.astype(np.float64)
print(aa.i1.dtype)
display(aa)
aa['i1'] = aa.i1.astype(np.int64)
print(aa.i1.dtype)
display(aa)

### -------------------- Question 2.7 (Exercise) --------------------

#    Do the following:
#    - Take first several rows for a dataframe (regardless of index)
#    - Take last several rows of a dataframe (regardless of index)
#    - Take group of rows in the middle (regardless of index)
#    - Take one row as a list (first / last / middle)


#### Answer

print("first rows as dataframe")
aa = ddd()
print(aa.head())  # by default takes up to 5 rows
print('-'*40)
print(aa.head(2)) 
print('-'*40)
print(aa[:3]) # slice - same as .head(3)
print('-'*40)
print("last rows as dataframe")
print(aa.tail())
print('-'*40)
print(aa[-5:])
print('-'*40)

print("rows in the middle as dataframe")
print(aa[2:4])

print("Take one row as a list (first / last / middle)")
print(aa.loc[aa.index[0]].tolist())
print(aa.loc[aa.index[-1]].tolist())
print(aa.loc[aa.index[3]].tolist())

### -------------------- Question 2.8 --------------------

#    Show how to take the first row of a DataFrame as a list or dict

#### Answer

aa = ddd()
#aa.index = [6,5,4,3,2,1,0]
display(aa)
mylist = aa.loc[aa.index[0]].tolist()
mydict = aa.loc[aa.index[4]].to_dict()
print(mylist)
print(mydict)

### -------------------- Question 2.9 --------------------

#    Show the following ways of combining two pandas DataFrames
#    - merge
#    - append
#    - concat
#    - combine_first

#### Answer

# Pandas DataFrames are similar to SQL database tables.
# they can be joined using two mechanisms: join() and merge()
# join() does joining on indexes, merge() - on columns
# I usually use merge()
#
# df_joined = merge(df1, df2, on=[columns], how='inner')
# df_joined = merge(df1, df2, on=[columns], how='left')

# This is exactly like joining 2 tables in SQL
# you can use inner join ('inner') or left outer join ('left')

# append allows to append two DataFrames vertically one on top of another
# 
df = aa.append(bb,ignore_index=True)
display(df)

# concat() allows to stack DataFrames vertically (default) or horizontally
#   concat([s1,s2,s3])      - stacks together objects along an axis (vertically)
#   concat([aa,bb],axis=1) - stacking horizontally

aa = ddd()
bb = ddd()
display(aa)
cc = pd.merge(aa, bb, on='i2')
display(cc)
# pd.merge?

# df1.combine_first(df2)
#   Combine two DataFrames
#   uses df2 to fill-in null values in df1

df1 = pd.DataFrame([[1, np.nan]])
df2 = pd.DataFrame([[3, 4]])
aa = df1.combine_first(df2)
display(df1)
print('---------')
display(df2)
print('---------')
display(aa)

### -------------------- Question 2.10 --------------------

#    Show the following:
#    - pandas stack()/unstack() functions
#    - grouping by mask

#### Answer

xx = pd.DataFrame(
    [ ["Jan","name1", 1, 2, 3],   
      ["Jan","name2", 4, 5, 6],
      ["Mar","name1",11,12,13],
      ["Mar","name2",14,15,16] 
    ],
    columns=["Month","Name","c1","c2","c3"])

display(xx)
print('-----------------------------')
# convert Month and Name into index
yy = xx.set_index(["Month","Name"])
display(yy)
print('-----------------------------')
# Stack all remaining columns (c1,c2,c3) - make a one-column Series
yy = xx.set_index(["Month","Name"]).stack()
display(yy)
print('-----------------------------')
yy = xx.set_index(["Month","Name"]).stack().unstack('Month')
display(yy)
print('-----------------------------')

mask = yy.Jan > 3
zz = yy.groupby(by=mask).sum()
display(zz)

### -------------------- Question 2.11 --------------------

#    Show use of pandas DataFrame.pivot()

#### Answer

aa = pd.DataFrame(
    { 'foo' : 3*['one'] + 3*['two'],
      'bar' : 2*['A','B','C'],
      'baz' : [1,2,3,4,5,6]
    }
)

aa = aa[['foo','bar','baz']]
display(aa)
print("---------------")
#       foo bar  baz
#    0  one   A    1
#    1  one   B    2
#    2  one   C    3
#    3  two   A    4
#    4  two   B    5
#    5  two   C    6

display(aa.pivot('foo','bar','baz'))
print("---------------")
display(aa.pivot('foo', 'bar')['baz'])

### -------------------- Question 2.12 --------------------

#    Create a pandas DataFrame and populate with data
#    - from dict of columns,
#    - from list
#    - from numpy array
#    - from list of series
#    - from list of lists

#### Answer

df = pd.DataFrame({
    'x'  : 3 * ['a'] + 2 * ['b'],
    'nn' : np.arange(5, dtype=np.float64), 
    'y'  : np.random.rand(5),
    'z'  : range(5)
})


df = pd.DataFrame([[1,2,3]], columns=['A','B','C'])

df = pd.DataFrame(
    np.arange(12).reshape((3,4)),
    index = ['A','B','C'],
    columns = ['AA','BB','CC','DD']
)

display(df)
nrows  = 10
ncols  =  5
mydata = np.random.rand(nrows, ncols)

# mydata = np.random.randn(nrows, ncols)

aa = pd.DataFrame(data=mydata)
aa = pd.DataFrame(data=mydata, 
                  index=range(nrows), 
                  columns=[chr(65+x)*2 for x in range(ncols)])

aa = pd.DataFrame( np.random.normal(size=12).reshape((3,4)), 
                   index = ['A','B','C'], 
                   columns = ['AA','BB','CC','DD'] )

s1 = pd.Series({'x':1,'y':2})
s2 = pd.Series({'x':3,'y':4})
aa = pd.DataFrame([s1,s2])   # s1 and s2 - rows

mydata = [[1,2],[3,4],[5,6]]
aa = pd.DataFrame(mydata, columns=['AA','BB'])

### -------------------- Question 2.13 --------------------

#    Generate random numbers to populate a DataFrame
#    use Numpy  np.random

#### Answer

# np.random.<TAB>
# np.random.seed(int)
Ncols = 4
Nrows = 5

# several ways to generate numbers
data = np.random.rand(Nrows, Ncols)
data = np.random.randn(Nrows, Ncols)
data = np.random.normal(size=Nrows*Ncols).reshape(Nrows,Ncols)
data = np.random.normal(size=Nrows*Ncols, loc=10.0, scale=1.0).reshape(Nrows,Ncols)

aa = pd.DataFrame(data, columns = ['c1','c2','c3','c4'] )
print(aa)

## -------------------- Question 2.13a --------------------

#    df.groupby().apply(func)
#    transform a row using flexible 
#    custom function operating on all columns

list(range(4,-1,-1))

df = pd.DataFrame({'aa':range(5), 'bb':range(5)})
print(df) # 5 rows
print('-'*40)

# ------------------------------------
def myfunc(df):
    """ This function is applied to a subset (groupping) of rows"""
    df['lev'] = df['aa'].map(lambda x: str(x**2)) + '_' + df['bb'].map(lambda x: str(x**2))
    df['bb'] = df.bb**3
    return df

df2 = df.groupby(df.bb, as_index=False).apply(myfunc)
print(df2)

### -------------------- Question 2.14 --------------------

#    Show how to iterate through rows of pandas DataFrame

#### Answer

aa=ddd()
for rr in aa.itertuples(): 
    print(rr)

print('-'*40)
for rr in aa.itertuples(index=False): 
    print(rr)

# pd.DataFrame.iterrows()  - a generator
#     yields tuple (index, row_as_Series)
#     Slow, because needs to create a Series from each row.
  
print('-'*40)
for row in aa.iterrows():
    ind = row[0]
    ser = row[1]
    cols = list(ser.index)
    vals = list(ser)
    print("ind = ",ind,", vals = ",vals)

print('-'*40)
for row in aa.iterrows():
    print(row[1].values)
print('-'*40)
for row in aa.iterrows():
    print(list(row[1].values))

# Another way:
# for ii in aa.index: 
#     do_something(aa.ix[ii])

### -------------------- Question 15 --------------------

#    Show how to do string operations on columns

#### Answer

aa = pd.DataFrame({
    'ss':['aa1','bb2','cc3',np.nan],
    'ff':['  11.11  ','  22.22  ','  33.33  ','  44.44  '],
    'ii':['  11     ','  22     ','  33     ','  44     ']
})
display(aa)
# use str method on Series/Column:
# aa.ss.str.<TAB>
print(aa.ss.str.contains('bb'))
print('-'*40)
print(aa.ss.str[:2])   # first 2 characters
print('-'*40)
print(aa.ss.str.upper())
print('-'*40)
print(aa.ss.str.len())
print('-'*40)
# etc.

# using regular expression
mask = aa.ss.map(lambda x: True if re.search(r'b[23]',str(x)) else False)
print(mask)
print('-'*40)
# --------------------
# convert from string to number and back
# aa['zz'] = aa.ff.astype(np.int64) # error
aa['zz'] = aa.ff.map(lambda x: int(float(x)) if x==x else np.nan).astype(np.int64)
display(aa)
print('-'*40)

aa['zz'] = aa.ii.astype(np.int64) # works
display(aa.zz.dtype)
aa['zz'] = aa.ff.astype(np.float64) # works
aa['zz'] = aa.ii.astype(np.float64) # works
print(aa.zz.dtype)
aa['zz'] = aa.ii.str.strip().astype(float)
print(aa.zz.dtype)
aa['zz'] = aa.ii.str.strip().str[0].astype(int)
print(aa.zz.dtype)
aa['zz'] = aa.ff.astype(object)  # use this to work with a string
print(aa.zz.dtype)
aa['zz'] = aa.ff.astype(str)     # silent error?
print(aa['zz'])
print(aa.zz.dtype)

# mask = aa.ss.str.match(r'1|3') - doesn't work yet
# mask = aa.ss.get(label) # ?? 

### -------------------- Question 2.16 --------------------

#    Make a histogram (cutting data into bins) from DataFrame

#### Answer

aa=np.random.normal(size=100)
print(aa)
bins=[-3, -2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5, 3]
vals = pd.cut(aa,bins)
pd.value_counts(vals)

# also look at pd.qcut

### -------------------- Question 2.17 --------------------

#    - Show how to get a short summary of data in the numeric DataFrame?
#    - Show how to remove outliers (values which are too big or small)

#### Answer

# short answer: use df.describe() method

aa = ddd()
#display(aa)
display(aa.describe())
print("-"*40)

np.random.seed(12345)
df = pd.DataFrame(np.random.randn(1000, 4), columns=['A','B','C','D'])
print(df)
print("-"*40)
print(df.describe())
print("-"*40)
print(df.describe().index)  # [count, mean, std, min, 25%, 50%, 75%, max]
print("-"*40)

### Here is how to remove outliers

# look at outliers (numbers with abs. value more than 1.5)
df = pd.DataFrame(np.random.randn(10, 4), columns=['A','B','C','D'])
mask = np.abs(df) > 1.5
print("type of the mask is - ", type(mask))
print("Here is the mask:")
display(mask)
print("Here is the series showing for each row")
print("if it contains a True value in any column:")
display(df[mask].any(1)) # True if there is a True value in any column

# remove outliers - limit the value by 
print("-"*40)
df[mask] = np.sign(df) * 1.5
display(df)

### -------------------- Question 2.18 --------------------

#    Show how to search and replace values in a column in a DataFrame

#### Answer

# most common way is in 2 steps:
#   step1 - create a mask to identify rows in which we need to do the change
#   step2 - do the change to the column using the mask
#   df.loc[mask,'col1'] = df.col1[mask] + df.col2[mask]

# alternative may be to use replace based on value(s)
#   df.col1.replace(list_of_values, replacing_value)
# or
#   df.col1.replace({val1:repl1, val2:repl2, etc.})

### -------------------- Question 2.19 --------------------

Difference between .apply() and .transform()

#### Answer

# it is described here:
# https://stackoverflow.com/questions/27517425/apply-vs-transform-on-a-group-object

# There are two major differences between 
# the transform and apply groupby methods.

# apply implicitly passes all the columns for each group 
# as a DataFrame to the custom function, 

# while transform passes each column for each group 
# as a Series to the custom function

# The custom function passed to apply 
# can return a scalar, or a Series or DataFrame 
# (or numpy array or even list). 

# The custom function passed to transform 
# must return a sequence (a one dimensional Series, array or list) 
# the same length as the group.

# So, transform works on just one Series at a time 
# and apply works on the entire DataFrame at once.

# Example
df = pd.DataFrame({'State':['Texas', 'Texas', 'Florida', 'Florida'], 
                   'a':[4,5,1,3], 'b':[6,10,3,11]})
display(df)

def subtract_two(x):
    return x['a'] - x['b']

# The above function will not work with transform()
# because it references two columns
#      df.groupby('State').transform(subtract_two)
#      KeyError: ('a', 'occurred at index a')

# But it will work OK with apply():
df.groupby('State').apply(subtract_two)

# Example of usage
df = pd.DataFrame({"c1":['shirt','shirt','pants','pants'],
                   "c2":['white','blue','black','brown'],
                   "amnt":[100,200,300,100]})
display(df)

# lets index by c1,c2:
df = df.set_index(['c1','c2'])
display(df)

# now lets calculate the percentage of each color 
# for each clothing type (shirt or pants):
df = df.groupby(level=0).transform(lambda x: 100*x/x.sum())
display(df)

-------------------- Question 2.20 --------------------
# df.aggregate()

df = pd.DataFrame([[1,      2,      3     ],
                   [4,      5,      6     ],
                   [7,      8,      9     ],
                   [np.nan, np.nan, np.nan]],
                  columns=['A', 'B', 'C'])

# -------------------------------------
#    Aggregate these two functions over all rows.
df.agg(['sum', 'min'])
#    A    B    C
#    sum    12.0    15.0    18.0
#    min    1.0    2.0    3.0

# -------------------------------------
# Different aggregations per column.
df.agg({'A' : ['sum', 'min'], 'B' : ['min', 'max']})
#            A    B
#    max    NaN    8.0
#    min    1.0    2.0
#    sum    12.0    NaN

# -------------------------------------
# Aggregate over the columns.
df.agg("mean", axis="columns")
#    0    2.0
#    1    5.0
#    2    8.0
#    3    NaN
#    dtype: float64

# -------------------------------------
# combine groupby().agg()
df = pd.DataFrame(data={
    'country': [1,1,1, 2,2,2, 3,3,3],
    'user'   : [1,2,2, 3,3,4, 5,5,5],
    'event'  : [1,1,1, 1,0,0, 1,1,0]})
df['unit'] = 1

#      country user event unit
#    0      1    1    1    1
#    1      1    2    1    1
#    2      1    2    1    1
#    3      2    3    1    1
#    4      2    3    0    1
#    5      2    4    0    1
#    6      3    5    1    1
#    7      3    5    1    1
#    8      3    5    0    1

df2 = df.groupby(['country','user'],as_index=False).agg({'event':np.mean, 'unit':np.sum})

#      country user  event    unit
#    0    1    1    1.000000    1
#    1    1    2    1.000000    2
#    2    2    3    0.500000    2
#    3    2    4    0.000000    1
#    4    3    5    0.666667    3
​