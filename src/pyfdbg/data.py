author = "DashBing(大师)"
copyright = "%s 保留所有权利"%author
version_class = "Alpha"
resource_code = "1"
version_code = "0.0.1"
project_name = "PyFDbg"
if version_class == "GM":
    version = "v%s %s"%(version_code,version_class)
    version_in = version_code
else:
    version = "v%s %s%s"%(version_code,version_class,resource_code)
    version_in = version_code + version_class[0].lower()

def_compler = "g++"

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

help_msg = ''''''

if __name__ == "__main__":
    print(copyr_msg.format(version=version, copyright=copyright))
