from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import pymysql

pymysql.install_as_MySQLdb()

db = 'mysql+mysqldb://root:password@172.16.6.137/wahl?charset=utf8'
engine = create_engine(db)
conn = engine.connect()
# create declarative base class
Base = automap_base()
# create declarative classes from dbms
Base.prepare(engine, reflect=True)
# create references for all reflected tables
wahl = Base.classes.wahl

s = Session(engine)
try:
    # create an instance of wahl (record in table wahl)
    #w = wahl(termin='2015-12-12', mandate=1000)
    # add it to the session (SQL INSERT statement)
    #s.add(w)
    s.commit()
except:
    s.rollback()
    raise
finally:
    s.close()

class DBConnection:

    def __init__(self, host, username, password, dbname):
        pymysql.install_as_MySQLdb()
        db = 'mysql+mysqldb://'+username+':'+password+'@'+host+'/'+dbname+'?charset=utf8'
        engine = create_engine(db)
        engine.connect()
        self.Base = automap_base()
        self.Base.prepare(engine, reflect=True)

    def get_entity(self, name):
        pass