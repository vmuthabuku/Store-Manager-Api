import psycopg2
from ..database.connect import conn, cur

class UserModel():
    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password 
        self.role = 0
  
    def create_store_attendant(self):
       
        try:
            conn
            cur.execute(
                """
                INSERT INTO users(username, email,role, password)
                VALUES(%s,%s,%s,%s)""",
                (self.username, self.email, self.password, self.role))            
                       
            return 'attendant registered succesful'