# Arquivo para verficar as tabelas do banco de dados e os dados contidos nelas.

import sqlite3
import pandas as pd

conn = sqlite3.connect("analise_impostos.db")
df = pd.read_sql("SELECT * FROM receitas LIMIT 50", conn)