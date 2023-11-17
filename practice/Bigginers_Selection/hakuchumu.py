def is_correct(S,T):
    T = ""
    S.replace("eraser","").replace("erase","").replace("draemer","").replace("dream","")
    if S == T:
        return "YES"
    else:
        return "NO"

print(is_correct("dreameraser",""))
