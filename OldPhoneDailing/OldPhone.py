def convert_nums_to_chars(a):
    #initialise the possible inputs and ouputs
    try:
        letters=(' ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
        numbers=('1','2', '22', '222', '3', '33', '333', '4', '44', '444', '5', '55', '555', '6', '66', '666', '7', '77', '777', '7777', '8', '88', '888', '9', '99', '999', '9999')
        send_to_user=""
        
        ziplist = dict(zip(numbers,letters))
        
        for i in a.split():
            send_to_user+=str(ziplist.get(i))
            
        return send_to_user
    
    except:
        return "ERROR"

def convert_chars_to_nums(a):
    try:
        #initialise the possible inputs and ouputs
        letters=(' ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
        numbers=('1','2', '22', '222', '3', '33', '333', '4', '44', '444', '5', '55', '555', '6', '66', '666', '7', '77', '777', '7777', '8', '88', '888', '9', '99', '999', '9999')
        send_to_user=""
        
        ziplist = dict(zip(letters,numbers))
        prepare=[]
        
        for i in a.split():
            for j in i:
                prepare.append(j)
            prepare.append(" ")
        
        for i in prepare:
            send_to_user+=ziplist.get(i)
            send_to_user+=" "
        
        return send_to_user[:-2]
    
    except:
        return "ERROR"

    
    
# if __name__ == "__main__":
#     main()