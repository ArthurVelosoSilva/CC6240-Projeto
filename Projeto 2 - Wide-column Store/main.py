from connect_astra import conectar_astra

def executar_arquivo_cql(session, caminho_arquivo):
    with open(caminho_arquivo, encoding="utf-8") as f:
        comandos = f.read().split(';')
        for comando in comandos:
            if comando.strip():
                session.execute(comando)

session = conectar_astra()

# Criação das tabelas
executar_arquivo_cql(session, "C:/Users/Windows 10/OneDrive/Área de Trabalho/Projeto 2 - Wide-column Store/cql_create_tables.cql")
# Inserção dos dados
executar_arquivo_cql(session, "C:/Users/Windows 10/OneDrive/Área de Trabalho/Projeto 2 - Wide-column Store/cql_insert_data.cql")

print("Tabelas criadas e dados inseridos com sucesso.\n")

# Histórico escolar do aluno
print("=== Histórico escolar do aluno 2021001 ===")
rows = session.execute("""
    SELECT codigo_disciplina, ano, semestre, nota_final 
    FROM historico 
    WHERE ra = '2021001'
""")
for row in rows:
    print(f"Disciplina: {row.codigo_disciplina}, Ano: {row.ano}, Semestre: {row.semestre}, Nota: {row.nota_final}")

# Disciplinas ministradas por professor
print("\n=== Disciplinas ministradas pelo professor P001 ===")
disciplinas = session.execute("SELECT codigo_disciplina FROM professor_disciplina WHERE prontuario = 'P001'")
for d in disciplinas:
    print(f"- {d.codigo_disciplina}")

# Status de formatura do aluno
print("\n=== Status de formatura do aluno 2021001 ===")
status = session.execute("SELECT formou FROM aluno_status_formatura WHERE ra = '2021001'").one()
if status:
    print(f"Formou? {'Sim' if status.formou else 'Não'}")
else:
    print("Aluno não encontrado")

# Professores chefes de departamento
print("\n=== Departamentos com chefe ===")
departamentos = session.execute("SELECT id, nome, chefe_prontuario, chefe_nome FROM departamento_com_chefe")
for dpt in departamentos:
    print(f"Departamento: {dpt.nome} (ID: {dpt.id}) - Chefe: {dpt.chefe_nome}")

# Alunos e orientador do TCC
print("\n=== Alunos e orientador do TCC ===")
tccs = session.execute("SELECT grupo_id, ra1, ra2, ra3, orientador FROM tcc")
for tcc in tccs:
    print(f"Grupo: {tcc.grupo_id}, Alunos: {tcc.ra1}, {tcc.ra2}, {tcc.ra3}, Orientador: {tcc.orientador}")
