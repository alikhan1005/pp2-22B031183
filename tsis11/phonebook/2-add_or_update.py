import  psycopg2

config = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    password = '1234',
    user = 'postgres'
)
current = config.cursor()

current.execute(
   '''CREATE OR REPLACE PROCEDURE add_or_update_user(i INTEGER, nm VARCHAR, num VARCHAR)
      LANGUAGE plpgsql
      AS $$
      DECLARE 
         cnt INTEGER;
      BEGIN
         SELECT INTO cnt (SELECT count(*) FROM qwer WHERE name = nm);
         IF cnt > 0 THEN
            UPDATE qwer
               SET number = num
               WHERE name = nm;
         ELSE
            INSERT INTO qwer(id, name, number) VALUES (i, nm, num);
            END IF;
      END;
      $$;''')

current.execute(
    '''CREATE OR REPLACE PROCEDURE insert_or_update_user(username VARCHAR(100), phone VARCHAR(12))
AS $$
BEGIN
    IF EXISTS (SELECT * FROM qwer WHERE name = username) THEN
        UPDATE qwer SET number = phone WHERE name = username;
    ELSE
        INSERT INTO qwer (name, number) VALUES (username, phone);
    END IF;
END;
$$ LANGUAGE plpgsql;
'''
)

current.execute("CALL insert_or_update_user( 'Alex', '87773854974')")
