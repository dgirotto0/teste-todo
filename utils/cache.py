from pymongo import MongoClient
import os

# Conectando ao MongoDB
client = MongoClient(os.getenv('MONGODB_URI'), tls=True, tlsAllowInvalidCertificates=True)
db = client['todo_db']  # Nome do banco de dados
cache_collection = db['cache']  # Coleção específica para o cache

# Função para obter um valor do cache
def get_cache(key):
    result = cache_collection.find_one({'_id': key})
    if result:
        return result['value']
    return None

# Função para definir um valor no cache
def set_cache(key, value):
    cache_collection.update_one({'_id': key}, {'$set': {'value': value}}, upsert=True)

# Função para excluir um valor do cache
def delete_cache(key):
    cache_collection.delete_one({'_id': key})
