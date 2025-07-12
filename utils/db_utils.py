import sqlite3
from random import randint
import config

def Find_UnitEID(pathdodb):
    conn = sqlite3.connect(pathdodb)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [row[0] for row in cursor.fetchall()]
    for table in tables:
        try:
            cursor.execute(f"SELECT UnitEID FROM {table} WHERE UnitEID IS NOT NULL AND UnitEID != '' LIMIT 1")
            result = cursor.fetchone()
            if result:
                conn.close()
                return result[0]
        except sqlite3.OperationalError:
            pass
    conn.close()
    return None

def add_homebrew(path_in_sd_card,uniteid,title="N/A"):
    conn = sqlite3.connect(config._DB_PATH)
    cursor = conn.cursor()
    pKey = randint(100,100000)
    request = """INSERT INTO "main"."Games_info" 
        ("pKey", "filename", "type", "title", "curriculum", "thumbnail", "UnitEID", "part_no", "lst_id", "ver_no") 
        VALUES (?, ?, 0, ?, NULL, NULL, ?, NULL, NULL, NULL);"""
    cursor.execute(request, (pKey, path_in_sd_card, title, uniteid))
    conn.commit()
    conn.close()
    return True

    