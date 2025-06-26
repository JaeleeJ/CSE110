# 05 Prove: Milestone - Adventure Game
# Jaelee

# introduce the game
print("It's shopping time! Let's see if you can get some good deals at the mall.")
store = str(input('Which store would you like to shop at: BATH AND BODY WORKS, PACSUN, or APPLE? '))

# choices for the store
if store.lower() == 'bath and body works':
    print('You enter the store and are blown away by the amazing scented products. There are so many options.')
    # first option: lotion or candles
    option1 = str(input('Do you buy LOTION or CANDLES? '))
    # choice: lotion
    if option1.lower() == 'lotion':
        print('It looks like they have some new fragrances!')
        # second option new or classic
        option2 = str(input('Would you like to purchase a NEW scent or a CLASSIC scent? '))
        # choice: new scent
        if option2 == 'new':
            print('Good thing you chose the new scents, because the sale on these is buy 2 get 1 free! Would')
            print('you like to take advantage of this offer?')
            # third option to take the deal or not
            option3 = str(input('YES or NO? '))
            # choice: yes
            if option3.lower() == 'yes':
                print('Congratulations! You got the best deal at Bath and Body Works!')
            # choice: no
            else:
                print("That's too bad that you didn't take advantage of the amazing promotion going on...")
        # choice: classic scent
        else:
            print("There are so many great classic scents available! Too bad they aren't on sale today. How about")
            print('trying somewhere else for a good deal...')
    # choice: candles
    else:
        print('Candles are a great for you friend and family, especially for this cold winter season! And you')
        print('are lucky that there is a promotion happening now for the candles! If you buy 5 candles, you get')
        print('50% off your order!')
        candles = int(input('How many candles will your purchase? '))
        # how many candles
        if candles >= 5:
            print('Yay! You got a great deal here!')
        else:
            print("You didn't buy enough candles, so you weren't eligible for the discount...")
# choice: pacsun
elif store.lower() == 'pacsun':
    print('You enter the store and are greeted with the new winter clothing line! There are so')
    print('many cozy clothes you could buy!')
    # first option: coat or jeans
    option1 = str(input('Which do you purchase: COAT or JEANS? '))
    # choice: coat
    if option1.lower() == 'coat':
        print('You take a look at a few racks filled with coats that are puffy, fluffy, long, and short. There')
        print('is a sale depending on which kind of coat you buy!') 
        # second option: puffy, fluffy, long, or short coat
        option2 = str(input('Do you choose a PUFFY, FLUFFY, LONG, or SHORT coat? '))
        # choice: fluffy coat
        if option2.lower() == 'fluffy':
            print("Wow you got lucky! Today's sale is fluffy coats so you can dress like a teddy bear. So cute!")
        # choice: puffy, long, or short
        else:
            print("Sorry, these coats aren't discounted today. Maybe try another type?")
    # choice: jeans
    else:
        print('A good pair of jeans is essential for the winer! There are so many different styles and colors.')
        print('All jeans are on sale depending on how many you purchase.')
        jeans = int(input('How many pairs of jeans would you like to buy? '))
        # how many jeans
        if jeans > 1:
            print('Looks like you got the deal! It is buy 1 get 1 50% off. Congratulations!')
        else:
            print('Sorry the promotion is for those who purchase 2 or more pairs of jeans. I hope you found a ')
            print('good pair though...')
# choice: apple store
elif store.lower() == 'apple':
    print('Here is the glorious Apple store. You see rows and rows of slick products that you want')
    print("to try out. There are watches, iPads, iPhones, laptops, and Airpods. Sadly, it doesn't") 
    print("seem like you have enough money to purchase them all today, so let's choose just one item:")
    # first option: watch or airpods
    option1 = str(input('WATCH or AIRPODS? '))
    # choice: watch
    if option1.lower() == 'watch':
        print('Look at all of those nice watches. The newer models have more health tracking features, but the')
        print('older models are more basic and less expensive. Which model would you like to purchase:')
        # second option: series 7 or SE
        option2 = str(input('7 or SE? '))
        # choice: 7
        if option2 == '7':
            print("Wow you bought the newest model! Too bad it wasn't on sale today.")
        # choice: SE
        else:
            print('Today is your lucky day! The basic model happened to have a $100 discount attached to it! You')
            print('walked out with a great deal!')
    # choice: airpods
    else:
        print('Time to get some new bluetooth headphones. You head to another section of the store and see a few')
        print('different models of Airpods.')
        # second option: regular, pro, or max
        option2 = str(input('Do you go with the REGULAR, PRO, or MAX? '))
        # choice: regular
        if option2.lower() == 'regular':
            print('The first and second generation models happened to have a discount today! Good choice!')
        # choice: pro
        elif option2.lower() == 'pro':
            print("The pros are the perfect choice for everyday wear. It's a shame they didn't have a discount today...")
        # choice: max
        else:
            print("The Airpods Max are perfect for noise cancellation, but not for the price. Sorry, you didn't")
            print('get a promotion for this model...')
# invalid choice
else:
    print('Invalid response. Choose a store listed.')
