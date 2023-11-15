from flask import Flask , request , render_template , redirect , session , flash
from flask_sqlalchemy import SQLAlchemy
import bcrypt 
from subprocess import run, PIPE


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
app.secret_key = '12345'

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(100),nullable=False, unique=True)
    password = db.Column(db.String(100),nullable=False)

    def __init__(self,username,password):
        self.username = username 
        self.password = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt()).decode('utf-8')

    def check_password(self,password):
        return bcrypt.checkpw(password.encode('utf-8'),self.password.encode('utf-8'))

with app.app_context():
    db.create_all()



@app.route('/')
def index():
    return 'hi'

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        #handle request
        username = request.form['username']
        password = request.form['password']

        new_user = User(username=username , password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect('login')

    return render_template('register_bootstrap.html')


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        #handle request
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            session['username'] =  user.username
            session['password'] = user.password
            return redirect('/dashboard')
        else:
            return render_template('login_bootstrap.html',error='Invalid user')


    return render_template('login_bootstrap.html')


@app.route('/dashboard')
def dashboard():
    if session['username']:
        return render_template('dashboard_bootstrap.html')


@app.route('/singlescan',methods =['GET','POST'])
def singlescan():
    ip = None
    # file = open(r'clientend_ssh.py', 'r').read()
    # exec(file)
    if request.method == 'POST':
        ip = request.form['ip']
        command = f"python3 clientend_ssh.py -t {ip}" 
        run(command, shell=True, stdout=PIPE ,stderr=PIPE, text=True)
        return render_template('singlescan_finished.html', debug="str")
    
    return render_template('singlescan.html')

@app.route('/multiscan',methods =['GET','POST'])
def multiscan():
   starting_ip = None
   ending_ip = None
   if request.method == 'POST':
       starting_ip = request.form['starting_ip']
       ending_ip = request.form['ending_ip']

       starting_ip_split = starting_ip.split(".")
       ending_ip_split = ending_ip.split(".")

       starting_ip_last_digit = starting_ip_split[3]
       starting_ip_last_digit_i = int(starting_ip_last_digit)

       ending_ip_last_digit = ending_ip_split[3]
       ending_ip_last_digit_i = int(ending_ip_last_digit)

       for i in range(starting_ip_last_digit_i,ending_ip_last_digit_i+1):
        count = i
        i = str(i)
        new_ip = starting_ip_split[0]+"."+starting_ip_split[1]+"."+starting_ip_split[2]+"."+i
        command = f"python3 clientend_ssh.py -t {new_ip}" 
        run(command, shell=True, stdout=PIPE ,stderr=PIPE, text=True)
        if count == ending_ip_last_digit_i:
            return render_template('multiscan_finished.html')

       
   return render_template('multiscan.html')


if __name__ == "__main__":
    app.run(debug=True)
