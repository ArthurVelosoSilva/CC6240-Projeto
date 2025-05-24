CREATE TABLE IF NOT EXISTS aluno (
    ra TEXT PRIMARY KEY,
    nome TEXT,
    curso_id TEXT
);

CREATE TABLE IF NOT EXISTS professor (
    prontuario TEXT PRIMARY KEY,
    nome TEXT,
    departamento_id TEXT
);

CREATE TABLE IF NOT EXISTS departamento (
    id TEXT PRIMARY KEY,
    nome TEXT,
    chefe_prontuario TEXT
);

CREATE TABLE IF NOT EXISTS curso (
    id TEXT PRIMARY KEY,
    nome TEXT,
    departamento_id TEXT
);

CREATE TABLE IF NOT EXISTS disciplina (
    codigo TEXT PRIMARY KEY,
    nome TEXT,
    curso_id TEXT
);

CREATE TABLE IF NOT EXISTS matriz_curricular (
    curso_id TEXT,
    codigo_disciplina TEXT,
    obrigatoria BOOLEAN,
    PRIMARY KEY (curso_id, codigo_disciplina)
);

CREATE TABLE IF NOT EXISTS historico (
    ra TEXT,
    ano INT,
    semestre INT,
    codigo_disciplina TEXT,
    nota_final FLOAT,
    PRIMARY KEY ((ra), ano, semestre, codigo_disciplina)
);

CREATE TABLE IF NOT EXISTS tcc (
    grupo_id TEXT PRIMARY KEY,
    ra1 TEXT,
    ra2 TEXT,
    ra3 TEXT,
    orientador TEXT,
    ano INT,
    semestre INT
);

-- Tabelas extras para casos especiais --

CREATE TABLE IF NOT EXISTS professor_disciplina (
    prontuario TEXT,
    codigo_disciplina TEXT,
    PRIMARY KEY (prontuario, codigo_disciplina)
);

CREATE TABLE IF NOT EXISTS aluno_status_formatura (
    ra TEXT PRIMARY KEY,
    formou BOOLEAN
);

CREATE TABLE IF NOT EXISTS departamento_com_chefe (
    id TEXT PRIMARY KEY,
    nome TEXT,
    chefe_prontuario TEXT,
    chefe_nome TEXT
);
