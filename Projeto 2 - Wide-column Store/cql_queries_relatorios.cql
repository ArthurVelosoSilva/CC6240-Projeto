-- Histórico escolar de um aluno
SELECT codigo_disciplina, ano, semestre, nota_final 
FROM historico 
WHERE ra = '2021001';

-- Disciplinas ministradas por um professor
SELECT codigo_disciplina FROM professor_disciplina WHERE prontuario = 'P001';

-- Verificar se aluno formou
SELECT formou FROM aluno_status_formatura WHERE ra = '2021001';

-- Professores chefes de departamento (usando tabela duplicada)
SELECT id, nome, chefe_prontuario, chefe_nome FROM departamento_com_chefe;

-- Alunos e orientador do TCC
SELECT grupo_id, ra1, ra2, ra3, orientador 
FROM tcc;
