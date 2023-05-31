import scapy.all as scapy
from scapy.layers.l2 import *
from io import StringIO
import sys


def scan_network(network)->ARPingResult:
    '''
    Scan network
    Returns an ARPingResult
    '''
    while True:
        result = scapy.arping(network)
        userInput = input("Scan again? Y/n: ")
        if userInput.lower() == 'n':
            print('Ok, the scan result will be used for further processing...')
            break
    
    # The arping function will return a tuple with a ARPingResult, and a PacketList.
    # We only want the ARPingResult
    return result[0]


def parse_ARPingResult(result:ARPingResult)->list:
    '''
    Parse ARPingResult, convert it into data that can be used for processing.
    Returns a list with dictionaries about hosts
    '''
    
    buffer = StringIO()
    
    # Move stdout from terminal into buffer
    sys.stdout = buffer
    
    # Run the show method to capture the stdout into the buffer
    result.show()

    # Fetch data from buffer, and store it into a variable
    raw_output = buffer.getvalue()

    # Restore stdout to default for print()
    sys.stdout = sys.__stdout__

    # Convert the captured stdout into dictionary
    parsed_data = []
    result_rows = raw_output.split('\n')
    for row in result_rows:
        # last row in results contains an empty row
        if(row != ''): 
            mac_address, name, ip_address = row.split()
            
            parsed_host = {
                'name': name,
                'mac': mac_address,
                'ip': ip_address
            }
            parsed_data.append(parsed_host)

    return parsed_data


if __name__ == '__main__':
    # 1. This script needs to ask the user for a network range to scan.
    network = input('Network to scan: ')

    # 2. Get the active IP hosts (Don’t scan all ports, scan for the most common ports (80, 22, 443, 23, 110, 143, 25).
    arp_scan_result = scan_network(network)
    hosts = parse_ARPingResult(arp_scan_result)


    # 3. Scan the active hosts for open ports.
    # 4. Display the results to the end user.
    # 5. Optional: Use command line arguments for the network range.


