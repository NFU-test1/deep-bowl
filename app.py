from flask import Flask,render_template,request,url_for,redirect,session
import os
from werkzeug.utils import secure_filename
import sqlite3 as sql
from flask import g
import uuid

DATABASE = 'database.db'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/upload/'

allow_file = {'png', 'jpg', 'jpeg',  'gif'}


@app.route("/")
def hello():
    return render_template('index.html')

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sql.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def allowed_file(name):
    x = None
    if '.' in name and name.rsplit('.', 1)[1].lower() in  allow_file:
        x = '.' + name.rsplit('.', 1)[1].lower()
    return x 

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
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if email == 'admin' and password == '1234':
            type = '登入成功'
            return render_template('Backstage.html',email=email,password=password,type = type)
        else:
            type = '登入失敗'
            return render_template('login.html',type = type)
        #print(email,password)
        
    else:
        return render_template('login.html')



@app.route("/test")
def about():
    return render_template('about.html')

@app.route('/page/app')
def pageAppInfo():
    name = '11161124'
    appInfo = {  # dict
        'id': 5,
        'name': 'Python - Flask',
        'version': '1.0.1',
        'author': 'Enoxs',
        'remark': 'Python - Web Framework'
    }
    x = ['a','b','c','d','e']
    #compute()
    return render_template('page.html', appInfo=appInfo,name = name,x = x)


@app.route("/upload",methods = ['GET','POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        f.filename = allowed_file(f.filename)
        name = str(uuid.uuid4())+f.filename
        #print(request.files)
        if f.filename == None:
            type = '副檔名不符'
        else:
            with get_db() as cur:
                cur.row_factory = sql.Row
                cur = cur.cursor()
                cur.execute(f"INSERT INTO picture (p_name) VALUES('{name}')")
                cur.close()
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], name))
            type = '新增成功'
        return render_template('upload.html',type=type)
    else:
        return render_template('upload.html')

@app.route('/page2')
def page2():
    email = request.args.get('id')
    password = request.args.get('ps')
    type = '登入成功'
    return render_template('page2.html',email=email,password=password,type=type)

@app.route('/show')
def show():
    return render_template('show.html')

@app.route('/tshow')
def tshow():
    with get_db() as cur:
        cur.row_factory = sql.Row
        cur = cur.cursor()
        cur.execute("select * from picture")
        name = cur.fetchall()
        cur.close()
    return render_template('testpg.html', name = name)

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