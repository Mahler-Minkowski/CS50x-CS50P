Amount_Due=50
insert_money= 0
while insert_money < 50 and Amount_Due >0:
    Money=int(input("toss money"))
    if Money == 5  or Money == 10 or Money == 25:
        Amount_Due= Amount_Due - Money
        insert_money= insert_money + Money
        print(Amount_Due)
if insert_money >= 50 and Amount_Due <=0:
    change_owed=insert_money-50
    print("change_owed "+str(change_owed))


