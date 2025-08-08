# 1. 准备工作(Ubuntu Web服务器)
## 1.1 系统更新

```bash
sudo apt update && sudo apt upgrade -y
```
## 1.2 安装必要工具
```bash
sudo apt install -y git curl wget vim
```

# 2. 安装Docker和Docker Compose
## 2.1 安装Docker
```bash
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io
sudo systemctl start docker
sudo systemctl enable docker
```

## 2.2 安装Docker Compose

```bash
sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.3/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```
## 2.3 验证安装

```bash
docker --version
docker-compose --version
```


# 3. 准备应用代码
## 3.1 创建项目目录

```bash
mkdir -p ~/todo-app/{backend,frontend/templates}
cd ~/todo-app
```

## 3.2 后端配置 (backend/app.py)

## 3.3 前端配置 (frontend/app.py)

## 3.4 创建Dockerfile和requirements文件
后端Dockerfile (backend/Dockerfile)
后端依赖 (backend/requirements.txt)
前端依赖 (frontend/requirements.txt)
前端Dockerfile (frontend/Dockerfile)

## 3.5 前端模板 (frontend/templates/index.html)

# 4. Docker Compose配置
创建 docker-compose.yml 文件：

# 5. 部署和运行
##5.1 构建和启动服务

```bash
docker-compose up -d --build
```

