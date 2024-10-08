import mysql.connetor

def view(set_list):
    for i in range(len(set_list)):
        print(i,".",set_list[i])
set_list=["TO create account","TO deposit amount","TO withdrawal", "TO view balance",'TO quit']
view(set_list)
