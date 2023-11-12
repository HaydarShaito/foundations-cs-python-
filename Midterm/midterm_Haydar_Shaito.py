# from bs4 import BeautifulSoup
# import requests
#1)
def addNewTab(title,url):
    lst.append({"Title":title,"URL":url})
    print(lst)
#2)
def closeLastTab():
    lst.remove(lst[-1])
    print(lst)
def closeTab(tab):
    if(tab<=len(lst)):
        lst.remove(lst[tab])
        print(lst)
def switchTab(tab):
    page_to_scrape=requests.get(lst[tab]["URL"])
    soup = BeautifulSoup(page_to_scrape.text, 'html.parser')
    data= soup.find_all("html")
    print(data)

#menu
print("""
1. Open Tab
2. Close Tab
3. Switch Tab
4. Display All Tabs
5. Open Nested Tab
6. Clear All Tabs
7. Save Tabs
8. Import Tabs
9. Exit
""")

#main list
lst=[{'Title': 'p1','URL': 'ee'}, {'Title': 'p2','URL': 'ew'}]
#choice loop
choice=""
while(choice!="9"):
    choice=input("Enter a command: ")
    #make sure to enter a positive nb
    while(not choice.isnumeric()):
        choice=input("Please enter a positive integer: ")
    if(choice=="1"):
        title=input("Enter the page title: ")
        url=input("Enter the page URL: ")
        addNewTab(title,url)
    if(choice=="2"):
        tabToClose=input("Enter which tab you wish to close: ")
        if(tabToClose==""):
            closeLastTab()
        else:
            while(not tabToClose.isnumeric()):
                tabToClose=input("Please enter a positive integer: ")
            closeTab(int(tabToClose))
    if(choice=="3"):
        tabToSwitch=input("Enter which tab: ")
        switchTab(tabToSwitch)