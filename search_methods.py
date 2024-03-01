import requests

def search_name(search_method:int) ->str:
  """Get the name to be searched on the API.\n
  Receive the option that define the kind of search
  and return a string using APIs' pattern.
  """
  search = ['livro','coleção','autor']
  name = input(f'Insira o nome do {search[search_method-1]}: ').lower()
  name = name.strip()
  name = name.replace(' ','+')
  return name

def search_mode(search_method:int) ->str:
  """Define how specific the search should be, according to APIs' pattern.\n
  Return a string that will be concatenated on the url.
  """
  mode = ['intitle:','inauthor:']
  if search_method == 1:
    search_method = mode[0]
  elif search_method == 3:
    search_method = mode[1]
  else:
    search_method = ''
  return search_method

def search_method(answer:int):
  """Unify the user input for name and mode in a single tuple.\n
  Returns:
      (name, mode)"""
  name = search_name(answer)
  mode = search_mode(answer)
  return (name,mode)

def get_results(name:str,tipo:str):
  """Send a request to the API using the get method.\n
  Returns a json with the data.
  """
  url = f'https://www.googleapis.com/books/v1/volumes?q={tipo}{name}&printType=books&langRestrict=pt&maxResults=1'
  response = requests.get(url)
  data = response.json()
  return data

def separate_book_info(data) ->list:
  """Filter the data from the json, keeping only what will be used."""
  information = []
  for i in range(len(data["items"])):
    volumeInfo = data["items"][i]["volumeInfo"]
    information.append(volumeInfo)
  return information

def colect_errors(received_data) ->list:
  """Generate a list with the information provided from the API.\n
  It catalogs the json keys, adding the values that will be displayed for the user into a list.\n
  Returns:
      [name, author, publisher, pages, category, description]"""
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

def create_dict(books:list) ->dict:
  """Create a dictionary for any book using the json structure from this program.\n
  Returns:
      { title : name, author : author, publisher : publisher,
      pages : pages, categories : category, description : description }"""
  for book in books:
    basic_book_info = ['title', 'author','publisher','pages','categories','description']
    book_info = [book[0], book[1], book[2], book[3], book[4], book[5]]
    books_found_list = dict(zip(basic_book_info,book_info))
  return books_found_list