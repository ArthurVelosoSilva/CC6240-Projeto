from pymongo import MongoClient
from pymongo.server_api import ServerApi
import queries as q

#Conexão
db_senha = "dbUserPassword"
uri = f"mongodb+srv://dbUser:{db_senha}@cluster0.dal1o62.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['Faculdade']

#Coleções
colecao_alunos = db['Alunos']
colecao_cursos = db['Cursos']
colecao_departamentos = db['Departamentos']
colecao_gruposTCC = db['GruposTCC']
colecao_disciplinas = db['Disciplinas']
colecao_professores = db['Professores']

#Consultas
print("\nHistórico escolar de A1:")
historico = q.historico_escolar(colecao_alunos, colecao_disciplinas, "A1")
print(f"Aluno: {historico['aluno']}")
for d in historico["historico"]:
    print(d)

print("\nDisciplinas ministradas por P1:")
print(q.historico_disciplinas_ministradas(colecao_professores, "P1"))

print("\nAlunos formados em 2024/1:")
print(q.alunos_formados(colecao_alunos, colecao_cursos, 2024, 1))

print("\nProfessores chefes de departamento:")
print(q.professores_chefes(colecao_professores, colecao_departamentos))

print("\nGrupos de TCC:")
print(q.grupos_tcc(colecao_gruposTCC, colecao_alunos, colecao_professores))

client.close()
