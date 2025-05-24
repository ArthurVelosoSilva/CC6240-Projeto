driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
with driver.session() as session:
    print("Criando nós...")
    executar_arquivo_cypher(session, "criar_nos.cypher")
    print("Criando relacionamentos...")
    executar_arquivo_cypher(session, "criar_relacionamentos.cypher")
    print("Executando consultas...")
    executar_consultas(session, "consultas_grafo.cypher")