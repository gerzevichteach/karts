import sqlite3
import csv

conn = sqlite3.connect('pr3.db')
cur = conn.cursor()

# cur.execute("""CREATE TABLE story ('operee' INT PRIMARY KEY, 'dat' text, 'id_mag' text, 'art' text, 'count_up' text, 'price' text );""")
# conn.commit()
# with open('3_1.csv', encoding='cp1251') as f:
#     f_read = csv.reader(f)
#     array = list(map(tuple, f_read))
#
# cur.executemany("INSERT INTO story VALUES (?,?,?,?,?,?,?);", array)
#
# conn.commit()

cur.execute("SELECT * FROM story;")
three_results = cur.fetchmany(3)
print(three_results)
