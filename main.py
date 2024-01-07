import subprocess

network = subprocess.check_output(['netsh','wlan','show','network'])

#netsh is used for network shall 

decode_network=network.decode('ascii')

#this will decode the incoming output in ascii formate 

print(decode_network)