import sqlite3


class Database:
	def __init__(self, db_name):
		self.conn = sqlite3.connect(db_name)
		self.cursor = self.conn.cursor()
		self.create_main_table()



	def create_main_table(self):
		self.cursor.execute(
			'''CREATE TABLE IF NOT EXISTS books (
							id INTEGER,
							title TEXT,
							author TEXT,
							description TEXT,
							genre TEXT
			)'''
		)

		self.conn.commit()



	def add(self, id, title, author, description, genre):
		self.cursor.execute('INSERT INTO books (id, title, author, description, genre) VALUES (?, ?, ?, ?, ?)', (id, title, author, description, genre))
		self.conn.commit()



	def add_genre(self, id, genre):
		self.cursor.execute('INSERT INTO book_genres (id, genre) VALUES (?, ?)', (id, genre))
		self.conn.commit()



	def delete(self, id):
		self.cursor.execute('DELETE FROM books WHERE id = ?', (id,))
		self.conn.commit()



	def search(self, word):
		return self.cursor.execute('SELECT * FROM books WHERE ID = ? OR genre LIKE ?', (word, '%' + word + '%')).fetchall()



	def get_all(self):
		return self.cursor.execute('SELECT * FROM books').fetchall()



	def close_connection(self):
		self.cursor.close()
		self.conn.close()