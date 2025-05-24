def historico_escolar(colecao_alunos, colecao_disciplinas, aluno_id):
    aluno = colecao_alunos.find_one({"_id": aluno_id})
    if aluno:
        disciplinas = []
        for cursada in aluno.get("disciplinas_cursadas", []):
            nome_disc = colecao_disciplinas.find_one({"_id": cursada["codigo"]})["nome"]
            disciplinas.append({
                "codigo": cursada["codigo"],
                "nome": nome_disc,
                "ano": cursada["ano"],
                "semestre": cursada["semestre"],
                "nota": cursada["nota"]
            })
        return {
            "aluno": aluno["nome"],
            "historico": disciplinas
        }
    return {}

def historico_disciplinas_ministradas(colecao_professores, professor_id):
    prof = colecao_professores.find_one({"_id": professor_id})
    return {
        "professor": prof["nome"],
        "disciplinas_ministradas": prof["disciplinas_ministradas"]
    } if prof else {}

def alunos_formados(colecao_alunos, colecao_cursos, ano, semestre):
    formados = []
    for aluno in colecao_alunos.find():
        curso = colecao_cursos.find_one({"_id": aluno["curso"]})
        matriz = set(curso.get("matriz_curricular", []))
        disciplinas_cursadas = set()
        for d in aluno.get("disciplinas_cursadas", []):
            if d["nota"] >= 6.0 and (d["ano"] < ano or (d["ano"] == ano and d["semestre"] <= semestre)):
                disciplinas_cursadas.add(d["codigo"])
        if matriz.issubset(disciplinas_cursadas):
            formados.append(aluno["nome"])
    return formados

def professores_chefes(colecao_professores, colecao_departamentos):
    resultado = []
    for dept in colecao_departamentos.find():
        chefe = colecao_professores.find_one({"_id": dept["chefe"]})
        if chefe:
            resultado.append({
                "professor": chefe["nome"],
                "departamento": dept["nome"]
            })
    return resultado

def grupos_tcc(colecao_gruposTCC, colecao_alunos, colecao_professores):
    resultado = []
    for grupo in colecao_gruposTCC.find():
        alunos = [colecao_alunos.find_one({"_id": a})["nome"] for a in grupo["alunos"]]
        orientador = colecao_professores.find_one({"_id": grupo["orientador"]})["nome"]
        resultado.append({
            "grupo_id": grupo["_id"],
            "ano": grupo["ano"],
            "semestre": grupo["semestre"],
            "alunos": alunos,
            "orientador": orientador
        })
    return resultado
