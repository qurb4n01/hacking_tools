import subprocess 
import optparse
import re

print("Mac-Changer Bashladi!")

interface = ''
mac_address = ''

def get_input():
    parser = optparse.OptionParser()
    parser.add_option('-i','--interface',dest='interface',help='bu secim interface secimi ucun istifade olunur')
    parser.add_option('-m','--mac',dest='mac_address',help='bu secim mac address secimi ucun istifade olunur')
    return parser.parse_args()

#eger flag-lar daxil edilmese
def control_inputs(interface,mac_address):
    if not interface:
        interface = input('Interface-i daxil edin: ')
    if not mac_address:
        mac_address = input('Mac Address-i daxil edin: ')
    return interface,mac_address

#scriptlerin cagirilmasi
def change_mac(interface,mac_address):
    subprocess.call(['ifconfig',interface,'down'])
    subprocess.call(['ifconfig','eth0','hw','ether',mac_address])
    subprocess.call(['ifconfig','eth0','up'])

def check_mac(interface):
    ifconfig = subprocess.check_output(['ifconfig',interface])
    ifconfig_str = ifconfig.decode()
    new_mac = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w',ifconfig_str)
    if new_mac:
        return new_mac.group(0)
    else:
        return False

print('''
  __  __ _  _          _____ _    _  _                          ___  __ 
 |  \/  | || |        / ____| |  | || |                        / _ \/_ |
 | \  / | || |_ ___  | |    | |__| || |_ _ __   __ _  ___ _ __| | | || |
 | |\/| |__   _/ __| | |    | '_ \__   _| '_ \ / _` |/ _ \ '__| | | || |
 | |  | |  | || (__  | |____| | | | | | | | | | (_| |  __/ |  | |_| || |
 |_|  |_|  |_| \___|  \_____|_| |_| |_| |_| |_|\__, |\___|_|   \___/ |_|
                                                __/ |                   
                                               |___/                    by Gurban Bannayev
      ''')

#flag-lardan goturulen datalari variable-lara kocurme
(user_inputs,arg)=get_input()
interface,mac_address = control_inputs(user_inputs.interface, user_inputs.mac_address)


change_mac(interface,mac_address)

#check_mac devami 
final_mac = check_mac(interface)
if final_mac == mac_address:
    print("Mac address ugurla deyisdirildi")
else:
    print("Mac address-i deyisdirerken bir xeta bas verdi")


