from argparse import ArgumentParser
import nmap3

parser = ArgumentParser()
parser.add_argument('-n','--net', 
                    help="Network to be scanned", 
                    required=True,
                    nargs=1)


def print_raw_nmap_result(results):
    print("{0}{1}{2}".format("Host".ljust(15), "MAC".center(30), "State".rjust(10)))
    print("-"*60)

    non_ip_row = ['runtime','stats','task_results']
    for key, data in results.items():
        if key not in non_ip_row:
            if data['state']['state'] == 'up':
                ip_address =  key
                if data['macaddress'] and data['macaddress'] != None:
                    mac_address = data['macaddress']['addr']
                else:
                    mac_address = 'not found'
                
                state = data['state']['state']
                print("{0}{1}{2}".format(
                    ip_address.ljust(15), mac_address.center(30), state.rjust(10)))
        
        if key == 'stats':
            print("-" * 60)
            print(f"Scan completed using nmap {data['version']}")
            print(f"Commands that where run: {data['args']}")


def task(network):
    '''
    Create a script with command line arguments that will scan the provided network. 
    For the command line arguments, you would need a net parameter. 

    In your script, you must use this net parameter you received from the 
    command line and scan that network. 
    
    You need to print your results to the screen for the end user.
    '''
    nmap = nmap3.NmapScanTechniques()
    print("Starting subnet scan")
    
    results = nmap.nmap_ping_scan(network)
    print_raw_nmap_result(results)
    

if __name__ == '__main__':
    args = parser.parse_args()
    task(args.net[0])