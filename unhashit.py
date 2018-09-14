#!/usr/bin/python3

#NXNJZ.NET

import os
import requests


def key_mng():
    try:
        global apikey
        apikey_file = open("hashes.org-api.key",)
        apikey = apikey_file.read()
    except FileNotFoundError:
        apikey = input("The file 'hashes.org-api.key' containing the api key was not found, enter your api key: ")
        savefile = input("\nWould you like to store this key in a file to avoid entering it every time? (y/n): ")
        if savefile == 'y':
            with open("hashes.org-api.key", "w") as apikey_file :
                apikey_file.write(apikey)
                os.chmod("hashes.org-api.key", 0o600)
                print("\nYour key was written to hashes.org-api.key, permissions set to rw------- (owner read/write, group nothing, others nothing)")

def multi_check(apikey, multi_hash):
    apiurl = "https://hashes.org/api.php?key=" + apikey + "&query=" + multi_hash
    rr = requests.get(apiurl)
    if rr.json()['status'] == 'success':
        try:
            plaintxt = rr.json()['result'][multi_hash]['plain']
            algo = rr.json()['result'][multi_hash]['algorithm']
            result = multi_hash + " : " + plaintxt + " : " + algo
        except TypeError:
            result = multi_hash + " : notfound"
        print(result)
    else:
        print("Error querying the hashes.org API, you may have overused it in a short period of time. ")


def md5_check(md5hash):
   apiurl = "http://www.nitrxgen.net/md5db/" + str(md5hash)
   r = requests.get(apiurl)
   if r.text != "":
       result = md5hash + " : " + r.text + " : MD5"
   else:
       result = md5hash + " : notfound"
   print(result)

print("This script uses APIs on nitrxgen.net and hashes.org. Do NOT use for illegal purposes\n")
print("\n1. Nitrxgen.net (MD5 only, unlimited requests)")
print("\n2. Hashes.org (API key required, 100 requests per 5 minutes allowed)")
api_choice = input("\n\n Choose: ")

if api_choice == '1':
    filename = input("Enter filename (one MD5 hash per line): ")
    with open(filename) as md5_file:
        for line in md5_file:
            md5_check(line.strip())
elif api_choice == '2':
    key_mng()
    filename = input("Enter filename (one hash per line): ")
    with open(filename) as multi_file:
        for line in multi_file:
            multi_check(apikey, line.strip())


else: print("Choice not recognized, exiting.")


