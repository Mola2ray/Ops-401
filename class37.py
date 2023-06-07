#!/usr/bin/python3
# Lamin Touray
# Scripts:





import requests
import webbrowser
import os

# targetsite = input("Enter target site:") # Uncomment this to accept user input target site
targetsite = "http://www.whatarecookies.com/cookietest.asp" # Comment this out if you're using the line above
response = requests.get(targetsite)
cookie = response.cookies

def bringforthcookiemonster(): # Now with hands!
    print('''
            .---. .---.
           :     : o   :    me want cookie!
       _..-:   o :     :-.._    /
   .-''  '  `---' `---' "   ``-.
 .'.   "   '  "  .    "  . '  "  `.
: '.---.,,.,...,.,.,.,..---.  ' ;
 `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.
     . ' `-   ' .  _  .  '  - ` .'
   . '    `- .` / `. `- '    ` .'

    ''')

bringforthcookiemonster()
print("Target site is " + targetsite)
print(cookie)

# Use the cookies we received to send a request back to the site
response_with_cookies = requests.get(targetsite, cookies=cookie)

# Generate an HTML file to capture the contents of the HTTP response
with open('response.html', 'w') as f:
    f.write(response_with_cookies.text)

# Open the HTML file with Firefox
firefox_path = '/usr/bin/firefox' # Change this to your actual Firefox executable path
webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path))

# Open the HTML file in Firefox
webbrowser.get('firefox').open_new_tab('file://' + os.path.realpath('response.html'))
