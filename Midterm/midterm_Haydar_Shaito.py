#link3: "https://stackoverflow.com/questions/47047998/printing-specific-html-values-with-python"
# from bs4 import BeautifulSoup
# import requests

#1)
def addNewTab(title,url):
    lst.append([{"Title":title,"URL":url}])
    print(lst)
    
#2)
def closeLastTab():
    lst.remove(lst[-1])
    print(lst)
def closeTab(tab):
    if(tab<len(lst)):
        lst.remove(lst[tab])
        print(lst)
    else:
        print("Page does not exist!")

#3)
#link3: "https://stackoverflow.com/questions/47047998/printing-specific-html-values-with-python"
def switchTab(tab):
    for i in range(len(lst[tab])):
        page_to_scrape=requests.get(lst[tab][i]["URL"])
        soup = BeautifulSoup(page_to_scrape.text, 'html.parser')
        data= soup.find_all("html")
        print(data)

def switchToLastTab():
    page_to_scrape=requests.get(lst[-1]["URL"])
    soup = BeautifulSoup(page_to_scrape.text, 'html.parser')
    data= soup.find_all("html")
    print(data)

#4)
def displayAllTabs():
    for i in range(len(lst)):
        if(len(lst[i])>1):
            for y in range(len(lst[i])):
                print(lst[i][y]["Title"])
        else:
            print(lst[i][0]["Title"])
            

#5)
def openNestedTab(tab,title,url):
    if(tab<len(lst)):
        lst[tab].append({"Title":title,"URL":url})
        print(lst)
    else:
        print("Nested page does not exist!")

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
lst=[[{'Title': 'p1','URL': 'ee'},{'Title': 'p2','URL': 'ee'}], [{'Title': 'p3','URL': 'ew'}]]
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
        if(tabToSwitch==""):
            switchToLastTab()
        else:
            while(not tabToSwitch.isnumeric()):
                tabToSwitch=input("Please enter a positive integer: ")
            switchTab(int(tabToSwitch))
    if(choice=="4"):
        displayAllTabs()
    if(choice=="5"):
        parentTab=input("Enter an index: ")
        while(not parentTab.isnumeric()):
            parentTab=input("Please enter a positive integer: ")
        title=input("Enter the page title: ")
        url=input("Enter the page URL: ")
        openNestedTab(int(parentTab),title,url)
    # if(choice=="6"):
    # if(choice=="7"):
    # if(choice=="8"):
    # if(choice=="9"):