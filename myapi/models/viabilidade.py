from pydantic import BaseModel

class Viabilidade(BaseModel):
    id: int
    logradouro: str
    numero: str
    bairro: str
    cidade: str
    uf: str
    produto: str
    velocidade: str
