file=input("FileName: ").strip().lower().split(".")
filetypes = {"jpg":"image/jpeg",
           "jpeg": "image/jpeg",
           "gif": "image/gif",
           "png": "image/png",
           "pdf": "application/pdf",
           "txt": "text/plain",
           "zip": "application/zip"
}
print(filetypes.get(file[-1],"application/octet-stream"))

