// Chefe de departamento
MATCH (p:Professor {nome: "Joao"}), (d:Departamento {nome: "Engenharia"}) CREATE (p)-[:CHEFE_DE]->(d);
MATCH (p:Professor {nome: "Maria"}), (d:Departamento {nome: "Matematica"}) CREATE (p)-[:CHEFE_DE]->(d);
MATCH (p:Professor {nome: "Fernanda"}), (d:Departamento {nome: "Computacao"}) CREATE (p)-[:CHEFE_DE]->(d);

// Curso -> Departamento
MATCH (c:Curso {codigo: "ENG01"}), (d:Departamento {nome: "Engenharia"}) CREATE (c)-[:PERTENCE_A]->(d);
MATCH (c:Curso {codigo: "MAT01"}), (d:Departamento {nome: "Matematica"}) CREATE (c)-[:PERTENCE_A]->(d);
MATCH (c:Curso {codigo: "COMP01"}), (d:Departamento {nome: "Computacao"}) CREATE (c)-[:PERTENCE_A]->(d);

// Curso -> Disciplinas
MATCH (c:Curso {codigo: "ENG01"}), (d1:Disciplina {codigo: "ENG101"}), (d2:Disciplina {codigo: "ENG102"}) 
CREATE (c)-[:INCLUI]->(d1), (c)-[:INCLUI]->(d2);

MATCH (c:Curso {codigo: "MAT01"}), (d1:Disciplina {codigo: "MAT101"}), (d2:Disciplina {codigo: "MAT102"}) 
CREATE (c)-[:INCLUI]->(d1), (c)-[:INCLUI]->(d2);

MATCH (c:Curso {codigo: "COMP01"}), (d1:Disciplina {codigo: "COMP201"}), (d2:Disciplina {codigo: "COMP202"}) 
CREATE (c)-[:INCLUI]->(d1), (c)-[:INCLUI]->(d2);

// Professores -> Disciplinas
MATCH (p:Professor {nome: "Joao"}), (d:Disciplina {codigo: "ENG101"}) CREATE (p)-[:MINISTRA {semestre: 1, ano: 2025}]->(d);
MATCH (p:Professor {nome: "Maria"}), (d:Disciplina {codigo: "MAT101"}) CREATE (p)-[:MINISTRA {semestre: 1, ano: 2025}]->(d);
MATCH (p:Professor {nome: "Fernanda"}), (d:Disciplina {codigo: "COMP201"}) CREATE (p)-[:MINISTRA {semestre: 1, ano: 2025}]->(d);

// Alunos -> Disciplinas (histórico)
MATCH (a:Aluno {matricula: "2023001"}), (d:Disciplina {codigo: "ENG101"}) CREATE (a)-[:CURSOU {semestre: 1, ano: 2025, notaFinal: 8.5}]->(d);
MATCH (a:Aluno {matricula: "2023001"}), (d:Disciplina {codigo: "ENG102"}) CREATE (a)-[:CURSOU {semestre: 2, ano: 2025, notaFinal: 7.0}]->(d);

MATCH (a:Aluno {matricula: "2023002"}), (d:Disciplina {codigo: "MAT101"}) CREATE (a)-[:CURSOU {semestre: 1, ano: 2025, notaFinal: 9.0}]->(d);
MATCH (a:Aluno {matricula: "2023002"}), (d:Disciplina {codigo: "MAT102"}) CREATE (a)-[:CURSOU {semestre: 2, ano: 2025, notaFinal: 8.0}]->(d);

MATCH (a:Aluno {matricula: "2023003"}), (d:Disciplina {codigo: "COMP201"}) CREATE (a)-[:CURSOU {semestre: 1, ano: 2025, notaFinal: 7.5}]->(d);
MATCH (a:Aluno {matricula: "2023003"}), (d:Disciplina {codigo: "COMP202"}) CREATE (a)-[:CURSOU {semestre: 2, ano: 2025, notaFinal: 6.5}]->(d);

// TCC
CREATE (tcc:GrupoTCC {id: 1});
MATCH (a1:Aluno {matricula: "2023001"}), (a2:Aluno {matricula: "2023002"}), (prof:Professor {nome: "Carlos"}) 
CREATE (a1)-[:PERTENCE_A]->(tcc), (a2)-[:PERTENCE_A]->(tcc), (prof)-[:ORIENTA]->(tcc);
