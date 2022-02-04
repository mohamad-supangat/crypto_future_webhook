from datetime import datetime

from pysondb import db

tradesDb = db.getDb("trades.json")


# save data to tradesDb
def save_order(indicator="", type="", qty=0, price=0, cause="", last_status="", market="", exchange="", candle_period=""):
    tradesDb.add({
        "candle_period": candle_period,
        "time": datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
        "market": market,
        "exchange": exchange,
        "indicator": indicator,
        "type": type,
        "last_status": last_status,
        "qty": qty,
        "price": price,
        "cause": cause
    })
