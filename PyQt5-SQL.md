# PyQt5与数据库的接口  
PyQt5的API中用QSqlDatabase类用来连接数据库, 一个实例代表一次数据库连接  
不同的数据库驱动类型不同, 例如QMYSQL为MYSQL驱动程序  
## 连接数据库  
from PyQt5.QtSql import QSqlDatabase  
db = QSqlDatabase.addDatabase("QMYSQL")  
db.setHostName("192.168.55.110")  
db.setDatabaseName("user")   
db.setUserName("root")  
db.setPassword("123")  
db.Conn = db.open()  
db.Conn = db.close()  
## 执行语句  
query = QSqlQuery()  
query.exec_("SQL语句")  


