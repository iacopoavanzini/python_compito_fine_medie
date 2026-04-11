from src.scadenza import calcolo_scadenza
from src.repository import scrivi

s = True
n = False

proposta = eval(input("vuoi aggiungere un compito alla lista?(s/n)"))
        
if proposta == s:
    input_nome_compito: str = input("inserisci i nome del compito:")
    input_descrizione_compito: str = input("inserisci la descrizione del compito:")
    input_data_compito: str = input("inserisci la data di scadenza:(dd/mm/yyyy)")
    data_avviso = calcolo_scadenza(input_data_compito)
    dati_compito = input_nome_compito + ";" + input_descrizione_compito+";"+ input_data_compito + ";" +  data_avviso + "\n"
    scrivi("compiti.txt", dati_compito)
    print("ok, ti avviserò il giorno ",data_avviso," cioè un giorno prima del compito")
else: proposta == n
print("passiamo agli avvisi di oggi")
