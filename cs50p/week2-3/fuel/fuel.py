while True:
        farc_1=input("Fraction: ")
        try:
            x, y = farc_1.split("/")
            farc_1=round(int(x)*100/int(y))
            #farc_1=round(int(farc_1[0])*100 / int(farc_1[1]))
            if 100>=farc_1>=99:
               print("F")
            elif 0<=farc_1<=1:
               print("E")
            elif 1<farc_1<99:
               print(f"{farc_1}%")
            else:
                continue
            break
        except (ValueError,ZeroDivisionError):
            print("plz insert the right form")
            pass
