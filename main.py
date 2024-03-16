from models.books import Book
import models.menus as menus
import models.load_api as sm
from models.file import JSONLoad
from models.math_operations import Math

def start_load():
 """Load favorite books from file"""
 conte = JSONLoad.see_favorites()
 for books in range(len(conte)):
   book = Book(conte[books])
   book.edit_favorite()
   
def show_favorites(json_dicio:dict, key_searched='title'):
 """Return all the values of a key from the dictionary."""
 books = [book[key_searched] for book in json_dicio]
 return books

def load_resources(search:int):
 """Run all resources needed to get book data from API and transform it into a dictionary."""
 name, mode = sm.search_method(search)
 string_json = sm.separate_book_info(sm.get_results(name,mode))
 new_object = sm.create_object(string_json)
 print(new_object)
 return search, new_object

def add_favorite(book):
 book.edit_favorite()
 book_info = book.to_dict()
 JSONLoad.write_favorite(book_info)

def remove_favorite(book):
 book.edit_favorite()
 book_info = book.to_dict()
 JSONLoad.unwrite_favorite(book_info['title'])

def load_info():
	name = show_favorites(JSONLoad.see_favorites())
	pages = show_favorites(JSONLoad.see_favorites(), key_searched='pages')
	category = show_favorites(JSONLoad.see_favorites(), key_searched='category')
	Math.get_extra_info(name,pages, category)

def display_favs_menu():
 """Display an interactive menu in user interface"""
 try:
  Book.print_names()
  while True:
   option = menus.favs_menu()
   try:
    match int(option):
     case 1:
      fav_name = input('Digite o nome do livro: ')
      answer = Book.search_book(fav_name)
      remove_favorite(answer)
     case 2:
      fav_name = input('Digite o nome do livro: ')
      answer = Book.search_book(fav_name)
      print(answer)
     case 3:
      load_info()
      break
     case 0:
      break
     case _:
      print('Essa não é uma opção válida')
   except ValueError:
    print('É necessário inserir um número')
 except TypeError:
  print(JSONLoad.see_favorites())

def display_menu(previous_option:int,book:object):
 """Display an interactive menu in user interface"""
 while True:
  option = menus.sub_favs_menu()
  try:
   match int(option):
    case 1:
     _, book = load_resources(previous_option)
    case 2:
     add_favorite(book)
     break
    case 0:
     break
    case _:
     print('Essa não é uma opção válida')
  except ValueError:
   print('É necessário inserir um número')

def main():
 """Display an interactive menu in user interface"""
 start_load()
 while True:
  option = menus.menu()
  try:
   option = int(option)
   if option in [1,2,3]:
    search, book = load_resources(option)
    display_menu(search,book)
   elif option == 4:
    display_favs_menu()
   elif option == 0:
    print('Encerrando...')
    break
   else:
    print('Essa não é uma opção válida')
  except ValueError:
   print('É necessário inserir um número')

if __name__ == '__main__':
 main()