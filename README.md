# Interface de consulta e armazenamento de livros
#### Projeto desenvolvido para o módulo 2 do curso Vem Ser Tech - Dados.

## Objetivos:
* Obter dados em uma API;
* Adicionar e remover dados em um arquivo JSON;
* Obter dados estatísticos a partir dos dados armazenados,

## Requisitos:
* Ler uma lista de objetos de um JSON;
* Realizar um mapeamento, um filtro e uma redução (map, filter e reduce);
* Garantir que todas as operações tenham validações (try-except);
* Criar uma função para obter uma lista de tuplas, com o máximo (ou o mínimo) valor de algum atributo numérico;
* Ao menos uma função deve ter um parâmetro opcional.

## Sobre o projeto:
* Linguagem: [Python](https://www.python.org/)
* API: [Google Books](https://developers.google.com/books?hl=pt-br)
* Bibliotecas: [Requests](https://pypi.org/project/requests/) & [JSON](https://docs.python.org/3/library/json.html)

## Preview:

### Usabilidade:
As opções disponíveis para o usuário são exibidas em menus, de modo que o usuário sempre tenha o controle sobre a ação que deseja tomar.
![Menu Inicial](menu.png)<br>
Após realizar sua pesquisa, o usuário é perguntado se deseja adicionar o livro aos favoritos ou pesquisar novamente. Na primeira opção, o livro é salvo e o usuário retorna ao menu principal, já na segunda o usuário retorna ao campo de pesquisa com o mesmo parâmetro que o definido anteriormente.

### Requisições:
As requisições são feitas a API de acordo com os parâmetros informados pelo usuário, permitindo uma busca mais específica.
O retorno da API é tratado - tanto em relação aos dados que serão utilizados quanto ao seu valor (por padrão, campos vazios são substituídos por None) - e por fim transformado em um novo dicionário com as informações pertinentes ao projeto. Por fim, os dados são exibidos ao usuário.<br>
*Importante:* Por questões de desempenho e usabilidade no terminal, somente um livro é buscado por vez.

### Persistência de dados:
Os dados são salvos em um arquivo JSON na estrutura de lista de dicionários com as seguintes chaves:
> Título, Autor, Editora, Páginas, Categoria e Descrição

### Buscas no arquivo JSON:
As buscas no arquivo json são feitas com os valores das chaves. Por padrão a chave de busca é o título do livro - 'title'. É possível pesquisar com outras chaves com a função `show_favorites()`, embora até o momento não seja possível ao usuário definir a chave de busca.

### Exibindo livros salvos:
Ao acessar a área de favoritos é exibido somente o nome dos livros, tal opção foi a que apresentou melhor design no terminal.<br>
Para obter informações detalhadas de cada livro, é necessário acessar a opção **2** (Detalhes sobre o livro) do sub-menu *Visualizar Favoritos*. Nesse caso é necessário digitar o nome do livro desejado a fim de receber a informação.<br>
Note que somente um livro é exibido em detalhes por vez.

### Dados estatísticos:
Localizado no item **3** (Informações adicionais) do sub-menu *Visualizar Favoritos*, os dados estatísticos obtidos são, na seguinte ordem:
- Maior livro e número de páginas;
- Menor livro e número de páginas;
- Quantidade de livros por categoria;
- Quantidade total de páginas;
- Média de páginas;
- Desvio padrão de páginas por livro.