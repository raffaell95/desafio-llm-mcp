from sqlalchemy.orm import Session
from infra.sqlalchemy.config.mockup import create_fake_car
from infra.sqlalchemy.models import car as models


class CarRespository():

    def __init__(self, db: Session) -> None:
        self.db = db


    def get_cars(self):
        cars = self.db.query(models.Car).all()
        return cars
    

    def create_car(self):

        for _ in range(100):
            car = create_fake_car()
            self.db.add(car)

            self.db.commit()
            self.db.close()
            print("100 carros fake inseridos com sucesso!")


