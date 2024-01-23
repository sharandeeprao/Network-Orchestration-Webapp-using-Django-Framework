import subprocess
def execplaybook(device):
    command = f'ansible-playbook -i /home/sharan-rao/NetworkOrchestrationProject/ansible_inventory_dir/inventory.ini /home/sharan-rao/NetworkOrchestrationProject/ansible_playbooks_dir/sh_ip_int_br_playbook.yml --limit {device}'  
    try:
        output = subprocess.check_output(command, shell=True, text=True)
        # print("Command output:")
        print(output)
       
        print(list(output.split('\n')))
        print(type(output))
    except subprocess.CalledProcessError as e:
       print(f"Error: {e}")
    return output