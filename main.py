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
  url = f'https://www.googleapis.com/books/v1/volumes?q={tipo}{name}&printType=books&langRestrict=pt&maxResults=5'
  response = requests.get(url)
  data = response.json()
  return data



def main():
  start = search_method()
  name = search_name(start)
  mode = search_mode(start)
  data = get_results(name,mode)
  print(data)
main()