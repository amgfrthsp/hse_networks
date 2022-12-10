# Домашнее задание 3
## Топология 
![](src/pics/topology.png)

## Инструкции
### R1
```
enable
configure terminal 
interface e0/0
no shutdown
ip address 10.0.0.1 255.255.255.0
exit
```
### R2
```
enable
conf t

interface e0/0
no shutdown
interface e0/0.10
encapsulation dot1q 10   
ip address 10.0.10.1 255.255.255.0
exit
interface e0/0.20
encapsulation dot1q 20   
ip address 10.0.20.1 255.255.255.0
exit
do write

ip dhcp pool VLAN10POOL
network 10.0.10.0 255.255.255.0
default-router 10.0.10.1
dns-server 8.8.8.8
exit
ip dhcp excluded-address 10.0.10.1 10.0.10.10

ip dhcp pool VLAN20POOL
network 10.0.20.0 255.255.255.0
default-router 10.0.20.1
dns-server 8.8.8.8
exit
ip dhcp excluded-address 10.0.20.1 10.0.20.10

interface e0/0
ip nat inside
exit
interface e0/0.10
ip nat inside
exit
interface e0/0.20
ip nat inside
exit
interface e0/1
ip address 10.0.0.5 255.255.255.0
no shutdown
ip nat outside
exit

ip nat pool POOL 10.0.0.5 10.0.0.255 netmask 255.255.255.0
access-list 10 permit 10.0.10.0 0.0.0.255
access-list 10 permit 10.0.20.0 0.0.0.255
ip nat inside source list 10 pool POOL

exit
```

### S3
```
enable
conf t
vlan 10
vlan 20
exit

spanning-tree vlan 10 root primary
spanning-tree vlan 20 root primary

interface e0/0
switchport trunk allowed vlan 10,20
switchport trunk encapsulation dot1q
switchport mode trunk
exit
interface e0/1
switchport trunk allowed vlan 10,20
switchport trunk encapsulation dot1q
switchport mode trunk
exit
interface e0/2
switchport trunk allowed vlan 10,20
switchport trunk encapsulation dot1q
switchport mode trunk
exit
exit
```
### S4
```
enable
conf t
vlan 10
vlan 20
exit

interface e0/0
switchport trunk allowed vlan 10,20
switchport trunk encapsulation dot1q
switchport mode trunk
exit
interface e0/1
switchport trunk allowed vlan 10,20
switchport trunk encapsulation dot1q
switchport mode trunk
exit
interface e0/2
switch mode access
switch access vlan 10
exit
exit
```
### S5
```
enable
conf t
vlan 10
vlan 20
exit

interface e0/0
switchport trunk allowed vlan 10,20
switchport trunk encapsulation dot1q
switchport mode trunk
exit
interface e0/1
switchport trunk allowed vlan 10,20
switchport trunk encapsulation dot1q
switchport mode trunk
exit
interface e0/2
switch mode access
switch access vlan 20
exit
exit
```

### VPC6
```
ip dhcp
```
![](src/pics/v1.png)
![](src/pics/ip1.png)

### VPC7
```
ip dhcp
```
![](src/pics/v2.png)
![](src/pics/ip2.png)

## Работоспособность

С одного клиента к другому и обратно:

![](src/pics/ping1.png)
![](src/pics/ping2.png)

Работа роутера, DHCP и NAT:

![](src/pics/trans.png)
