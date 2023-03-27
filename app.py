from flask import Flask,render_template,request
import os

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

@app.route("/login",methods = ['GET'])
def user():
    id = request.args.get('id')
    password = request.args.get('password')
    return f"{id},{password}"



@app.route("/test")
def about():
    return render_template('about.html')

@app.route("/testans",methods = ['post'])
def check():
    if request.method == 'POST':
        ans = request.form['ans']
        #return(ans)
    cmd = f"python -c {ans}"
    a = os.system(cmd)
    #print(a)
    return 'ans'

    #return render_template('about.html')

if __name__ == "__main__":
    #app.debug=True
    app.run(debug=True)

#test 

#-------------------------------#
'''



'''  