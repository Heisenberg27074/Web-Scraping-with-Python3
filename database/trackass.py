import xml.etree.ElementTree as ET
import sqlite3

conn=sqlite3.connect('tracka.sqlite')
cur=conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Tracks;

CREATE TABLE Artist(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                    name TEXT UNIQUE

);
CREATE TABLE Genre(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                    name TEXT UNIQUE

);
CREATE TABLE Album(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                    title TEXT UNIQUE,
                    artist_id TEXT
);
CREATE TABLE Tracks(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                    title TEXT UNIQUE,
                    album_id INTEGER,
                    genre_id INTEGER,
                    length INTEGER, count INTEGER, rating INTEGER
);
''')
fname=input('Enter your file name:')
if len(fname)<1:fname='Library.xml'

def lookup(d,key):
    found=False
    for child in d:
        if found:return child.text
        if child.tag=='key' and child.text==key:
            found =True
    return None

stuff=ET.parse(fname)
all=stuff.findall('dict/dict/dict')

print('Dict count:',len(all))

for entry in all:
    if lookup(entry,'Track ID')==None:continue

    name=lookup(entry,'Name')
    album=lookup(entry,'Album')
    artist=lookup(entry,'Artist')
    genre=lookup(entry,'Genre')
    count=lookup(entry,'Play Count')
    rating=lookup(entry,'Rating')
    length=lookup(entry,'Total Time')

    if name is None or album  is None or artist is None or genre is None:
        continue
    print(name,artist,album,genre ,count, rating, length)
    cur.execute('INSERT OR IGNORE INTO Artist(name) VALUES(?) ',(name,))
    cur.execute('SELECT id FROM Artist WHERE name=?',(name,))
    artist_id=cur.fetchone()[0]
    cur.execute('''INSERT OR IGNORE INTO Genre(name) VALUES(?)''',(genre,))
    cur.execute('SELECT id FROM Genre WHERE name=?',(genre,))
    genre_id=cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album(title,artist_id ) VALUES (?,?)''',(album,artist_id))
    cur.execute('''SELECT id FROM Album WHERE title=?''',(album,))
    album_id=cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Tracks(title,album_id,genre_id,length,rating,count) VALUES(?,?,?,?,?,?)''',
            (name,album_id,genre_id,length,rating,count))

    conn.commit()
