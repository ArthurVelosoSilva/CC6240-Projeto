# Projeto NoSQL - Wide-column Store com DataStax Astra

**Aluno:** Arthur Veloso  
**Matrícula:** 22.221.038-7

## Descrição do Projeto

Este projeto tem como objetivo migrar um banco de dados relacional desenvolvido na disciplina CC6240 para um banco NoSQL do tipo *Wide-column Store*, utilizando o DataStax Astra.

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

### Instalação

1. Instale a biblioteca necessária:

```bash
pip install cassandra-driver
