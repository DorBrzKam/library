import sqlite3


def get_books(cur):
    return cur.execute('SELECT book_id, title, author FROM books')


def save_book(conn, titl, auth):
    c = conn.cursor()
    c.execute('INSERT INTO books(title, author) VALUES(?, ?)', (titl, auth))
    connection.commit()


action = input('Co chcesz zrobić? [w]yświetl, [d]odaj: ')
if action == 'w':
    with sqlite3.connect('library.db') as connection:
        cursor = connection.cursor()
        for book in get_books(cursor):
            book_id, title, author = book
            print(f'id: {book_id}, tytuł: {title}, autor: {author}')
elif action == 'd':
    with sqlite3.connect('library.db') as connection:
        title = input('Tytuł: ')
        author = input('Author: ')
        cursor = connection.cursor()
        save_book(connection, title, author)
else:
    print('Nie wiem co mam zrobić.')
