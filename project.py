import psycopg2 as pg
import psycopg2.extras 

hostname = 'localhost'
database = 'postgres'
username = 'postgres'
pwd = 'admin'
post_id = 5432

con = None



try:
    with pg.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = post_id
    ) as con:

        with con.cursor(cursor_factory = psycopg2.extras.DictCursor) as cur:

            create_table = '''
                            CREATE TABLE IF NOT EXISTS users(
                                name   varchar(40) NOT NULL,
                                email   varchar(40),
                                phone_number   varchar(20),
                                age   int,
                                gender   varchar(10),
                                salary   float,
                                date_of_birth   date,
                                created_date    date
                            )
            '''

            cur.execute(create_table)

            # inserting the values in the database
            insert_script = 'insert into users (name, email, phone_number, age, gender, salary, date_of_birth, created_date) values (%s, %s, %s, %s, %s, %s, %s, %s)'
            insert_value = ('rohit', 'rohit@mail.com', '582265', 20, 'male', 55000.50, '2015-12-17', '2015-12-17')
            cur.execute(insert_script, insert_value)

            # query to fetch the data
            cur.execute('Select * from users')
            print(cur.fetchall())

            # query to update the record
            update_script = 'update users set email = %s where name = %s'
            update_value = ('rohit11','rohit')
            cur.execute(update_script,update_value)

            # query to delete a row
            cur.execute("delete from users where name = 'rohit'")

except Exception as error:
    print(error)

finally:
    if con is not None:
        con.close()