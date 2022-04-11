import psycopg2 as ps

DB_HOST = "ec2-3-228-222-169.compute-1.amazonaws.com"
DB_NAME = "d65unat87kvmcm"
DB_USER = "lpkkulcjvlcwac"
DB_PASS = "a807632e5a088ae0029187cfa56b9a4679ebbb173265d59fc00200b35ba2175e"


# def connect_to_db(sql_script):
#     conn = ps.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
#     cur = conn.cursor()
#     cur.execute(sql_script)
#     conn.commit()
#
# def close_connection():
#     conn.close()
#
# conn = ps.connect(dbname=DB_NAME,user=DB_USER, password= DB_PASS, host=DB_HOST)
# cur = conn.cursor()
# # cur.execute("CREATE TABLE Codes (id INTEGER PRIMARY KEY, groupNum INTEGER);")
#
# conn.commit()
#
# # cur.close()
# #
# # conn.close()


def update_db(sql_script):
    try:
        conn, cur = open_connection()
        execute_script(cur, sql_script)
        conn.commit()
        print(f"Number of rows updated: {cur.rowcount}")
    except ps.DatabaseError as e:
        print(f'Error {e}')
        # sys.exit(1)
    finally:
        close_connection(conn)


def insertDB(sql_script):
    try:
        conn, cur = open_connection()
        execute_script(cur, sql_script)
        conn.commit()
        # print(f"Number of rows updated: {cur.rowcount}")
    except ps.DatabaseError as e:
        print(f'Error {e}')
        # sys.exit(1)
    finally:
        close_connection(conn)


def get_data_from_db(sql_script):
    try:
        conn, cur = open_connection()
        print("getting data")
        execute_script(cur, sql_script)
        data = cur.fetchall()
    except ps.DatabaseError as e:
        print(f'Error {e}')
    finally:
        close_connection(conn)
    return data


def execute_script(cur, sql_script):
    cur.execute(sql_script)


def close_connection(conn):
    conn.close()


def open_connection():
    conn = ps.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
    cur = conn.cursor()
    return conn, cur

# conn = ps.connect(dbname=DB_NAME,user=DB_USER, password= DB_PASS, host=DB_HOST)
# cur = conn.cursor()
# cur.execute("CREATE TABLE Codes (id INTEGER PRIMARY KEY, groupNum INTEGER);")

# conn.commit()

# cur.close()
#
# conn.close()
