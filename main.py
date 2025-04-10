import mariadb
import tkinter as tk
from tkinter import ttk
import sys

# Verbindung zu MariaDB
try: 
    conn = mariadb.connect( 
        user="marc", 
        password="marc", 
        host="localhost", 
        port=3306, 
        database="schlumpfshop3" 
    )

except mariadb.Error as e: 
    print(f"Error connecting to MariaDB Platform: {e}") 
    sys.exit(1)

def abfrage(cur, tb_entry):
    # SQL Befehl, der ausgeführt wird
    cur.execute(f"""SELECT artikel.Artikelname, artikel.Lagerbestand, lieferant.Lieferantenname
            FROM artikel
            INNER JOIN lieferant ON artikel.Lieferant = lieferant.ID_lieferant
            # WHERE artikel.Lagerbestand < '{tb_entry}'""")

cur = conn.cursor()
# GUI erstellen
root = tk.Tk()
root.geometry("500x800")
lb_info = tk.Label(root, text="Bitte Datum eingeben (JJJJ-MM-TT)")
tb_entry = tk.Entry(root)
bn_start = tk.Button(root, text="Start", command=abfrage(cur, tb_entry))


# SQL Befehl, der ausgeführt wird
cur.execute()