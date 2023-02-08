def Guess(g , n, think, name):
    # n +=1
    n+=1
    if g > think:
        print("Your guess is too high.")
        
    elif g < think:
        print("Your guess is too low.")
        
    elif g == think:
        print(f'Good job, {name}! You guessed my number in {n} guesses!')
    
    d = int(input("Take a guess."))
    
    Guess (d, n, think, name)






t = 19
name = input("Hello! What is your name? ")
print(f"Well, {name}, I am thinking of a number between 1 and 20.")
print("Take a guess.")

gu = int(input())
m = 0
guesses =  Guess(gu , m, t, name)

# print(f'Good job, {name}! You guessed my number in {guesses} guesses!')