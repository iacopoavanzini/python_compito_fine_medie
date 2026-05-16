from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app .route("/compiti") 
def compiti(): 
    memory_file = open("compiti.txt", "r", encoding = "utf8")
    contenuto_file = memory_file.read()
    # print(contenuto_file)
    memory_file.close()
    return contenuto_file

if __name__ == '__main__':
    app.run(debug=True)
