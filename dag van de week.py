from sys import base_exec_prefix


maandag = "Maandag"
dinsdag = "Dinsdag"
woensdag="Woensdag"
donderdag="Donderdag"
vrijdag="Vrijdag"
zaterdag="Zaterdag"
zondag="Zondag"
dag = input("welke dag wilt u zien?")

while dag == "maandag":
    print (maandag)
    break
if dag == "dinsdag":
    print(maandag,dinsdag)
elif dag == "woensdag":
    print(maandag,'',dinsdag,'',woensdag)
elif dag == "donderdag":
    print(maandag,'',dinsdag,'',woensdag,'',donderdag)
elif dag == "vrijdag":
    print(maandag,'',dinsdag,'',woensdag,'',donderdag,'',vrijdag)
elif dag == "zaterdag":
    print(maandag,'',dinsdag,'',woensdag,'',donderdag,'',vrijdag,'',zaterdag)
elif dag == "zondag":
    print(maandag,'',dinsdag,'',woensdag,'',donderdag,'',vrijdag,'',zaterdag,'',zondag)

