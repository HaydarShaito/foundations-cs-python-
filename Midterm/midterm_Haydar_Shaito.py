#1)
def addNewTab(title,url):
    lst.append({"Title",title})
    lst.append({"URL",url})
    #print(lst)

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
lst=[]
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