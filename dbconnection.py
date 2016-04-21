from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import pymysql

from orderedset._orderedset import OrderedSet


class DBConnection:
    def __init__(self, host, username, password, dbname):
        pymysql.install_as_MySQLdb()
        db = 'mysql+mysqldb://' + username + ':' + password + '@' + host + '/' + dbname + '?charset=utf8'
        self.engine = create_engine(db)
        self.engine.connect()
        self.s = Session(self.engine)
        self.Base = automap_base()
        self.Base.prepare(self.engine, reflect=True)

    def write_data(self, data, termin):
        Wahl = self.Base.classes.wahl
        Sprengel = self.Base.classes.sprengel
        Partei = self.Base.classes.partei
        Stimmen = self.Base.classes.parteistimmen

        try:
            parteien = []
            for k in data[0].keys():
                if k not in ("T", "WV", "WK", "BZ", "SPR", "WBER", "ABG", "UNG"):
                    p = Partei(bez=k)
                    self.s.merge(p)
                    parteien.append(p)

            wahl = Wahl(termin=termin)

            self.s.merge(wahl)

            for l in data:
                sp = Sprengel(snr=l["SPR"], bnr=l["BZ"], termin=termin, berechtigte=l["WBER"], ungueltige=l["UNG"], abgegeben=l["ABG"])
                self.s.add(sp)
                for p in parteien:
                    st = Stimmen(pbez=p.bez, snr=sp.snr, bnr=sp.bnr, termin=termin, stimmanzahl=int(l[p.bez]))
                    self.s.add(st)

            self.s.commit()
        except:
            self.s.rollback()
            raise

    def read_data(self, termin):

        query = "SELECT wahlkreis.id, bezirk.bnr, sprengel.snr, sprengel.berechtigte, " \
                "sprengel.abgegeben, sprengel.ungueltige, parteistimmen.pbez, parteistimmen.stimmanzahl " \
                "FROM wahlkreis " \
                "INNER JOIN bezirk ON wahlkreis.id = bezirk.wkid " \
                "INNER JOIN sprengel ON bezirk.bnr = sprengel.bnr " \
                "AND sprengel.termin = '" + termin + "' " \
                "INNER JOIN parteistimmen ON parteistimmen.termin = '" + termin + "' " \
                "AND parteistimmen.bnr = bezirk.bnr " \
                "AND parteistimmen.snr = sprengel.snr;"

        r = self.s.execute(query).fetchall()

        header = OrderedSet(["WK", "BZ", "SPR", "WBER", "ABG", "UNG"])
        datalist = []
        line = {}
        first_party = None
        for i in range(0, len(r)):
            current_party = r[i]["pbez"]
            if first_party is None or current_party == first_party:
                line = {}
                first_party = current_party
                line["WK"] = r[i]["id"]
                line["BZ"] = r[i]["bnr"]
                line["SPR"] = r[i]["snr"]
                line["WBER"] = r[i]["berechtigte"]
                line["ABG"] = r[i]["abgegeben"]
                line["UNG"] = r[i]["ungueltige"]
                datalist.append(line)
            line[current_party] = r[i]["stimmanzahl"]
            header.add(current_party)

        return datalist, list(header)

    def create_prediction(self, termin, time):

        query = "CALL erzeugeHochrechnung('" + termin + "', '" + time + "');"
        self.s.execute(query)
        self.s.commit()

    def get_predictions(self):

        HR = self.Base.classes.hochrechnung

        hrs = self.s.query(HR).all()

        result = []
        for hr in hrs:
            result.append({"termin": hr.termin, "time": hr.zeitp})

        return result

    def get_prediction_data(self, termin, time):

        hrresult = self.Base.classes.hrergebnis

        hrs = self.s.query(hrresult).filter(hrresult.termin == termin, hrresult.zeitp == time).all()

        datalist = []
        for hr in hrs:
            line = {}
            line["Party"] = hr.pbez
            line["Percentage"] = ("%.2f" % (hr.prozent * 100)) + "%"
            datalist.append(line)

        return datalist, ["Party", "Percentage"]


    def get_termine(self):
        Wahl = self.Base.classes.wahl

        return self.s.query(Wahl.termin).all()