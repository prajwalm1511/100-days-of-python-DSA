#function and inputs
def friends(name,nick_name): # a variable that is being defined here is a PARAMETER

    print(f"call my friend {name} as {nick_name} ")

friends("mohanish","momo") # here while calling the function
    #the values that u input for the parameters are called ARGUMENTS

def friends(name='momo',nick_name='yedava'): #u can input multiple arguments by separating with comma

    print(f"call my friend {name} as {nick_name} ")
friends()

def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()
    
    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e
    
    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e
    
    
    score = int(str(first_digit) + str(second_digit))
    print(score)
    
calculate_love_score("Kanye West", "Kim Kardashian")