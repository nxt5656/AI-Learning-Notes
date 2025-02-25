# 学习环境的搭建

## 一. 使用Docker
为什么要搞这么复杂,还要搞个docker出来?
说明: 主要是为自己电脑环境的纯洁性考虑,自己学习的东西越多,有很多软件/工具或其它东西依赖的东西,都会对不同版本有交叉依赖,导致排查问题比较复杂,所以建议使用docker来搭建学习环境

过程:
1. 安装 Docker
2. 通过 Dockerfile构建自己的学习环境镜像
3. 通过自己的镜像启动自己的学习环境容器
4. 通过 Chrome或 Pycharm访问 JupyterLab

### 1.1 安装Docker
[如何安装](.安装Docker.md)
### 1.2 通过 Dockerfile构建自己的学习环境镜像
注意: 可以不构建自己的镜像,直接使用现成镜像
[构建学习环境镜像](.构建学习环境镜像.md)
### 1.3 启动学习环境容器

```shell
docker run -d -p 8080:8888 -p 8022:22 ghcr.io/nxt5656/ai-learning-notes:latest
```
### 1.4 访问学习环境
1. 通过chrome访问
```shell
http://127.0.0.1:8080
密码是: UserPas$0w
```

## 二. 直接在本机上开发
说明:
过程:
1. 安装Python
2. 安装MiniConda
3. 创建并激活虚拟环境
4. 安装并启动 JupyterLab
5. 通过 Chrome或 Pycharm访问 JupyterLab

