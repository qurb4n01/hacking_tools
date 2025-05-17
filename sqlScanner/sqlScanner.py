import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option('-u',
                  '--url',
                  dest='url',
                  help='scan etmek istediyiniz url-i qeyd edin')
parser.add_option('-f',
                  '--file',
                  dest='urls_file',
                  help='scan etmek istediyiniz url-ler olan fayli qeyd edin')

(user_inputs,arg) = parser.parse_args()
url = user_inputs.url

urls_file = user_inputs.urls_file



urls=[]
if urls_file:
    # fayl varsa onu ac
    with open(urls_file,'r') as file:
        for line in file:
            urls.append(line.strip())
    for i in urls:
        command = ['sqlmap','-u',i,'--batch','--dbs',
                    '--timeout=10',
                    '--retries=1',
                    '--threads=1',
                    '--level=1',
                    '--risk=1']
        result = subprocess.check_output(command)

        if b'available databases' in result:
            print(f'{i} | sql-injection-a hessasdir')
        else:
            print(f'{i} | sql-injection-a hessas deyil')
elif url:
    # url varsa onu birbasa yoxla
    command = ['sqlmap','-u',url,'--batch','--dbs',
               '--timeout=10',
                '--retries=1',
                '--threads=1',
                '--level=1',
                '--risk=1']
    result = subprocess.check_output(command)

    if b'available databases' in result:
        print(f'{url} | sql-injection-a hessasdir')
    else:
        print(f'{url} | sql-injection-a hessas deyil')
else:
    print('zehmet olmasa ya -u ile bir url, ya da -f ile bir fayl qeyd edin')