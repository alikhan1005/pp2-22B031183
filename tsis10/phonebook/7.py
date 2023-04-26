import psycopg2

config = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    password = '1234',
    user = 'postgres'
)
sql = '''
        DELETE FROM phonebook_ WHERE name = %s RETURNING *
    '''
# удаление данных по имени или по номеру
current = config.cursor()
del_data = input("By what do you want to delete? (name or number): ")
del_data = del_data.lower()
temp = input(f'Which {del_data} do you want to delete?: ')
if del_data == 'name':
    sql = '''
        DELETE FROM phonebook_ WHERE name = %s RETURNING *
    '''
elif del_data == 'number':
    sql = '''
        DELETE FROM phonebook_ WHERE number = %s RETURNING *
    '''
current.execute(sql, (temp,))
config.commit()
current.close()
config.close()