import random
# welcome to the quote generator
quotes = [
   "The only way to do great work is to love what you do. - Steve Jobs",
   "Believe you can and you're halfway there. - Theodore Roosevelt",
   "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
   "The harder I work, the luckier I get. - Gary Player",
   "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle. - Christian D. Larson"
]

def get_random_quote():
   return random.choice(quotes)
print("The Quote of the Day is \n")

print(get_random_quote()+"\n")