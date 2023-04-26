import psycopg2
config = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    password = '1234',
    user = 'postgres'
)

current = config.cursor()
sql = '''
        CREATE TABLE uuu(
            username VARCHAR(100) PRIMARY KEY,
            level VARCHAR(12),
            score VARCHAR(12)
    );
'''
current.execute(sql)

current.close()
config.commit()
config.close()