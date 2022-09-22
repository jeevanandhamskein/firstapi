from sqlalchemy import create_engine,MetaData

engine=create_engine("mysql+mysqldb://root:root@localhost:3306/thirddb")
#engine=create_engine("mysql+mysqldb(pip:mysqlclient)://uname:password@localhost:3306/dbname")

conn=engine.connect()


meta=MetaData()


