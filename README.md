# Check_list_API
<p>
Neste repositorio foi feito uma aplicação RESTful com proposito de servir recursos baseado ne uma lista to-do. 'nome', 'descrição', 'deadline' e 'status' são os atributos que compõem a tarefa. Foi utilizado no desenvolvimento o framework Flask, o ORM SQLAlchemy e o Serializador Marshmallow. Além da lib flask_restx que contem o Blueprint e o Swagger para a documentação.
</p>
<p>
 O intuito desse projeto é desenvolver bons fundamentos em algoritimos, boa pratica de programação (metodos e atributos e organização dos folders), utilização correta da classe de serialização e Model, e coerencia lógica nos endpoinst
</p>
<h2>Instalação</h2>
<p>para fazer a instalação da aplicação você deve ter o python 3 instalado na sua maquin, além de ser recomendável a criação de um ambiente virtual de desenvolvimento 'venv'</p>
Passo 1- instale as dependencias necessarias da aplicação.<br>
 SO Windows
	
```
pip install requirements.txt       
```
 SO Linux

```
pip install -r requirements.txt
```
Após essa configurações já sera possivel rodar a aplicação utilizando-o

```
python main.py
```
<h2>EndPoints</h2>
<ul>
    <li> 'GET api/to_do': Retorna todas as tarefas existentes.</li>
    <li> 'POST api/to_do': Cria uma nova tarefa.</li>
    <li> 'GET api/to_do/{id}': Retorna uma tarefa específica com base no ID.</li>
    <li> 'GET api/to_do/{name}': Retorna a tarefa específica com base no seu nome.</li>
    <li> 'PUT api/to_do/{id}': Atualiza uma tarefa existente com base no ID</li>
    <li> 'DELETE api/to_do/{id}': Remove uma tarefa existente. com base no ID</li>
</ul>
<h2>Corpo da Requisição</h2>
<p>
Para o campo 'status' sera aceito apenas tres valores: nao feito, em progresso, finalizado.  
</p>
<p><b>As requisições devem ser do formato JSON</b></p>
Para o Metodo <b>POST</b>:
<p>{
   "name": "Revisão do Carro",<br>
   "description": "Levar o carro para a revisão do sistema de freio",<br>
   "deadline": "2024-05-12T15:03:34",<br>
   "status": "nao feito"
}</p>
Para o Metodo <b>PUT</b>:
<p>{
   "name": "Revisão do Carro",<br>
   "description": "Levar o carro para a revisão do sistema de freio",<br>
   "deadline": "2024-05-12T15:03:34",<br>
   "status": "em progresso"
}</p>
O ID sera passado pelo Headers <br>
Para as get e delete devera ser passado o id desejado pelo 'headers'.<br>
Para o get com filtro, devera ser passado o nome da tarefa (name) pelo 'headers'.<br>

<h2>Para mais informações a respeito dos parâmetros</h2>
<p>você pode acessar 'api/docs' onde tera as informações completas sobre o corpo das requisições e poderá testalas usando uma interface de requisição nativa da aplicação</p>

<h2>Code Status</h2>
  <p>Na aplicação é usado 5 status code como resposta</p>
  200: retornado ao executar com sucesso uma requisição get, uma requisição get com id, uma requisição get com 'name' e uma   atualização de dados via put. <br>
  201: ao criar uma nova to_do (POST) <br>
  204: ao deletar (DELETE) com sucesso uma tarefa <br>
  400: ao existir um erro na sintaxe passada em: PUT e POST <br>
  404: ao não encontrar um intem buscado em: GET por id, DELETE e GET por 'name' <br>
<h2>Tratamento de Erros</h2>
<p>
A aplicação tratara erros de forma adequada retornando o devido 'status code' e sua 'messenge'. Isso facilitará na hora de corrigir uma solicitação mal feita ou atributos enviados de forma erronea.
</p>
<p>Por Exemplo: ao fizer um POST com o atributo status fora do padrão aceito, ele ira informar de forma clara quais campos são aceitos na requisição.</p>
{<br>
  "name": "Revisão do Carro",<br>
  "description": "Levar o carro para a revisão do sistema de freio",<br>
  "deadline": "2024-05-12T15:03:34",<br>
  "status": "fazendo"<br>
}
<p>
response: 400 Undocumented Error: BAD REQUEST <br>
{ <br>
  "message": "Data Validation Error: {'status': ['Must be one of: nao feito, em progresso, finalizado.']}" <br>
}
 </p>

 
