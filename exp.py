host="127.0.0.1"
user="root"
password="root"
db_name='kuki'
import pymysql

try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("норм все")
    print("*"*20)

    try:
        # with connection.cursor() as cursor:
        #     create_table_query = "CREATE TABLE `kuki`(id int AUTO_INCREMENT," \
        #                          " name varchar(32)," \
        #                          " password varchar(32)," \
        #                          " email varchar(32), PRIMARY KEY (id));"
        #     cursor.execute(create_table_query)
        #     print("есть табла, чекай")

        #************************************

        with connection.cursor() as cursor:
            insert_query="INSERT INTO `kuki` (name, password, email) VALUES ('gena','qw','pu333p')"
            cursor.execute(insert_query)
            connection.commit()
            print("гатава дынные")

        #************************************

        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM `kuki`"
            cursor.execute(select_all_rows)
            rows=cursor.fetchall()
            for row in rows:
                print(row)
    finally:
        connection.close()
except Exception as ex:
    print("не дела...")
    print(ex)