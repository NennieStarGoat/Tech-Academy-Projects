import sqlite3

file_list = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

conn = sqlite3.connect('test2.db')

with conn:
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS tbl_filelist( \
    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
    col_name TEXT, \
    col_suffix TEXT \
    )')
    conn.commit()
conn.close()


conn = sqlite3.connect('test2.db')

with conn:
    cur = conn.cursor()
    for item in file_list:
        name, ext = item.split('.')
        cur.execute("INSERT INTO tbl_filelist(col_name, col_suffix) VALUES (?, ?)",
                    (name, ext))
    conn.commit()
conn.close()

conn = sqlite3.connect('test2.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_name, col_suffix FROM tbl_filelist WHERE col_suffix = 'txt'")
    var_texts = cur.fetchall()
    for item in var_texts:
        msg = "File Name: {}".format(item[0], item[1])
        print(msg)
