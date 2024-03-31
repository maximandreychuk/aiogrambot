import sqlite3 as sq

db = sq.connect('tg.db')
cur = db.cursor()

async def db_start():
    cur.execute("CREATE TABLE IF NOT EXISTS couriers("
                "id INTEGER PRIMARY KEY, "
                "data TEXT"
                "work_time TEXT, "
                "method TEXT)"
                )
    db.commit()
