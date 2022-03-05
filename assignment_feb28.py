# 1. Make a shopping list of 5 things you need at the grocery store # put each item on a line by itself

market_day_list = ['tomatoes', 'onions', 'beans', 'boes', 'apple']
for i in market_day_list: 
    print(i) 
#2 Your items ring up as 9.45, 5.67, 3.20, 7.47 and 20.23. Use python as a handy # calculator to calculate the total of your shopping.

total_price_list = [9.45, 5.67, 3.20, 7.47, 20.23]
print(sum(total_price_list))

#3. But wait, you decide to buy five more of the last item. Recalculate the total

total_price_list = [9.45, 5.67, 3.20, 7.47, (5 * 20.23)]
print(sum(total_price_list))

#4. Using a built in function, determine the length of this phrase: 'Blood oxygenation level dependant functional magnetic resource imaging ' 
length_of_phrase = 'Blood oxygenation level dependant functional magnetic resource imaging '
len(length_of_phrase)

# #5. Pick your favorite snack, use the * operator to print it a 100 times.

my_snack = 'pawpaw'
print(my_snack * 100)
# Modify the code to print it with spaces in between.
my_snack = 'pawpaw'
print((my_snack + " ") * 100)
#Challenge: run 'dir('any_string')' Pick any two interesting methods and #run 'help('any_string'.interesting_method)' Can you figure out how to use these #methods #Bonus Challenge Can you figure out how to do the same thing on exercise 1 with just one line

help('any_string'.lower)
help('any_string'.upper)
help('any_string'.title)






