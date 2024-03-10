class CarPage:
    def __init__(self, connection):
        self.connection = connection

    def create_car_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''
            CREATE TABLE cars (
                id INTEGER PRIMARY KEY,
                brand TEXT,
                model TEXT,
                year INTEGER
            )
        ''')

        cursor.execute("INSERT INTO cars (brand, model, year) VALUES (?, ?, ?)", ('Кіберкопійка', 'ВАЗ-21010', 2047))
        cursor.execute("INSERT INTO cars (brand, model, year) VALUES (?, ?, ?)", ('ЗАЗ Запорожець', 'ЗАЗ-966', 1966))
        cursor.execute("INSERT INTO cars (brand, model, year) VALUES (?, ?, ?)", ('Ford', 'Мустанг', 1964))

        self.connection.commit()

    def get_car_brands(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT brand FROM cars")
        return [row[0] for row in cursor.fetchall()]

    def get_car_models(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT model FROM cars")
        return [row[0] for row in cursor.fetchall()]

    def get_car_years(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT year FROM cars")
        return [row[0] for row in cursor.fetchall()]

    def table_exists(self, table_name):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
        return cursor.fetchone() is not None
