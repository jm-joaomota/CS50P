#Ask user for a file name
file = input("File Name: ").lower().strip().split(".")

application = ["zip", "pdf"]
image = ["png", "gif", "jpeg", "jpg", "png"]
text = ["txt"]

if file[-1] in text:
    print("text/plain")
elif file[-1] in application:
    print(f"application/{file[-1]}")
elif file[-1] in image:
    print(f"image/{file[-1]}")
else:
    print("application/octet-stream")

