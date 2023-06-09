
#!/usr/bin/env python3

# Author:      Abdou Rockikz
# Description: TODO: XSS Vulnerability Detection with Python
# Date:        TODO: 8Jun2023
# Modified by: TODO: Lamin Touray

### TODO: Install requests bs4 before executing this in Python3

# Import libraries



import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

# Declare functions

### This function retrieves all HTML forms present on a given URL. ###
### It uses BeautifulSoup library to parse the HTML content of the URL ###
### and returns a list of form elements ###
def get_all_forms(url):
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")

### This function extracts the details of a given HTML form ###
### including its action URL, method, and input fields. ###
### It returns a dictionary containing the form details. ###
def get_form_details(form):
    details = {}
    action = form.attrs.get("action").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

### This function submits a form with a specified value ###
### for each input field and returns the response. ###
### It constructs the request URL based on the form's action URL ###
### and the form data based on the input fields. ###
def submit_form(form_details, url, value):
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            data[input_name] = input_value

    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)

### This function scans a given URL for XSS vulnerabilities. ###
### It retrieves all the forms on the URL using get_all_forms() function ###
### and submits each form with a JavaScript XSS payload. ###
### If the payload is executed and detected in the response content, ###
### it prints the details of the vulnerable form. ###
### It returns a boolean indicating if any vulnerabilities were found. ###
def scan_xss(url):
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    js_script = "<script>alert('XSS')</script>"
    is_vulnerable = False
    for form in forms:
        form_details = get_form_details(form)
        content = submit_form(form_details, url, js_script).content.decode()
        if js_script in content:
            print(f"[+] XSS Detected on {url}")
            print(f"[*] Form details:")
            pprint(form_details)
            is_vulnerable = True
    return is_vulnerable

# Main

### The main function prompts the user to enter a URL to test for XSS vulnerabilities. ###
### It then calls the scan_xss() function with the provided URL and prints the result. ###
if __name__ == "__main__":
    url = input("Enter a URL to test for XSS:") 
    print(scan_xss(url))


### TODO: When you have finished annotating this script with your own comments, copy it to Web Security Dojo
### TODO: Test this script against one XSS-positive target and one XSS-negative target
# [+] Detected 1 forms on https://xss-game.appspot.com/level1/frame.
# [+] XSS Detected on https://xss-game.appspot.com/level1/frame
# [*] Form details:
# {'action': '',
# 'inputs': [{'name': 'query',
#           'type': 'text',
#          'value': "<script>alert('XSS')</script>"},
#        {'name': None, 'type': 'submit'}],
# 'method': 'get'}
# True


### TODO: Paste the outputs here as comments in this script, clearling indicating which is positive detection and negative detection
