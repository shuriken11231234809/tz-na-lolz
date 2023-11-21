import os, random, time, sys

from colorama import init, Fore

from data.database import Database

# ининциализация колорамы и бд (•‿•)
init(autoreset=True)
db = Database('data/db.db')


# "типо" умный и сделал отдельную функцию, чтобы если что на линуксе cls был clear ⸂⸂⸜(രᴗര๑)⸝⸃⸃
def clear():
	if os.name == 'nt': # если имя ос == nt, то есть винда, то cls, иначе clear
		os.system('cls')

	else:
		os.system('clear')


# основная функция, которая посылает юзера по своим дорожкам ( • )( • ) ԅ(‾⌣‾ԅ)
def main():
	clear()
	print(Fore.YELLOW + 'Приветствую тебя, дорогой друг, в нашей лучшей библиотеке!!!')

	choice = input('\nВыберите действие:\n1. Добавить книгу\n2. Просмотреть список книг\n>>> ')

	if choice == '1':
		create_book() # функция создания книги

	elif choice == '2':
		show_books() # функция показа книг

	else:
		print(Fore.RED + 'Неправильно!!! Это не то, что нужно!')
		time.sleep(2)
		clear()
		main()


# функция вывода списка книг (－_－) zzZ
def show_books():
	clear()
	print(Fore.YELLOW + 'Выберите книгу: \n')

	for i in db.get_all(): # перебирание всех книг из бд циклом и вывод поочередно
		print(Fore.MAGENTA + f'ID: {i[0]}, Название: {i[1]}, Автор: {i[2]}, Жанр: {i[4]}')

	word = input(Fore.YELLOW + '\n\nВозврат в меню: 0 \nДля просмотра информации о книге введите её ID \nТак же вы можете ввести жанр для просмотра всех книг из этого жанра \n\n>>> ')

	if word == '0':
		main()

	else:
		choose_book(word) # выбор конкретной книги


# выбор конкретной книги (-‿◦☀)
def choose_book(word):
	try:

		clear()
		books = db.search(word) # поиск книги
		
		for i in books:
			print(Fore.MAGENTA + f'ID: {i[0]}, Название: {i[1]}, Автор: {i[2]}, Описание: {i[3]}, Жанр: {i[4]} \n')

		choice = input(Fore.YELLOW + '0. Назад \n1. Удалить книгу \n>>> ')

		if choice == '0':
			show_books() # возврат на показ книг

		elif choice == '1':
			delete_book() # удаление книги

		else:
			main() #возврат в основное меню

	except:
		print(Fore.RED + 'Не нашёл похожих книг')
		time.sleep(2)
		clear()
		main()


# удаление книжечьки =＾● ⋏ ●＾=
def delete_book():
	book = input(Fore.YELLOW + 'Введите ID книги для удаления: \n>>> ')

	try:
		clear()

		db.delete(book) # удаляшка книжки
		print(Fore.GREEN + 'Книга удалена')

		time.sleep(2)
		main()

	except:
		print(Fore.RED + 'Ошибка, книга не найдена')
		time.sleep(2)
		clear()
		main()


# создание книшьки ⸂⸂⸜(രᴗര๑)⸝⸃⸃
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
	db.add(book_id, title, autor, desc, genre) # добавление книги

	print(Fore.GREEN + 'Книга создана!')
	
	time.sleep(2)
	clear()
	main()
	


main()
