'''#from collections import defaultdict
lista=[{1:1},{1:2}]
final_config={}
#final_config=defaultdict(list)
for each in lista:
    for key,value in each.items():
        final_config[key].append(value)
print(final_config)'''

device_node_ip={}
device_name='sw01'
device_ip='192.168.0.1'
device_node_ip[device_name]=device_ip
print(device_node_ip)