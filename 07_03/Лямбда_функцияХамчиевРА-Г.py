contains_a = lambda word: 'a' in word
long_string = lambda string: len(string) > 12
end_in_a = lambda string: string[-1] == 'a'
even_or_odd = lambda num: "четное" if num % 2 == 0 else "нечетное"
multiple_of_three = lambda num: "кратное трем" if num % 3 == 0 else "не кратное"
rate_movie = lambda rating: "Мне понравился этот фильм" if rating > 8.5 else "Этот фильм был не очень хорошим"