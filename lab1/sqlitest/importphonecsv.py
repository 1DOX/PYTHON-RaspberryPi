from sys import argv
import csv
import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()

if len(argv) < 2:
	print("Please provide a name of a csv file. ex: python importcsv.py myfile.csv")
	exit(1)
else:
	csvfile = argv[1]
	
c.execute("CREATE TABLE phonenum ( id INT PRIMARY KEY, name TEXT, phone TEXT )")
phonenum = csv.reader(open(csvfile, 'r'), delimiter=',', quotechar='"')
index = 0

for row in phonenum:
	index = index + 1
	print("%s %s" % (index, row))
	c.execute("INSERT INTO phonenum VALUES(?, ?, ?)", (index, row[0], row[1]))

conn.commit()
conn.close()
exit()
