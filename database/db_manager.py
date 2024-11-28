import mysql.connector

class DBManager:
    _connection = None

    @classmethod
    def connect(cls):
        if cls._connection is None:
            cls._connection = mysql.connector.connect(
                host = 'localhost',
                user = 'root',
                password = 'root',
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


if __name__ == "__main__":
    DBManager.create_neighborhood_table()
    DBManager.create_property_table()

    from models.properties import Neighborhood, Property, Terrain
    n1 = Neighborhood('bleu', 200)
    rp = Terrain('Rue de la Paix', [1, 2, 3, 4, 5], 200)
    DBManager.add_neighborhood(n1)
    DBManager.add_property(rp)

    print(DBManager.get_all_properties())
    print(DBManager.get_all_neighborhood())