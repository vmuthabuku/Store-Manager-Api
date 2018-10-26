from .v2.database.connect import conn, cur
import psycopg2

def create_tables():
    """ 
    create tables in the database
    """
    create_users = """ CREATE TABLE IF NOT EXISTS users (
        id serial PRIMARY KEY NOT NULL,
        username char(20) NOT NULL,
        email char(50) NOT NULL,
        role char(15) NOT NULL,
        admin bool NOT NULL,
        password varchar(250) NOT NULL
    )
    
    """
    create_products = """ CREATE TABLE IF NOT EXISTS products (
        id serial PRIMARY KEY NOT NULL,
        name char(20) NOT NULL,
        price float(10) NOT NULL,
        quantity float(10) NOT NULL,
        description char(100) NOT NULL
           
    )
    """

    table_list = [create_users, create_products]

    try:
        for table in table_list:
            cur.execute(table)
        
        conn.commit()
        print("Created successfully")
    
    except (Exception, psycopg2.DatabaseError) as e:
        print(e)