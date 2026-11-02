Filename = input("File name? ")
match Filename:
    case Filename.endswith(".gif"):
        print("image/gif")
    case Filename.endswith(".jpg") | Filename.endswith(".jpeg"):
        print("image/jpeg")  
    case Filename.endswith(".png"):
        print("image/png")
    case Filename.endswith(".pdf"):
        print("application/pdf")    
    case Filename.endswith(".txt"):
        print("text/plain")
    case Filename.endswith(".zip"):
        print("application/zip")
    case _:                       
        print("application/octet-stream")
