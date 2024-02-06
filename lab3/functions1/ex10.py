def unique(list):
    now = []
    for i in list:
        if i not in now:
            now.append(i)
    return now