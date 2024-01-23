from .models import InventoryData
import paramiko
import re
def ansibleinventory():
    # Define SSH connection parameters
    hostname = "192.168.1.4"
    port = 22  # Default SSH port
    username = "sharan"
    password = "sharan"  # You can also use key-based authentication

    # Initialize an SSH client
    ssh = paramiko.SSHClient()

    # Automatically add the server's host key (this is insecure for production)
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connect to the remote server
        ssh.connect(hostname, port, username, password)

        # Execute a remote command (e.g., "ls" to list files)
        command = "show cdp entry *"

        stdin, stdout, stderr = ssh.exec_command(command)

        # Read and print the command output
        output = stdout.read().decode()
        
        print("Command Output:")
        print(output)
        devices = re.findall('Device ID: (.*m?)\n',output)
        Ipaddr  = re.findall('IP address: (.*\d?)\n',output)
        # print(devices,Ipaddr)


    except paramiko.AuthenticationException as e:
        print("Authentication failed:", str(e))
    except paramiko.SSHException as e:
        print("SSH connection failed:", str(e))
    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        # Close the SSH connection
        ssh.close()
    
    with open('/home/sharan-rao/NetworkOrchestrationProject/ansible_inventory_dir/inventory.ini','w') as file:
        file.write('[hosts]\n')
        for i in range(len(devices)):
            file.write(f'{devices[i].strip()} ansible_host={Ipaddr[i].strip()} ansible_user=sharan ansible_ssh_pass=sharan\n')
            Invendata=InventoryData(Hostname=devices[i].strip(),IPaddress=Ipaddr[i].strip())
            Invendata.save()

        file.close()
    
    
        