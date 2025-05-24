// Criar Alunos
CREATE (:Aluno {matricula: "2023001", nome: "Ana"});
CREATE (:Aluno {matricula: "2023002", nome: "Bruno"});
CREATE (:Aluno {matricula: "2023003", nome: "Carla"});
CREATE (:Aluno {matricula: "2023004", nome: "Daniel"});
CREATE (:Aluno {matricula: "2023005", nome: "Eduarda"});

// Criar Professores
CREATE (:Professor {nome: "Joao"});
CREATE (:Professor {nome: "Maria"});
CREATE (:Professor {nome: "Carlos"});
CREATE (:Professor {nome: "Fernanda"});

// Criar Departamentos
CREATE (:Departamento {nome: "Engenharia"});
CREATE (:Departamento {nome: "Matematica"});
CREATE (:Departamento {nome: "Computacao"});

// Criar Cursos
CREATE (:Curso {codigo: "ENG01", nome: "Engenharia de Software"});
CREATE (:Curso {codigo: "MAT01", nome: "Matematica Aplicada"});
CREATE (:Curso {codigo: "COMP01", nome: "Ciência da Computação"});

// Criar Disciplinas
CREATE (:Disciplina {codigo: "ENG101", nome: "Programação I"});
CREATE (:Disciplina {codigo: "ENG102", nome: "Estruturas de Dados"});
CREATE (:Disciplina {codigo: "MAT101", nome: "Cálculo I"});
CREATE (:Disciplina {codigo: "MAT102", nome: "Álgebra Linear"});
CREATE (:Disciplina {codigo: "COMP201", nome: "Banco de Dados"});
CREATE (:Disciplina {codigo: "COMP202", nome: "Redes de Computadores"});
