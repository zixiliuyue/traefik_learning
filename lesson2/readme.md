## 概述 二进制启动 

https://doc.traefik.io/traefik/providers/file/#filename

```shell
https://github.com/traefik/traefik/releases/tag/v2.9.8
```

## 后台运行

```
./traefik -d
```

## 前台运行
```shell
./traefik --configFile=./file_providers/traefik.yml
python3 py_demo_api.py
python3 py_demo_host.py

curl http://10.21.248.211/foo

curl http://example.com/host
```