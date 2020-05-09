def searcher(): #it is a coroutine
    import time
    # Some 4 seconds time consuming task
    book = "This is a book on Manisha jaiswal and code with Manisha is good"
    time.sleep(4)

    while True:
        text = (yield) #yield means we are using this searcher as a coroutine
        if text in book:
            print("Your text is in the book")
        else:
            print("Text is not in the book")

search = searcher()
print("search started")
next(search) #next method is used for start this
print("Next method run")
search.send("Manisha")

search.close() #close the function
#search.send("Manisha")
"""
input("press any key")
search.send("Manisha and")
input("press any key")
search.send("thi si")
input("press any key")
search.send("joker")
input("press any key")
search.send("like this video")"""