import ansible_runner
import yaml

def load_inventory_and_ping():
    # Define the path to the inventory file
    inventory_path = 'hosts.yml'

    # Load inventory
    r = ansible_runner.run(private_data_dir='.', inventory=inventory_path, playbook='hello.yml')

    # Load the inventory YAML file
    with open(inventory_path, 'r') as file:
        inventory = yaml.safe_load(file)

    # Extract group information
    host_to_group = {}
    for group, hosts in inventory.items():
        if group == 'all':
            continue
        for host in hosts['hosts']:
            host_to_group[host] = group

    # Print names, IP addresses, and group names of all hosts
    for event in r.events:
        if event['event'] == 'runner_on_ok':
            host = event['event_data']['host']
            group = host_to_group.get(host, 'Unknown')
            print(f"Name: {host}, IP: {event['stdout']}, Group: {group}")

    # Output ping results
    print("\nPing Results:")
    for event in r.events:
        if event['event'] == 'runner_on_ok':
            host = event['event_data']['host']
            if 'stdout_lines' in event:
                print(f"{host}: {event['stdout_lines']}")
            else:
                print(f"{host}: No output available")

if __name__ == "__main__":
    load_inventory_and_ping()
