from netmiko import ConnectHandler
import os
import time

LogTime = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
Devices_path = r'D:\python-3.6.5-amd64\project\netmiko\Devices.txt'
CMD_path = r'D:\python-3.6.5-amd64\project\netmiko\CMD.txt'
Fail_path = r'D:\python-3.6.5-amd64\project\netmiko\fail.txt'
File_path = r'D:\python-3.6.5-amd64\project\netmiko'

def get_devices_info(path):
    Devices=[]
    try:
        with open(Devices_path,'r') as f:
           for line in f:
               if line[0]=='#':
                   continue
               elif len(line)==1:
                   continue
               else:
                   info_list=(line.strip().split())
                   info_dict={'ip':info_list[0],'username':info_list[1],'password':info_list[2]}
                   Devices.append(info_dict)
        return Devices
    except FileNotFoundError as e:
        print('找不到设备的配置文件')
    except IndexError as e:
        print('设备配置文件内容格式有误')

def get_cmd_info(path):
    CMD=[]
    try:
        with open(CMD_path,'r') as f:
            for line in f :
                if line[0]=='#':
                    continue
                elif len(line)==1:
                    continue
                else:
                    CMD.append(line.strip())
        return CMD
    except FileNotFoundError as e:
        print('找不到设备的配置文件')

def run_cmd(hosts=get_devices_info(Devices_path),commands=get_cmd_info(CMD_path)):
    print(hosts)
    print(commands)
    if os.path.exists(Fail_path)==True:
        os.remove(Fail_path)
    for ip_host in hosts:
        try:
            net_connect = ConnectHandler(device_type='huawei_telnet',**ip_host)  #telnet主机，输入账号密码
            net_connect.write_channel("sys\n") #输入sys
            net_connect.enable() #进入特权模式
            current_view = net_connect.find_prompt() #查看当前模式
            print(current_view)  #查看当前模式
            print('{}登陆设备成功'.format(ip_host['ip']))
            current_ip=ip_host['ip']
            show_path=File_path+'\\'+current_ip+'_'+LogTime
            os.makedirs(show_path)
            for ip_cmd in commands:
                output = net_connect.send_command(ip_cmd)
            #   print(output)
                time.sleep(1)
                with open(show_path+'\\'+ip_cmd+'.txt','a+') as f:
                    f.write(output)
            print('{}设备巡检完成'.format(ip_host['ip']))    
        except:
            print('{}设备巡检失败，失败记录保存在D:\python-3.6.5-amd64\\project\\netmiko\\fail.txt'.format(ip_host['ip']))
            with open(Fail_path,'a') as f:
                f.write(ip_host['ip']+'\n')

if __name__=='__main__':
    run_cmd()



