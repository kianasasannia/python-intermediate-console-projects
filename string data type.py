##lower
input_str ='The 5 biggest countries by population in 2017 are China, India, United States, Indonesia, and Brazil'
input_str = input_str.upper()
#print(input_str)


##sub(del numbers)
import re
input_str = 'Box A contains 3 red and 5 white balls, while Box B contains 4 red and 2 blue balls.'
result = re.sub(r'\d+', '', input_str)
print(result)

