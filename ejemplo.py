string = "asdasd1"
dic = {'1':"a",2:"b",3:"c"}

def asd(s:str):
    value = ''
    
    for i in string:
        if i in dic.keys():
            value = True
    print(value)

asd(string)