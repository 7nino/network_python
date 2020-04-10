import ipaddress
import sys
def ipjisuan(ip_net):
    try:
        net=ipaddress.ip_network(ip_net,strict=False)
        print('IP版本:'+str(net.version))
        print('是否是私有地址:'+str(net.is_private))
        print('IP地址总数:'+str(net.num_addresses))
        print('可用IP地址总数:'+str(len([x for x in net.hosts()])))
        print('起始可用IP地址:'+str(net[0]))
        print('最后可用IP地址:'+str(net[-1]))
        print('可用IP地址范围:'+str(net[0]) + '~' + str(net[-1]))
        print('掩码地址:'+str(net.netmask))
        print('反掩码地址:'+str(net.hostmask))
        print('网络号:'+str(net.network_address))
        print('广播地址:'+str(net.broadcast_address))
    except ValueError:
        print('您输入格式有误，请检查！')
if __name__=='__main__':
#    for host in ip_net(sys.argv[1]):
#   ip_net='10.10.0.5/28'
    ipjisuan(sys.argv[1])
#[x for x in net.hosts()