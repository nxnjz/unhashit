# unhashit

Simple Python 3 Script to query APIs on nitrxgen.net and hashes.org

#### Requirements:
**Python3** with the **argparse**, **os** and **requests** modules.


#### Output is in the following format:

hash : plain-text-value : algorithm (if found)

hash : "notfound" (if not found

#### Usage:

./unhashit.py [-h] -a API -i INPUT [-o OUTPUT] [-k KEY]

optional arguments:
  -h, --help            show this help message and exit
  -a API, --api API     nitrxgen.net (MD5 only) or hashes.org
  -i INPUT, --input INPUT
                        List of hashes, one per line.
  -o OUTPUT, --output OUTPUT
                        Choose an output file if you want to save the results
  -k KEY, --key KEY     API key for hashes.org

