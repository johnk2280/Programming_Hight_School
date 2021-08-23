def find_subs(s, subs):

    for i in range(len(s) - len(subs) + 1):
        for j in range(len(subs)):
            if subs[j] != s[i + j]:
                break
            if j == len(subs) - 1:
                return i
    return -1

