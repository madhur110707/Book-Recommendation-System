import mysql.connector

def connect_db():

    connection = mysql.connector.connect(

        host="localhost",

        user="root",

        password="kalyana@130907",

        database="book_recommender"

    )

    return connection