# Домашняя работа 1

## Топология

![](src/pics/topology.png?raw=true "")

## Инструкции

### VPC4
```
ip 10.0.10.1/24 10.0.10.2
```

### VPC5
```
ip 10.0.20.1/24 10.0.20.2
```

### R1
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

### R2
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

### R3
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

### R6
```
enable
conf t
interface e0/0
no shutdown
interface e0/0.10
encapsulation dot1q 10   
ip address 10.0.10.2 255.255.255.0
exit
interface e0/0
no shutdown
interface e0/0.20
encapsulation dot1q 20   
ip address 10.0.20.2 255.255.255.0
exit
do write
exit

```

## STP
### R1 (root)

![](src/pics/R1.png?raw=true "")

### R2

![](src/pics/R2.png?raw=true "")

### R3

![](src/pics/R3.png?raw=true "")


## Работоспособность

### От VPC4 к VPC5
![](src/pics/ping1.png?raw=true "")

### От VPC5 к VPC4
![](src/pics/ping2.png?raw=true "")

## Отказоустойчивость

Отключаю **e0/0** на **R1**:

```
enable
configure terminal
interface e0/0
shutdown
exit
exit
```
![](src/pics/shutdown.png?raw=true "")

Системе нужно пару секунд, чтобы восстановиться, затем она снова работает: 

![](src/pics/after_shutdown.png?raw=true "")
