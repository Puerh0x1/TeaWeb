import requests
from threading import Thread
import argparse
import time
from termcolor import colored
import sys

from concurrent.futures import ThreadPoolExecutor
import socket
from termcolor import colored



def make_host_header_request(ip, rlink, headers, timeout, verbosemode, goodcodes):
    try:
        response = requests.get(f"http://{ip}", headers=headers, timeout=timeout)
        if str(response.status_code) in goodcodes:
            return colored(f"{rlink} FOUND!", "green")
        else:
            if verbosemode == "all":
                return colored (f"{rlink} NOT FOUND", "red")
    except:
        if verbosemode == "all":
            return colored (f"{rlink} Not Found", "red")



def make_simple_request(rlink, timeout, verbosemode, goodcodes):
	try:
		response = requests.get(f"{rlink}", timeout=timeout)
		if str(response.status_code) in goodcodes:
			return colored(f"{rlink} FOUND!", "green")

		else:
			if verbosemode == "all":
				return colored (f"{rlink} NOT FOUND", "red")
	except:
		if verbosemode == "all":
			return colored (f"{rlink} Not Found", "red")







def subdf(link, wordlist, fuzztype, timeout, num_threads, verbosemode, goodcodes):
    words = open(wordlist, "r").read().split("\n")
    
    if fuzztype == "hostheader":
        original_domain = link.replace("_TEA_.", "").replace("http://", "").replace("https://", '').replace("/", "")
        ip = socket.gethostbyname(original_domain)
        
        
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = []
            for word in words:
                rlink = link.replace("_TEA_", word)
                headers = {'Host': rlink.replace("http://", "").replace("https://", '').replace("/", "")}
                futures.append(executor.submit(make_host_header_request, ip, rlink, headers, timeout, verbosemode, goodcodes))


            for future in futures:
            	if str(future.result()) != "None":
                	print(future.result())

    elif fuzztype == "requests":
        
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = []
            for word in words:
                rlink = link.replace("_TEA_", word)
                futures.append(executor.submit(make_simple_request, rlink, timeout, verbosemode, goodcodes))

            for future in futures:
            	if str(future.result()) != "None":
                	print(future.result())



    print("\n~~Finished~~")



helpmsg = '''
-m Fuzzing mode.
Fuzzing modes:
	- subdomains or links fuzzing  (-m fuzz)

-w Wordlist file (-w file.txt)

-u URL (-u example.com)
For subdomains fuzzing mark the part you want to fuzz with the symbol _TEA_
Example: https://_TEA_.example.com | https://example.com/_TEA_

-ft Fuzzing method. 
	requests (-ft requests) - simple GET requests 
	hostheader (-ft hostheader) - making header HOST: in requests (best for localnets)
	Default is hostheader

-t request timeout in seconds (-t 2)
	default is 1 second (1)

-T threads (-T 10)
	default is 5

-v verbose mode
	all - prints all requests (bad and good)
	good - prints only good requests
	Example: -v good
	default good

-gc requests goodcodes (response codes of goodresults)
	example: -gc 200,301,500
	No Space.
	default: 200,201,202,203,204,205,206,300,301,302,303,304,500,502,503,504
'''

parser = argparse.ArgumentParser(description='teaweb')

parser.add_argument('--mode', '-m', metavar='mode', help='Fuzz Mode ( subdomains | links )')
parser.add_argument('--wordlist', '-w', metavar='wordlist', help='Wordlist File')
parser.add_argument('--url', '-u', metavar='url', help='URL. Replace word for fuzz to _TEA_\nExample _TEA_.example.com')
parser.add_argument('--fuzztype', '-ft', metavar='fuzztype', help='Subdomains fuzz type (requests | hostheader)')
parser.add_argument('--timeout', '-t', metavar='timeout', help='Timeout for 1 link (in seconds)')
parser.add_argument('--threads', '-T', metavar='threads', help='Threads Num')
parser.add_argument('--verbosemode', '-v', metavar='verbosemode', help='Verbose Mode: all | good')
parser.add_argument('--goodcodes', '-gc', metavar='goodcodes', help='List of good response status code\nExample: -gc 200,201,202,301,302,500')

args = parser.parse_args()

mode = args.mode

if mode is None:
	print(helpmsg)
	sys.exit()

wordlistfile = args.wordlist


if wordlistfile is None:
	print(helpmsg)
	sys.exit()


url = args.url


if url is None:
	print(helpmsg)
	sys.exit()


fuzztype = args.fuzztype

if fuzztype is None:
	fuzztype = "hostheader"

timeout = args.timeout
if timeout is None:
	timeout = 1

threads_num = args.threads
if threads_num is None:
	threads_num = 5

verbosemode = args.verbosemode
if verbosemode is None:
	verbosemode = "good"

stringsnum = len(open(wordlistfile, "r").read().split("\n"))

goodcodes = args.goodcodes
if goodcodes is None:
	goodcodeslist = "200,201,202,203,204,205,206,300,301,302,303,304,500,502,503,504"
	goodcodes = goodcodeslist.split(",")


if mode == "fuzz":
	print("Mode: ", colored("subdomains", "green"), "\nURL: ", colored(url, "green"), "\nFuzzing method: ", colored(fuzztype, "green"), "\nTimeout: ", colored(timeout, "yellow"), "\nThreads: ", colored(threads_num, "green"), "\nWordlist: ", colored(wordlistfile, "green"), "\nStrings: ", colored(stringsnum, "green"), "\nGood response codes:", colored(str(goodcodeslist), "green"), "\nVerbose mode: ", colored(verbosemode, "green"))
	print("~~Starting~~\n")
	time.sleep(2)
	subdf(url, wordlistfile, fuzztype, int(timeout), int(threads_num), verbosemode, goodcodes)
	
