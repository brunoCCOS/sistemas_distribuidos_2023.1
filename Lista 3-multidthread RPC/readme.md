<h2> Arquitetura de Software </h2>

 A arquitetura de software da solução foi baseada em objetos. Temos essencialmente 4 componentes que se comunicam entre si e são responsáveis pelas próprios processos: Processo,Interface,Database,Fila. As chamadas de comunicação entre elas acontece através da chamada de métodos de cada classe e envio de mensagens(caso do Cliente e Server).

 Interface: Responsável pela comunicação e envio de requisições a respeito do dicionário, serve como uma interface ao usuário.
 Métodos:

 <ul>
    <li>process_input: Faz o tratamento inicial e chamada ao servidor </li>

 </ul>

 Processo: Cuida e trata de todos as rotinas de caráter de recebimento e processamento de requisições por parte do servidor, serve como uma interface entre o usuário o cliente e os outros recursos
 Métodos: 

<ul>
    <li>processar_requisicao: Processa a requisição e resolve o tipo de operação
    <li>processar_registro: Cadastra uma nova palavra no db
    <li>processar_consulta: Retorna o valor de uma palavra

 </ul>

 Database: Trata da conexão,persistência,inserção e busca de informações dentro do dicionário
 Métodos:

 <ul>
    <li>carregar_dicionario: Inicializa a base de dados e desserializa dicionário
    <li>salvar_dicionario: Serializa dicionário e salva
    <li>adicionar_definicao: Insere par chave valor no dicionário
    <li>obter_definicoes: Retorna valor de uma chave
    <li>persistir_dicionario: Persiste o dicionário
 </ul>

 Fila: Instancia e guarda o estado e ordem das requisições
 Métodos:

 <ul>
    <li>adicionar_requisicao: Insere mensagem no fim da fila de requisição 
    <li>obter_requisicao: Retorna o primeiro pedido da fila
    <li>adicionar_resposta: Adiciona uma resposta a fila de respostas
    <li>obter_resposta: Obtem a resposta da fila de respostas pelo ID da requisição
    <li>checar_resposta: Checa se a resposta esta na fila de respostas pelo ID da requisição
    <li>check_vazia: Checa se a fila está vazioa
 </ul>

<h2> Arquitetura Cliente/Servidor </h2>

 Para o modelo Cliente/Servidor nossos componentes residirão todos do lado do servidor com excessão do componente cliente. O cliente fica responsável por estabelecer conexão ao servidor e enviar requisições e aguardar respostas, enquanto o servidor é responsável por ouvir por conexões e requisições e processa-las de acordo. As mensagens trocadas são no formato de string, sendo esperado do cliente uma mensagem entre os dois tipos (word ou word:sentence). O conteúdo nela deve conter a chave referente a palavra do dicionário a ser acessada (caso word) ou a palavra e a definição para a mesma que deve ser cadastrada (caso word:sentence). O servidor por sua vez atende paralelamente múltiplos clientes que tem suas requisições enviadas a uma fila, onde uma única thread é responsável por processa-la sequencialmente e devolver as respostas as requisições indexadas por ID, 

 Servidor: Responsável pelo estabelecimento do endpoint e processamento das requisições enviadas a ele
 Métodos:

 <ul>
   <li>process_input: Faz o tratamento inicial e chamada ao servidor </li>
   <li>adicionar_requisicao: Adiciona requisição ao fim da fila
   <li>desligar: Anuncia intenção de desligar o servidor e para de aceitar requisições
   <li>shutdown: Encerra a conexão e persiste o dicionário
   <li>monitorar_prompt: Trata entradas do keyboard e processa comandos de desligamente e histórico de usuários
   <li>listar_clientes_conectados: Printa lista de conexões realizadas
   <li>iniciar: Inicializa o servidor
 </ul>
 Classe secundária :
  <p> Atendentes: Cuida e processa das requisições na fila

 Cliente: Responsável pelo estabelecimento da conexão com o servidor e envio das requisições
 Métodos: Opera atráves do componente de interface



