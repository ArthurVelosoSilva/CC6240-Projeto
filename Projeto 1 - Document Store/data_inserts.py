from pymongo import MongoClient
from pymongo.server_api import ServerApi

# Conexão com o MongoDB
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

#Limpa o banco antes de inserir
colecao_alunos.delete_many({})
colecao_cursos.delete_many({})
colecao_departamentos.delete_many({})
colecao_gruposTCC.delete_many({})
colecao_disciplinas.delete_many({})
colecao_professores.delete_many({})

#Disciplinas
disciplinas = [
    {"_id": "BD", "nome": "Banco de Dados", "departamento": "D1"},
    {"_id": "POO", "nome": "Programação Orientada a Objetos", "departamento": "D1"},
    {"_id": "ED", "nome": "Estrutura de Dados", "departamento": "D1"},
    {"_id": "SO", "nome": "Sistemas Operacionais", "departamento": "D2"},
]
colecao_disciplinas.insert_many(disciplinas)

#Departamentos
departamentos = [
    {"_id": "D1", "nome": "Computação", "chefe": "P1"},
    {"_id": "D2", "nome": "Engenharia de Software", "chefe": "P2"},
]
colecao_departamentos.insert_many(departamentos)

#Professores
professores = [
    {
        "_id": "P1",
        "nome": "Carlos Silva",
        "departamento": "D1",
        "disciplinas_ministradas": [
            {"codigo": "BD", "ano": 2025, "semestre": 1},
            {"codigo": "POO", "ano": 2025, "semestre": 2}
        ]
    },
    {
        "_id": "P2",
        "nome": "Maria Souza",
        "departamento": "D2",
        "disciplinas_ministradas": [
            {"codigo": "SO", "ano": 2025, "semestre": 2}
        ]
    }
]
colecao_professores.insert_many(professores)

#Curso com matriz curricular
cursos = [
    {
        "_id": "C1",
        "nome": "Ciência da Computação",
        "matriz_curricular": ["BD", "POO", "ED", "SO"]
    }
]
colecao_cursos.insert_many(cursos)

#Alunos
alunos = [
    {
        "_id": "A1",
        "nome": "João Pereira",
        "curso": "C1",
        "disciplinas_cursadas": [
            {"codigo": "BD", "ano": 2025, "semestre": 1, "nota": 8.5},
            {"codigo": "POO", "ano": 2025, "semestre": 2, "nota": 7.0},
            {"codigo": "ED", "ano": 2025, "semestre": 1, "nota": 6.0},
            {"codigo": "SO", "ano": 2025, "semestre": 1, "nota": 9.0}
        ],
        "tcc": {"grupo_id": "G1", "orientador": "P1"}
    },
    {
        "_id": "A2",
        "nome": "Fernanda Lima",
        "curso": "C1",
        "disciplinas_cursadas": [
            {"codigo": "BD", "ano": 2025, "semestre": 1, "nota": 9.0},
            {"codigo": "POO", "ano": 2025, "semestre": 2, "nota": 8.5},
            {"codigo": "ED", "ano": 2025, "semestre": 1, "nota": 7.5},
            {"codigo": "SO", "ano": 2025, "semestre": 1, "nota": 6.5}
        ],
        "tcc": {"grupo_id": "G1", "orientador": "P1"}
    }
]
colecao_alunos.insert_many(alunos)

#Grupo TCC
grupos_tcc = [
    {
        "_id": "G1",
        "ano": 2025,
        "semestre": 1,
        "alunos": ["A1", "A2"],
        "orientador": "P1"
    }
]
colecao_gruposTCC.insert_many(grupos_tcc)

print("Dados inseridos com sucesso.")
