import sqlite3

conn = sqlite3.connect("owosch.db")
cursor = conn.cursor()

def execute_query(query, params=()):
    try:
        cursor.execute(query, params)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print(f"Помилка при виконанні коду: {e}")

# print("\nВся інформація про овоч")

# execute_query("""
#         SELECT vegetable_id, vegetable_name, vegetable_price, vegetable_harvest
#         FROM vegetables
# """)

# print("\nЯке виробництво завезе овочі і коли овочі завезуть в магазини")

# execute_query("""
#         SELECT production_name, production_delivery
#         FROM production      
# """)

# print("\nВиробництва з найбільшою популярністю")

# execute_query("""
#         SELECT production_name, production_popularity
#         FROM production
#         WHERE production_popularity = 'Висока'     
# """)

# print("\nНазва виробництва в алфавітному порядку")

# execute_query("""
#         SELECT production_name
#         FROM production
#         ORDER BY production_name ASC                         
# """)

print("\nОвочі з ціною вище 20 ")

execute_query("""
        SELECT vegetable_name, vegetable_price
        FROM vegetables
        WHERE vegetable_price > 20.0
""")

# print("\nОвочі, зібрані у серпні 2024 року")

# execute_query("""
#         SELECT vegetable_name, vegetable_harvest
#         FROM vegetables
#         WHERE vegetable_harvest LIKE '2024-08-%'
# """)