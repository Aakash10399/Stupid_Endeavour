#ThankYouGoogle
import requests
import re
def printRequests(link):
    link1 = "https://www.google.co.in/search?q="
    for word in link.split():
        link1 = link1 + word + "+"    
    a = re.sub('<[^<]+?>', '', requests.get(link1[:len(link1)-2]).text)
    return a[a.find("Spouse"):].count("(m. 1") + a[a.find("Spouse"):].count("(m. 2")
print "No. of Spouses : "+str(printRequests(raw_input("Enter Celebrity Name : ")))
