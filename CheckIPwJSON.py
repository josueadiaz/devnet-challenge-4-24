import json
import ipaddress

deviceJSON = '{"Version": "15.6", "locationN": "500 Northridge", "role": "Access", "upTime": "12:10:53.49", "hostname": "ATL-3650-1", "macAddress": "39:58:1f:9e:38:c1", "series": "Cisco Catalyst 3650 Series Switches", "lastUpdated": "2017-09-21 13:12:46", "bootDateTime": "2016-10-27 05:24:53", "interfaceCount": "24", "lineCardCount": "1", "managementIpAddress": "192.168.10.10", "interfaces": {"interface": [{"GigabitEthernet0": {"ipv4": "100.100.100.1"}}, {"GigabitEthernet1": {"ipv4": "10.10.10.2"}}]}}'

if __name__ == '__main__':
    # print(f'The Python data format for the "deviceJSON" variable is {type(deviceJSON)}')
    # print()
    # print(deviceJSON)

    data = json.loads(deviceJSON)

    for interfaces in data['interfaces']['interface']:
        for int_name, int_address in interfaces.items():
            try:
                ipaddress.ip_address(int_address['ipv4'])

                if ipaddress.IPv4Address(int_address['ipv4']).is_private:
                    print(f"{int_name} has an IP address of {int_address['ipv4']} and is a Private Address")
                else:
                    print(f"{int_name} has an IP address of {int_address['ipv4']} and is not a Private Address")

            except ValueError:
                print(f"{int_name} has an IP address of {int_address['ipv4']} and is not a Valid IP Address")
