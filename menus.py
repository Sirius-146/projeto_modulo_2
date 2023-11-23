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