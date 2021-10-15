woord =True
aantal=0
while woord:
    aantal+=1
    vraag = input("zolang je geen quit in type zal het blijven vragen?")
    if vraag != "quit":
        print("probeer t nog een keer")
    
    else :
        print("u heeft",aantal,"keer geprobeerd")
        woord= False

