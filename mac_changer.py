import subprocess
import optparse
import re

def get_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option('-i', '--interface', dest='interface', help='Interface to change!')
    parse_object.add_option('-m', '--mac', dest='mac_address', help='new mac address')

    (user_inputs, arguments) =parse_object.parse_args()
    return user_inputs.interface, user_inputs.mac_address

user_interface, user_macaddress = get_input()

def change_macaddress(interface, maccaddress):
        print('Commands are working!')
        subprocess.call(['ifconfig', interface, 'down'])
        subprocess.call(['ifconfig', interface,'hw','ether',maccaddress])
        subprocess.call(['ifconfig', interface, 'up'])

def control_new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig",interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))

    if new_mac:
        return new_mac.group(0)
    else:
        return None

print('MacChanger Started!')
change_macaddress(user_interface,user_macaddress)
finalized_mac = control_new_mac(str(user_interface))
if finalized_mac == user_macaddress:
    print('Success!')
else:
    print('Error!')
