# network address 속성

import ipaddress as ipa

NetAddrs = ['10.9.0.0/24', 'fdfd:87b5:b475:5e3e::/64']

for addr in NetAddrs:
    net = ipa.ip_network(addr)
    print(f'Network address: {net!r}')
    print(f'Is private: {net.is_private}')
    print(f'Broadcast address: {net.broadcast_address}')
    print(f'Compressed: {net.compressed}')
    print(f'Addr with netmask: {net.with_netmask}')
    print(f'Addr with hostmask: {net.with_hostmask}')
    print(f'Num addresses: {net.num_addresses}')
    print()