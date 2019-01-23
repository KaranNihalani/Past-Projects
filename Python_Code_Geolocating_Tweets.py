import tkinter as tk
import json
import folium
from tkinter import ttk
from tkinter import scrolledtext
import webbrowser
import re


# Create instance
win = tk.Tk()
# Add a title
win.title("Python GUI")

#win.minsize(width=850, height=500)
#win.maxsize(width=850, height=500)
# Disable resizing the GUI
win.resizable(0,0)
# Modify adding a Label
aLabel = ttk.Label(win, text="A Label")
aLabel.grid(column=0, row=0)
#Modified Button Click Function
def clickMe():
    map_osm = folium.Map(location=[53.472328361821766,-2.23959064483645])
    action.configure(text='Tweets: ' + name.get())
    #action.configure(text='Hello ' + name.get())
    #print("you have entered ... "+name.get())
    count = 0
    searchkeyword = name.get()
    print("you have entered ... "+searchkeyword)
    
    with open('Manchester_Part-1_records.json', encoding = 'utf 8') as data_file:
        
        for row in data_file:
            data = json.loads(row)
            tempText = data['text']
            createdAt= data['createdAt']['$date']
            print("you have entered ... "+tempText)
         
            if searchkeyword in tempText:
                StringToScroll = "\n" + "\nDate: " + data['createdAt']['$date'] + "\nLatitude:" + str(data['geoLocation']['latitude']) + "\nLongitude:" + str(data['geoLocation']['longitude']) + "\nTweet Text:" + data['text']
                count = count + 1
                scr.insert(tk.INSERT,StringToScroll)
                latt = data['geoLocation']['latitude']
                long = data['geoLocation']['longitude']
                folium.Marker([latt, long], popup=tempText, icon=folium.Icon(color='blue',icon='twitter', prefix='fa')).add_to(map_osm)
                #print("Geo-Location "+str(data['geoLocation']['latitude']))
                print("Tweet Text: "+data['text'])
                print("Place Name: "+data['place']['name'])
                print("Place Full Name: "+data['place']['fullName'])
                print(" ...... Next Record ........")
                map_osm.save('plotted-map.html')

    webbrowser.open_new_tab('plotted-map.html')  

def templateBasedSearch():
    beer = ["drinking" , "stout", "brewing", "brew"]
    map_osm = folium.Map(location=[53.472328361821766,-2.23959064483645])
     
    with open('Manchester_Part-1_records.json', encoding = 'utf 8') as data_file:
         #count = 0
         for row in data_file:
            data = json.loads(row)
            
            tempText = data['text']
            latt = data['geoLocation']['latitude']
            long = data['geoLocation']['longitude']
            
            for word in beer:
                if word in tempText:
                    #count = count + 1
                    StringToScroll = "\n" + "\nDate: " + data['createdAt']['$date'] + "\nLatitude:" + str(data['geoLocation']['latitude']) + "\nLongitude:" + str(data['geoLocation']['longitude']) + "\nTweet Text:" + data['text']
                    folium.Marker([latt, long], popup=tempText, icon=folium.Icon(color='blue',icon='twitter', prefix='fa')).add_to(map_osm)
                    scr.insert(tk.INSERT,StringToScroll) 
                    print("Tweet Text: "+data['text'])
                    print("Place Name: "+data['place']['name'])
                    print("Place Full Name: "+data['place']['fullName'])
                    print(" ...... Next Record ........")
                    map_osm.save('plotted-map.html')
               
    webbrowser.open_new_tab('plotted-map.html')

def RegularExpression():
    # Open file
    f = open('Manchester_Part-1_records.json', 'r')
    #set the findall pattern to the amount of digits in each user's twitter ID
    regex = re.compile ('\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d')
    #read the data from the file
    twitter_ID = regex.findall(f.read())
    
    if twitter_ID:
        print ("Twitter ID numbers:", twitter_ID)
    else:
        print("Unable to remove each user twitter ID")
    
         
# Changing our Label
ttk.Label(win, text="Enter a name:").grid(column=0, row=0)
# Adding a Textbox Entry widget
name = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0, row=1)
# Adding a Button
action = ttk.Button(win, text="Click for Tweet!", command=clickMe)
action.grid(column=2, row=1)

beerSearch = ttk.Button(win, text=" Beer Search ", command=templateBasedSearch)
beerSearch.grid(column=0, columnspan=3)


regularExpression = ttk.Button(win, text=" Regular Expression Search ", command=RegularExpression)
regularExpression.grid(column=0, columnspan=4)

#action.configure(state='disabled') # Disable the Button Widget

# Using a scrolled Text control
scrolW = 30
scrolH = 10
scr = scrolledtext.ScrolledText(win, width=scrolW, height=scrolH, wrap=tk.WORD)
scr.grid(column=0, columnspan=3)

# Place cursor into name Entry
nameEntered.focus()
#======================
# Start GUI
#======================
win.mainloop()
