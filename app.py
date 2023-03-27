from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/name/<name>")
def name(name):
    print("type(name) : ", type(name))
    return f'String => {name}'

@app.route("/number/<int:id>",methods = ['GET'])
def number(id):
    for i in range(id):
        print(i)
    return f'{id}'

if __name__ == "__main__":
    #app.debug=True
    app.run(debug=True)


#-------------------------------#
'''



'''  