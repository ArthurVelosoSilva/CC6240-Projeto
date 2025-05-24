// 1. Histórico escolar de um aluno
MATCH (a:Aluno {matricula: $matriculaAluno})-[r:CURSOU]->(d:Disciplina)
RETURN d.codigo AS codigoDisciplina,
       d.nome AS nomeDisciplina,
       r.semestre AS semestre,
       r.ano AS ano,
       r.notaFinal AS notaFinal
ORDER BY r.ano, r.semestre, d.codigo
// ---
// 2. Histórico de disciplinas ministradas por professor
MATCH (p:Professor {nome: $nomeProfessor})-[r:MINISTRA]->(d:Disciplina)
RETURN d.codigo AS codigoDisciplina,
       d.nome AS nomeDisciplina,
       r.semestre AS semestre,
       r.ano AS ano
ORDER BY r.ano, r.semestre, d.codigo
// ---
// 3. Listar alunos formados em um semestre/ano
MATCH (a:Aluno)
WHERE NOT EXISTS {
    MATCH (c:Curso)-[:INCLUI]->(d:Disciplina)
    WHERE NOT EXISTS {
        MATCH (a)-[r:CURSOU]->(d)
        WHERE r.notaFinal >= 6.0
    }
}
WITH a
MATCH (a)-[r:CURSOU]->(d:Disciplina)
WHERE r.semestre = $semestre AND r.ano = $ano
RETURN DISTINCT a.matricula AS matriculaAluno, a.nome AS nomeAluno
// ---
// 4. Listar professores chefes de departamento com nome do departamento
MATCH (p:Professor)-[:CHEFE_DE]->(d:Departamento)
RETURN p.nome AS nomeProfessor, d.nome AS nomeDepartamento
// ---
// 5. Saber alunos de um grupo TCC e orientador
MATCH (tcc:GrupoTCC)<-[:PERTENCE_A]-(a:Aluno), (tcc)<-[:ORIENTA]-(prof:Professor)
RETURN tcc.id AS idGrupoTCC,
       collect(a.nome) AS nomesAlunos,
       prof.nome AS nomeOrientador
