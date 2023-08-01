# PyFDbg
```
 ____        _____ ____  _
|  _ \ _   _|  ___|  _ \| |__   __ _
| |_) | | | | |_  | | | | '_ \ / _` |
|  __/| |_| |  _| | |_| | |_) | (_| |
|_|    \__, |_|   |____/|_.__/ \__, |
       |___/                   |___/
```
### *一个简单且强大、易于使用的调试器*
### 本项目由Python3.11环境下编写，资源在该环境下编译
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](http://choosealicense.com/licenses/mit/)
### 本项目说明文档暂时仅支持中文

# 项目链接
[Github](https://github.com/DashBing/pyfdbg/ "Github") | [Pypi](https://pypi.org/project/pyfdbg/ "Pypi")
<br><br>
[Kgithub](https://kgithub.com/DashBing/pyfdbg/)：国内Github镜像站，可能会有延迟，推送请使用Github链接推送

# 版本
## 稳定版本
+ 暂无

## 最新正式版本
+ 暂无

## 最新版本
### *(master分支下数据不准确, 具体查看dev分支)*
+ v0.0.1-alpha1

# 使用


# 从源码构建
## 准备工作
+ 安装git和make (方法自行百度)
+ 安装Python(3.9版本或者3.11版本皆可)
+ 从源码仓库克隆源代码
```
git clone git@github.com:DashBing/phap.git
```
#### 或者
```
git clone https://github.com/DashBing/phap.git
```
### 国内网比较差可以尝试：
```
git clone https://kgithub.com/DashBing/phap.git
```

## 初始化打包环境
```
make init
```
#### 或者
#### 尝试手动安装以下包:
+ build
+ twine
#### 以下是在Windows环境下的示例命令行:
```
python -m pip install build
python -m pip install twine
```

## 构建包
```
make build
```

## 上传包
```
make up-pypi
```
