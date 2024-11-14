import mysql.connector
from config import DB_CONFIG

class DBManager:
    def __init__(self):
        self.connexion = mysql.connector.connect(**DB_CONFIG)
        self.cursor = self.connexion.cursor()

    def get_properties(self):
        self.cursor.execute("SELECT * FROM properties")
        return self.cursor.fetchall()
    
    def save_property(self,property):
        pass

    def close(self):
        self.cursor.close()
        self.connexion.close()