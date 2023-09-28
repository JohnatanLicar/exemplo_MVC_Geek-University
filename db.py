import sqlite3

def _execute(query):
    db_path = './geek.university'
    connection = sqlite3.connect(db_path)
    cursos = connection.cursor()
    result = None

    try:
        cursos.execute(query)
        result = cursos.fetchall() #lista de tupas
        connection.commit()
    except Exception as err:
        print(f'Erro na execução da query: {err}')
    
    connection.close()
    return result

