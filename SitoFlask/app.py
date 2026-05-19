from flask import Flask, render_template, request, redirect, url_for
from DB_Operations import add_text
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html' , text= "hello world 1")
@app .route("/compiti" , methods=["GET"]) 
def compiti(): 
    memory_file = open("compiti.txt", "r", encoding = "utf8")
    contenuto_file = memory_file.read()
    memory_file.close()
    return contenuto_file

@app.route("/compiti", methods=["POST"]) 
def  AddText(): 
    if request.method == "POST" : 
        title = request.form["title"] 
        description = request.form["description"]
        #salvataggio di tutti i valori nel db
        add_new = add_text(title, description) 
        return redirect("/") 

if __name__ == '__main__':
    app.run(debug=True)
