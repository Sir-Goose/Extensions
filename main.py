fileName = input("File name: ")
fileName = fileName.strip()
length = len(fileName)

first = fileName[(length - 3)]
second = fileName[(length - 2)]
third = fileName[(length - 1)]

extension = (first + second + third)
extension = extension.lower()

if extension == "gif":
    print("image/gif")
elif extension == "jpg":
    print("image/jpeg")
elif extension == "png":
    print("image/png")
elif extension == "txt":
    print("text/plain")
elif extension == "pdf":
    print("application/pdf")
elif extension == "zip":
    print("application/zip")
else:
    print("application/octet-stream")


