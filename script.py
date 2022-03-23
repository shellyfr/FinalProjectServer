import psycopg2 as ps

DB_HOST = "ec2-3-228-222-169.compute-1.amazonaws.com"
DB_NAME = "d65unat87kvmcm"
DB_USER = "lpkkulcjvlcwac"
DB_PASS = "a807632e5a088ae0029187cfa56b9a4679ebbb173265d59fc00200b35ba2175e"


conn = ps.connect(dbname=DB_NAME,user=DB_USER, password= DB_PASS, host=DB_HOST)
cur = conn.cursor()
# cur.execute("CREATE TABLE Codes (id INTEGER PRIMARY KEY, groupNum INTEGER);")

conn.commit()

# cur.close()
#
# conn.close()
