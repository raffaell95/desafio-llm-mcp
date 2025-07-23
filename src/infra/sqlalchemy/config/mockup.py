from faker import Faker
from random import choice, uniform, randint
from infra.sqlalchemy.models import car as models

fake = Faker()

# Opções para alguns campos
fuels = ['Gasolina', 'Diesel', 'Flex', 'Elétrico', 'Híbrido']
engines = ['1.0', '1.4', '1.6', '2.0', '2.4', '3.0', 'V6', 'V8']
transmissions = ['Manual', 'Automática', 'CVT']

def create_fake_car():
    return models.Car(
        marca=fake.company(),
        modelo=fake.word().capitalize(),
        ano=randint(1990, 2025),
        motorizacao=choice(engines),
        tipo_combustivel=choice(fuels),
        cor=fake.color_name(),
        quilometragem=round(uniform(0, 300000), 2),
        numero_portas=choice([2, 3, 4, 5]),
        transmissao=choice(transmissions),
        preco=round(uniform(10000, 150000), 2)
    )