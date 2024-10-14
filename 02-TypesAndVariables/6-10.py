###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
if (movie.islower()) :
   print (movie.upper())
# print title in small letters
if (movie.isupper()) :
   print (movie.lower())

# print how many times the vowel "e" appears in the title


# print where in the text is the word "Lord"
print({movie[4:8]})

# print where in the text is the word "dragon"
print({movie[7]},{movie[6]},{movie[19]},{movie[5]},{movie[32]})