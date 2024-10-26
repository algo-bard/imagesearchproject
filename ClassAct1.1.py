
# Write an algorithm that calculates the price that a customer will pay for a bag of oranges, given the price per kilo and the weight of the bag.
individualorangeweight = 0.150
priceperkilo = 20

print("Welcome to the Orange Section of the Supermarket")
print("The price per kilo of orange is " + " 20 pesos")
selectnumber = str(input("How 4much oranges do you want?"))


finalweight = selectnumber * individualorangeweight
finalprice = priceperkilo*finalweight
print("Your total is " + finalprice)
