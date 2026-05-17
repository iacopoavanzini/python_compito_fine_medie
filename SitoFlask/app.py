from flask import Flask, request, render_template, redirect, url_for
from DB_Operations import add_text
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html' , text= "hello world 1")
@app .route("/compiti" , methods=["POST" , "GET"]) 
def compiti(): 
    memory_file = open("compiti.txt", "r", encoding = "utf8")
    contenuto_file = memory_file.read()
    memory_file.close()
    return contenuto_file

@app.route("/add_text", methods=["POST", "GET"]) 
def  AddText(): 
    if request.method == "POST" : 
        text_value = request.form["textv"] 
        #salvataggio di tutti i valori nel db
        add_new = add_text(text_value) 
        return redirect("/") 
    else : 
        return render_template('index.html') 

if __name__ == '__main__':
    app.run(debug=True)
