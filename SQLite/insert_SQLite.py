import sqlite3

conn = sqlite3.connect("customer.db")  # Conecta con el archivo de base de datos llamado customer.db, si no existe lo crea en blanco

# Crea un cursor para usar nuestra base de datos
c = conn.cursor()

# Rellena los valores de la tabla de nuestra base de datos
c.execute("INSERT INTO customers VALUES ('Jhon', 'Elder', 'juanmgv98@gmail' )")

conn.commit()
conn.close()













































































































