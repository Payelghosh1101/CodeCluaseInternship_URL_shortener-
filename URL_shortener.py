import pyshorteners


url = input("\nEnter the url : ")

def shortenurl(url):
    s = pyshorteners.Shortener()
    print("\nshot url : ",s.tinyurl.short(url),"\n")

shortenurl(url)



