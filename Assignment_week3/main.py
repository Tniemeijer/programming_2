"""main function of week 1.4"""

from crawler_class import Crawler


if __name__ == "__main__":
    url = "https://sport050.nl/sportaanbieders/alle-aanbieders/"
    c = Crawler(url)
    
    for x in range(5):
        print(str(next(c)))
