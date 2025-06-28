import datetime
import mysql.connector

__cnx = None

def get_sql_connection():
  print("Opening mysql connection")
  global __cnx

  __cnx = mysql.connector.connect(user='root', password='Krish@2005',
                                host='127.0.0.1',
                                database='gs')
  
  return __cnx