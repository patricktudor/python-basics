import pandas as pd
import pyodbc

# connect to db
conn = pyodbc.connect('Driver={SQL Server};' 'Server=MY_SERVER;' 'Database=MY_DATABASE;' 'Trusted_Connection=yes')

qry = """
SELECT MY_COL_1, MY_COL_2 FROM [MY_DATABASE].[MY_TABLE]
"""

df = pd.DataFrame(pd.read_sql_query(qry, conn))

# close connection
conn.close()