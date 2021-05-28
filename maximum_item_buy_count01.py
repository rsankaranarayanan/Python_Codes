# Today is Sunday and Disha is out for the shopping. She has reached to the famous market of the city. She has a list of items which she wants to buy but she has a very low amount of cash today and no shop accepts any online payment method in the market. Disha has only D rupees with her and wants to buy N items (she wants to buy as many units of item as possible). She wants to shop in a way such that first she buy 1 quantity of all the items she wants to buy and then she will move to buy 2nd quantity of any item.

# Can you help her by calculating how many items she can buy today if she shops optimally?

# You are given an array which represents the price of items Disha wants to buy.
# Example :-
# If she wants to buy 4 items having price 4, 6, 2, 5 respectively and has 49 rupees only then she will buy in this order:- 1st item, 2nd item, 3rd item, 4th item (It will cost 17 rupees). Again she will buy in this order 1st, 2nd, 3rd, 4th (it will cost 17 rupees). Now, she has remaining 15 rupees so she can buy any 3 items.


# Input Format
# The first line of input consists of two space-separated integers, N (number of items Disha wants to buy) and D (amount of cash Disha has with her).
# The second line of input consists of N space-separated integers which represents the price of the N items Disha wants to buy.


# Constraints
# 1<= N <=1e9
# 1<= Ni <=10^15 (1e15)
# 1<= D <=10^18 (1e18)


# Output Format
# Print the count of items which Disha can buy.

# Sample TestCase 1
# Input
# 5 24
# 4 8 9 7 2
# Output
# 4

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():

 # Write code here 
 N = input().split()
 Itmes = int(N[0])
 Amount = int(N[1])
 Price = input().split()
 Price_list = list()
 for p in Price:
     Price_list.append(int(p))
 Price_list.sort()
 count = 0
 sum = 0
 while sum <= Amount:
     for i in range(0, Itmes, 1):
         if (sum+Price_list[i] <= Amount):
             sum = sum + Price_list[i]
             count += 1
         else:
             sum = sum + Price_list[i]
 print(count)

main()

