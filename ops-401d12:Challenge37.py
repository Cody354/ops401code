#!/usr/bin/env python3

import requests
import webbrowser

# targetsite = input("Enter target site:") # Uncomment this to accept user input target site
targetsite = "http://www.whatarecookies.com/cookietest.asp" # Comment this out if you're using the line above
response = requests.get(targetsite)
cookie = response.cookies

def bringforthcookiemonster(): # Because why not!
    print('''

              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.

        ''')

bringforthcookiemonster()
print("Target site is " + targetsite)
print(cookie)

# Sending the cookie back to the site
cookies_dict = requests.utils.dict_from_cookiejar(cookie)
response_with_cookie = requests.get(targetsite, cookies=cookies_dict)

# Generate a .html file to capture the contents of the HTTP response
html_content = response_with_cookie.text
file_name = "response.html"
with open(file_name, 'w') as file:
    file.write(html_content)

# Open it with Firefox
webbrowser.get('firefox').open_new_tab(file_name)

# Stretch Goal - Give Cookie Monster hands
def bringforthcookiemonster_with_hands():
    print('''
          .--.  .--.
         : ("\\` )`\\   : me want cookie!
      _  `.    ; .--'  /_
     ( `\\  `. .-"    / .-. `.
      `._ `- /__..--' /   \  `.
         `"--._      /     \   \\
              `"\  -'    _.'._   ;
                 `-._.-'  __ `\\ :
                     :""--`--`-' \\.
                     |              \\
                     :   |   |        \\
                     :   :   :         `.
                      `-._____`.__..-'
    ''')

bringforthcookiemonster_with_hands()
