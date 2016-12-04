#ThankYouGoogle
import requests
import re
def printRequests(link):
    link1 = "https://www.google.co.in/search?q="
    temp = link.split()
    for word in temp:
        link1 = link1 + word + "+"
    link1 = link1[:len(link1)-2]    
    r = requests.get(link1)
    a = re.sub('<[^<]+?>', '', r.text)
    b = "Spouse"
    f = a[a.find(b):]
    return f.count("(m. 1") + f.count("(m. 2")
print "No. of Spouses : "+str(printRequests(raw_input("Enter Celebrity Name : ")))
