import psycopg2

config = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    password = '1234',
    user = 'postgres'
)

current = config.cursor()
current.execute(
    '''CREATE OR REPLACE PROCEDURE delete_user(del VARCHAR)
AS $$
BEGIN
    DELETE FROM qwer WHERE name = del OR number = del;
END;
$$ LANGUAGE plpgsql;
'''
)
current.execute("CALL delete_user('rtyuiuytr')")