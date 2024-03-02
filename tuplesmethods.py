
countries = ("India", "Australia", "USA", "China", "Brazil")
print(countries)
temp=(list(countries))
temp.append("Russia")
temp.pop(3)
countries =tuple(temp)
print(countries)

countries2 = ("England", "Germany", "France")
totalcountries =  countries + countries2
print(len(totalcountries), totalcountries)
