import sqlite3

def db_init():
    from os.path import exists
    if exists('rgd.db'):  # TODO: are all tables okay
        return
    conn = sqlite3.connect('rgd.db')
    conn.execute('''create table locomotive_types
            (
            locomotive_type_id integer primary key not NULL,
            type_name text not NULL
            );''')
    # TODO: all the tables
    conn.commit()
    conn.close()

