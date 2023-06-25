-- Criação da tabela tb_parceiros
CREATE TABLE tb_parceiros (
    id SERIAL PRIMARY KEY,
    nome_parceiro VARCHAR(100),
    endereco_parceiro VARCHAR(255),
    cnpj_parceiro VARCHAR(100),
    uf_cobertura VARCHAR(100)
);

-- Criação da tabela tb_viabilidade
CREATE TABLE tb_viabilidade (
    id SERIAL PRIMARY KEY,
    logradouro VARCHAR(100),
    numero VARCHAR(100),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    uf VARCHAR(100),
    produto VARCHAR(100),
    velocidade VARCHAR(100)
);

-- Criação da tabela tb_resultado_viabilidade
CREATE TABLE tb_resultado_viabilidade (
    id SERIAL PRIMARY KEY,
    id_parceiro_resposta INTEGER,
    id_viabilidade INTEGER,
    resultado_parceiro VARCHAR(100),
    FOREIGN KEY (id_parceiro_resposta) REFERENCES tb_parceiros (id),
    FOREIGN KEY (id_viabilidade) REFERENCES tb_viabilidade (id)
);

-- Inserção dos dados na tabela tb_parceiros
INSERT INTO tb_parceiros (nome_parceiro, endereco_parceiro, cnpj_parceiro, uf_cobertura)
VALUES
    ('13Telecom', 'Rua Abilio Soares, 15, Paraiso', '888888888/0001-23', 'SP; RJ;MG'),
    ('14Telecom', 'R. João Pessoa - Jacutinga', '888888888/0001-24', 'SP'),
    ('15Telecom', 'Rua 10 - SHVP Colônia Agrícola Vicente Pires Chácara 147 - Setor Habitacional Vicente Pires - Taguatinga Brasília - DF', '888888888/0001-25', 'DF;RJ'),
    ('16Telecom', 'Rua 10 - Setor Habitacional Vicente Pires - Taguatinga -  Brasília - DF', '888888888/0001-26', 'RJ;SP;MG'),
    ('17Telecom', 'Avenida Jacutinga - Indianópolis - São Paulo - SP', '888888888/0001-27', 'SP; RJ;PA'),
    ('18Telecom', 'R. São Joaquim, 44 - Centro, Diadema - SP, 09911-020, Brasil', '888888888/0001-28', 'SP;RJ;GO'),
    ('19Telecom', 'Cachoeira do Arari - PA, 68840-000, Brasil', '888888888/0001-29', 'PA;SP'),
    ('20Telecom', 'Via L2 Sul - Asa Sul, Brasília - DF, 70297-400, Brasil - Asa Sul, Brasília - DF, 70200-010, Brasil', '888888888/0001-30', 'DF;SP;GO'),
    ('21Telecom', 'Av. Argélia, 173 - Miragaia, Ubá - MG, 36500-000, Brasil', '888888888/0001-31', 'MG;MS'),
    ('22Telecom', 'QN 211 Cj. 1, 42 - Samambaia Norte, Brasília - DF, 72343-052, Brasil', '888888888/0001-32', 'DF; MG;SP;MS'),
    ('23Telecom', 'Av. Me. Tereza de Calcutá, 27 - Parque Industrial Joao Bras, Goiânia - GO, 74492-000, Brasil', '888888888/0001-33', 'GO;DF');

-- Inserção dos dados na tabela tb_viabilidade
INSERT INTO tb_viabilidade (logradouro, numero, bairro, cidade, uf, produto, velocidade)
VALUES
    ('Rod. Mario Batista Mori', '33', 'Res. Ecopark', 'São Paulo', 'SP', 'Ip Connect', '10MBPS'),
    ('Av. Paulista', '1146', 'Bela Vista', 'São Paulo', 'SP', 'VPN VIP', '10MBPS'),
    ('R. Francisco Bernardes de Assis', '210', 'Jardin Brasilia', 'Uberlandia', 'MG', 'VPN VIP', '1MBPS'),
    ('R. Dr. Tancredo de Almeida Neves', '33', 'Glória de Dourados', 'Mato Grosso do Sul', 'SP', 'Ip Connect', '100MBPS'),
    ('Rua do Lavradio', '71', 'Centro', 'Rio de Janeiro', 'RJ', 'DIGITRONCO', '30 Canais'),
    ('Rua Arq. Olavo Redig de campos', '105', 'Morumbi', 'São Paulo', 'SP', 'Ip Connect', '1GBPS'),
    ('R. Francisco Bezerra', '10', 'Mambuca', 'Angra dos Reis', 'RJ', 'DIGITRONCO', '10 Canais'),
    ('Avenida Sto Amaro', '94', 'Santo Amaro', 'São Paulo', 'SP', 'Ip Connect', '50MBPS'),
    ('Rua Itabapoana', '1000', 'Vila Isa', 'São Paulo', 'SP', 'Ip Connect', '500MBPS'),
    ('Praça Milton Campos', '100', 'Serra', 'Belo Horizonte', 'MG', 'Ip Connect', '200MBPS');

-- Inserção dos dados na tabela tb_resultado_viabilidade
INSERT INTO tb_resultado_viabilidade (id_viabilidade, id_parceiro_resposta, resultado_parceiro)
VALUES
    (7, 4, 'Viavel'),
    (7, 5, 'Projeto Especial'),
    (7, 1, 'Inviável'),
    (7, 6, 'Inviável'),
    (1, 1, 'Inviável'),
    (1, 2, 'Inviável'),
    (1, 5, 'Viavel'),
    (1, 6, 'Viavel'),
    (1, 7, 'Viavel'),
    (1, 8, 'Viavel'),
    (1, 10, 'Viavel'),
    (3, 1, 'Viavel'),
    (3, 9, 'Viavel'),
    (3, 4, 'Viavel'),
    (3, 10, 'Viavel'),
    (10, 1, 'Projeto Especial'),
    (10, 4, 'Inviável'),
    (10, 9, 'Viavel'),
    (10, 10, 'Projeto Especial'),
    (8, 1, 'Projeto Especial'),
    (8, 2, 'Projeto Especial'),
    (8, 5, 'Inviável'),
    (8, 6, 'Viavel'),
    (8, 7, 'Inviável'),
    (8, 8, 'Viavel'),
    (8, 10, 'Inviável'),
    (5, 1, 'Projeto Especial'),
    (5, 3, 'Projeto Especial'),
    (5, 4, 'Viavel'),
    (5, 5, 'Viavel'),
    (5, 6, 'Viavel');

