import pymysql

host = "inst-db-col.cn20eomwe8v9.us-west-2.rds.amazonaws.com"
user = "jlgb0125"
passw = "5010Jorge"
db_name = "db_user"

def connection_SQL():
    try:
        connection =  pymysql.connect (
            host=host,
            user=user,
            password=passw,
            database=db_name
        )
        
        print("succesfull connection to database")
        return connection
    except Exception as err:
        print("Error", err)
        return None

def insert():
    try:
        instruction = "insert into users values (435,'paula','garzon','2020-10-13');"
        connection = connection_SQL()
        cursor = connection.cursor()
        cursor.execute(instruction)
        connection.commit()
        print("User added")
    except Exception as err:
        print("Error", err)
        return None





## sudo python database/db.py - valida instacia
## sudo python pip install pymysql - instala la instancia pymysql
## sudo python database/db.py - ejecutar codigo
