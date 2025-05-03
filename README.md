# Docker Flask Nginx 示例项目

这是一个使用 Docker 部署 Flask 应用并通过 Nginx 反向代理的示例项目。该项目展示了如何使用 Docker Compose 来编排多个容器服务。

## 项目结构

```
.
├── app.py              # Flask 应用主文件
├── requirements.txt    # Python 依赖文件
├── Dockerfile         # Flask 应用的 Dockerfile
├── nginx.conf         # Nginx 配置文件
├── nginx.Dockerfile   # Nginx 的 Dockerfile
├── docker-compose.yml # Docker Compose 配置文件
└── .dockerignore      # Docker 构建忽略文件
```

## 功能特点

- Flask Web 应用服务
- Nginx 反向代理
- Docker 容器化部署
- Docker Compose 服务编排

## 快速开始

### 前提条件

- 安装 [Docker](https://www.docker.com/get-started)
- 安装 [Docker Compose](https://docs.docker.com/compose/install/)

### 构建和运行

1. 克隆仓库：
```bash
git clone https://github.com/zhang-zimin/docker.git
cd docker
```

2. 构建并启动服务：
```bash
docker-compose up --build
```

3. 访问应用：
打开浏览器访问 http://localhost

### 停止服务

```bash
docker-compose down
```

## 服务说明

### Flask 应用
- 运行在 5000 端口
- 提供基本的 Web 服务
- 通过 Nginx 反向代理访问

### Nginx
- 运行在 80 端口
- 作为反向代理服务器
- 处理所有外部请求

## 开发说明

### 修改 Flask 应用
1. 编辑 `app.py` 文件
2. 重新构建并启动服务：
```bash
docker-compose up --build
```

### 修改 Nginx 配置
1. 编辑 `nginx.conf` 文件
2. 重新构建并启动服务：
```bash
docker-compose up --build
```

## 环境变量

目前项目没有使用环境变量，如需添加，可以在 `docker-compose.yml` 中配置。

## 贡献指南

1. Fork 本仓库
2. 创建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个 Pull Request

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情
