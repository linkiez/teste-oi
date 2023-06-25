import asyncpg

async def database_query(query: str):
    conn = await asyncpg.connect(
        user="postgres",
        password="fabio123",
        host="localhost",
        port="5432",
        database="teste_oi"
    )
    
    result = await conn.fetch(query)
    
    await conn.close()
    
    return result
