from sys import argv, platform
from os import system as cmd
from time import time as gettime
from .stdlib import cut_args
from .data import copyr_msg, version, copyright, help_msg, def_compler, def_tmp, noname, benchmark

def debuger(argv, dbgarg=""):
    cpl = def_compler
    if "c" in argv or "compiler" in argv:
        if "c" in argv:
            cpl = argv["c"]
        else:
            cpl = argv["compiler"]
    tmp = def_tmp
    if "t" in argv or "temp" in argv:
        if "t" in argv:
            tmp = argv["t"]
        else:
            tmp = argv["temp"]
    fn = argv[noname][0]
    if platform.lower() in ["win32", "windows"]:
        tmpl = [cpl, fn, "-o {dirname}/{filename}.exe".format(tmp,fn)]
    else:
        tmpl = [cpl, fn, "-o {dirname}/{filename}".format(tmp,fn)]
    cmd(" ".join(tmpl))
    del tmpl
    if platform.lower() in ["win32", "windows"]:
        time1 = gettime()
        cmd("./{filename}.exe {args}".format(fn, dbgarg))
    else:
        time1 = gettime()
        cmd("./{filename} {args}".format(fn, dbgarg))
    time2 = gettime()
    print("\n")
    print(benchmark%(time2 - time1))


def shell():
    lc = "\033[1;33m%s\033[0m"
    fn = input(lc%"Q: 请输入要调试的文件名 ?.>")
    cpl = input(lc%"Q: 请输入编译器名(文件位置) 默认则填“@n” ?.>")
    tmp = input(lc%"Q: 请输入临时文件夹名 默认则填“@n” ?.>")
    args = input(lc%"Q: 请输入参数命令行 无则填“@n” ?.>")
    print()
    d = {noname:[fn]}
    if cpl.lower() != "@n":
        d = d | {"c":cpl}
    if tmp.lower() != "@n":
        d = d | {"t":tmp}
    if args.lower() != "@n":
        arg = args
    else:
        arg = ""
    del args
    debuger(d, arg)

def main(argv):
    print(copyr_msg.format(version=version, copyright=copyright))
    v = argv
    v = " ".join(argv)
    v = v.split("-a")
    del v[0]
    v = "-a".join(v)
    dbgarg = v
    del v
    f = False
    for i in range(len(argv)):
        if argv[i].lower() == "-a":
            f = True
            del argv[i]
        if f:
            del argv[i]
    del f
    argv = cut_args(argv)
    if ("help" in argv or "h" in argv) or ("HELP" in argv or "H" in argv):
        print(help_msg)
    elif len(argv[noname]) > 0:
        debuger(argv, dbgarg)
    else:
        shell()

if __name__ == "__main__":
    main(argv)
