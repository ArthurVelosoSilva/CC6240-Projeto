# Projeto 3 - Graph Database

## Autor

**Nome:** Arthur Veloso  
**Matrícula:** 22.221.038-7

## Descrição do Projeto

Este projeto tem como objetivo modelar, migrar e consultar dados acadêmicos utilizando um banco de dados grafo (Neo4j).

O modelo contempla os seguintes elementos:

- Alunos  
- Professores  
- Cursos  
- Departamentos  
- Disciplinas  
- Matrizes curriculares  
- Grupos de TCC

A estrutura permite responder a questões como:

- Histórico escolar de qualquer aluno  
- Disciplinas ministradas por qualquer professor  
- Alunos formados em determinado semestre ou ano  
- Professores que atuam como chefes de departamento  
- Alunos que participam de grupos de TCC e seus respectivos orientadores

## Banco de Dados Utilizado

**Neo4j AuraDB (nuvem)**  
URI: `neo4j+s://326fa464.databases.neo4j.io`  

**Autenticação:**  
- Usuário: `neo4j`  
- Senha: presente no `main.py`

## Estrutura de Arquivos

| Arquivo                        | Descrição                                                                 |
|-------------------------------|---------------------------------------------------------------------------|
| `main.py`                     | Script principal que carrega dados, cria relacionamentos e executa consultas |
| `criar_nos.cypher`            | Criação dos nós principais (alunos, professores, cursos, etc.)             |
| `criar_relacionamentos.cypher`| Criação dos relacionamentos entre os nós (ex: ministra, cursou, pertence_a)|
| `consultas_grafo.cypher`      | Consultas para atender os requisitos definidos                             |
| `README.md`                   | Documentação e instruções de execução                                      |

## Nós e Relacionamentos

### Nós

- `Aluno` (matricula, nome)  
- `Professor` (nome)  
- `Departamento` (nome)  
- `Curso` (codigo, nome)  
- `Disciplina` (codigo, nome)  
- `GrupoTCC` (id)

### Relacionamentos

- `(Curso)-[:PERTENCE_A]->(Departamento)`  
- `(Curso)-[:INCLUI]->(Disciplina)`  
- `(Aluno)-[:CURSOU {semestre, ano, notaFinal}]->(Disciplina)`  
- `(Professor)-[:MINISTRA {semestre, ano}]->(Disciplina)`  
- `(Professor)-[:CHEFE_DE]->(Departamento)`  
- `(Aluno)-[:PERTENCE_A]->(GrupoTCC)`  
- `(Professor)-[:ORIENTA]->(GrupoTCC)`

### Pré-requisitos

- Python 3.8 ou superior  
- Conta no Neo4j Aura  
- Instalar dependências:

```bash
pip install neo4j
