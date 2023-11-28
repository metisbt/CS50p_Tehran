ex = {"gif" : "image/gif", "jpg" : "image/jpeg", "jpeg" : "image/jpeg", "png" : "image/png", "pdf" : "application/pdf", "txt" : "text/plain", "zip" : "application/zip"}
name = input("File name: ").strip().lower()

if name.rfind(".") != -1:
    i = int(name.rfind(".")) + 1
    flag = name[i:]

    if flag in ex:
        print(ex[flag])
    else:
        print("application/octet-stream")
else:
    print("application/octet-stream")