# Projeto NoSQL - Wide-column Store com DataStax Astra

**Aluno:** Arthur Veloso  
**Matrícula:** 22.221.038-7

## Descrição do Projeto

Este projeto implementa um banco de dados NoSQL do tipo *Wide-column Store*, utilizando o DataStax Astra.

O modelo de dados foi adaptado para contemplar as seguintes entidades:

- Alunos  
- Professores  
- Cursos  
- Departamentos  
- Disciplinas  
- Matriz Curricular  
- Grupos de TCC  

Além da modelagem, o projeto responde a consultas que envolvem relacionamentos entre essas entidades, como:

1. Histórico escolar de um aluno  
2. Disciplinas ministradas por um professor  
3. Alunos formados em determinado semestre  
4. Professores que são chefes de departamento  
5. Alunos que formaram grupo de TCC e seus respectivos orientadores  

## Estrutura dos Arquivos

- **`connect_astra.py`**  
  Script responsável pela conexão com o banco de dados Astra DB, utilizando o bundle de segurança.

- **`cql_create_tables.cql`**  
  Contém os comandos CQL para criação das tabelas no banco NoSQL.

- **`cql_insert_data.cql`**  
  Script com os dados fictícios utilizados para popular as tabelas.

- **`cql_queries_relatorios.cql`**  
  Contém as queries utilizadas para gerar os relatórios e consultas do projeto.

- **`main.py`**  
  Executa o processo completo: criação das tabelas, inserção dos dados e execução das consultas.

## Como Executar

### Pré-requisitos

- Python 3.8 ou superior  
- Biblioteca `cassandra-driver`  
- Conta ativa no [DataStax Astra](https://www.datastax.com/astra)  
- Bundle de conexão seguro (`secure-connect-<seu-banco>.zip`)

### Passo a Passo para Rodar em Outro Computador

1. **Criar uma Conta no Astra DB**  
   Acesse [https://www.datastax.com/astra](https://www.datastax.com/astra) e crie uma conta gratuita (pode usar login com Google).

2. **Criar um Novo Banco de Dados**
   - Vá para "Dashboard" e clique em “Create Database”.
   - Dê um nome para o banco e selecione o provedor de nuvem desejado (recomenda-se usar o gratuito, se disponível).
   - Aguarde até que o banco esteja com status “ACTIVE”.

3. **Baixar o Bundle de Conexão**
   - Na página do banco, clique em “Connect”.
   - Escolha a opção **“Python”**.
   - Clique em **Download Bundle** para baixar o arquivo `secure-connect-<seu-banco>.zip`.

4. **Adicionar o Bundle ao Projeto**
   - Extraia o conteúdo do arquivo ZIP.
   - Copie a pasta extraída para o diretório raiz do projeto.
   - O nome da pasta deve coincidir com o nome usado no `connect_astra.py`.

5. **Instalar a Biblioteca Necessária**
   No terminal, execute:

   ```bash
   pip install cassandra-driver
