

def join(*lists,sep='-'):
    if len(lists)==0:
        return None
    result=[]
    for l in lists:
        result+=l
        result+=[sep]
    return result[:-1]



#print(join())