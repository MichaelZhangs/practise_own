import  happybase

host = "192.168.237.165"
table_name = "user"
row_key  = "rowkey_10"
column_family = "base_info"

conn = happybase.Connection(host)
print(conn)