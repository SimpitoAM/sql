#import the sqlite3 library
import sqlite3

#create database if database doesn't already exist
conn = sqlite3.connect("cars.db")

#get a  cursor object used to execute SQL commands
cursor = conn.cursor()

#create a table
cursor.execute("DELETE FROM orders WHERE make = 'Ford'")

#close the database connection
conn.close()
