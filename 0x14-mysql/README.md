### 0x14. MySQL
### Installation
```
sudo apt-key add signature.key
sudo sh -c 'echo "deb http://repo.mysql.com/apt/ubuntu bionic mysql-5.7" >> /etc/apt/sources.list.d/mysql.list'
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys B7B3B788A8D3785C
sudo apt-get update
sudo apt-cache policy mysql-server
sudo apt install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*
```

if you have issues on 3

run 

```
sudo ufw disable
```

After installation

run

```
sudo ufw enable
```
