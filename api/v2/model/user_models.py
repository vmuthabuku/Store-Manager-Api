import psycopg2
from ..database.connect import conn, cur

class UserModel():
    def __init__(self,username,email,password,role):
        self.username = username
        self.email = email
        self.password = password 
        self.role = role
  
    def create_store_attendant(self):
        try:
            conn
            cur.execute(
                """
                INSERT INTO users(username, email,role, password)
                VALUES(%s,%s,%s,%s)""", (self.username,self.email,self.password,self.role)
                )
                
            conn.commit()
            

        except Exception as e:
            print(e)
            return ("ran into trouble registering you")

    def get_all_users(self):
        user_list = []
        conn
        user = cur.execute("SELECT * FROM users")
        try:
            user
        except (Exception, psycopg2.DatabaseError) as e:
            print(e)
            conn
            cur
            result = cur.fetchall()
            for i in result:
                user_list.append(result)
            return result








        