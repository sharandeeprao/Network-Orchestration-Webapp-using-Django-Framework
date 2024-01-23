import yaml
from Networkwireapp.anisbleplaybookexec import execplaybook
def ansibleplaybookupdate(command,device):
    yaml_file_path = "/home/sharan-rao/NetworkOrchestrationProject/ansible_playbooks_dir/sh_ip_int_br_playbook.yml"

    with open(yaml_file_path, "r") as yaml_file:
        yaml_data = yaml.load(yaml_file, Loader=yaml.FullLoader)
        # print(yaml_data)
        print(yaml_data[0]['tasks'][0]['raw'])
        yaml_data[0]['tasks'][0]['raw'] = command
        # print(yaml_data)
        yaml_file.close()
    with open(yaml_file_path, "w") as yaml_file:
        yaml.dump(yaml_data, yaml_file, default_flow_style=False)
        yaml_file.close()
    data=execplaybook(device)
    return data
    