### traefik 学习


[docker-compose 快速开始](./lesson1/)

[lesson2 二进制文件启动,负载到2个自定义服务](./lesson2/)

[lesson3 负载到容器进程](./lesson3/)

[traefik-simple 简单配置](./traefik-simple/)

### Routers Services Providers Middlewares


Routers
在Traefik中，Routers是将传入的请求路由到正确的服务的机制。Routers可以根据请求的主机名、路径、请求头、请求方法等进行匹配，并将请求转发到相应的Service。以下是Routers的定义和一个示例：

定义
Routers定义了如何将传入的请求路由到正确的Service。每个Router都具有一个唯一的名称和一个或多个入口点。入口点可以是HTTP请求的主机名、路径、请求头、请求方法等。

示例
Router示例，它将所有到example.com的HTTP请求路由到名为example的Service：
```code
http:
  routers:
    my-router:
      rule: "Host(`example.com`)"
      service: "example"
```

### Services


在Traefik中，Services是实际处理请求的后端应用程序。Services可以是容器、Kubernetes Pod、虚拟机等。Traefik支持多种类型的Service，例如HTTP、TCP、UDP、gRPC等。以下是Services的定义和一个示例：

定义
Services定义了后端应用程序的地址和端口，并定义了如何将请求传递给该应用程序。每个Service都具有一个唯一的名称和一个或多个后端地址。

示例
以下是一个基本的HTTP Service示例，它将所有请求传递到名为my-app的HTTP服务：
```code
http:
  services:
    my-app:
      loadBalancer:
        servers:
        - url: "http://my-app:8080"
```

### Providers


在Traefik中，Providers是用于动态配置Traefik的插件。Traefik支持多种Providers，包括Docker、Kubernetes、Mesos、Consul、ZooKeeper等。以下是Providers的定义和一个示例：

定义
Providers定义了Traefik可以使用的外部源，以获取动态路由和负载平衡信息。每个Provider都具有一个唯一的名称和一个或多个配置参数。

示例
以下是一个基本的Docker Provider示例，它从本地Docker守护程序获取容器信息，并自动为这些容器配置路由规则和负载平衡：
```code
providers:
  docker:
    endpoint: "unix:///var/run/docker.sock"
```

### Middlewares



在Traefik中，Middlewares是一种在请求处理过程中添加逻辑的机制。Middlewares可以用于添加安全性、日志记录、重定向、认证等功能。以下是Middlewares的定义和一个示例：

定义
Middlewares定义了请求处理过程中要执行的逻辑。每个Middleware都具有一个唯一的名称和一个或多个配置参数。

示例
以下是一个基本的Redirect Middleware示例，它将所有HTTP请求重定向到HTTPS：
```code
http:
  middlewares:
    my-middleware:
      basicAuth:
        users:
          - "username:password"
    rate-limit:
      rateLimit:
        average: 100
        burst: 200
        period: 10s
  routers:
    my-router:
      rule: "Host(`example.com`) && Path(`/api`)"
      middlewares:
        - my-middleware
        - rate-limit
      service: my-service
      entryPoints:
        - web
```

```code
http:
  routers:
    my-router:
      rule: "Host(`example.com`) && Path(`/api`)"
      service: my-service
      entryPoints:
        - web
        - secure
  services:
    my-service:
      loadBalancer:
        servers:
          - url: "http://localhost:8080"
  entryPoints:
    web:
      address: ":80"
    secure:
      address: ":443"
```

在上述示例中，Traefik定义了两个入口点，一个是web，另一个是secure。然后，在名为my-router的路由器中，entryPoints属性被定义为web和secure，表示该路由器将使用这两个入口点。最后，Traefik定义了一个名为my-service的服务，它将负责将流量路由到后端服务器。

### 其他

Global Configuration
全局配置包括Traefik的基本设置，如日志记录级别、入口点、TLS配置等。以下是全局配置的定义和一个示例：

定义
Global Configuration定义了Traefik的全局设置。每个Global Configuration都具有一个唯一的名称和一些基本设置，如日志记录级别、入口点、TLS配置等。

示例
以下是一个基本的Global Configuration示例，它定义了Traefik的日志记录级别、入口点和TLS配置：

```code
global:
  log:
    level: "DEBUG"

  entryPoints:
    web:
      address: ":80"

  tls:
    certificates:
      - certFile: "/path/to/cert.pem"
        keyFile: "/path/to/key.pem"
```

#### TLS


在Traefik中，TLS用于配置HTTPS。TLS证书用于验证服务器身份，并加密数据传输。以下是TLS配置的定义和一个示例：

定义
TLS定义了Traefik使用的HTTPS配置。每个TLS配置都具有一个唯一的名称和一个或多个证书配置。

示例
以下是一个基本的TLS配置示例，它定义了Traefik使用的HTTPS证书和私钥：

```code
tls:
  certificates:
    - certFile: "/path/to/cert.pem"
      keyFile: "/path/to/key.pem"

```

#### Access Logging


在Traefik中，Access Logging用于记录请求和响应的详细信息。这些日志可以用于监控、故障排除和性能优化等目的。以下是Access Logging的定义和一个示例：

定义
Access Logging定义了Traefik如何记录请求和响应的详细信息。每个Access Logging都具有一个唯一的名称和一些配置参数，如日志格式、输出位置等。

示例
以下是一个基本的Access Logging示例，它将请求和响应的详细信息记录到指定的文件中：

```code
accessLog:
  filePath: "/path/to/access.log"

```

#### Tracing


在Traefik中，Tracing用于跟踪请求的流经和处理过程。Tracing可以用于诊断问题和优化性能。以下是Tracing的定义和一个示例：

定义
Tracing定义了Traefik如何跟踪请求的流经和处理过程。每个Tracing都具有一个唯一的名称和一些配置参数，如跟踪工具、采样率等。

示例
以下是一个基本的Tracing示例，它使用Jaeger跟踪请求的流经和处理过程：

```code
tracing:
  serviceName: "my-service"
  provider: "jaeger"
  jaeger:
    endpoint: "http://jaeger:14268/api/traces"

```