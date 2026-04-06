CREATE TABLE receitas (
    id_receita INTEGER PRIMARY KEY AUTOINCREMENT,
    Ano INTEGER NOT NULL,
    Setor TEXT NOT NULL,
    Orgao_Superior TEXT,
    Orgao TEXT,
    Unidade_Gestora TEXT,
    Categoria TEXT,
    Origem TEXT,
    Especie TEXT,
    Detalhamento TEXT,
    Orcamento_Atualizado REAL,
    Receita_Realizada REAL,
    Percentual_Previsto_Realizado REAL,
    Valor_Lancado REAL
);

CREATE TABLE despesas (
    id_despesa INTEGER PRIMARY KEY AUTOINCREMENT,
    MesAno DATE NOT NULL,
    Ano INTEGER NOT NULL,
    Setor TEXT NOT NULL,
    Area_Atuacao TEXT,
    Subfuncao TEXT,
    Orgao_Superior TEXT,
    Valor_Empenhado REAL,
    Valor_Liquidado REAL,
    Valor_Pago REAL,
    Valor_Restos_Pagar REAL
);
