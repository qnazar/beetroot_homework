import sqlite3

try:
    connection = sqlite3.connect('example_db.db')
    cursor = connection.cursor()
    print('Connected')
    get_data_query = "SELECT * FROM your_users"

    create_table_query = """CREATE TABLE IF NOT EXISTS my_users 
                                (id INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(255) NOT NULL)"""
    cursor.execute(create_table_query)
    print('Table created')

    rename_table_query = "ALTER TABLE my_users RENAME TO your_users"
    cursor.execute(rename_table_query)
    print('Table renamed')

    add_column_query = "ALTER TABLE your_users ADD COLUMN gender char(1)"
    cursor.execute(add_column_query)
    print('Column Added')

    users = [('Masha', 'F'), ('Pasha', 'M'), ('Igor', 'M')]

    for user in users:
        add_user_query = """INSERT INTO your_users (name, gender) VALUES (?, ?)"""
        cursor.execute(add_user_query, user)
    print('Rows added')
    cursor.execute(get_data_query)
    data = cursor.fetchall()
    print(data)

    update_query = "UPDATE your_users SET name='Ira' WHERE id = 1"
    cursor.execute(update_query)
    cursor.execute(get_data_query)
    data = cursor.fetchall()
    print(data)

    delete_query = "DELETE FROM your_users WHERE name = 'Igor'"
    cursor.execute(delete_query)
    cursor.execute(get_data_query)
    data = cursor.fetchall()
    print(data)


except sqlite3.Error as e:
    print(e)
finally:
    cursor.execute('DROP TABLE your_users')
    print('Table droped')
    cursor.close()
    connection.close()
    print('CLOSED')
