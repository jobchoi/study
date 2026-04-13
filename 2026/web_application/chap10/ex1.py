# 
import binascii
import ipaddress as ipa

# =============== >리스트형 변수 생성 시작
# ip : 192.168.0.5로 설정한 뒤라, 출력결과가 0.5 ip로 나오는 것을 확인할 수 있다
Address = [
    '192.168.0.5',
    '2001:0:9d38:6abd:480:f1f:3f57:fffd'
]
# =============== >리스트형 변수 생성 끝

for ipaddr in Address:
    addr = ipa.ip_address(ipaddr)
    print(f'IP Address: {addr!r}')
    print('IP version:',addr.version)
    print('packed addr:',binascii.hexlify(addr.packed))
    print('Is private:',addr.is_private)
    print()


