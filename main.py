import sqlite3

# Ruta al archivo .localstorage
db_path = "/work/chrome-extension_pionmdlpdbkonlgpimjbaminkcbdgjnm_0.localstorage"
# Conéctate a la base de datos
conn = sqlite3.connect(db_path)
# Crea un cursor para ejecutar consultas
cursor = conn.cursor()

#MODIFICAR VALORES COINS

#Nuevo valor Coins
new_coins_value = b'1\x006\x000\x000\x00'
# Consulta SQL para actualizar el valor de 'collect_panz' en la tabla 'ItemTable'
update_query = """
UPDATE ItemTable
SET value = ?
WHERE key = 'coins';
"""
# Actualizar la clave 'coins'
cursor.execute(update_query, (new_coins_value,))
# Guarda los cambios en la base de datos
conn.commit()
print(f"Valor de 'coins' actualizado a: {new_coins_value}")

# MODIFICAR VALORES PANZ

#Nuevo valor panz
new_collect_panz_value = b'8\x000\x000\x00'
# Consulta SQL para actualizar el valor de 'collect_panz' en la tabla 'ItemTable'
update_query = """
UPDATE ItemTable
SET value = ?
WHERE key = 'collect_panz';
"""
# actualizar la clave 'collect_panz'
cursor.execute(update_query, (new_collect_panz_value,))
# Guarda los cambios en la base de datos
conn.commit()
print(f"Valor de 'collect_panz' actualizado a: {new_collect_panz_value}")

#FIN
conn.close()
