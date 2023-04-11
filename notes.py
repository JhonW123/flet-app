import sqlite3

# Funcion de ChahGPT
def insert_data(fecha, tasa_compra, tipo_operacion, tasa_venta, transaccion_usd, transaccion_bs, cantidad_vendida_usd, forma_salida, forma_entrada, no_confirmacion, balance_usd, balance_bs, vendedor, comprador, observaciones):
    conn = sqlite3.connect('testdb.db')
    conn.execute('''INSERT INTO transacciones (Fecha, Tasa_de_Compra, Tipo_de_Operacion, Tasa_de_Venta, Transaccion_en_USD, Transaccion_Bs, Cantidad_Vendida_en_USD, Forma_de_Salida, Forma_de_Entrada, No_de_Confirmacion, Balance_en_USD, Balance_en_Bs, Vendedor, Comprador, Observaciones)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);''', (fecha, tasa_compra, tipo_operacion, tasa_venta, transaccion_usd, transaccion_bs, cantidad_vendida_usd, forma_salida, forma_entrada, no_confirmacion, balance_usd, balance_bs, vendedor, comprador, observaciones))
    conn.commit()
    print("Data inserted successfully")
    conn.close()
    
# Funcion que no carga los valores 
def insert_all_compra():
    conn = sql.connect('pruebadb.db')
    cursor = conn.cursor()
    instruccion = f"INSERT INTO transactions (Fecha, Tasa_de_Compra, Tipo_de_Operacion, Transaccion_en_USD, Transaccion_Bs, Forma_de_Salida, Forma_de_Entrada, No_de_Confirmacion, Balance_en_USD, Balance_en_Bs, Vendedor, Observaciones) VALUES ({fecha}, {tasa_compra}, {tipo_operacion}, {transaccion_usd}, {transaccion_bs}, {forma_salida}, {forma_entrada}, {no_confirmacion}, {balance_usd}, {balance_bs}, {vendedor}, {observaciones})"
    cursor.execute(instruccion)
    conn.commit()
    print("Data inserted successfully")
    conn.close()



# Nueva funcion hibrida

def insert_all_compra():
    conn = sql.connect('pruebadb.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO transacciones (Fecha, Tasa_de_Compra, Tipo_de_Operacion, Transaccion_en_USD, Transaccion_Bs, Forma_de_Salida, Forma_de_Entrada, No_de_Confirmacion, Balance_en_USD, Balance_en_Bs, Vendedor, Observaciones)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);''', (fecha, tasa_compra, tipo_operacion, transaccion_usd, transaccion_bs, forma_salida, forma_entrada, no_confirmacion, balance_usd, balance_bs, vendedor, observaciones))
    conn.commit()
    print("Data inserted successfully")
    conn.close()
