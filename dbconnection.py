from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import pymysql


class DBConnection:
    def __init__(self, host, username, password, dbname):
        pymysql.install_as_MySQLdb()
        db = 'mysql+mysqldb://' + username + ':' + password + '@' + host + '/' + dbname + '?charset=utf8'
        engine = create_engine(db)
        engine.connect()
        self.s = Session(engine)
        self.Base = automap_base()
        self.Base.prepare(engine, reflect=True)

    def write_data(self, data, termin):
        Wahl = self.Base.classes.wahl
        Sprengel = self.Base.classes.sprengel
        Partei = self.Base.classes.partei
        Stimmen = self.Base.classes.parteistimmen

        try:
            parteien = []
            for k in data[0].keys():
                if k not in ("T", "WV", "WK", "BZ", "SPR", "WBER", "ABG.", "UNG."):
                    p = Partei(bez=k)
                    self.s.add(p)
                    parteien.append(p)

            wahl = Wahl(termin=termin)

            self.s.add(wahl)

            for l in data:
                sp = Sprengel(snr=l["SPR"], bnr=l["BZ"], termin=termin, berechtigte=l["WBER"], ungueltige=l["UNG."])
                self.s.add(sp)
                for p in parteien:
                    st = Stimmen(pbez=p.bez, snr=sp.snr, bnr=sp.bnr, termin=termin, stimmanzahl=int(l[p.bez]))
                    self.s.add(st)

            self.s.commit()
        except:
            self.s.rollback()
            raise
