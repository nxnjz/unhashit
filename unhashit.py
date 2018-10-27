#!/usr/bin/python3

#NXNJZ.NET

import os
import requests
import argparse
from bs4 import BeautifulSoup


# Manage api keys for hashes.org
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


# Function to save each line of output to text file
def save_out(line):
    try:
        with open(argus.output, 'a') as out_file:
            out_file.write(line + '\n')
    except TypeError:
        pass


# Function to parse from crackhash.com
def crackhashcom_check(hash_value):
    if len(hash_value) == 32:
        algo = 'MD5'
    elif len(hash_value) == 40:
        algo = 'SHA1'
    else:
        print(hash_value, "seems like an invalid hash for crackhash.com")
    r = requests.post("http://crackhash.com", data = {'hash':hash_value, 'crack':'crack'})
    soup = BeautifulSoup(r.text, "lxml")
    try:
        parsed = soup.th.center.string.split()
        result = hash_value + ' : ' + parsed[len(parsed)-1] + ' : ' + algo
    except AttributeError:
        result = hash_value + ' : notfound'
    print(result) 
    save_out(result)


# Function to call the nitrxgen.net api
def nitrxgen_check(hash_value):
    apiurl = "http://www.nitrxgen.net/md5db/" + str(hash_value)
    r = requests.get(apiurl)
    if r.text != "":
        result = hash_value + " : " + r.text + " : MD5"
    else:
        result = hash_value + " : notfound"
    print(result)
    save_out(result)


# Function to call the hashes.org api
def hashesorg_check(apikey, hash_value):
    apiurl = "https://hashes.org/api.php?key=" + apikey + "&query=" + hash_value
    rr = requests.get(apiurl)
    if rr.json()['status'] == 'success':
        try:
            plaintxt = rr.json()['result'][hash_value]['plain']
            algo = rr.json()['result'][hash_value]['algorithm']
            result = hash_value + " : " + plaintxt + " : " + algo
        except TypeError:
            result = hash_value + " : notfound"
        print(result)
        save_out(result)
    else:
        print("Error querying the hashes.org API, you may have overused it in a short period of time, or your key is invalid")


# argument parsing
prsr = argparse.ArgumentParser(description="This script automates lookup of hashes by using the APIs on nitrxgen.net and hashes.org, and parsing on crackhash.com")
prsr.add_argument('-a','--api',required=True,help='nitrxgen.net (MD5 only)  OR  hashes.org (key required)  OR  crackhash.com (unreliable and slow due to parsing, MD5 and SHA1 only)')
prsr.add_argument('-i','--input',required=True,help='List of hashes, one per line.')
prsr.add_argument('-o','--output',help='Choose an output file if you want to save the results')
prsr.add_argument('-k','--key',help='API key for hashes.org')

argus = prsr.parse_args()


# Open input file and check lines
with open(argus.input) as hashfile:
    if argus.api == 'nitrxgen.net':
        for line in hashfile:
            nitrxgen_check(line.strip())
    elif argus.api == 'hashes.org':
        key_mng()
        for line in hashfile:
            hashesorg_check(apikey, line.strip()) 
    elif argus.api == 'crackhash.com':
        for line in hashfile:
            crackhashcom_check(line.strip())
