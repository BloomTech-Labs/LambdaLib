import psycopg2
import sqlite3
import re
import pymongo
import mysql.connector

#Multiple DB Class
class MultiDB:
    """Connects and Executes Commands on Multiple DB from one CLASS"""
    def __init__(self,dbtype=None):
        self.dbtype = dbtype
        self.conn = None

    # Detects DB if Parameter not supplied.   
    def __detect_db(self,db_url):
        if db_url.split('.',1)[1] == 'sqlite3':
            return "sqlite"
        elif ((db_url.split(':',1)[0] == "postgres") | (db_url.split(':',1)[0] == "postgresql")):
            return "postgres"
        elif (db_url.split(':',1)[0] == "mongodb+srv"):
            return "mongodb"
        elif (db_url.split(':',1)[0] == "mysql"):
            return "mysql"
        else:
            return "Invalid DB"
  
    # Connects to Databa
    def db_connect(self,url):
        if (self.dbtype is None):
            self.dbtype = self.__detect_db(url)
        if (self.dbtype == "sqlite"):
            self.conn = sqlite3.connect(url)
        elif (self.dbtype == "postgres"):
            self.conn = psycopg2.connect(url)
        elif (self.dbtype == "mysql"):
            conn_params = {
                'user': re.search("mysql://(.*):",url).group(1),
                'password': re.search(":(.*)@",url.split(":",1)[1]).group(1),
                'host': re.search("@(.*)/",url).group(1),
                'database': url.split("/")[-1]
                }
            self.conn = mysql.connector.connect(**conn_params)
        elif (self.dbtype == "mongodb"):
            self.conn = pymongo.MongoClient(url)
    # Create Database Tables for Relational Databases (myql, sqlite, postgres) 
    def db_create_table(self,table_name,**data):

        if ((self.dbtype == "sqlite") | (self.dbtype== "postgres") | (self.dbtype=="mysql")):
            values = ""
            for key,value in data.items():
                values += "{} {},".format(key,value)
            values = values.rstrip(",")
            table_query = f"""CREATE TABLE IF NOT EXISTS {table_name} ("""+values+")".rstrip(",")
            curs = self.conn.cursor()
            curs.execute(table_query)
            self.conn.commit()      
            curs.close()
            print(f"{table_name} Table Created")
            return
        elif (self.dbtype == "mongodb"):
            print("MongoDB tables are created automatically on insert statements")
            
    # Insert One for DB and MongoDB
    def db_insertOne(self,table_name,db_name=None,**data):
        if ((self.dbtype == "sqlite") | (self.dbtype== "postgres")):
            columns = ",".join(data.keys())
            values = ""
            for key,value in data.items():
                values += "'{}',".format(value)
            values = values.rstrip(",")
            query = f"INSERT INTO {table_name} ("+columns+") VALUES ("+values+");"
            print(query)
            cursor = self.conn.cursor()
            cursor.execute(query)
            cursor.close()
        elif (self.dbtype == "mongodb"):
            query = {k:v for k,v in data.items()}
            self.conn[db_name][table_name].insert_one(query)
    # Closes the Database Connection
    def db_close(self):
        self.conn.close()
    def __repr__(self):
        return "DB CONN: {}\n DBTYPE: {}".format(self.conn,self.dbtype)

if __name__ == "__main__":
    #mysql test:
    import os
    from dotenv import load_dotenv
    load_dotenv()
    db_url = os.environ.get('DB_URL')
    print(db_url)
    test = MultiDB()
    test.db_connect(db_url)
    print(test)
    test.db_close()