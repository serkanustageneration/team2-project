
import psycopg2



hostname = 'localhost'
database = 'team-2_group-project'
username = 'root'
pwd = 'pass' 

conn = None
cur = None
try:
    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd
    )

    cur = conn.cursor()
    
    ## create customer table ## as ** customer_df
    create_customer_table = '''CREATE TABLE customer_df
                            (
                            customer_name	TEXT,
                            card_number	    text 
                           
                            );'''
  
    conn.commit()
    
    ## create store table ## as ** store_df
    create_store_table = '''CREATE TABLE  store_df(
                            store     	 TEXT
                            );'''
    conn.commit() 
    ## create basket table ## as ** basket_df                     
    create_basket_table = '''CREATE TABLE  basket_df(
                            product_id     	 integer,
                            order_id         integer,
                            customer_id      integer,
                            store_id         integer,
                            time_stamp       text
                            );'''
    conn.commit() 
     ## create products table ## as ** basket_df                     
    create_products_table = '''CREATE TABLE products_df  (
                            product_name	TEXT,
                            product_flavour    text,  	
                            product_price	 integer
                            
                            );'''
    conn.commit()
    
    # executing tables 
    cur.execute(f' {create_customer_table}{create_store_table}{create_products_table}{create_basket_table}')
    print('tables have been created!!')
    
 
   
    conn.commit()


except Exception as error:
    print(error)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()



