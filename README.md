
# README.md

## Afazeres

- [ ] Linkar os `check buttons` e os `select menus` ao Flask
- [ ] Criar função de elaboração de _concordance_ da palavra pelo contexto de onde ela é retirada.
- Funcionalidades
	- [ ] Lematizar
	- [ ] Dar o contexto
	- [ ] Pegar exemplos da internet via scraping 
	- [ ] Conectar com o Anki
		- [ ] Comparar com o vocabulário presente no Anki

## Futuro

- [ ] Treinar modelo de tradução para prescindir do Context Reverso
- [ ] Estimar $\theta$ do usuário a partir dos seus escores no Anki
- [ ] Criar banco de dados com as palavras já inseridas e os contextos onde elas aparecem
	- [ ] O banco deve lematizar as palavras para ou inseri-las no banco de lemas ou descobrir a qual lema associá-la; no banco podem ficar reservados os exemplos do mesmo lema sendo flexionado em diferentes variantes, e a partir desse novos exemplos podem ser elaborados.
	- [ ] Após a criação do modelo de tradução, esses banco pode passar por algo como um teste de coerência, para ver se o input faz sentido ou se o se está alimentando com _gibberish_.
