import subprocess, socket
from dialog import Dialog

d = Dialog(dialog="dialog")
d.set_background_title("define RMM network")

ipmitool = "/usr/bin/ipmitool"
set_ipmitool = "lan set 1"

get_dhcp_static = "IP Address Source"
get_ipaddr = "IP Address"
get_netmask = "Subnet Mask"
get_default_gateway = "Default Gateway IP"

set_ipsrc = "ipsrc"
set_ipaddr = "ipaddr"
set_netmask = "netmask"
set_defgw = "defgw ipaddr"
dhcp = "dhcp"
static = "static"


def error_msg_exit(msg):
    d.msgbox("ERROR: " + msg + ".", width=50)
    os.system('clear')
    sys.exit(1)


def is_valid_ipv4(addr):
    """ Check for ip validity """

    try:
        socket.inet_aton(addr)
    except socket.error:
        return False

    return addr.count('.') == 3


def choose_bootproto(bootproto_to_set):
    """ Choose BootProto dhcp or none """

    if dhcp_static == "static":
        opt_static = True
        opt_dhcp = False
    else:
        opt_static = False
        opt_dhcp = True

    code, options = d.radiolist(
         "IP Mode (space bar to choose)", height=0, width=40, list_height=0,
         choices=[
            ("DHCP", "", opt_dhcp),
            ("Static", "", opt_static)
            ])

    if options == "DHCP":
         bootproto_to_set = "dhcp"
    else:
          bootproto_to_set = "static"

    set_ipmitool_lan(set_ipsrc, bootproto_to_set)

    return  bootproto_to_set

def set_ip_gateway_and_netmask(nic_parameters):
    """ Enter ip netmask and default geteway and dhcp """

    nic_config = []

    while True:
        code, nic_config = d.form("RMM Configuration", [
            ("IP address", 1, 1, nic_parameters["IP"], 1, 20, 20, 0),
            ("Netmask", 2, 1, nic_parameters["Netmask"], 2, 20, 20, 0),
            ("Gateway", 3, 1, nic_parameters["Gateway"], 3, 20, 20, 0),
            ])

        if code != d.OK:
            return nic_config

        while True:
            if is_valid_ipv4(nic_config[0]) is False:
                d.msgbox("Error: Invalid IP address '" + nic_config[0] + "'.", width=50)
                break
            if is_valid_ipv4(nic_config[1]) is False:
                d.msgbox("Error: Invalid Netmask '" + nic_config[1] + "'.", width=50)
                break
            if nic_config[2]:
                if is_valid_ipv4(nic_config[2]) is False:
                    d.msgbox("Error: Invalid Gateway '" + nic_config[2] + "'.", width=50)
                    break
            return nic_config


def get_ipmitool_lan(para):
    """ Get information on RMM lan """

    ipmi_cmd = ipmitool + " lan print"
    proc = subprocess.Popen(ipmi_cmd.split(), stdout=subprocess.PIPE)
    for line in proc.stdout.readlines():
         if line.startswith(para + "  "):
              value_str = line.split(":",1)[1]
              value_str = value_str.split()[0]
              break
    return value_str


def set_ipmitool_lan(para, valu_para):
    """ Set parameter on RMM lan """

    ipmi_cmd = ipmitool + " lan set 1 " + para + " " + valu_para
    p = subprocess.Popen(ipmi_cmd.split(), stdout=subprocess.PIPE)


dhcp_static = get_ipmitool_lan(get_dhcp_static)
ipaddr = get_ipmitool_lan(get_ipaddr)
netmask = get_ipmitool_lan(get_netmask)
defult_gateway = get_ipmitool_lan(get_default_gateway)
nic_parameters = {"IP":ipaddr, "Netmask":netmask, "Gateway":defult_gateway}

bootproto_to_set = choose_bootproto(dhcp_static)

if bootproto_to_set == "static":

    nic_config = set_ip_gateway_and_netmask(nic_parameters)
    set_ipmitool_lan(set_ipaddr, str(nic_config[0]))
    set_ipmitool_lan(set_netmask, str(nic_config[1]))
    set_ipmitool_lan(set_defgw, str(nic_config[2]))

print ("\nipsrc: %s" % get_ipmitool_lan(get_dhcp_static))
print ("ipaddr: %s" % get_ipmitool_lan(get_ipaddr))
print ("netmask: %s" % get_ipmitool_lan(get_netmask))
print ("defgw ipaddr: %s" % get_ipmitool_lan(get_default_gateway))
