import mysql.connector

class DBManager:
    _connection = None

    @classmethod
    def create_database(cls):
        cls.execute("""
            CREATE DATABASE IF NOT EXISTS monopoly;
            USE monopoly;
        """)


    @classmethod
    def connect(cls):
        if cls._connection is None:
            cls._connection = mysql.connector.connect(
                host = 'localhost',
                user = 'root',
                password = '',
                database = 'monopoly'
            )
        return cls._connection
    
    @classmethod
    def close(cls):
        if cls._connection is not None:
            cls._connection.close()
            cls._connection = None
    
    @classmethod
    def execute(cls, query, params=None, fetch_one=False, fetch_all=False):
        connection = cls.connect()
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute(query, params)
            if fetch_one:
                return cursor.fetchone()
            elif fetch_all:
                return cursor.fetchall()
            connection.commit()
        finally:
            cursor.close()

# GESTION DE LA TABLE NEIGHBORHOOD

    @classmethod
    def create_neighborhood_table(cls):
        cls.execute("""
            CREATE TABLE IF NOT EXISTS neighborhood (
                id INT AUTO_INCREMENT PRIMARY KEY,
                color VARCHAR(255),
                house_price INT
            );
        """)

    @classmethod
    def drop_neighborhood_table(cls):
        cls.execute("DROP TABLE IF EXISTS neighborhood;")

    @classmethod
    def get_last_insert_id(cls):
        return cls.execute("SELECT LAST_INSERT_ID() AS id;", fetchone=True)['id']

    @classmethod
    def add_neighborhood(cls, neighborhood):
        if neighborhood.id is None:
            result = cls.execute("""
                        INSERT INTO neighborhood (color, house_price)
                        VALUES (%s, %s);
                    """, (neighborhood.color, neighborhood.house_price))
            neighborhood.id = cls.get_last_insert_id()
        else:
            cls.execute("""
                    UPDATE neighborhood
                    SET color = %s, house_price = %s
                    WHERE id = %s;
                    """, (neighborhood.color, neighborhood.house_price, neighborhood.id))

    @classmethod
    def get_neighborhood(cls, id=None, color=None):
        return cls.execute("""
                    SELECT id, color, house_price
                    FROM neighborhood
                    WHERE (%s IS NULL OR is = %s)
                        AND (%s IS NULL OR color like %s);
                    """, (id, id, color, color), fetch_one=True)

    @classmethod
    def get_all_neighborhood(cls):
        return cls.execute("""
                SELECT id, couleur, prixMaison
                FROM neighborhood;
                """, fetchall=True)
    
# GESTION DE LA TABLE PROPERTY

    @classmethod
    def create_property_table(cls):
        cls.execute("""
            CREATE TABLE IF NOT EXISTS properties (
                id INT AUTO_INCREMENT PRIMARY KEY,
                type VARCHAR(50),
                idNeighborhood INT,
                name VARCHAR(255),
                price INT,
                rent TEXT,
                FOREIGN KEY (idNeighborhood) REFERENCES neighborhood(id)
            );
        """)

    @classmethod
    def drop_property_table(cls):
        cls.execute("DROP TABLE IF EXISTS property;")
    
    @classmethod
    def add_property(cls, prop):
        if prop.id is None:
            cls.execute("""
                INSERT INTO property (type, idNeighborhood, name, price, rent)
                VALUES (%s, %s, %s, %s, %s);
            """, (prop.type, prop.idNeighborhood, prop.name, prop.price, ",".join(map(str, prop.rent))))
        else:
            cls.execute("""
                UPDATE property
                SET type = %s, idNeighborhood = %s, name = %s, price = %s, rent = %s
                WHERE id = %s;
            """, (prop.type, prop.idNeighborhood, prop.name, prop.price, ",".join(map(str, prop.rent)), prop.id))

    @classmethod
    def get_all_properties(cls):
        return cls.execute("""
                    SELECT id, type, idNeighborhood, name, price, rent 
                    FROM properties;
                """, fetch_all=True)

# GESTION DU JOUEUR

    @classmethod
    def create_player_table(cls):
        cls.execute("""
            CREATE TABLE IF NOT EXISTS player (
                idPlayer INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(50),
                balance INT,
                color VARCHAR(25),
                position INT
            );
        """,)

    @classmethod
    def drop_player_table(cls):
        cls.execute("DROP TABLE IF EXISTS player;")

    @classmethod
    def add_player(cls, player):
        if player.id is None:
            cls.execute("""
                INSERT INTO player (idPlayer, name, balence, color, position)
                VALUES (%s, %s, %s, %s, %s)
            """, (player.id, player.name, player.balence, player.color, player.position))

    @classmethod
    def get_player(cls, id=None, name=None):
        return cls.execute("""
                    SELECT idPlayer, name, balance, color, position
                    FROM player
                    WHERE (%s IS NULL OR is %s)
                        AND %s IS NULL OR name like %s
                """, (id, id, name, name))


if __name__ == "__main__":
    DBManager.create_neighborhood_table()
    DBManager.create_property_table()

    from ..models.properties import Neighborhood, Terrain, Property
    from ..models.player import Player
    j1 = Player('Raf')
    print(j1)
    n1 = Neighborhood('bleu', 200)
    print(n1)
    rp = Terrain('Rue de la Paix', [1, 2, 3, 4, 5], 200)
    print(rp)
    DBManager.add_neighborhood(n1)
    DBManager.add_property(rp)

    print(DBManager.get_all_properties())
    print(DBManager.get_all_neighborhood())