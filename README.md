# LambdaLib
Lambda Labs Python Library of General Solutions


## CSV Similarity Score
Compares two csv files and returns a score between 0.0 and 1.0 to indicate how 
similar the data is. 


### Assumptions
- The data files have the same header, delimiter and number of rows.
- Each row of data should be a unique observation, with each column representing a single aspect.
- CSV is a convenient format, but a database adapter could be useful in the future.
- Data will be primitive strings or numbers and not more complex types.
