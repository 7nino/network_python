import openpyxl
import os.path
from jinja2 import Environment,PackageLoader
from netmiko import ConnectHandler
from collections import defaultdict
from time import sleep
from lxml import etree

config_container=[]
device_node_ip={}

router_config_excel=openpyxl.load_workbook(r'D:\python-3.6.5-amd64\project\PyEZ\cisco\实验工作表.xlsx')
router_int_config=router_config_excel.get_sheet_by_name("接口配置")

#jinja_loader=FileSystemLoader('./')
env=Environment(loader=PackageLoader('site-packages','jinja2'))
router_int_template=env.get_template('router_int_config.txt')

each=2
while each <= router_int_config.max_row:
    device_name=router_int_config["A"+str(each)].value
    device_ip=router_int_config["B"+str(each)].value
    device_username=router_int_config["J"+str(each)].value
    device_password=router_int_config["K"+str(each)].value
    config_paramter={"int_name":router_int_config["C"+str(each)].value,
                     "ip_add": router_int_config["D" + str(each)].value,
                     "ospf_number": router_int_config["G" + str(each)].value,
                     "router_id": router_int_config["H" + str(each)].value,
                     "network_ip":router_int_config["L" + str(each)].value,
                     "area_number": router_int_config["I" + str(each)].value}
    routing_config=router_int_template.render(config_paramter)
    config_container.append({device_name:routing_config})
    device_node_ip[device_name]=device_ip
    each+=1

final_config=defaultdict(list)
for each in config_container:
    for key,value in each.items():
        final_config[key].append(value)

#print(config_container)
#print(device_node_ip)

for key,value in device_node_ip.items():
    try:
        print(key)
        print(value)
        print(final_config[key])
        net_connect = ConnectHandler(device_type='cisco_ios_telnet',host=value,username='root',password='root') 
        net_info=net_connect
        current_view = net_connect.find_prompt() #查看当前模式
        print(current_view)  #查看当前模式
        net_connect.write_channel("enable\n") #输入enable
        net_connect.write_channel("root\n")
        current_view = net_connect.find_prompt() #查看当前模式
        print(current_view)  #查看当前模式
        net_connect.enable() #进入特权模式
        for each in final_config[key]:
            input = net_connect.send_config_set(each)
            time.sleep(3)
    except:
        print('{}设备配置完成'.format(value)) 
    
    



