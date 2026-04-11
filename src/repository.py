
def scrivi(nome_file, da_scrivere):
    memory_file = open(nome_file,"a", encoding = "utf8")
    memory_file.write(da_scrivere)
    memory_file.close()