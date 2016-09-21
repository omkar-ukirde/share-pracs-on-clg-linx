# lab_spread
import paramiko
from scp import SCPClient
import threading
ssh = paramiko.SSHClient()
#ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
def connect_to():
  for i in range(5,7):
    for j in range(2,255):
	    try:
		    ip='10.11.'+str(i)+'.'+str(j)
        #ssh.connect('ip','port','user','pass')
		    print "connecting to "+ip
		    ssh.connect(ip,22,'root','fedora')
        # SCPCLient takes a paramiko transport as its only argument
		    scp = SCPClient(ssh.get_transport())
		    scp.put('test2.txt',remote_path='/usr/local/bin')
        #scp.get('test2.txt')
		    print "file transfered to  "+ip
		    scp.close()

	    except:
	      ip='10.11.'+str(i)+'.'+str(j)
        #ssh.connect('ip','port','user','pass')
		    print "connecting to "+ip
		    ssh.connect(ip,22,'student','student')
        # SCPCLient takes a paramiko transport as its only argument
		    scp = SCPClient(ssh.get_transport())
		    scp.put('test2.txt',remote_path='/home/student/')
        #scp.get('test2.txt')
		    print "file transfered to  "+ip
		    scp.close()
		    print "exception raised for "+ip
		  
		  except:
		     ip='10.11.'+str(i)+'.'+str(j)
        #ssh.connect('ip','port','user','pass')
		    print "connecting to "+ip
		    ssh.connect(ip,22,'Student','student')
        # SCPCLient takes a paramiko transport as its only argument
		    scp = SCPClient(ssh.get_transport())
		    scp.put('test2.txt',remote_path='/home/Student/')
        #scp.get('test2.txt')
		    print "file transfered to  "+ip
		    scp.close()
		    print "exception raised for "+ip
		    
		  else:
		     print "Tried with Root \n With student \n With Student"
		     print "exception raised for "+ip
		    

th1 = threading.Thread(target = connection_to)
th2 = threading.Thread(target = connection_to)
th1.start()
th2.start()
