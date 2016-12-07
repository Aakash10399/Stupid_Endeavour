#ThankYouGoogle
import requests
import re
def printRequests(link):
    link1 = "https://www.google.co.in/search?q="
    for word in link.split():
        link1 = link1 + word + "+"    
    a = re.sub('<[^<]+?>', '', requests.get(link1[:len(link1)-2]).text)
    return a[a.find("Spouse"):].count("(m. 1") + a[a.find("Spouse"):].count("(m. 2")
<<<<<<< HEAD
print("No. of Marriages : "+str(printRequests(input("Enter Celebrity Name : "))))
=======
print "No. of Marriages : "+str(printRequests(raw_input("Enter Celebrity Name : ")))
>>>>>>> origin/master
