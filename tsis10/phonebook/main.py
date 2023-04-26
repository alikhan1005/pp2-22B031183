import csv
import psycopg2
global config
config = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    password = '1234',
    user = 'postgres'
)
#     pgAdmin4  ------>    select * from qwer
def from_csv():
    current = config.cursor()
    arr = []
# вставляем данные в телефонную книгу загружая их из csv-файла
    with open('номер.csv') as f:
        reader = csv.reader(f, delimiter=',')

        for row in reader:
            row[0] = int(row[0])
            arr.append(row)

    sql = '''
        INSERT INTO qwer VALUES (%s, %s, %s) RETURNING *; 
    '''

    for row in arr:
        current.execute(sql, row)

    # final = current.fetchall()
    # print(final)

    current.close()
    config.commit()



def input_data():
    current = config.cursor()

    sql = '''
    INSERT INTO qwer
    VALUES (%s, %s, %s);
    '''
# вставляем данные в телефонную книгу вводя их с консоли
    print("ID:")
    id = int(input())
    print("Name:")
    username = input()
    print("Phone number:")
    number = input()
    current.execute(sql, (id, username, number))

    current.close()
    config.commit()


def update_data():
    current = config.cursor()
# обновление данных в таблице 
    sql = '''
            UPDATE qwer SET name = %s WHERE id = %s;
        '''

    user_id = int(input("Enter ID: "))
    change = input("What do you want to change? (name or number): ")
    change = change.lower()
    data = input(f'To what value set the {change}?: ')
    if change == 'name':
        sql = '''
            UPDATE qwer SET name = %s WHERE id = %s;
        '''
    elif change == 'number':
        sql = '''
            UPDATE qwer SET number = %s WHERE id = %s;
        '''
    current.execute(sql, (data, user_id))
    config.commit()
    current.close()


def sort_or_request():
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



def delete():
    sql = '''
        DELETE FROM qwer WHERE name = %s RETURNING *
    '''
# удаление данных по имени или по номеру
    current = config.cursor()
    del_data = input("By what do you want to delete? (name or number): ")
    del_data = del_data.lower()
    temp = input(f'Which {del_data} do you want to delete?: ')
    if del_data == 'name':
        sql = '''
            DELETE FROM qwer WHERE name = %s RETURNING *
        '''
    elif del_data == 'number':
        sql = '''
            DELETE FROM qwer WHERE number = %s RETURNING *
        '''
    current.execute(sql, (temp,))
    config.commit()
    current.close()



run = True
while run:
    answer = """
    что вы хотите делать ?
      1 - вставить данные в телефонную книгу загружая их из csv-файла
      2 - вставить данные в телефонную книгу вводя их с консоли
      3 - обновление данных в таблице (name)
      4 - данные по отсортированному имени или номер определенного человека
      5 - удаление данных по имени или по номеру
      другое число чтобы прекратить
    """
    print(answer)

    q = int(input())
    if q == 1:
        from_csv()
    elif q == 2:
        input_data()
    elif q == 3:
        update_data()
    elif q == 4:
        sort_or_request()
    elif q == 5:
        delete()
    else:
        print("давай :) ")
        run = False