#!/usr/bin/python3

#NXNJZ.NET

import os
import requests
import argparse


def key_mng():
    global apikey
    try:
        with open(argus.key) as key_file:
            apikey = key_file.read()
            print("Reading key from", argus.key)
    except FileNotFoundError:
        apikey = argus.key
    except TypeError:
        print("API key is required for hashes.org")
        exit()

def save_out(line):
    try:
        with open(argus.output) as out_file:
            out_file.write(line)
    except TypeError:
        pass

def nitrxgen_check(md5hash):
    apiurl = "http://www.nitrxgen.net/md5db/" + str(md5hash)
    r = requests.get(apiurl)
    if r.text != "":
        result = md5hash + " : " + r.text + " : MD5"
    else:
        result = md5hash + " : notfound"
    print(result)
    save_out(result)

def hashesorg_check(apikey, multi_hash):
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
        save_out(result)
    else:
        print("Error querying the hashes.org API, you may have overused it in a short period of time, or you key is invalid")


prsr = argparse.ArgumentParser(description="This script automates lookup of hashes by using the APIs on nitrxgen.net and hashes.org")
prsr.add_argument('-a','--api',required=True,help='nitrxgen.net (MD5 only) or hashes.org')
prsr.add_argument('-i','--input',required=True,help='List of hashes, one per line.')
prsr.add_argument('-o','--output',help='Choose an output file if you want to save the results')
prsr.add_argument('-k','--key',help='API key for hashes.org')

argus = prsr.parse_args()

with open(argus.input) as hashfile:
    if argus.api == 'nitrxgen.net':
        for line in hashfile:
            nitrxgen_check(line.strip())
    elif argus.api == 'hashes.org':
        key_mng()
        for line in hashfile:
            hashesorg_check(apikey, line.strip()) 
