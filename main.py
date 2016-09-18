from subprocess import call
import paramiko
from scp import SCPClient

ssh = SSHClient()
#ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
for byte_3rd in range([5:7]):
  for byte_4th in range([2:255]):
    #ssh.connect('ip','port','user','pass')
    ssh.connect('10.11.{}.{}','22','student','studnet').format(byte_3rd,byte_4th)
    
    #scp.put('test.txt', 'test2.txt')
    #scp.get('test2.txt')
    scp.close()

# SCPCLient takes a paramiko transport as its only argument
scp = SCPClient(ssh.get_transport())
