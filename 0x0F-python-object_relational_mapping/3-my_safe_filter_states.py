#!/usr/bin/python3
""" test "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '" as an input """
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    match = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))
    rows = cur.fetchall()
    for r in rows:
        print(r)
    cur.close()
    db.close()
