import calendar
import re


if __name__ == '__main__':
  print(calendar.month(2022, 7))

  str = "Python is a high-level, general-purpose programming language. Its design philosophy emphasizes " \
        "code readability with the use of significant indentation. " \
        "Python is dynamically typed and garbage-collected. It supports multiple" \
        " programming paradigms, including structured, object-oriented and functional" \
        " programming. "
  search = input("Search here")
  print('Searching...')
  patt = re.compile(r"use")
  matchess = patt.finditer(str)
  for match in matchess:
      if(match is not  search):
          print('Sorry , no finding')
      else:
       print(match)


