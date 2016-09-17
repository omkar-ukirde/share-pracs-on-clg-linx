from subprocess import call
import paramiko
from scp import SCPClient

ssh = SSHClient()
#ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
def client(ip,)
  ssh.connect('example.com')
  
  scp.put('test.txt', 'test2.txt')
  #scp.get('test2.txt')
  scp.close()

# SCPCLient takes a paramiko transport as its only argument
scp = SCPClient(ssh.get_transport())
