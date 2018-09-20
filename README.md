# unhashit

Simple Python 3 Script to query APIs on nitrxgen.net and hashes.org, and automatically lookup and parse on crackhash.com

#### Requirements:
**Python3** with the **beautifulsoup4**, **lxml**, **argparse**, **os** and **requests** modules.


#### Output is in the following format:

hash : plain-text-value : algorithm (if found)

hash : "notfound" (if not found)

#### Usage:

./unhashit.py [-h] -a API -i INPUT [-o OUTPUT] [-k KEY]

  -h, --help            show this help message and exit
  -a API, --api API     nitrxgen.net (MD5 only) OR hashes.org (key required)
                        OR crackhash.com (unreliable and slow due to parsing,
                        MD5 and SHA1 only)
  -i INPUT, --input INPUT
                        List of hashes, one per line.
  -o OUTPUT, --output OUTPUT
                        Choose an output file if you want to save the results
  -k KEY, --key KEY     API key for hashes.org

