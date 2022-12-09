# Домашняя работа 1

## Топология

<img src="https://user-images.githubusercontent.com/80028987/206670524-1bd860b8-eb61-4d15-81cb-efeb760c9d8e.png" width="400">


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

<img src="https://user-images.githubusercontent.com/80028987/206670840-f150a9e0-a6a0-464d-a9c1-5f48b186dd3f.png" width="500">

### R2

<img src="https://user-images.githubusercontent.com/80028987/206671019-c31b9e8f-3619-4fb5-aee6-737d90dde494.png" width="500">

### R3

<img src="https://user-images.githubusercontent.com/80028987/206671112-51e7cab7-f9c0-40bf-b239-1ea6dfe98611.png" width="500">


## Работоспособность

### От VPC4 к VPC5
<img src="https://user-images.githubusercontent.com/80028987/206671238-5c3d3a7d-ca2a-454d-b578-e9c6f684c98a.png" width="700">

### От VPC5 к VPC4
<img src="https://user-images.githubusercontent.com/80028987/206671330-6127e1a2-a448-4acd-a9e7-d79ddad03c32.png" width="700">

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
<img src="https://user-images.githubusercontent.com/80028987/206671419-ed2e12d0-6db4-4e7b-a6b9-594fe9efa98f.png" width="700">

Системе нужно пару секунд, чтобы восстановиться, затем она снова работает: 

<img src="https://user-images.githubusercontent.com/80028987/206671483-0ebbb1a7-72ec-4b60-b5a3-7399128055a7.png" width="700">
