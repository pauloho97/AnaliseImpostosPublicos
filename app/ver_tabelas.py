import sqlite3
import pandas as pd

conn = sqlite3.connect("analise_impostos.db")
df = pd.read_sql("SELECT * FROM receitas LIMIT 50", conn)