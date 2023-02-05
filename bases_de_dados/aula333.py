import sqlite3

conexao = sqlite3.connect('database.db')
cursor = conexao.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
                'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                ')')








cursor.close()
conexao.close()