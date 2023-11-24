import requests

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
      name = (received_data[book]["title"]).title().strip()
      name = name.split('(')[0]
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
      category = received_data[book]["categories"][0]
    except KeyError:
      category = None
    try:
      description = received_data[book]["description"]
      description = '.\n'.join(description.split('. '))
    except KeyError:
      description = None
    books.append([name, authors, publisher, pages, category, description])
  return books

def create_dict(books):
  for book in books:
    basic_book_info = ['title', 'author','publisher','pages','categories','description']
    book_info = [book[0], book[1], book[2], book[3], book[4], book[5]]
    books_found_list = {key_name:info_book for key_name,info_book in zip(basic_book_info,book_info)}
  return books_found_list