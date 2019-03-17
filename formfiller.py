import mechanize
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