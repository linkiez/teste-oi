from fastapi import APIRouter, Request
from config.database import database_query
from typing import List

import sys
sys.path.append("..")
from models.parceiros import Parceiros
from models.viabilidade import Viabilidade

router = APIRouter()

@router.get("/parceiro")
async def get_parceiros():
    try:
        parceiros: List[Parceiros] = await database_query("SELECT * FROM tb_parceiros")
        return parceiros
    except Exception as e:
        return {"error": str(e)}

@router.get("/parceiro/{parceiro_id}")
async def get_parceiro(parceiro_id: int):
    try:
        parceiros: Parceiros = await database_query("SELECT * FROM tb_parceiros WHERE id = " + str(parceiro_id))
        return parceiros[0]
    except Exception as e:
        return {"error": str(e)}

@router.post("/parceiro")
async def create_parceiro(request: Request):
    request_body = await request.json()
    try:
        parceiro = await database_query("INSERT INTO tb_parceiros (nome_parceiro, endereco_parceiro, cnpj_parceiro, uf_cobertura) VALUES ('" + request_body["nome_parceiro"] + "', '" + request_body["endereco_parceiro"] + "', '" + request_body["cnpj_parceiro"] + "', '" + request_body["uf_cobertura"] + "') RETURNING id")
        return parceiro[0]
    except Exception as e:
        return {"error": str(e)}

@router.put("/parceiro/{parceiro_id}")
async def update_parceiro(parceiro_id: int, request: Request):
    request_body = await request.json()
    try:
        await database_query("UPDATE tb_parceiros SET nome_parceiro = '" + request_body["nome_parceiro"] + "', endereco_parceiro = '" + request_body["endereco_parceiro"] + "', cnpj_parceiro = '" + request_body["cnpj_parceiro"] + "', uf_cobertura = '" + request_body["uf_cobertura"] + "' WHERE id = " + str(parceiro_id))
        return {"status": "success"}
    except Exception as e:
        return {"error": str(e)}

@router.delete("/parceiro/{parceiro_id}")
async def delete_parceiro(parceiro_id: int):
    try:
        await database_query("DELETE FROM tb_parceiros WHERE id = " + str(parceiro_id))
        return {"status": "success"}
    except Exception as e:
        return {"error": str(e)}
    
@router.get("/viabilidade")
async def get_viabilidades():
    try:
        viabilidades: List[Viabilidade] = await database_query("SELECT * FROM tb_viabilidade")
        return viabilidades
    except Exception as e:
        return {"error": str(e)}

@router.get("/viabilidade/{viabilidade_id}")
async def get_viabilidade(viabilidade_id: int):
    try:
        viabilidades: Viabilidade = await database_query("SELECT * FROM tb_viabilidade WHERE id = " + str(viabilidade_id))
        return viabilidades[0]
    except Exception as e:
        return {"error": str(e)}
    
@router.post("/viabilidade")
async def create_viabilidade(request: Request):
    request_body = await request.json()
    try:
        viabilidade = await database_query("INSERT INTO tb_viabilidade (logradouro, numero, bairro, cidade, uf, produto, velocidade) VALUES ('" + request_body["logradouro"] + "', '" + request_body["numero"] + "', '" + request_body["bairro"] + "', '" + request_body["cidade"] + "', '" + request_body["uf"] + "', '" + request_body["produto"] + "', '" + request_body["velocidade"] + "') RETURNING id")
        return viabilidade[0]
    except Exception as e:
        return {"error": str(e)}
    
@router.put("/viabilidade/{viabilidade_id}")
async def update_viabilidade(viabilidade_id: int, request: Request):
    request_body = await request.json()
    try:
        await database_query("UPDATE tb_viabilidade SET logradouro = '" + request_body["logradouro"] + "', numero = '" + request_body["numero"] + "', bairro = '" + request_body["bairro"] + "', cidade = '" + request_body["cidade"] + "', uf = '" + request_body["uf"] + "', produto = '" + request_body["produto"] + "', velocidade = '" + request_body["velocidade"] + "' WHERE id = " + str(viabilidade_id))
        return {"status": "success"}
    except Exception as e:
        return {"error": str(e)}
    
@router.delete("/viabilidade/{viabilidade_id}")
async def delete_viabilidade(viabilidade_id: int):
    try:
        await database_query("DELETE FROM tb_viabilidade WHERE id = " + str(viabilidade_id))
        return {"status": "success"}
    except Exception as e:
        return {"error": str(e)}
    
@router.get("/viabilidade/parceiro/")
async def get_viabilidades_parceiro():
    try:
        resultado = await database_query("SELECT * FROM tb_resultado_viabilidade INNER JOIN tb_viabilidade ON tb_resultado_viabilidade.id_viabilidade = tb_viabilidade.id INNER JOIN tb_parceiros ON tb_resultado_viabilidade.id_parceiro_resposta = tb_parceiros.id;")
        return resultado
    except Exception as e:
        return {"error": str(e)}
    

