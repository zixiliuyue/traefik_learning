## 概述 docker-compose 启动服务

## 启动全部服务
```json
docker-compose up -d
```
## 启动部分服务
```json
docker-compose up -d reverse-proxy
docker-compose up -d whoami
```
## 扩容
```code
docker-compose up -d --scale whoami=2

curl -H Host:whoami.docker.localhost http://10.21.248.211:891

Hostname: c7de1119e9a6
IP: 127.0.0.1
IP: 172.21.0.4
RemoteAddr: 172.21.0.2:49372
GET / HTTP/1.1
Host: whoami.docker.localhost
User-Agent: curl/7.29.0
Accept: */*
Accept-Encoding: gzip
X-Forwarded-For: 10.21.248.211
X-Forwarded-Host: whoami.docker.localhost
X-Forwarded-Port: 80
X-Forwarded-Proto: http
X-Forwarded-Server: 187cc35bc134
X-Real-Ip: 10.21.248.211

curl -H Host:whoami.docker.localhost http://10.21.248.211:891
Hostname: 6220ac349b37
IP: 127.0.0.1
IP: 172.21.0.3
RemoteAddr: 172.21.0.2:51650
GET / HTTP/1.1
Host: whoami.docker.localhost
User-Agent: curl/7.29.0
Accept: */*
Accept-Encoding: gzip
X-Forwarded-For: 10.21.248.211
X-Forwarded-Host: whoami.docker.localhost
X-Forwarded-Port: 80
X-Forwarded-Proto: http
X-Forwarded-Server: 187cc35bc134
X-Real-Ip: 10.21.248.211
```