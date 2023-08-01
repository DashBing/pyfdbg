from sys import argv
from .stdlib import cut_args
from .data import copyr_msg, version, copyright, help_msg

def debuger(argv, dbgarg):
    pass

def shell():
    pass

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
    elif len(argv["@noname"]) > 0:
        debuger(argv, dbgarg)
    else:
        shell()

if __name__ == "__main__":
    main(argv)
