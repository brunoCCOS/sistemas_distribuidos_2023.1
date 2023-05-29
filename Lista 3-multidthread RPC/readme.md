<h2> Arquitetura de Software </h2>

 A arquitetura de software da solução foi baseada em objetos. Temos essencialmente 4 componentes que se comunicam entre si e são responsáveis pelas próprios processos: Server,Cliente,Database,Fila. As chamadas de comunicação entre elas acontece através da chamada de métodos de cada classe e envio de mensagens(caso do Cliente e Server).

 Cliente: Responsável pela comunicação e envio de requisições a respeito do dicionário, serve como uma interface ao usuário.
 Métodos:

 <ul>
    <li>IniciaCliente: Realiza conexão com o socket e instancia objeto </li>
    <li>fazRequisicoes: Envie requisicoes ao servidor e printa resposta </li>

 </ul>

 Server: Cuida e trata de todos as rotinas de caráter de recebimento e processamento de requisições por parte do servidor, serve como uma interface entre o usuário o cliente e os outros recursos
 Métodos: 

<ul>
    <li>start_server: Inicializa servidor e ouve por requisições
    <li>aceitaConexao: Aceita conexão
    <li>atendeRequisicoes: Processa as requisições e chama as rotinas necessárias
    <li>check_requisicao: Verifica se a requisição está no formato esperado
    <li>shutdown: Persiste banco de dados e desliga servidor
 </ul>

 Database: Trata da conexão,persistência,inserção e busca de informações dentro do dicionário
 Métodos:

 <ul>
    <li>connect_db: Inicializa a base de dados e serializa dicionário
    <li>read_key: Procura pela chave e retorna valor no dicionário
    <li>insert_pair: Insere par chave valor no dicionário
    <li>persist_db: Serializa dicionário
 </ul>

 Fila: Instancia e guarda o estado e ordem das requisições
 Métodos:

 <ul>
    <li>get_first: Retorna o primeiro pedido da fila
    <li>insert_msg: Insere mensagem no fim da fila
    <li>check_empty: checa fila para ver se está vazio
 </ul>

<h2> Arquitetura Cliente/Servidor </h2>

 Para o modelo Cliente/Servidor nossos componentes residirão todos do lado do servidor com excessão do componente cliente. O cliente fica responsável por estabelecer conexão ao servidor e enviar requisições e aguardar respostas, enquanto o servidor é responsável por ouvir por conexões e requisições e processa-las de acordo. As mensagens trocadas são no formato de string, sendo esperado do cliente uma mensagem entre os dois tipos (word ou word:sentence), caso contrário o servidor retornará erro. O conteúdo nela deve contar a chave referente a palavra do dicionário a ser acessada (caso word) ou a palavra e a definição para a mesma que deve ser cadastrada (caso word:sentence)

