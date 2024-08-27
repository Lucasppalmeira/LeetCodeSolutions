def drawTriangle(num):
    cont = 0
    output = ""

    while(cont < num):
        print(f"{output}" + "*")
        output += "*"
        cont += 1

drawTriangle(6)