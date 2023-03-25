#!/bin/bash访问https://defillama.com/并抓取usdc价格

# 拉取最新代码
git pull

# 进入项目目录
cd Prompt

# 安装缺失的npm组件
npm install

# 编译项目
npm run build

# 接收open api的key作为输入
read -p "请输入open api的key：" OPEN_API_KEY

# 启动项目
cd build
OPEN_API_KEY=$OPEN_API_KEY npm start