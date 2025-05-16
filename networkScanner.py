import scapy.all as scapy
import optparse 

print(r'''
  _   _      _                      _       _____      _  _                         
 | \ | |    | |                    | |     / ____|    | || |                        
 |  \| | ___| |___      _____  _ __| | __ | (___   ___| || |_ _ __  _ __   ___ _ __ 
 | . ` |/ _ \ __\ \ /\ / / _ \| '__| |/ /  \___ \ / __|__   _| '_ \| '_ \ / _ \ '__|
 | |\  |  __/ |_ \ V  V / (_) | |  |   <   ____) | (__   | | | | | | | | |  __/ |   
 |_| \_|\___|\__| \_/\_/ \___/|_|  |_|\_\ |_____/ \___|  |_| |_| |_|_| |_|\___|_|   
                                                                                    
                                                                                    by Gurban Bannayev
      ''')

parser = optparse.OptionParser()
parser.add_option('-i','--ip',
                   dest='ip_address',
                   help='ip address-i teyin et'
                   )

(user_input,args) = parser.parse_args()
ip_address = user_input.ip_address

if not ip_address:
    ip_address = input('ip address-i daxil edin: ')
    


arp_request_packet = scapy.ARP(pdst=ip_address)
broadcast_packet = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')

full_packet = broadcast_packet/arp_request_packet

(answered,unanswered) = scapy.srp(full_packet, timeout=4)

print(answered.summary())

#scapy.ls(scapy.Ether())