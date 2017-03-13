import socket, sys
from struct import *
import netifaces as ni
from netifaces import *


'''

                                IP HEADER

    0                   1                   2                   3
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |Version|  IHL  |Type of Service|          Total Length         |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |         Identification        |Flags|      Fragment Offset    |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |  Time to Live |    Protocol   |         Header Checksum       |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                       Source Address                          |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                    Destination Address                        |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                    Options                    |    Padding    |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+


'''
def toBytes(x):
    return (int(x,16))

def helloPacket(interface):
    if interface not in ni.interfaces():
        return None

    S_MAC = ni.ifaddresses(interface)[AF_LINK][0]['addr'].split(":")
    S_MAC = pack('!6c',chr(int(S_MAC[0], 16)), chr(int(S_MAC[1],16)),  chr(int(S_MAC[2],16)) , chr(int(S_MAC[3],16)), chr(int(S_MAC[4],16)), chr(int(S_MAC[5],16)))
    D_MAC = pack('!6c',chr(int('ff', 16)), chr(int('ff',16)),  chr(int('ff',16)) , chr(int('ff',16)), chr(int('ff',16)), chr(int('ff',16)))
    ETH_TYPE = pack('!2c',chr(int('08',16)),chr(int('00',16)))

    ethernet_header = S_MAC+D_MAC+ETH_TYPE  # 14 bytes


    ip_v_ihl  = pack('!c',chr(int('45',16)))
    ip_tos = pack('!c',chr(int('00',16)))
    ip_tot_len = pack('!2c',chr(int('00',16)),chr(int('00',16)))
    ip_id = pack('!2c',chr(int('ff',16)),chr(int('ff',16)))
    ip_frag_off = pack('!2c',chr(int('00',16)),chr(int('00',16)))
    ip_ttl = pack('!c',chr(int('ff',16)))
    ip_proto = pack('!c',chr(253))
    ip_check = pack('!2c',chr(0),chr(0))

    Src_IP = ni.ifaddresses(interface)[ni.AF_INET][0]['addr'].split('.')

    ip_src = pack('!4c',Src_IP[0],Src_IP[1],Src_IP[2],Src_IP[3])
    ip_dst = pack('!4c',chr(224),chr(0),chr(0),chr(4))
    ip_options = pack('!4c',chr(0),chr(0),chr(0),chr(0))

    ip_header = ip_v_ihl + ip_tos + ip_tot_len + ip_id + ip_frag_off + ip_ttl + ip_proto + ip_check + ip_src + ip_dst + ip_options

    payload = 'hello'

    return ethernet_header+ip_header+payload





interface = 'en0'

s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
s.bind((interface,0))
s.send(helloPacket(interface))

'''
packet = ''

src_ip = '10.0.2.15'
dst_ip = '10.0.2.15'

ip_ihl = 5
ip_ver = 4
ip_tos = 0
ip_tot_len = 0
ip_id = 54321
ip_frag_off = 0
ip_ttl = 255
ip_proto = 253
ip_check = 0
ip_saddr = socket.inet_aton(src_ip)
ip_daddr = socket.inet_aton(dst_ip)
ip_ihl_ver = (ip_ver << 4) + ip_ihl
ip_header = pack('!BBHHHBBH4s4s', ip_ihl_ver, ip_tos, ip_tot_len, ip_id, ip_frag_off, ip_ttl, ip_proto, ip_check,
                 ip_saddr, ip_daddr)

packet = ip_header + 'user data'
s.sendto(packet, (dst_ip, 0))
'''