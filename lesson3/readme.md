## 概述 docker启动路由

docker-compose up -d

## 配置文件地址

### https://doc.traefik.io/traefik/routing/providers/docker/
```json
curl http://10.21.248.211:8110/ 可以正常访问说明，docker-compose部署成功

然后直接访问 http://example.com:802/ 能够打开和10.21.248.211:8110相同的页面说明路由成功
```