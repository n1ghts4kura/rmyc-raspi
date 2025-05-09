# 系统配置指南

## 零、工具推荐

### SSH客户端

> 可以选择在 *Microsoft Store* 或者 *Github* 下载 ***Windows Terminal***

### VNC客户端

> ***RealVNC***

## 一、系统安装

### 下载镜像

前往树莓派官网下载最新版 ***64-bit*** 桌面镜像

`https://www.raspberrypi.com/software/operating-systems/`

### 烧录镜像

下载镜像烧录工具 **Rufus**

`https://rufus.ie/zh/`

> 建议下载便携版

打开烧录工具

- 选择你要烧录的micro-SD卡设备

- 选择刚刚下载的镜像文件 (.img)

- 点击开始并等待完成

### 首次启动系统

账号: pi

密码: raspberrypi

自行使用外接屏幕(或VNC途径) **在桌面环境下** 进行基础系统配置

---

#### 语言&地区选项 (Languange & Timezone)

选择完成后 **勾选 Use English Language 和 Use US Keyboard**

#### 更新软件 (Update Software)

建议 ***SKIP***

## 二、详细系统配置

### Raspi-Config 工具

```sh
$ sudo raspi-config
```

#### 选中 Interface Options

- I1 SSH
    开

- I3 VNC
    开

- I6 Serial Port
    第一个 *login shell* 关 第二个 开