# LambdaLib
Lambda School Labs Python Library of General Data Science Solutions


## LambdaLib Developer Guidelines
1. No PEP8 violations.
2. No global state.
3. Must be backwards compatible to 3.6.x
4. Must be forward compatible up to the latest version of Python 3.9.x
5. Should avoid dependencies outside the standard library.
6. Every feature will be documented in detail.
7. Code examples will be included for each feature.


## Analysis

### CSV Similarity Score
Compares two csv files and returns a score between 0.0 and 1.0 to indicate how 
similar the data is. 

#### Assumptions
- The data files have the same header, delimiter and number of rows.
- Each row of data should be a unique observation, each column representing a single aspect.
- CSV is a convenient format, but a database adapter could be useful in the future.
- Data will be primitive strings or numbers and not more complex types.


## DataBase Ops

### DataModelMongo Class
- `find(dict) -> dict`
- `insert(dict)`
- `find_many(dict, int) -> Iterator[dict]`
- `insert_many(dict)`
- `get_df() -> DataFrame`

### DataModelSQL Class

### MultiDB
 This class is so it is only one import for multiple databases. Beta Version. As of now, for creating PostresSQL, SQLITE, and Mysql Tables, although simplified, the Data Types must be specified. Example:

 ```
 DB = MultiDB()
 DB.db_connect(connection_url)
 DB.db_create_table(table_name,id="SERIAL PRIMARY KEY,name="VARCHAR(30)",price="Integer")
 ```
# Connection format: 
All databases must be provided in URL form except for mysql. Examples: 
```
postgres_conn = "postgres://...." or postgresql://...."
mysql = "mysql://..."
sqlite = "db.sqlite3"
```
Connection format for postgres/mysql is 
```
://username:password@host/database_name
```
# Insert Statement
At the moment only db_insertOne is valid. 

Format:
```
DB = db_insertOne(name="any name", price=1)
```
Database Detection is automatic. But it can be declared optionally Example: 
```
DB = MultiDB("postgres")
```
 Options 
- postgres
- sqlite
- mysql

Always close the Database when you are done with 
```
DB.db_close()
```
Direct Import
```
from LambdaLib.DataBaseOps.multidb import MultiDB
```
## API & DevOps
