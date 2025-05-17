import requests
from requests.exceptions import ReadTimeout, SSLError, RequestException
import optparse

parser = optparse.OptionParser()
parser.add_option('-f',
                  '--file',
                  dest='domains_file',
                  help='bu secim yoxlamaq istediyiniz domain-lerin faylini qebul edir')

(user_input, args) = parser.parse_args()
domains_file = user_input.domains_file

if not domains_file:
    domains_file = input('domain-ler olan fayli daxil edin: ')



domains=[]
with open(domains_file,'r') as file:
    for line in file:
        domains.append(line.strip())

print(r'''
 __          __  _        _____      _  _                         
 \ \        / / | |      / ____|    | || |                        
  \ \  /\  / /__| |__   | (___   ___| || |_ _ __  _ __   ___ _ __ 
   \ \/  \/ / _ \ '_ \   \___ \ / __|__   _| '_ \| '_ \ / _ \ '__|
    \  /\  /  __/ |_) |  ____) | (__   | | | | | | | | |  __/ |   
     \/  \/ \___|_.__/  |_____/ \___|  |_| |_| |_|_| |_|\___|_|   
                                                                  
                                                                  by Gurban Bannayev     
''')





for domain in domains:
    url = 'https://'+domain

    try:
        headers = requests.get(url,timeout=5).headers

        if "X-Frame-Options" in headers:
            print(f'++{domain} click-jacking-e hessasdir')
        else:
            print(f'--{domain} click-jacking-e hessas deyil')

    except ReadTimeout:
        print(f"?Timeout while trying to connect to {domain}")
    except SSLError:
        print(f"?SSL error with {domain}")
    except RequestException:
        #print(f"//Failed to connect to {domain} via HTTPS")
        try:
            url = 'http://'+domain
            try:
                headers = requests.get(url,timeout=5).headers

                if "X-Frame-Options" in headers:
                    print(f'++{domain} click-jacking-e hessasdir')
                else:
                    print(f'--{domain} click-jacking-e hessas deyil')

            except ReadTimeout:
                print(f"?Timeout while trying to connect to {domain}")
            except SSLError:
                print(f"?SSL error with {domain}")
        except:
            print(f'Failed to connect to {domain} via HTTP and HTTPS')