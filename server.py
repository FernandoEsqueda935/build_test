import mysql.connector
import paho.mqtt.subscribe as sub
from datetime import datetime

conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Ibiza123",
    database="proyecto")

cursor = conn.cursor()

while True:
    msg = sub.simple("esqueda/d01", hostname="mqtt.eclipseprojects.io")
    valor = float(msg.payload.decode())/1000
    valores = (1, 2, valor, datetime.now().date(), datetime.now().time())
    query = "INSERT INTO medicion (d_id, s_id, valor, fecha, hora) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, valores)
    conn.commit()