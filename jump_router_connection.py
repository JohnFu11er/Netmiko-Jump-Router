#!/usr/bin/env python3
from netmiko import ConnectHandler
import time

device = {
    'device_type': 'cisco_ios',
    'host': '192.168.10.1',             # this is the IP for my "jump router"
    'username': 'bob',                  # ssh username for "jump router"
    'password': 'supersecretpassword'   # ssh password for "jump router"
}

# Initalize Netmiko object
net_connect = ConnectHandler(**device)

# Write the SSH command to the "jump router" to get to the target router
net_connect.write_channel("ssh -l bob 192.168.1.2\n")   

# Pause to give "jump router" time to respond and prompt for ssh password
time.sleep(2)

# Send ssh password for the target router
net_connect.write_channel("supersecretpassword\n")

# Print the prompt that of the router that Netmiko is actively connected to
# Should print the name of your target server indicating that you are connected
# to the "jump server"
print(net_connect.find_prompt())
