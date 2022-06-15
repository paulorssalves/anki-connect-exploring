# TODO:

- [ ] Aperfeiçoar o modo como o scraper do BibleHub toma a decisão de qual link seguir
  - talvez se possa tentar lematizar os próprios títulos?
  - Testar com a palavra "Πατηρ"

- [ ] Procurar os blanks em outros lugares
	- considerar: 
		- [ ] Perseus Digital Library
		- [ ] Wiktionary

- [ ] Fazer com que programa analise o CSV no final da iteração e remova as aspas extras
- [ ] Trocar os "\n" do coletor de exemplos do BibleHub por "<br><br>" 

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

- [X] Fazer com que o *Wait* entre iterações de busca não produza múltiplas linhas, mas que se atualize em um mesmo lugar tal como a barra de carregamento.

- [X] acrescentar aspas a todas as células do .csv, para evitar que eventuais vírgulas baguncem a formatação do documento
	- basicamente estão sendo acrescentados espaços/quebras-de-células entre interpontos e ponto-e-vírgulas

- [X] Fazer com que o material seja criado instantanemaente após a aquisição de cada palavra, para não depender de alcançar até o final do script para conseguir extrair *alguma* coisa.
