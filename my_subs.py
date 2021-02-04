def find_subs(s, subs):

    for i in range(len(s) - len(subs) + 1):
        c = 0
        for j in range(len(subs)):
            if subs[j] != s[i + j]:
                break
            else:
                c += 1
        if c == len(subs):
            return i
    return -1

