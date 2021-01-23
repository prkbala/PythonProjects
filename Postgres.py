import psycopg2
from psycopg2 import sql

def connect():
    conn = psycopg2.connect(
        host = "localhost",
        database="TissueBank",
        user="postgres",
        password="postgres",
        port = 5433)

    cur = conn.cursor()
    cur.execute(sql.SQL("SELECT * FROM {}.{}").format(
        sql.Identifier('Data'),
        sql.Identifier('TissueBlocks')))
    # cur.execute("select * from Data.TissueBlocks")
    rowsa = cur.fetchall()

    conn.close()

if __name__ == '__main__':
    connect()