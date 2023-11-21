import os, random, time, sys

from colorama import init, Fore

from data.database import Database


init(autoreset=True)
db = Database('data/db.db')


def clear():
	if os.name == 'nt':
		os.system('cls')

	else:
		os.system('clear')


def main():
	os.system('cls')
	print(Fore.YELLOW + 'Приветствую тебя, дорогой друг, в нашей лучшей библиотеке!!!')

	choice = input('\nВыберите действие:\n1. Добавить книгу\n2. Просмотреть список книг\n3. Выйти\n>>> ')

	if choice == '1':
		create_book()

	elif choice == '2':
		listing_books()

	elif choice == '3':
		print(Fore.RED + 'Пока - пока!')
		sys.exit()

	else:
		print(Fore.RED + 'Неправильно!!! Это не то, что нужно!')
		time.sleep(2)
		clear()
		main()



def listing_books():
	clear()

	choice = input(Fore.YELLOW + '0. Назад\n1. Просмотр списка книг\n>>> ')

	if choice == '0':
		clear()
		main()

	elif choice == '1':
		show_books()

	else:
		print(Fore.RED + 'Неправильно!!! Это не то, что нужно!')
		time.sleep(2)
		clear()
		listing_books()



def show_books():
	clear()
	print(Fore.YELLOW + 'Выберите книгу: \n')

	for i in db.get_all():
		print(Fore.MAGENTA + f'ID: {i[0]}, Название: {i[1]}, Автор: {i[2]}, Жанр: {i[4]}')

	word = input(Fore.YELLOW + '\n\nВозврат в меню: 0 \nДля просмотра информации о книге введите её ID \nТак же вы можете ввести жанр для просмотра всех книг из этого жанра \n\n>>> ')

	if word == '0':
		main()

	else:
		choose_book(word)



def choose_book(word):
	try:

		books = db.search(word)
		clear()
		print(books)
		for i in books:
			print(Fore.MAGENTA + f'ID: {i[0]}, Название: {i[1]}, Автор: {i[2]}, Описание: {i[3]}, Жанр: {i[4]} \n')

		choice = input(Fore.YELLOW + '0. Назад \n1. Удалить книгу \n>>> ')

		if choice == '0':
			show_books()

		elif choice == '1':
			delete_book()

		else:
			main()

	except:
		print(Fore.RED + 'Не нашёл похожих книг')
		time.sleep(2)
		clear()
		main()



def delete_book():
	book = input(Fore.YELLOW + 'Введите ID книги для удаления: \n>>> ')

	try:
		db.delete(book)
		clear()
		print(Fore.GREEN + 'Книга удалена')

		time.sleep(2)
		main()

	except:
		print(Fore.RED + 'Ошибка, книга не найдена')
		time.sleep(2)
		clear()
		main()



def create_book():
	clear()

	title = input(Fore.MAGENTA + 'Введите заголовок книги: ')
	clear()

	autor = input(Fore.MAGENTA + 'Введите имя автора книги: ')
	clear()
	
	genre = input(Fore.MAGENTA + 'Введите жанр книги: ')
	clear()
	
	desc = input(Fore.MAGENTA + 'Введите описание книги: ')
	clear()

	book_id = random.randint(1, 10000)
	db.add(book_id, title, autor, desc, genre)
	db.add_genre(book_id, genre)

	print(Fore.GREEN + 'Книга создана!')
	
	time.sleep(2)
	clear()
	main()
	
main()