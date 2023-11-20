import requests


def search_method():
  print('''O que você está procurando?
    1 - Um título específico
    2 - Uma coleção
    3 - Um autor''')
  search = None
  while True:
    answer = input('Digite aqui: ')
    try:
      answer = int(answer)
      if answer == 1:
        search = answer
        break
      elif answer == 2:
        search = answer
        break
      elif answer == 3:
        search = answer
        break
      else:
        print('Essa não é uma opção válida')
        continue
    except ValueError:
      print('É necessário inserir um número')
  return search

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

def get_results(name,tipo):
  import requests
  url = f'https://www.googleapis.com/books/v1/volumes?q={tipo}{name}&printType=books&langRestrict=pt&maxResults=5'
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
      title = (received_data[book]["title"]).title()
    except KeyError:
      title = None
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
    books.append([title, authors, publisher, pages, description])
  return books

def show_results(book):
  for i in range(len(book)):
    print(f'{book[i][0]} \nAutor: {book[i][1]}\t Editora: {book[i][2]}\t Páginas: {book[i][3]}\nDescrição: \n{book[i][4]}')


def main():
  start = search_method()
  name = search_name(start)
  mode = search_mode(start)
  data = get_results(name,mode)
  print(data)
main()