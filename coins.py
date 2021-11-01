# name of student:Roua Almulhem 
# number of student:9068421
# purpose of program: 
# function of program:
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) #variable.
paid = int(float(input('Paid amount: ')) * 100) #variable.
change = paid - toPay #variable 
betaald = [] # variable die een lijst van wordt gemaakt.
if change > 0: #if change is groter dan 0.
  coinValue = 500 #
  
  while change > 0 and coinValue > 0: #while change and coin value groter is dan 0 dan ga je de onderste code runnen.
    nrCoins = change // coinValue # nrCoins is het uitrekenen van change en coinValue.
    if coinValue > 100 :
     if nrCoins > 0: # if nrCoins groter is dan 0 ga je de onderste code runnen.
      print('return maximal ', nrCoins, ' coins of ', int(coinValue/100), ' euro!' ) #
      nrCoinsReturned = int(input('How many coins of ' + str(int(coinValue/100)) +  ' euro did you return? ')) #
      change -= nrCoinsReturned * coinValue # change - (nrcoinsreturned x coinValue), en dat zou de niuew waarde van change zijn.
      betaald.append("je hebt  {} muntjes van {} Euro coins betaald " .format(nrCoinsReturned, str(int(coinValue/100))))
      # betaald is een leege lijst en .append zou het invullen met de informatie die word ingevul bij de input, en daarna zit er een text en leege haakjes, en daar komt de format te spelen hij gaat wat er ingevuld wordt in nrCoinReturnd in de haakjes plaatsen.
    else :
     if nrCoins > 0: # if nrCoins groter is dan 0, gaat de onderste code runnen.
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cent!' ) #
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cent did you return? ')) #
      change -= nrCoinsReturned * coinValue # change - (nrcoinsreturned x coinValue), en dat zou de niuew waarde van change zijn.
      betaald.append("je hebt  {} muntjes van {} Cent coins betaald " .format(nrCoinsReturned, coinValue))
     # betaald is een leege lijst en .append zou het invullen met de informatie die word ingevul bij de input, en daarna zit er een text en leege haakjes, en daar komt de format te spelen hij gaat wat er ingevuld wordt in nrCoinReturnd in de haakjes plaatsen.
# comment on code below: een combinatie van if en elif en else om het code uit te kunnen reken, bv: if coinValue groter is dan 500 dan is de waarde van coinVlaue is 300
    if coinValue ==500:

      coinValue = 300
    elif coinValue ==300:
      coinValue = 200
    elif coinValue == 200 :
      coinValue = 50 
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0
 

if change > 0: # dus als alle codes word uitgevoerd en er blijft een nummer die groter is dan 0 wordt de onderste code uitgevoerd.
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')
  for x in betaald :
    print(x)
# een for loop om alle info uit het lijst "betaald" te halen en in de terminal netjes uit te printen.