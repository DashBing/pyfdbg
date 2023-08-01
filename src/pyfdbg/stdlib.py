def cut_args(argv, cmd_begin = ["-", "--", "/"], max_begin_long = 2, self_tip = "@self", notiparg_tip = "@noname"):
    d = {}
    d = d | {self_tip : argv[0], notiparg_tip:[]}
    del argv[0]
    i = 0
    while i < len(argv):
        s = ""
        t = False
        for j in range(len(cmd_begin)):
            if j in argv[i][0:max_begin_long:]:
                s = j
                t = True
        tmp = argv[i]
        if t:
            tmp = s.join(tmp.split(s))
            try:
                d = d | {tmp:argv[i+1]}
            except:
                d[tmp] = argv[i+1]
            i += 1
        else:
            d[notiparg_tip] = d[notiparg_tip] + [argv[i]]
        i += 1
    return(d)
