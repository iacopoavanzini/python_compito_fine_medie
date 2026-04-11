import datetime
from src import calcolo_scadenza

def test_calcola_scadenza_should_return_a_day_before():
    assert calcolo_scadenza(datetime.now()) == datetime.now()