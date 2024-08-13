def count_vowels(input_string):
    return sum(1 for char in input_string if char in 'aeiouAEIOU')
input_string = input("Enter a string: ")
print("Number of vowels:", count_vowels(input_string))
