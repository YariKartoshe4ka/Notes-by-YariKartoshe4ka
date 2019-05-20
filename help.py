import sqlite3

def create_db():
    con = sqlite3.connect('saves/saves.db')
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS notes(id INTEGER, body TEXT)')

    con.commit()

    cur.close()
    con.close()

def write_none_values_db():
    con = sqlite3.connect('saves/saves.db')
    cur = con.cursor()

    cur.execute('INSERT INTO notes VALUES(1, \"\")')
    con.commit()

    cur.execute('INSERT INTO notes VALUES(2, \"\")')
    con.commit()

    cur.execute('INSERT INTO notes VALUES(3, \"\")')
    con.commit()

    cur.execute('INSERT INTO notes VALUES(4, \"\")')
    con.commit()

    cur.close()
    con.close()