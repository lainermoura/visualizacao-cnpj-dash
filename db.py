import sqlite3
import pandas as pd
import random

# Lista de bairros de Niterói
bairros_niteroi = [
    "Bairro de Fátima", "Boa Viagem", "Cachoeiras", "Centro", "Charitas", 
    "Gragoatá", "Icaraí", "Ingá", "Jurujuba", "Morro do Estado", 
    "Pé Pequeno", "Ponta d'Areia", "Santa Rosa", "São Domingos", 
    "São Francisco", "Viradouro", "Vital Brazil", "Baldeador", 
    "Barreto", "Caramujo", "Cubango", "Engenhoca", "Fonseca", 
    "Ilha da Conceição", "Santa Bárbara", "Santana", "São Lourenço", 
    "Tenente Jardim", "Viçoso Jardim", "Cafubá", "Camboinhas", 
    "Engenho do Mato", "Itacoatiara", "Itaipu", "Jacaré", "Jardim Imbuí", 
    "Maravista", "Piratininga", "Santo Antônio", "Serra Grande", 
    "Badu", "Cantagalo", "Ititioca", "Largo da Batalha", "Maceió", 
    "Maria Paula", "Matapaca", "Sapê", "Vila Progresso", 
    "Muriqui", "Rio do Ouro", "Várzea das Moças"
]

# Criar um banco de dados SQLite e uma tabela
conn = sqlite3.connect('empresas_niteroi.db')
cursor = conn.cursor()

# Criar a tabela para empresas
cursor.execute('''
CREATE TABLE IF NOT EXISTS empresas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cnpj TEXT,
    bairro TEXT,
    atividade TEXT
)
''')

# Inserir dados aleatórios no banco de dados
for _ in range(100):
    cnpj = f"{random.randint(10000078000100, 99999978000199)}"
    bairro = random.choice(bairros_niteroi)
    atividade = random.choice(['Comércio', 'Indústria', 'Serviços', 'Tecnologia'])
    
    cursor.execute('''
    INSERT INTO empresas (cnpj, bairro, atividade) VALUES (?, ?, ?)
    ''', (cnpj, bairro, atividade))

# Salvar (commit) as mudanças e fechar a conexão
conn.commit()
conn.close()
