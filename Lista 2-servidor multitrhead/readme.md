<h2> Arquitetura de Software </h2>

 A arquitetura de software da solução foi baseada em objetos. Temos essencialmente 4 componentes que se comunicam entre si e são responsáveis pelas próprios processos: Server,Cliente,Database,Fila. As chamadasd de comunicação entre elas acontece atráves da chamada de métodos de cada classe e envio de mensagens(caso do Cliente e Server).

 Cliente: Responsavel pela comunicação e envio de requisições a respeito do dicionário, serve como uma interface ao usuário.
 Métodos: <il>
    IniciaCliente: Realiza conexão com o socket e instancia objeto
    fazRequisicoes: Envie requisicoes ao servidor e printa resposta 
 </il>

 Server: Cuida e trata de todos as rotinas de caráter de recebimento e processamento de requisições por parte do servidor, serve como uma interface entre o usuário o cliente e os outros recursos
 Métodos: <il>
    start_server: Inicializa servidor e ouve por requisições
    aceitaConexao: Aceita conexão
    atendeRequisicoes: Processa as requisições e chama as rotinas necessárias
    check_requisicao: Verifica se a requisição está no formato esperado
    shutdown: Persiste banco de dados e desliga servidor
 </il>

 Database: Trata da conexão,persistencia,inserção e busca de informações dentro do dicionário
 Métodos: <il>
    connect_db: Inicializa a base de dados e serializa dicionário
    read_key: Procura pela chave e retorna valor no dicionário
    insert_pair: Insere par chave valor no dicionário
    persist_db: Serializa dicionário
 </il>
 Fila: Instancia e guarda o estado e ordem das requisições
 Métodos: <il>
    get_first: Retorna o primeiro pedido da fila
    insert_msg: Insere mensagem no fim da fila
    check_empty: checa fila para ver se está vazio
 </il>

<h2> Arquitetura Cliente/Servidor </h2>

 Para o modelo Cliente/Servidor nossos componentes residirão todos do lado do servidor com excessão do componente cliente. O cliente fica responsável por estabelecer conexão ao servidor e enviar requisições e aguardar respostas, enquanto o servidor é responsável por ouvir por conexões e requisições e processa-las de acordo. As mensagens trocadas são no formato de string, sendo esperado do cliente uma mensagem entre os dois tipos (word ou word:sentence), caso contrário o servidor retornará erro. O conteudo nela deve contar a chave referente a palavra do dicionário a ser acessada (caso word) ou a palavra e a definição para a mesma que deve ser cadastrada (caso word:sentence)
 
