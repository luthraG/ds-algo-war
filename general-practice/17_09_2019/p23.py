'''
    Given a valid (IPv4) IP address, return a defanged version of that IP address.

    A defanged IP address replaces every period "." with "[.]".

    

    Example 1:

    Input: address = "1.1.1.1"
    Output: "1[.]1[.]1[.]1"

    Example 2:

    Input: address = "255.100.50.0"
    Output: "255[.]100[.]50[.]0"

    Constraints:

    The given address is a valid IPv4 address.
'''

import re

def defanged_ip_address(ip_address):
    pattern = re.compile(r'\.')
    ip_address = re.sub(pattern, '[.]', ip_address)
    return ip_address

ip_address = str(input('Enter IP address = '))
print('Defanged IP address is {}'.format(defanged_ip_address(ip_address)))