
import requests,time
from bs4 import BeautifulSoup
# to store url value
url1="http://54.225.7.146/"
# sending http request to server on given URL 
response=requests.get(url1)
if  response.status_code == 200 : 
    print("we got the response ")
    time.sleep(2)
    # lets print actual data
    #print(response.text) # actual html code 
    # time to do parsing in above data
    time.sleep(1)
    print("please wait my BS4 is doing parsing in above raw data ..")
    parsed_data=BeautifulSoup(response.text,'lxml') # we can also use html5lib
    my_data=parsed_data.find_all('ul')
    # checking tag
    if my_data:
        for item in my_data:
            li1_data=item.find_all('li')
            if li1_data:
                for li in li1_data:
                    print(li.get_text())
                    time.sleep(1)
    else :
        print("No title found in given ",url1)
else :
    print("you need to check code or web admin")
