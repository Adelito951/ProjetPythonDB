from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["jeu_video"]

db.characters.delete_many({})
db.monsters.delete_many({})
db.scores.delete_many({})

characters = [
    {"name": "Guerrier", "atk": 15, "def": 10, "hp": 100},
    {"name": "Mage", "atk": 20, "def": 5, "hp": 80},
    {"name": "Archer", "atk": 18, "def": 7, "hp": 90},
    {"name": "Voleur", "atk": 22, "def": 8, "hp": 85},
    {"name": "Paladin", "atk": 14, "def": 12, "hp": 110},
    {"name": "Sorcier", "atk": 25, "def": 3, "hp": 70},
    {"name": "Chevalier", "atk": 17, "def": 15, "hp": 120},
    {"name": "Moine", "atk": 19, "def": 9, "hp": 95},
    {"name": "Berserker", "atk": 23, "def": 6, "hp": 105},
    {"name": "Chasseur", "atk": 16, "def": 11, "hp": 100},
]

monsters = [
    {"name": "Gobelin", "atk": 10, "def": 5, "hp": 50},
    {"name": "Orc", "atk": 20, "def": 8, "hp": 120},
    {"name": "Dragon", "atk": 35, "def": 20, "hp": 300},
    {"name": "Zombie", "atk": 12, "def": 6, "hp": 70},
]

db.characters.insert_many(characters)
db.monsters.insert_many(monsters)

print("Base de données initialisée")