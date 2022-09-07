userreply = input('Do you need to ship a package? (enter yes or no) ')
if userreply == 'yes':
    print('We can help you ship that package!')
else:
    print('Please come back when you need to ship a package. Thank you.')

userreply = input('Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ')
if userreply == 'stamps':
    print('We have many stamps designs to choose from.')
elif userreply == 'envelope':
    print('We have many evelope sizes to choose from.')
elif userreply == 'copy':
    copies = input('How many copys would you like? (enter a number) ')
    print(f'Here are {copies} copies')
else:
    print('Thank you, please come again.')