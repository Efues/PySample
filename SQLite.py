import sqlite3
from contextlib import closing

dbname = 'database.db'

with closing(sqlite3.connect(dbname)) as conn:
    c = conn.cursor()

    # create_table = '''create table users (id int, name varchar(64),
    #                   age int, gender varchar(32))'''
    # c.execute(create_table)
    #
    # sql = 'insert into users (id, name, age, gender) values (?,?,?,?)'
    # user = (1, 'Taro', 20, 'male')
    # c.execute(sql, user)
    #
    # insert_sql = 'insert into users (id, name, age, gender) values (?,?,?,?)'
    # users = [
    #     (2, 'Shota', 54, 'male'),
    #     (3, 'Nana', 40, 'female'),
    #     (4, 'Tooru', 78, 'male'),
    #     (5, 'Saki', 31, 'female')
    # ]
    # c.executemany(insert_sql, users)
    # conn.commit()

    select_sql = 'select * from users'
    for row in c.execute(select_sql):
        print(row)