# Projeto Banco NoSQL para Faculdade

## Descrição

Este projeto utiliza o MongoDB para armazenar informações sobre alunos, professores, cursos, departamentos, disciplinas e matrizes curriculares, permitindo consultas importantes como histórico escolar, disciplinas ministradas, alunos formados, chefes de departamento e grupos de TCC.

---

## Estrutura do Projeto e Descrição dos Arquivos

- **main.py**  
  Contém a conexão com o MongoDB, definição das coleções, execução das queries principais para consulta dos dados e fechamento da conexão.

- **data_inserts.py**  
  Script responsável por limpar o banco de dados e inserir os dados iniciais de teste nas coleções: alunos, professores, cursos, departamentos, disciplinas e grupos de TCC.

- **queries.py**  
  Contém as funções com as queries MongoDB para realizar as consultas solicitadas, como o histórico escolar de alunos, disciplinas ministradas, alunos formados, professores chefes de departamento e grupos de TCC.

---

## Modelo de Dados

### Coleções e Campos principais:

- **Alunos**  
  - `_id`: string (ID do aluno)  
  - `nome`: string  
  - `curso`: string (referência ao curso)  
  - `disciplinas_cursadas`: lista de documentos com campos:  
    - `codigo`: string (código da disciplina)  
    - `ano`: int  
    - `semestre`: int  
    - `nota`: float  
  - `tcc`: documento com `grupo_id` e `orientador`

- **Professores**  
  - `_id`: string (ID do professor)  
  - `nome`: string  
  - `departamento`: string (referência ao departamento)  
  - `disciplinas_ministradas`: lista de documentos com `codigo`, `ano` e `semestre`

- **Cursos**  
  - `_id`: string (ID do curso)  
  - `nome`: string  
  - `matriz_curricular`: lista de códigos de disciplinas

- **Departamentos**  
  - `_id`: string (ID do departamento)  
  - `nome`: string  
  - `chefe`: string (ID do professor chefe)

- **Disciplinas**  
  - `_id`: string (código da disciplina)  
  - `nome`: string  
  - `departamento`: string (ID do departamento)

- **GruposTCC**  
  - `_id`: string (ID do grupo)  
  - `ano`: int  
  - `semestre`: int  
  - `alunos`: lista de IDs de alunos  
  - `orientador`: ID do professor

---

## Validação das Queries

Após rodar o `main.py`, valide as queries com base nos seguintes critérios:

1. **Histórico Escolar de um Aluno**  
   - **Entrada:** ID do aluno (ex: `"A1"`)  
   - **Saída esperada:** Lista das disciplinas cursadas pelo aluno, contendo código, nome, ano, semestre e nota.  
   - **Validação:** Confirme que todas as disciplinas listadas foram realmente cursadas e que os dados batem com os inseridos no banco.

2. **Disciplinas Ministradas por um Professor**  
   - **Entrada:** ID do professor (ex: `"P1"`)  
   - **Saída esperada:** Lista das disciplinas que o professor ministrou, com ano e semestre.  
   - **Validação:** Confira que as disciplinas e períodos correspondem aos registros da coleção de professores.

3. **Alunos Formados em um Semestre e Ano**  
   - **Entrada:** Ano e semestre (ex: `2024`, semestre `1`)  
   - **Saída esperada:** Lista de alunos que completaram todas as disciplinas da matriz curricular do curso antes ou até o semestre informado.  
   - **Validação:** Verifique se os alunos retornados possuem todas as disciplinas exigidas e que suas notas são aprovadas.

4. **Professores Chefes de Departamento**  
   - **Saída esperada:** Lista com o nome do professor chefe e o departamento que ele lidera.  
   - **Validação:** Confirme que cada professor listado é realmente o chefe do respectivo departamento.

5. **Grupos de TCC**  
   - **Saída esperada:** Listagem dos grupos de TCC com informações do ano, semestre, alunos participantes e orientador.  
   - **Validação:** Cheque se os alunos e orientadores listados pertencem aos grupos de TCC conforme dados inseridos.

