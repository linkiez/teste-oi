from pydantic import BaseModel

class ResultadoViabilidade(BaseModel):
    id: int
    id_parceiro_resposta: int
    id_viabilidade: int
    resultado_parceiro: str
