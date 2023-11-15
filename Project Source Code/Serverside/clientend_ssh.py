import getpass
import datetime
import paramiko
import optparse

def getarguments():
    parser = optparse.OptionParser()
    parser.add_option("-t",'--target',dest="target",help="The target network to be scanned")
    (options,arguments)=parser.parse_args()
    if not options.target:
        parser.error("[-] Please enter the target ip range to use , use --help for more help")
    return options

options = getarguments()
# Create a SSH client
ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.load_system_host_keys()
key_pass = getpass.getpass("Enter your key password : ")
key_file = paramiko.RSAKey.from_private_key_file("/.ssh/test", key_pass)
# Connect to the client device
ssh.connect(options.target,
            username='test',
            pkey=key_file,
            allow_agent=False,
            look_for_keys=False,
            port=33556)



# Execute the Python file
stdin, stdout, stderr = ssh.exec_command('python3 scanner.py')

# Get the output of the Python file
output = stdout.read().decode()
print(output)
# Close the SSH connection
stdin.close()
ssh.close()

# Save the output to a file
now = datetime.datetime.now()
file_name = now.strftime("%Y-%m-%d_%H-%M-%S") +"_"+options.target + ".html"
with open(file_name, 'w') as f:
    f.write(output)
