
def main():
   f=input("Fraction: ")
   f_1=convert(f)
   gauge(f_1)

def convert(farc_1):
    try:
      x, y = farc_1.split("/")
      farc_1=round(int(x)*100/int(y))
      return farc_1
    except (ValueError,ZeroDivisionError):
      print('Check your input')
def gauge(farc_1):
    try:
      if 100>=farc_1>=99:
         return("F")
      elif 0<=farc_1<=1:
         return("E")
      elif 1<farc_1<99:
         return(f"{farc_1}%")
    except (ValueError):
         pass



if __name__ == "__main__":
    main()
