import sqlite3

def create_connection(db_file):

    try:
        connection = sqlite3.connect(db_file)
        return connection
    except sqlite3.Error as e:
        print(e)


def create_table(connection , sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)

#
def create_products(connection , products: tuple):
    sql = '''
    INSERT INTO products(
    product_title ,price ,quantity)
    VALUES (?,?,?)
    '''
    try:
        cursor = connection.cursor()
        cursor.execute(sql,products)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def create_products(connection):
    products = [
        ("мыло жидкое", 100, 5),
        ("шампунь мыло", 358.34, 8),
        ("зубная щетка", 56, 3),
        ("хлеб", 25.50, 12),
        ("бритва", 1000.90, 7),
        ("жвачка", 30, 2),
        ("кока-кола", 89.99, 9),
        ("фанта", 89.99, 6),
        ("макси чай", 1321, 4),
        ("сникерс", 78.12, 11),
        ("сендвич", 75.24, 8),
        ("мороженое", 20.00, 3),
        ("зарядка", 1800.00, 7),
        ("наушники", 10000.00, 5),
        ("зарядка на айфон", 2500.00, 9)
    ]
    connection.executemany('INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)', products)
    connection.commit()

def update_quantity(product_id, new_quantity):
    sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
    cursor = connection.cursor()
    cursor.execute(sql, (new_quantity, product_id))
    connection.commit()

def update_price(product_id, new_price):
    sql = '''UPDATE products SET price = ? WHERE id = ?'''
    cursor = connection.cursor()
    cursor.execute(sql, (new_price, product_id))
    connection.commit()

def delete_product(product_id):
    sql = '''DELETE FROM products WHERE id = ?'''
    cursor = connection.cursor()
    cursor.execute(sql, (product_id,))
    connection.commit()


def print_all_products():
    sql = '''SELECT * FROM products'''
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def print_all_price():
    sql = '''SELECT * FROM products WHERE price < 100 AND quantity > 5 '''
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def search_products():
    sql = '''SELECT * FROM products WHERE product_title LIKE "%мыло%" '''
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)




connection=create_connection("hw.db")
sql_create_table_products = '''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    product_title VARCHAR(200) NOT NULL,
    price DOUBLE(10,2) NOT NULL DEFAULT 0.00,
    quantity INTEGER NOT NULL DEFAULT 0
);'''

if connection:
    print("Соединение с БД установлено")
    create_table(connection,sql_create_table_products)
    create_products(connection)
    update_quantity(1,30)
    update_price(2,300)
    delete_product(4)
    print_all_products()
    print_all_price()
    search_products()

    connection.close()
