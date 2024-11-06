# Matter Stablizer Server

## Run native
Install python first:
1. Switch  to root
```bash
su root
```
2. Install python
```bash
apt update && apt install python3 python3-pip
```
3. Run the server:
```bash
export VARIABLE_NAME=192.168.100.XXX && pip3 install -r requirements.txt && python3 main.py
```
Replace XXX with your specific ip

## Run with docker
```bash
docker run -d --name matter-stabiliser-server -p 2101:2101 -e VM_IP=192.168.100.XXX jzeladmin2006/m321-matter-stabiliser-server
```
Replace XXX with your specific ip
