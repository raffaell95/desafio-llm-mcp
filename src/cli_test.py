from infra.sqlalchemy.config.database import get_db, create_db
from sqlalchemy.orm import Session
from infra.sqlalchemy.repository.car_repository import CarRespository
import typer

app = typer.Typer()


@app.command()
def create_database():
    """Cria o banco de dados."""
    create_db()

@app.command()
def create_cars():
    """Cria carros de exemplo no banco de dados.
    """
    session: Session = next(get_db())
    CarRespository(session).create_car()
    typer.echo("Carros criados com sucesso!")

@app.command()
def get_cars():
    """Lista os carros no banco de dados.
    """
    session: Session = next(get_db())
    cars = CarRespository(session).get_cars()
    if not cars:
        typer.echo("Nenhum carro encontrado.")
    else:
        for car in cars:
            typer.echo(f"marca={car.marca} - modelo={car.modelo} - ano={car.ano} - cor:{car.cor} - quilometragem={car.quilometragem} - preco={car.preco}")


if __name__ == "__main__":
    app()