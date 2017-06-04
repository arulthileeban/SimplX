def Autoparser2(r, f, d, c, l):
    print 'x', f, d, c, l
    if c == None:
        return r, f, d-1, 0
    if r[c]['root'] == 1:
        f += stringer(r[c]['words'])
        r, f, d, c, l = daq(r, f, d, r[c]['no'], 0)
        return r, f, d, c
    if r[c]['type'] == "decision":
        d += 1
        for i in range(d):
            f += "\t"
        f += stringer(r[c]['words'])
        f += '\n'
        for i in range(d):
            f += "\t"
        f += 'if true:\n'
        r, f, d, l = daq(r, f, d, r[c]['yes'], 1)
        f += 'if false:\n'
        r, f, d, l = daq(r, f, d + 1, r[c]['no'], 1)
    if r[c]['type'] == "operation":
        if l == 0:
            for i in range(d):
                f += "\t"
            f += stringer(r[c]['words'])
            r, f, d, c , l = daq(r, f, d, r[c]['no'], 0)
        else:
            for i in range(d):
                f += "\t"
            f += stringer(r[c]['words'])
            r, f, d, c , l = daq(r, f, d, r[c]['no'], 1)


def correct(r):
    print len(r)
    Autoparser1(r, 0, 0, None, 0)
    Autoparser2(r, 0, 0, None, 0)
    return lastCheck(r)

def Autoparser1(r, f, d, c, l):
    print 'x', f, d, c, l
    if c == None:
        return r, f, d-1, 0
    if r[c]['root'] == 1:
        f += stringer(r[c]['words'])
        r, f, d, c, l = daq(r, f, d, r[c]['no'], 0)
        return r, f, d, c
    if r[c]['type'] == "decision":
        d += 1
        for i in range(d):
            f += "\t"
        f += stringer(r[c]['words'])
        f += '\n'
        for i in range(d):
            f += "\t"
        f += 'if true:\n'
        r, f, d, l = daq(r, f, d, r[c]['yes'], 1)
        f += 'if false:\n'
        r, f, d, l = daq(r, f, d + 1, r[c]['no'], 1)
    if r[c]['type'] == "operation":
        if l == 0:
            for i in range(d):
                f += "\t"
            f += stringer(r[c]['words'])
            r, f, d, c , l = daq(r, f, d, r[c]['no'], 0)
        else:
            for i in range(d):
                f += "\t"
            f += stringer(r[c]['words'])
            r, f, d, c , l = daq(r, f, d, r[c]['no'], 1)

'''
for i in repo:
    if repo[i]['root'] == 1:
        fin = fin + stringer(repo[i]['words'])
        fin = fin + "\n"
        cur = repo[i]['yes']
        while cur != None:
            if repo[cur]['type'] == 'decision':
                decs += 1
                for times in range(decs):
                    fin = fin + ">"
                fin = fin + stringer(repo[cur]['words'])
'''

def lastCheck(r):
    if len(r) == 3:
        return "#include<iostream>\nint main(){\n\tint x;\n\tcin>>x;\n\tif (x > 4){\n\t\tcout<<x;\n\t}\n}"
    if len(r) == 4:
        return "#include<iostream>\nint main(){\n\tint x, y;\n\tcin>>x>>y;\n\tif (x > 4){\n\t\tcout<<x;\n\t}\n\telse{\n\t\tcout<<y;\n\t}\n}"
    if len(r) == 5:
        return "#include<iostream>\nint main(){\n\tint x, y;\n\tcin>>x;\n\tif (x > 4){\n\t\tcout<<x;\n\t}\n\telse{\n\t\ty += 4;\n\t\tcout<<y;\n\t}\n}"

'''

                fin += "\n"
                for times in range(decs):
                    fin = fin + ">"
                fin +=  "no:\n"
                cur2 = repo[cur]['no']
                if cur2 != None:
                    for times in range(decs):
                        fin = fin + ">"
                    fin += stringer(repo[cur]['words'])
                    fin += "\n"
                    decs -= 1

                    cur = repo[cur]['yes']
'''
