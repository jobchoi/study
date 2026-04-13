# p.163
# ipaddress_interfaces.py

import ipaddress

ADDRESS = [
    '10.9.0.6/24',
    'fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa/64',
]

for ip in ADDRESS:
    iface = ipaddress.ip_interface(ip)  # 인터페이스 주소
    print('{!r}'.format(iface))
    print('Network : \n',iface.network) # 네트워크 주소
    print('ip:\n',iface.ip) # host주소
    print('Ip with prefixlen:\n',iface.with_prefixlen) # CIDR표기
    print('netmask:\n',iface.with_netmask) # 넷마스크
    print('hostmask:\n',iface.with_hostmask) # 호스트마스크

    print()