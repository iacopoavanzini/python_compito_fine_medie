import datetime

def calcolo_scadenza(input_data_compito):
    data_scadenza = datetime.datetime.strptime(input_data_compito,"%d/%m/%Y")
    if data_scadenza < datetime.datetime.now():
        raise(ValueError("non puoi inserire date nel passato"))
    data_avviso = data_scadenza - datetime.timedelta(days = 1)
    return data_avviso.strftime("%d/%m/%Y")