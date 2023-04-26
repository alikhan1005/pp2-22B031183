import psycopg2

config = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    password = '1234',
    user = 'postgres'
)
current = config.cursor()
sql = '''
        DELETE FROM uuu WHERE username = %s RETURNING *
    '''
# удаление данных по имени

temp = 'sekas'

current.execute(sql, (temp,))
config.commit()
current.close()
config.close()