import requests
import json

def search_name(search_method):
  search = ['livro','coleção','autor']
  name = input(f'Insira o nome do {search[search_method-1]}: ').lower()
  name = name.strip()
  name = name.replace(' ','+')
  return name

def search_mode(search_method):
  mode = ['intitle:','inauthor:']
  if search_method == 1:
    search_method = mode[0]
  elif search_method == 3:
    search_method = mode[1]
  else:
    search_method = ''
  return search_method

def search_method(answer):
  name = search_name(answer)
  mode = search_mode(answer)
  return (name,mode)

def get_results(name,tipo):
  url = f'https://www.googleapis.com/books/v1/volumes?q={tipo}{name}&printType=books&langRestrict=pt&maxResults=1'
  response = requests.get(url)
  data = response.json()
  return data

def separate_book_info(data):
  information = []
  for i in range(len(data["items"])):
    volumeInfo = data["items"][i]["volumeInfo"]
    information.append(volumeInfo)
  return information

def colect_errors(received_data):
  books = []
  for book in range(len(received_data)):
    try:
      name = (received_data[book]["title"]).title()
    except KeyError:
      name = None
    try:
      authors = received_data[book]["authors"][0]
    except KeyError:
      authors = None
    try:
      publisher = received_data[book]["publisher"]
    except KeyError:
      publisher = None
    try:
      pages = received_data[book]["pageCount"]
    except KeyError:
      pages = None
    try:
      description = received_data[book]["description"]
      description = '.\n'.join(description.split('. '))
    except KeyError:
      description = None
    books.append([name, authors, publisher, pages, description])
  return books

def create_dict(books):
  for book in books:
    basic_book_info = ['title', 'author','publisher','pages','description']
    book_info = [book[0], book[1], book[2], book[3], book[4]]
    books_found_list = dict(zip(basic_book_info, book_info))
  return books_found_list

def show_favorites(json_dicio):
  books = [book['title'].lower() for book in json_dicio['book']]
  return books

def show_book_info(book):
  try:
    print(f'{book["title"]} \nAutor: {book["author"]}\t Editora: {book["publisher"]}\t\t Páginas: {book["pages"]}\nDescrição: \n{book["description"]}\n')
  except TypeError:
    print('Sua lista está vazia')

def load_resources(search):
  name, mode = search_method(search)
  string_json = separate_book_info(get_results(name,mode))
  dicio = create_dict(colect_errors(string_json))
  show_book_info(dicio)
  return search,dicio

def add_favorite(book):
  try:
    with open('favorites.json', 'r') as arquivo:
      favorites = json.load(arquivo)
  except (FileNotFoundError, json.JSONDecodeError):
    favorites = {'book': []}
  favorites['book'].append(book)
  with open('favorites.json', 'w') as arquivo:
    json.dump(favorites, arquivo, indent=2)

def remove_favorite(fav_name):
    try:
        with open('favorites.json', 'r') as arquivo:
            favorites = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return 'Não há livros na lista'
    
    favorites['book'] = [book for book in favorites['book'] if book['title'].lower() != fav_name]

    with open('favorites.json', 'w') as arquivo:
        json.dump(favorites, arquivo, indent=2)

def see_favorites():
  try:
    with open('favorites.json', 'r') as arquivo:
      conteudo = json.load(arquivo)
  except FileNotFoundError:
    conteudo = 'Sua lista está vazia'
  return conteudo

def find_favorite(fav_list, fav_name):
  if fav_name.lower() in fav_list:
    remove_favorite(fav_name)
  else:
    print('Esse livro não está em sua lista de favoritos')

def menu():
    menu = '''
  ---------- Menu ----------
  [1] - Pesquisar Livro
  [2] - Pesquisar Coleção
  [3] - Pesquisar Autor
  [4] - Visualizar Favoritos
  [0] - Finalizar
  --------------------
  => '''
    return input(menu)

def sub_favs_menu():
  menu = '''
  ---------- Menu ----------
  [1] - Pesquisar Novamente
  [2] - Adicionar aos favoritos
  [0] - Retornar
  --------------------
  => '''
  return input(menu)

def favs_menu():
  menu = '''
  ---------- Menu ----------
  [1] - Remover favorito
  [2] - Detalhes sobre o livro
  [3] - Informações adicionais
  [0] - Retornar
  --------------------
  => '''
  return input(menu)

def search_book(fav_name):
  book = None
  for livro in see_favorites()['book']:
    if fav_name == livro['title'].lower():
      book = livro
  show_book_info(book)

def display_favs_menu():
  try:
    for livro in show_favorites(see_favorites()):
          print(livro)
    while True:
      opcao = favs_menu()
      try:
        opcao = int(opcao)
        if opcao == 1:
          fav_name = input('Digite o nome do livro: ').lower()
          remove_favorite(fav_name)
          break
        elif opcao == 2:
          fav_name = input('Digite o nome do livro: ').lower()
          search_book(fav_name)
          break
        elif opcao == 0:
          break
        else:
          print('Essa não é uma opção válida')
          continue
      except ValueError:
        print('É necessário inserir um número')
        continue
  except TypeError:
    print(see_favorites())

def display_menu(previous_option,book):
  while True:
    opcao = sub_favs_menu()
    try:
      opcao = int(opcao)
      if opcao == 1:
        _, book = load_resources(previous_option)
      elif opcao == 2:
        add_favorite(book)
        break
      elif opcao == 0:
        break
      else:
        print('Essa não é uma opção válida')
        continue
    except ValueError:
      print('É necessário inserir um número')
      continue

def main():
  while True:
    opcao = menu()
    try:
      opcao = int(opcao)
      if opcao == 1:
        search, livro = load_resources(opcao)
        display_menu(search,livro)
      elif opcao == 2:
        search, livro = load_resources(opcao)
        display_menu(search,livro)
      elif opcao == 3:
        search, livro = load_resources(opcao)
        display_menu(search,livro)
      elif opcao == 4:
        display_favs_menu()
      elif opcao == 0:
        print('Encerrando...')
        break
      else:
        print('Essa não é uma opção válida')
        continue
    except ValueError:
      print('É necessário inserir um número')
      continue

main()
