# rmyc-raspi
一个使用树莓派操控RMYC中EP机器人的Python项目

## 一、项目说明

### 文件结构

- **assets** 文件夹  
    * **log** 文件夹  
        存放每次运行留存下来的日志
    * ___skill_config.json___ 文件  
        以**JSON**格式存放 技能键位配置

- **modules** 文件夹
    * **utils** 文件夹  
        - **logger.py** 文件 日志工具

## 二、使用指南

### 创建Python虚拟运行环境
```sh
# 切换到 项目根目录
$ python3 -m venv ./venv
$ source ./venv/bin/Activate
```

### 运行
```sh
# 切换到 项目根目录
$ python3 main.py
```