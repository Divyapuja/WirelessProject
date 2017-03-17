import DDPacket
import ExtractPacket

neighbors = {}
rib = {}

# on reception of hello reply packet update neighbors
def update_neighbors(srcip, s_mac, delay,age):
    neighbors[srcip] = [s_mac,delay,age]

# on an update on local RIB send a DD packet
def sendDD(sending_socket,interface):
    sending_socket.send(DDPacket.ddPacket(interface,rib))

# on reception of hello reply packet if triggers a change in the local RIB or on reception of DD packet
# which results in the change of local RIB update RIB

def updateRIB(packet):
    src_mac,dst_mac,eth_type,src_ip,dst_ip,dsdv_type,rib_neighbor = ExtractPacket.extractPacketFields(packet)

    if dsdv_type == 2:
        # hello reply packet update the local RIB and neighbors data structure get the timer
        pass
    if dsdv_type == 3:
        # DD packet updating RIB logic goes here
        pass

def sendHello(interface):
    # periodically send hello packets through the interface
    pass

def updateFIB():
    #update tshe host FIB
    pass



