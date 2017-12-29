# CSV Merge

by [Frey Hargarten](http://github.com/jeffhargarten)

Joins two CSV files on a common header name Requires [Python3](https://www.python.org/download/releases/3.0/) and [pandas](https://github.com/pandas-dev/pandas).


To configure, just change CSV1.csv and CSV2.csv to the two files you want to merge. Change COMMONHEADER to the column name you want to join the files by. Running the script will produce MERGED_FILE.csv.


```bash
a = pd.read_csv("CSV1.csv")
b = pd.read_csv("CSV2.csv")
b = b.dropna(axis=1)
merged = a.merge(b, on='COMMONHEADER')
merged.to_csv("MERGED_FILE.csv", index=False)
```


To run the script:

```bash
$ python csvmerge.py    
```


Some notes:

a.) Pandas chokes on blank cells in your CSV. Fill them with null or whatever, just make certain they have a value. Otherwise it will skip columns even if it has one blank value.


b.) Capitalization matters. Make certain the names of the column header you're joining on are exactly the same.