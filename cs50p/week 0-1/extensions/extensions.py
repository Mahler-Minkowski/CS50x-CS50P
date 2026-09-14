#一个问题：输入abc. 会报错？？并不会 else兜底了
file=input("FileName: ").strip().lower().split(".")
if file[-1]=="gif":
    print("image/gif")
#elif file[-1]=="jpg" or "jpeg":
elif file[-1]=="jpg" or file[-1]=="jpeg":
    print("image/jpeg")
elif file[-1]=="png":
    print("image/png")
elif file[-1]=="pdf":
    print("application/pdf")
elif file[-1]=="txt":
    print("text/plain")
elif file[-1]=="zip":
    print("application/zip")
else:
    print("application/octet-stream")
