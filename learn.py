"""
@project: Web Scrapper v0.1
@author: Zeeshan
@websiteTOscrap: http://www.utexas.edu/world/univ/alpha/
"""
"""
HTML:QuickGuide
HTML is a markup language , which basically means it works on tags 

some of the tags are :
    <img> tag for displaying tag
    <a> tag for displaying url
    <div> tag for styling purpose 
    There are some tags inside tags , for example :
        href inside <a> . so the full thing is <a href="www.abcd.com">A link </a>
        some inside tags like span ,class which can be used anywhere 
        eg:
        <a href="www.abcd.com" class= "SomeClass">A link </a>
        <div class = "someclass">
        One more important inside tag is "id" -> Very important as Javascript also uses this.
"""

"""
ok

Lets get down to business.
Our target is to get all the college names from the webpage and write it in a file. Ok?
I want you to see the source code of the webpage
k
if you see the source code , you can see a similarity.
<LI><A HREF="http://www.rowan.edu/" TARGET="_blank" CLASS="institution">Rowan University</A> (NJ)</LI>
^
All the college names are inside a li (list tag) followed by <a> tag. And then the <a> tag has an inside tag 
called class , whose value is "insitution", ok>
Now tell me , what is the most unique thing in this 
<LI><A HREF="http://www.rowan.edu/" TARGET="_blank" CLASS="institution">Rowan University</A> (NJ)</LI>
qhich can identify that the information here is a college name
Class
CLASS = "institution"
Exactly , so we need to find all <a link whose class is insitution. Then we need to extract the data between the 
tags , which is the insitution name
ok
So here is how our logic will work:
connect to the url:
load all the html content in a variable
use BeautifulSoup to search for our required content.
ok
??
"""
#First import beautifulSoup

from bs4 import BeautifulSoup

#Secondly import a module which lets you connect to the url
import urllib2

#define the url
url="http://www.utexas.edu/world/univ/alpha/"

connect = urllib2.urlopen(url)# I hope this is right , doing from memory. Basically we are just connecting
htmlContent= connect.read() #Get the data
#------TIll here everything is working -----
soup = BeautifulSoup(htmlContent,"lxml") #We initialize the BeautifulSoup class with the html as parameter.

#Now we need to find all the data (that is university name)

data = soup.findAll("a",{'class':'institution'}) #We need to find all <a> tag then filter those <a tag which has the class institution
#soup.find_all returns a list, so data is a list . lets print info from data
print "Test 2"
for links in data:
    try:
        
        b =  links.contents[0]
        print b#Run the code. We can get the data inside the tag using contents[0]
        with open("","a") as file:
            file.write(b) #error is here, wen need to write links not data
    except UnicodeEncodeError:
        print "A encode error happened"
    except:
        pass #Lets keep the code ruuning

"""
How to catch errors

we catch errors using try except

for example 

    try:
        do something
    except:
        An error occured
Anything which happens inside the try block will run and if it faces an exception then the thing inside the 
except block will run 

Suppose we want to ignore the error and keep the code running 
    try:
        do something
    except:
        pass
Suppose we only want to catch a specific type of error , for eg: the UnicodeEncodeError

    try:
        do something
    except UnicodeEncodeError:
        print "A encode error happened"
    except:
        print "Some other error happened"
        
ok??
ok

"""