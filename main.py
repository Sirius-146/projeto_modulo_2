import json
import menus
import search_methods as sm
import json_edit as jed
import math_operations as mto

def show_favorites(json_dicio, key_searched='title'):
  books = [book[key_searched] for book in json_dicio]
  return books

def show_book_info(book):
  try:
    print(f'{book["title"]} \nAutor: {book["author"]:^20}\t Editora: {book["publisher"]}\t\t Páginas: {book["pages"]}\t Categoria: {book["categories"]}')
    print(f'Descrição: \n{book["description"]}\n')
  except TypeError:
    print('Sua lista está vazia')

def load_resources(search):
  name, mode = sm.search_method(search)
  string_json = sm.separate_book_info(sm.get_results(name,mode))
  dicio = sm.create_dict(sm.colect_errors(string_json))
  show_book_info(dicio)
  return search,dicio

def see_favorites(filename='favorites.json'):
  try:
    with open(filename, 'r') as arquivo:
      conteudo = json.load(arquivo)
      if conteudo == []:
        raise FileNotFoundError
  except FileNotFoundError:
    conteudo = 'Sua lista está vazia'
  return conteudo

def search_book(fav_name):
  book = list(filter(lambda book: book['title'].lower()==fav_name, see_favorites()))
  show_book_info(book[0])

def extra_info():
  name = show_favorites(see_favorites())
  pages = show_favorites(see_favorites(), key_searched='pages')
  categories = show_favorites(see_favorites(), key_searched='categories')
  dicionary = dict(zip(name,categories))
  max_min_results = mto.return_max_min(name,pages)
  total_pages, media = mto.calc_media_total_pages(pages)
  st_dev = mto.std_dev(pages, media)
  grouped_categories = mto.list_categories(dicionary)
  books_category = mto.reduce_categories(grouped_categories,dicionary)
  print(f'Maior livro: {max_min_results[0][0]:^20}\t Páginas: {max_min_results[0][1]} \nMenor livro: {max_min_results[1][0]:^20}\t Páginas: {max_min_results[1][1]}\n')
  print('Livros por categoria:')
  for category in books_category:
    print(f'{category} - {books_category[category]}')
  print(f'\nTotal de páginas: {total_pages}\t Média de páginas: {int(media)}\t Desvio Padrão: {st_dev:.2f}')

def display_favs_menu():
  try:
    for book_name in show_favorites(see_favorites()):
          print(f'{book_name:^30}')
    while True:
      option = menus.favs_menu()
      try:
        match int(option):
          case 1:
            fav_name = input('Digite o nome do livro: ').lower()
            jed.remove_favorite(fav_name)
          case 2:
            fav_name = input('Digite o nome do livro: ').lower()
            search_book(fav_name)
          case 3:
            extra_info()
            break
          case 0:
            break
          case _:
            print('Essa não é uma opção válida')
      except ValueError:
        print('É necessário inserir um número')
  except TypeError:
    print(see_favorites())

def display_menu(previous_option,book):
  while True:
    option = menus.sub_favs_menu()
    try:
      match int(option):
        case 1:
          _, book = load_resources(previous_option)
        case 2:
          jed.add_favorite(book)
          break
        case 0:
          break
        case _:
          print('Essa não é uma opção válida')
    except ValueError:
      print('É necessário inserir um número')

def main():
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

main()