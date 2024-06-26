import paramiko
#import time
import yaml
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader("."))

temp1 = env.get_template("BGP.j2")
temp2 = env.get_template("OSPF.j2")
temp3 = env.get_template("Static.j2")

print("--------------------------------------------------------------")
print("--------------------------------------------------------------")
print("------Hello ...... Welcome to A.SoFy Environment -------------")
print("----- For Network DevOps [ CSR - Jenkins ] -------------------")
print("------If you Want to use Routing protocols like :-------------")
print("----- [ BGP press 1 ] [ OSPF press 2 ] [ Static press 3 ] ----")
inp = input()
print("--------------------------------------------------------------")
print("--------------------------------------------------------------")

if inp == "1":
    with open("inputBGP.yml") as file:
        bgp_data = yaml.full_load(file)
        output = temp1.render(int=bgp_data)

elif inp == "2":
    with open("inputOSPF.yml") as file1:
        OSPF_data = yaml.full_load(file1)
        output = temp2.render(int=OSPF_data)

elif inp == "3":
    with open("inputStatic.yml") as file2:
        st_data = yaml.full_load(file2)
        output = temp3.render(int=st_data)

else:
    print("Sorry Enter Correct Answer")


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.8.30',port=22,username='ahmed',password='dev_2024')
cli = ssh.invoke_shell()
cli.send('enable \n')
cli.send('terminal length 0 \n')
cli.send("conf t \n ")
cli.send(output)
print(output)
cli.send("\n do sh ip route \n ")
cli.send("\n do wr \n ")




# from netmiko import ConnectHandler
# vxr = ConnectHandler(host="192.168.32.161",username="ahmed",password="dev_2024",device_type="cisco_ios")
# vxr.enable()
# vxr.send_command_timing("conf t")
# vxr.send_command_timing("show ip int br")
# vxr._send_command_str()
# show = vxr.send_command_timing("show ip route")
# print(show)

