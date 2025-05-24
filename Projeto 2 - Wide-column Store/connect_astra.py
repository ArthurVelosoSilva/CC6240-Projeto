from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

def conectar_astra():
    SECURE_CONNECT_BUNDLE = "C:/Users/Windows 10/Downloads/secure-connect-faculdade.zip"
    
    cloud_config = {
        'secure_connect_bundle': SECURE_CONNECT_BUNDLE
    }
    
    auth_provider = PlainTextAuthProvider(
        'TUbfzNXAXatHPaqbhZHFfZUs', 
        '.9kGzChAoYSFw9M93BqZH+68J-6yJ_5l5FCdiyWTgANf+zq8DY.gTLhXRHrYxMmuOHULEBvpqLW3T+8zpGUjEvcPKQqa_Jq9vbrizrJlBZ,tXdLZTDDi-j0X7F7PPBpw'
    )
    
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
    session = cluster.connect()
    session.set_keyspace('123')
    return session
