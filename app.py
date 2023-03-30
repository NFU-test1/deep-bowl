from flask import Flask,render_template,request,url_for,redirect
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

@app.route("/login",methods = ['GET','POST'])
def user():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        #print(email,password)
        return redirect(url_for('page2',id=email,ps=password))
    else:
        return render_template('login.html')



@app.route("/test")
def about():
    return render_template('about.html')

@app.route('/page/app')
def pageAppInfo():
    name = 'asdfjlkejaeklf'
    appInfo = {  # dict
        'id': 5,
        'name': 'Python - Flask',
        'version': '1.0.1',
        'author': 'Enoxs',
        'remark': 'Python - Web Framework'
    }
    x = [i for i in range(5)]
    return render_template('page.html', appInfo=appInfo,name = name,x = x)

@app.route('/page2')
def page2():
    email = request.args.get('id')
    password = request.args.get('ps')
    return render_template('page2.html',email=email,password=password)

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