import re
ui=True
while(ui):
    print("Want to know how to keep an idiot busy for hours?")
    userinp=input()
    c=re.compile(r"(^y)|(^n)", re.IGNORECASE)
    val=re.search(c,userinp)
    if val==None:
        print("is not a valid yes/no response.")
    elif val.group(1):
        continue;
        
    else:
        print("thanks , have a nice day")
        break;        


