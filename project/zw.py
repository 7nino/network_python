import ipaddress
net = ipaddress.ip_network('192.168.1.0/24')
print(net[0])
print(net[-1])
 

