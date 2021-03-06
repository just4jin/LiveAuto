#!usr/bin/env

import cx_Oracle

def db_connect(localhost = "******", port = ****, sid = '******' ):
    dsn_tns = cx_Oracle.makedsn(localhost, port, sid)
    conn = cx_Oracle.connect('****', '****', dsn_tns)
    c = conn.cursor()
    return conn, c
	
def exe_query(cursor, query):
    try:
        cursor.execute(query)
    except cx_Oracle.DatabaseError as e:
	error, = e.args
	if error.code == 942:
	    print"Try again! Error " + error.message
	raise
    return cursor

def read_query(cursor, query):
    exe_query(cursor,query)
    names = [x[0] for x in cursor.description]
    rows=cursor.fetchall()
    return pd.DataFrame(rows, columns=names)
	
def read_db(db_taer_query):
    conn, c = db_connect()
    db = read_query(c, db_taer_query)
    return db 
