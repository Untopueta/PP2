#ex1
import json

with open('sample-data.json', 'r') as file:
    data = json.load(file)

interface_status = data.get('imdata', [])

print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<10} {:<5}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

for interface in interface_status:
    dn = interface.get('attributes', {}).get('dn', '')
    description = interface.get('attributes', {}).get('descr', '')
    speed = interface.get('attributes', {}).get('speed', 'inherit')
    mtu = interface.get('attributes', {}).get('mtu', '')

    print("{:<50} {:<20} {:<10} {:<5}".format(dn, description, speed, mtu))