import csv, psycopg2

config = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    password = '1234',
    user = 'postgres'
)
current = config.cursor()
arr = []
# вставляем данные в телефонную книгу загружая их из csv-файла
with open('номер.csv') as f:
    reader = csv.reader(f, delimiter=',')

    for row in reader:
        row[0] = int(row[0])
        arr.append(row)

sql = '''
    INSERT INTO phonebook_ VALUES (%s, %s, %s) RETURNING *; 
'''

for row in arr:
    current.execute(sql, row)

final = current.fetchall()
print(final)

current.close()
config.commit()
config.close()