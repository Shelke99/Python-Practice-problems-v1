#use forever loop
while True:
    i_put = input("enter the input:")
    print("command received")
    value = i_put.lower()
    if value == "exit":
        print("goodbye")
        break