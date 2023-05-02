import csv, psycopg2, re

config = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    password = '1234',
    user = 'postgres'
)
current = config.cursor()


current.execute(
    '''CREATE OR REPLACE FUNCTION search( a VARCHAR)
      RETURNS SETOF qwer 
   AS
   $$
      SELECT * FROM qwer WHERE name = a or number = a;
   $$
   language sql;
   '''
)

current.execute(
   '''CREATE OR REPLACE PROCEDURE insert_to_qwer(i INTEGER, nm VARCHAR, phon VARCHAR)
      LANGUAGE plpgsql
      AS $$
      DECLARE 
         cnt INTEGER;
      BEGIN
         SELECT INTO cnt (SELECT count(*) FROM qwer WHERE name = nm);
         IF cnt > 0 THEN
            UPDATE qwer
               SET number = phon
               WHERE name = nm;
         ELSE
            INSERT INTO qwer(i, name, phone) VALUES (id, nm, phon);
            END IF;
      END;
      $$''')

current.execute(
   '''CREATE OR REPLACE PROCEDURE by_list(
  IN users TEXT[][]
)

LANGUAGE plpgsql

AS $$

DECLARE
  i TEXT[];
  invalid_users TEXT[][];
BEGIN 

   Foreach i slice 1 in array users
    LOOP
    IF LENGTH(i[3]) != 11 THEN
        invalid_users := array_cat(invalid_users, ARRAY[i]);
    ELSE
        INSERT INTO qwer (id, name, number) VALUES (CAST(i[1] AS INTEGER), i[2], i[3]);
    END IF;
END LOOP;
    IF array_length(invalid_users, 1) > 0 THEN
    RAISE NOTICE 'The following users have invalid phone numbers: %', invalid_users;
    END IF;
END
$$
;
'''
)

current.execute(
   """CREATE OR REPLACE FUNCTION paginating(a integer, b integer)
RETURNS SETOF qwer
AS $$
   SELECT * FROM qwer
	ORDER BY name
	LIMIT a OFFSET b;
$$
language sql;""")


current.execute(
    '''CREATE OR REPLACE PROCEDURE delete_from(del VARCHAR)
AS $$
BEGIN
    DELETE FROM qwer WHERE name = del OR number = del;
END;
$$ LANGUAGE plpgsql;
'''
)

qw = '''
1 - search
2 - add_or_update
3 - loop
4 - paginating
5 - delete
'''

print(qw)
ask = int(input())
if ask == 1:
    current.execute("SELECT search('Asel')")
    result = current.fetchall()
    print(result)
if ask == 2:
    current.execute(f"CALL insert_to_qwer('80', 'Alex', '87994756854')")
if ask == 3:
    current.execute('''CALL by_list(ARRAY[
    ARRAY['89', 'Ademi', '8707605'],
    ARRAY['90', 'Brat', '87079815569'],
    ARRAY['91', 'Yana', '8707579368664']
]);''')  
if ask == 4:
    current.execute(
      '''SELECT * FROM paginating(3, 2);'''
    )
    print(*current.fetchall())
if ask == 5:
    current.execute("CALL delete_from('name')")
config.commit()
current.close()
config.close()