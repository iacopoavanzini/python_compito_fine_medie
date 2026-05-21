from flask import Flask, render_template, request, redirect, url_for
from DB_Operations import add_text, get_compiti
app = Flask(__name__)
@app.route('/')
def home():
    compiti = get_compiti()
    for row in compiti:
        print(row)
    return render_template('index.html' , compiti=compiti)

@app .route("/compiti" , methods=["GET"]) 
def compiti(): 
    return get_compiti()

@app.route("/compiti", methods=["POST"]) 
def  AddText(): 
    if request.method == "POST" : 
        title = request.form["title"] 
        description = request.form["description"]
        materia = request.form["materia"]
        data_scadenza = request.form["scadenza"]
        #salvataggio di tutti i valori nel db
        add_new = add_text(title, description, data_scadenza, materia) 
        return redirect("/") 

if __name__ == '__main__':
    app.run(debug=True)
