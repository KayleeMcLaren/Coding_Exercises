
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_names = name1 + name2
lower_case_names = combined_names.lower()

name_true_count = 0
name_true_count += lower_case_names.count("t")
name_true_count += lower_case_names.count("r")
name_true_count += lower_case_names.count("u")
name_true_count += lower_case_names.count("e")

name_love_count = 0
name_love_count += lower_case_names.count("l")
name_love_count += lower_case_names.count("0")
name_love_count += lower_case_names.count("v")
name_love_count += lower_case_names.count("e")

love_score = str(name_true_count) + str(name_love_count)
love_score_as_int = int(love_score)

if (love_score_as_int < 10) or (love_score_as_int > 90):
    print(f"Your score is {love_score_as_int}, you go together like coke and mentos.")
elif (love_score_as_int >= 40) and (love_score_as_int >= 50):
    print(f"Your score is {love_score_as_int}, you are alright together.")
else:
    print(f"Your score is {love_score_as_int}.")
