
import os
import ast
import pandas as pd

def load_text_as_tuples(path: str):
    tuples = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip().rstrip(',')  # quitamos el salto de línea y la coma final
            if line:  # si la línea no está vacía
                parsed = ast.literal_eval(line)
                tuples.append(parsed)
    return tuples


def verifica_tabla(table_name: str, connection):
    """
    Funcion que devuelve los datos de una tabla en una base de datos limitada por 5 registros
    """

    df = pd.read_sql_query(f'''SELECT * FROM {table_name} LIMIT 5''', connection)
    return df