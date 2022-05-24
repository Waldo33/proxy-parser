import urllib.request
import socket
import urllib.error

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

with open('proxy.txt') as f:
    proxyList = [row.strip() for row in f]

good = []
bad = []

def is_bad_proxy(pip):
    try:
        proxy_handler = urllib.request.ProxyHandler({'http': pip})
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)
        req=urllib.request.Request('https://ya.ru')  # change the URL to test here
        sock=urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print('Error code: ', e.code)
        return e.code
    except Exception as detail:
        print("ERROR:", detail)
        return True
    return False
def main():
    socket.setdefaulttimeout(200)
    # two sample proxy IPs
    for currentProxy in proxyList:
        if is_bad_proxy(currentProxy):
            print(f"{currentProxy}is {bcolors.FAIL}Bad{bcolors.ENDC}")
            bad.append(currentProxy)
            with open('bad.txt', 'w', encoding='utf-8') as f:
                f.write("\n".join(bad))
        else:
            print(f"{currentProxy} is {bcolors.OKGREEN}Good{bcolors.ENDC}")
            good.append(currentProxy)
            with open('good.txt', 'w', encoding='utf-8') as f:
                f.write("\n".join(good))

if __name__ == '__main__':
    main()