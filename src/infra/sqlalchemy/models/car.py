from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from infra.sqlalchemy.config.database import Base

class Car(Base):
    __tablename__ = 'carros'

    id = Column(Integer, primary_key=True, index=True)
    marca = Column(String)
    modelo = Column(String)
    ano = Column(Float)
    motorizacao = Column(String)
    tipo_combustivel = Column(String)
    cor = Column(String)
    quilometragem = Column(String)
    numero_portas = Column(Integer)
    transmissao = Column(String)
    preco = Column(Float)

    def __repr__(self):
        return (f"<marca={self.marca}, modelo={self.modelo}, ano={self.ano}, "
                f"cor={self.cor}, quilometragem={self.quilometragem} preco={self.preco})>")