INSERT INTO aluno (ra, nome, curso_id) VALUES ('2021001', 'Ana Silva', 'ENG01');
INSERT INTO aluno (ra, nome, curso_id) VALUES ('2021002', 'Bruno Souza', 'ENG01');

INSERT INTO professor (prontuario, nome, departamento_id) VALUES ('P001', 'Dr. Carlos Lima', 'DPT01');

INSERT INTO departamento (id, nome, chefe_prontuario) VALUES ('DPT01', 'Engenharia', 'P001');

INSERT INTO curso (id, nome, departamento_id) VALUES ('ENG01', 'Engenharia Mecânica', 'DPT01');

INSERT INTO disciplina (codigo, nome, curso_id) VALUES ('MEC101', 'Mecânica Geral', 'ENG01');
INSERT INTO disciplina (codigo, nome, curso_id) VALUES ('MEC102', 'Termodinâmica', 'ENG01');

INSERT INTO matriz_curricular (curso_id, codigo_disciplina, obrigatoria) VALUES ('ENG01', 'MEC101', true);
INSERT INTO matriz_curricular (curso_id, codigo_disciplina, obrigatoria) VALUES ('ENG01', 'MEC102', true);

INSERT INTO historico (ra, ano, semestre, codigo_disciplina, nota_final) 
VALUES ('2021001', 2022, 1, 'MEC101', 8.0);
INSERT INTO historico (ra, ano, semestre, codigo_disciplina, nota_final) 
VALUES ('2021001', 2022, 2, 'MEC102', 7.5);

INSERT INTO tcc (grupo_id, ra1, ra2, ra3, orientador, ano, semestre)
VALUES ('TCC001', '2021001', '2021002', null, 'P001', 2023, 2);

INSERT INTO professor_disciplina (prontuario, codigo_disciplina) VALUES ('P001', 'MEC101');
INSERT INTO professor_disciplina (prontuario, codigo_disciplina) VALUES ('P001', 'MEC102');

INSERT INTO aluno_status_formatura (ra, formou) VALUES ('2021001', false);
INSERT INTO aluno_status_formatura (ra, formou) VALUES ('2021002', true);

INSERT INTO departamento_com_chefe (id, nome, chefe_prontuario, chefe_nome) VALUES ('DPT01', 'Engenharia', 'P001', 'Dr. Carlos Lima');
