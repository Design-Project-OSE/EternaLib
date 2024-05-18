import pypyodbc
connection = pypyodbc.connect('DRIVER={SQL Server};SERVER=SINAN\SQLEXPRESS;DATABASE=kullanıcı;UID=sa;PWD=Şifre')
cursor = connection.cursor()
cursor.execute("SELECT * FROM HumanResources.Department")
sonuc = cursor.fetchall()
for i in sonuc:
    print(i)