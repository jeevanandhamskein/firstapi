from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String
#from db.db import engine ,Meta
from config.db import meta,engine

users=Table("users",meta,Column(
    "id",Integer,primary_key=True, autoincrement = True),
    Column("name",String(255)),
    Column("email",String(255)),
    Column("password",String(20)))

meta.create_all(engine)

 