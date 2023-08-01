from sys import argv
from .stdlib import cut_args
from .data import copyr_msg, version, copyright, help_msg

def debuger(argv):
    pass

def shell(argv):
    pass

def main(argv):
    print(copyr_msg.format(version=version, copyright=copyright))
    argv = cut_args(argv)
    if "help" in argv or "h" in argv:
        print(help_msg)
    elif len(argv["@noname"]) > 0:
        debuger(argv)
    else:
        shell(argv)

if __name__ == "__main__":
    main(argv)
