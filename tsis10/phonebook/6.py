import psycopg2

config = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    password = '1234',
    user = 'postgres'
)

current = config.cursor()
sql = ''''''
print("1 - данные по отсортированному имени")
print("2 - номер определенного человека")
s = int(input())
if s == 1:
    # запрос id, name, number по отсортированному имени 
    sql = '''
        SELECT id, name, number FROM qwer ORDER BY name ASC
    '''
elif s == 2:
    name = input()
    # запрос номера телефона определенного человека 
    sql = "SELECT * FROM qwer WHERE name = '{}'".format(name)
        
current.execute(sql)

final = current.fetchall()
print(*final, sep='\n')
current.close()
config.commit()
config.close()