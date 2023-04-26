import psycopg2

config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    user='postgres',
    password='1234'
)

current = config.cursor()
# добавляем значения в таблицу 
id = 89
name = 'Alikhan'
number = '87472401004'

sql = '''
    INSERT INTO nureke VALUES (%s, %s, %s); 
'''

current.execute(sql, (id, name, number))

current.close()
config.commit()
config.close()