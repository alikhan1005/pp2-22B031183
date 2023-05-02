import csv, psycopg2

config = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    password = '1234',
    user = 'postgres'
)
current = config.cursor()

current.execute(
    '''CREATE OR REPLACE FUNCTION search_qwer(a VARCHAR)
      RETURNS SETOF qwer 
   AS
   $$
      SELECT * FROM qwer WHERE name = a or number = a;
   $$
   language sql;
   '''
)

current.execute("SELECT * FROM search_qwer('87777777777')")
res = current.fetchall()
print(*res, sep='\n')