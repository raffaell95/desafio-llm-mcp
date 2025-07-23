from mcp.server.fastmcp import FastMCP, Context
from sqlalchemy.orm import Session
from infra.sqlalchemy.repository.car_repository import CarRespository
from infra.sqlalchemy.config.database import get_db

mcp = FastMCP("mcp-automoveis")

@mcp.tool()
async def list_cars(context: Context):
    """
    Lista todos os carros cadastrados no sistema.
    Esta função recupera e exibe todos os carros do banco de dados,
    mostrando marca, modelo, ano, quilometragem e preco.
    Retorna:
        str: Lista formatada de todos os carros  ou mensagem informando que não há carros
    Exemplo:
        get_cars()
    """
    session: Session = next(get_db())

    cars = CarRespository(session).listar()

    if not cars:
        result = "Nenhum carro encontrado."
        await context.info(result)
        return result

    car_list = []

    for car in cars:
        car_info = f"ID: {car.id}, Marca: {car.marca}, Modelo: {car.modelo}, Preço: {car.preco}"
        car_list.append(car_info)
        await context.debug(f"Carro encontrados")
    result = "\n".join(car_list)
    await context.info(f"Total de {len(car_list)} carros encontrados")
    return result

if __name__ == "__main__":
    mcp.run()