<!-- good -->
## Enhancements crawler_class.py

Some more comments and docstrings would improve the readability.
The use of for loops could be reduced, there are some instances where a list is generated using list = [] followed by a for loop with a list.append(). Replacing it with a list comprehension would be more efficient.

Another thing that is very obvious is the limited error handling.
In the main loop it has Try: (all the processes in the main loop)
Except e: print(e) followed by a hard exit(). This way of catching errors has no advantage compared to not using a try and except. A better way would be to check for instance if the site exists by pinging it raising a suitable error. Also the use of a try except inside of a try except for getting the phone number could probably be done differently, cause the statement is conditional a IF ELSE would suffice. something like IF PHONE: phone = str(phone[0]) ELSE: [find phonenumer somewhere else].

Next up is the single responsibility aspect. The Crawler class takes care of more things than just simply executing a 'crawl'. It would be better to split different pre process steps into multiple classes/files and call them accordingly from the Crawler class. This also improves maintainability, it is now possible to  work on different parts that handle a sub process which touches on multiple SOLID principles. Or at least create the opportunity to 
