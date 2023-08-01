author = "DashBing(大师)"
copyright = "%s 保留所有权利"%author
version_class = "Alpha"
resource_code = "1"
version_code = "0.1.0"
project_name = "PyFDbg"
if version_class == "GM":
    version = "v%s %s"%(version_code,version_class)
    version_in = version_code
else:
    version = "v%s %s%s"%(version_code,version_class,resource_code)
    version_in = version_code + version_class[0].lower()

def_compler = "g++"
def_tmp = ".temp"

copyr_msg = '''
\033[1;32m
   ____        _____ ____  _
  |  _ \ _   _|  ___|  _ \| |__   __ _
  | |_) | | | | |_  | | | | '_ \ / _` |
  |  __/| |_| |  _| | |_| | |_) | (_| |
  |_|    \__, |_|   |____/|_.__/ \__, |
         |___/                   |___/
\033[1;31m                                         \033[1;34m{version}\033[1;33m
                                Copyright \033[1;33m(C)\033[1;31m {copyright}\033[0m

'''

help_msg = '''\033[1;33m【帮助页面】\033[0;34m

常见命令：
    -h             用于获取帮助命令
        --help

必须参数：
    <filename> 文件名 (没有引导命令)

可选参数：
    -c <compiler name>                配置编译器  默认为：命令行g++
        --compiler <compiler name>

    -t <temp directory name>           配置临时文件目录  默认为：当前目录下的.temp/文件夹，无则会创建
        --temp <temp directory name>

    -a           如果遇到这个参数，那么后面所有的参数都为调试命令行输入参数

\033[0m'''

if __name__ == "__main__":
    print(copyr_msg.format(version=version, copyright=copyright))
