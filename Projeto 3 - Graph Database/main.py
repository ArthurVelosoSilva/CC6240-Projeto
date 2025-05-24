from neo4j import GraphDatabase

NEO4J_URI = "neo4j+s://326fa464.databases.neo4j.io"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "xfOh8ZqgEf1sSSTTGduB9QNjK9cE8yXNfWysMH5dFRk"

def executar_arquivo_cypher(session, caminho_arquivo):
    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        comandos = f.read().strip().split(";")
    for comando in comandos:
        comando = comando.strip()
        if comando:
            session.run(comando)

def executar_consultas(session, arquivo_cypher):
    with open(arquivo_cypher, "r", encoding="utf-8") as f:
        consultas = f.read().split("// ---")

    topicos = [
        "1. Histórico escolar de um aluno",
        "2. Disciplinas ministradas por um professor",
        "3. Alunos formados em determinado semestre/ano",
        "4. Chefes de departamento",
        "5. Grupos de TCC com alunos e orientador"
    ]

    parametros = {
        "matriculaAluno": "2023001",
        "nomeProfessor": "Joao",
        "semestre": 1,
        "ano": 2025
    }

    for i, consulta in enumerate(consultas):
        consulta = consulta.strip()
        if not consulta:
            continue
        print("=" * 60)
        print(f"{topicos[i]}")
        print("=" * 60)
        resultado = session.run(consulta, parametros)
        registros = [dict(record) for record in resultado]
        if registros:
            vistos = set()
            unicos = []
            for r in registros:
                chave = tuple(sorted(r.items()))
                if chave not in vistos:
                    vistos.add(chave)
                    unicos.append(r)
            for registro in unicos:
                print(registro)
        else:
            print("Nenhum resultado encontrado.")
        print("\n")

driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
with driver.session() as session:
    executar_arquivo_cypher(session, "criar_nos.cypher")
    executar_arquivo_cypher(session, "criar_relacionamentos.cypher")
    executar_consultas(session, "consultas_grafo.cypher")
