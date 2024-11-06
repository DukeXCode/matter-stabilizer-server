# Matter Stablizer Server

## Run native
Install python first:
```bash
sudo apt update && sudo apt install python3 python3-pip
```
Run the server:
```bash
pip3 install -r requirements.txt && python3 main.py
```

## Run with docker
```bash
docker run -d --name matter-stabiliser-server -p 2101:2101 -e VM_IP=192.168.100.XXX jzeladmin2006/m321-matter-stabiliser-server
```
Replace XXX with your specific ip
