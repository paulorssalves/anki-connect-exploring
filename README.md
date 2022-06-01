# TODO:

- [ ] Aperfeiçoar o modo como o scraper do BibleHub toma a decisão de qual link seguir
  - talvez se possa tentar lematizar os próprios títulos?
  - Testar com a palavra "Πατηρ"

- [ ] Procurar os blanks em outros lugares
	- considerar: 
		- [ ] Perseus Digital Library
		- [ ] Wiktionary

# DONE
- [X] arrumar forma de extrair contexto a partir da palavra 


- [X] Tornar a palavra em evidência da *concordance* negrita
	- é necessário inserir o HTML na string
	- É necessário discriminar o conteúdo "left" e "right" da concordance
- [X] cortar última e primeira palavra de uma dada *concordance* **desde que** ela não seja a palavra em foco. 

- [X] Aperfeiçoar a função `searcher` como exposto no comentário acima dela

- [X] Organizar os arquivos dos programas:
	- Reduzir a redundância das ferramentas utilizadas e seus nomes
		- "Tools" e "Toolset", por exemplo
	- Colocá-las em uma pasta (como "Tools", neste caso sendo necessário alterar o nome de "Tools" e "Toolset"
	- Criar uma pasta para ser o diretório dos .csv
	- Criar uma pasta para ser o diretório dos .txt

- [X] Direcionar os outputs e blanks direto para seus diretórios específicos

- [X] Inserir *qual é a palavra original* nos dados a serem inseridos no flashcard
- [X] Inserir *a fonte dos dados* nos dados a serem inseridos no flashcard

- [X] Limpar os resultados das palavras obtidas do BibleHub para remover as flexões extras dos termos

