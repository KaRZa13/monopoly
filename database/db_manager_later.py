import mysql.connector
from config import DB_DEV_CONFIG


class DBManager2:
    def __init__(self):
        self.connexion = mysql.connector.connect(**DB_DEV_CONFIG)
        self.cursor = self.connexion.cursor()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS neighborhood (
                id INT AUTO_INCREMENT PRIMARY KEY,
                color VARCHAR(255),
                house_price INT
            )
        """)
        self.connexion.commit()

    def save_neighborhood(self, neighborhood):
        self.cursor.execute("""
            INSERT INTO neighborhood (color, house_price) VALUES (%s, %s)
        """, (neighborhood.color, neighborhood.house_price))
        self.conn.commit()

    def load_neighborhood(self):
        self.cursor.execute("SELECT * FROM neighborhood")

    def close(self):
        self.cursor.close()
        self.connexion.close()