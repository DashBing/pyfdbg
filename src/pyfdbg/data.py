author = "DashBing(大师)"
copyright = "(c) %s 保留所有权利"%author
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

   ____        _____ ____  _
  |  _ \ _   _|  ___|  _ \| |__   __ _
  | |_) | | | | |_  | | | | '_ \ / _` |
  |  __/| |_| |  _| | |_| | |_) | (_| |
  |_|    \__, |_|   |____/|_.__/ \__, |
         |___/                   |___/
                                         {version}
                                Copyright {copyright}
'''
