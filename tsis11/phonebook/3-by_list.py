import csv, psycopg2

config = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    password = '1234',
    user = 'postgres'
)
current = config.cursor()

current.execute(
    '''CREATE OR REPLACE PROCEDURE insert_list_of_users(
  IN users TEXT[][]
)
LANGUAGE plpgsql
AS $$
DECLARE
  i TEXT[];
  invalid_users TEXT[][];
BEGIN 
   FOREACH i SLICE 1 IN ARRAY users
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
$$;
''')

current.execute('''CALL insert_list_of_users(ARRAY[
    ARRAY['22', 'aveke', '8787497949'],
    ARRAY['23', 'aldik', '8707894'],
    ARRAY['24', 'google', '87973688975']
]);
''') 
# В конце процедуры проверяется, есть ли в массиве invalid_users какие-либо записи, и если есть, выводится уведомление с их данными.