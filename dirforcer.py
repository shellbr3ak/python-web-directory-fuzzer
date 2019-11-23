import requests
import argparse


BLUE = "\033[34m"
GREEN = "\033[0;32m"
RED = "\033[1;31m"
YELLOW = "\033[33m"
RESET = "\033[0;0m"

print(BLUE + """\n\n
       +------------------------------------------------+
       |                  Coded by : L                  |
       |                                                |
       | https://github.com/shellbr3ak?tab=repositories |
       +------------------------------------------------+
         ____  _          _ _ ____                 _    
        / ___|| |__   ___| | | __ ) _ __ ___  __ _| | __
        \___ \| '_ \ / _ \ | |  _ \| '__/ _ \/ _` | |/ /
         ___) | | | |  __/ | | |_) | | |  __/ (_| |   < 
        |____/|_| |_|\___|_|_|____/|_|  \___|\__,_|_|\_|
                                                                                                     
                        offensive python                
                        ----------------
                                                                                                                                                                     
""" + RESET)

def make_request(url, dirname):
    r = requests.get(url + "/" + dirname)
    if not (r.status_code == 404):
        if(r.status_code == 200):
            print("/" + dirname + "  (Status " + GREEN + f"{r.status_code}" + RESET + ")")
        else:
            print("/" + dirname + "(Status " + BLUE + f"{r.status_code}" + RESET + ")")



parser = argparse.ArgumentParser(description="Example: python3 bf.py -u http://example.com -w wordlist.txt")
parser.add_argument("-u", dest="url", help="The Url You Want To Fuzz")
parser.add_argument("-w", dest="wordlist", help="The Wordlist to use for Fuzzing")
#parser.add_argument("-s", data="status_code", help="The Status Code of The Made Request")

parsed_args = parser.parse_args()


url = parsed_args.url
wordlist = parsed_args.wordlist


dirnames = open(wordlist).read().splitlines()

try:
    if not (url.startswith("http")):
        print(RED + "URL has to be in form of : <http://example.com>" + RESET)
        exit(1)
    for dirname in dirnames:
        make_request(url, dirname)
    
    else:
        print(RED + "Try another wordlist" + RESET)

except KeyboardInterrupt:
    print(RED + "You Stopped The Script" + RESET)
except TypeError:
    print(RED + parser.description + RESET)
