import sqlite3

conn=sqlite3.connect('orgdata.sqlite')
cur=conn.cursor()

cur.executescript('''DROP TABLE IF EXISTS Counts;
                    CREATE TABLE Counts(org TEXT,count INTEGER)''')

fname=input('Enter file name:')
if(len(fname)<1):   fname='mbox-short.txt'

fhand=open(fname)
for line in fhand:
    if not line.startswith('From: '):continue
    pieces=line.split('@')
    org=pieces[1]
    cur.execute('SELECT count FROM Counts WHERE org=?',(org,))
    row=cur.fetchone()
    if row==None:
        cur.execute('INSERT INTO Counts(org,count) VALUES (?,1)',(org,))
    else:
        cur.execute('UPDATE Counts SET count=count+1 WHERE org=?',(org,))
    conn.commit()
sqlstr='SELECT org,count FROM Counts ORDER BY count DESC LIMIT 15'
for row in cur.execute(sqlstr):
    print(row[0],row[1])

cur.close()
