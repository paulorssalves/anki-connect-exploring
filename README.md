
# README.md

## Jupyter

- Instalar os pacotes em `requirements.txt` com pip
- Instalar os corpora: 
	- `punkt` com nltk.download('punkt')
	- `grc_models_cltk` com `importer = cltk.data.fetch.FetchCorpus(language='grc')` e `importer.import_corpus('grc_models_cltk')`

## Afazeres

### Context
- [ ] Criar um console readonly com o output que vai normalmente pro terminal (algo como um console.out())
	- Vai ser necessário usar JavaScript pra fazer isso
- [ ] Fazer o update do `#output_form` a cada _fetch()_ da API, em vez de só no final.

### Connect
- [ ] Linkar os `check buttons` e os `select menus` ao Flask
- [X] Criar função de elaboração de _concordance_ da palavra pelo contexto de onde ela é retirada.
- Funcionalidades
- [X] Lematizar
- [ ] Dar o contexto
- [ ] Pegar exemplos da internet via scraping (reaproveitar a implementação do _Context_)
- [ ] Conectar com o Anki
	- [ ] Comparar com o vocabulário presente no Anki

#### Futuro

- [ ] Calcular escore médio de texto a partir da pontuação das palavras individuais nele num índice de frequência
	- [ ] Lematizar a lista com os ngramas para determinar os radicais mais comuns (começar, na verdade, com o corpus de 10.000 palavras, para ver se o programa é escalável); 
		- [ ] n-gramas com posições diferentes na lista tem seus escores somados e a média dentre os dois (ou mais) é calculada, virando o novo escore.
- [ ] Treinar modelo de tradução para prescindir do Context Reverso
- [ ] Estimar $\theta$ do usuário a partir dos seus escores no Anki
- [ ] Criar banco de dados com as palavras já inseridas e os contextos onde elas aparecem
	- [ ] O banco deve lematizar as palavras para ou inseri-las no banco de lemas ou descobrir a qual lema associá-la; no banco podem ficar reservados os exemplos do mesmo lema sendo flexionado em diferentes variantes, e a partir desse novos exemplos podem ser elaborados.
	- [ ] Após a criação do modelo de tradução, esses banco pode passar por algo como um teste de coerência, para ver se o input faz sentido ou se o se está alimentando com _gibberish_.
