from pydantic import BaseModel

class Parceiros(BaseModel):
    id: int
    nome_parceiro: str
    endereco_parceiro: str
    cnpj_parceiro: str
    uf_cobertura: str

