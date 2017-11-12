'''
Created on Apr 9, 2015

@author: Ayse Akin & Jenn Cafiero
Pledge: I pledge my honor that I have abided by the Stevens Honor System. 
'''

FILE_NAME = "musicrecplus.txt"
    
def mainOptions(name, readDict):
    '''Creates a text menu for the user to choose options from.
    Enter a letter to choose an option:
    e - enter preferences
    r - get recommendations
    p - show most popular artists
    h - how popular is the most popular 
    m - which user has the most likes 
    q - save and quit
    Any other letter will prompt an error message and print the menu again.'''
    l = raw_input("Enter a letter to choose an option: \n e - enter preferences \n r - get recommendations \n p - show most popular artists \n h - how popular is the most popular \n m - which user has the most likes \n q - save and quit \n")
    if l != "q":
        if l == "e":
            prefs = preferences(name, readDict)
            My_write(name, prefs, readDict, FILE_NAME)
            return mainOptions(name, readDict)
        if l == "r":
            prefs = getPrefs(name, readDict)
            recs = recommendations(name, prefs, readDict)
            print "\n" + name + "," + "based on the users I currently know, I believe you will like: "
            for artisto in recs:
                print (artisto)
            print "\n Enjoy!"
            return mainOptions(name, readDict)
        if l == "p":
            popArtists(artistLikes(readDict))
            return mainOptions(name, readDict)
        if l == "h":
            howPop(artistLikes(readDict))
            return mainOptions(name, readDict)
        if l == "m":
            mostLikes(readDict)
            return mainOptions(name, readDict)
        else:
            print ("You didn't choose one of the options, please try again.")
            return mainOptions(name, readDict)
    else:
        print ("ByeBye!")
           
def My_read():
    '''Opens the file to read the dictionary stored in the file "musicrecplus.txt"'''
    myFile = open(FILE_NAME, "r")
    D = {}
    for l in myFile:
        [userName, bands] = l.strip().split(":")
        bandList = bands.split(",")
        bandList.sort()
        D[userName] = bandList
    myFile.close()
    return D

def My_write(name, prefs, listofUsers, theFile):
    '''Writes all the user's preferences to the file.'''
    listofUsers[name] = prefs
    myFile = open(theFile, "w")
    for i in listofUsers:
        save = str(i) + ":" + ",".join(listofUsers[i]) + "\n"
        myFile.write(save)
    myFile.close()
    
def getPrefs(userName, listofUsers):
    '''Returns the preferences of the user'''
    if userName in listofUsers:
        pref = listofUsers[userName]
    else:
        print("This user is not here. Sorry. Please enter another name")
        mainOptions(userName)
    pref.sort()
    return pref

def preferences(userName, listofUsers):
    '''Checks to see if the user is in the dictionary, and if not,
    asks the user to enter their preferences. If so, asks the user if he/she
    would like to add to the preference list.'''
    newPref = ""
    if userName in listofUsers:
        pref = listofUsers[userName]
        print ("You have used the system before. \nYour music preferences include: ")
        for artist in pref:
            print artist
        print ("To add to your preferences, please enter the name of an artist or band you like,")
        newPref = raw_input("Or just press enter to go back to the main menu: ")
    else:
        pref = []
        print("I see you are a new user.")
        newPref = raw_input("Please enter the name of an artist or band you like: ")
    
    while newPref != "":
        pref.append(newPref.strip().title())
        print("Please enter another artist or band that you like,")
        newPref = raw_input(" or press enter to go back to the main menu: ")
    
    pref.sort()
    return pref

def recommendations(userName, prefs, listofUsers):
    ''' Gets recommedations for a user based on the users in the dictionary
    and the user's preferences.'''
    bestUser = findBestUser(userName, prefs, listofUsers)
    recommendation = drop(prefs, listofUsers[bestUser])
    return recommendation

def findBestUser(userName, prefs, listofUsers):
    '''Find the user who has the most similar preferences to the user and returns the best user's name.'''
    users = listofUsers.keys()
    bestUser = None
    bestScore = -1
    for user in users:
        score = numMatches(prefs, listofUsers[user])
        if score > bestScore and userName != user:
            bestScore = score
            bestUser = user
    return bestUser

def drop(list1, list2):
    ''' Return a new list that contains only the elements in
        list2 that were NOT in list1. '''
    list3 = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            list3.append(list2[j])
            j += 1
    
    return list3

def numMatches (list1, list2):
    '''Returns the number of elements that match between two sorted list'''
    matches = 0
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            matches += 1
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return matches
    
def popArtists(likes):
    '''Prints the most popular artist'''
    mostPop = []
    for artisto in likes:
        if mostPop == []:
            mostPop = [artisto]
        else:
            if likes[artisto] > likes[mostPop[0]]:
                mostPop = [artisto]
            elif likes[artisto] == likes[mostPop[0]]:
                mostPop = mostPop + [artisto]
    print "The most popular artist(s): " + str(mostPop) + '\n'

def howPop(likes):
    ''' Prints the number of likes that the most popular artist has'''
    most = 0
    for artist in likes:
        if likes[artist] > most:
            most = likes[artist]
    print 'The most popular artist(s) has %s likes' % most + '\n'

def mostLikes(listofUsers):
    ''' Finds out what artist has the most amount of likes and tells the user'''
    mostlikes = 0
    mrUser = []
    for userperson in listofUsers:
        if '$' in userperson:
            pass
        elif len(listofUsers[userperson]) > mostlikes:
            mostlikes = len(listofUsers[userperson])
            mrUser = [userperson]
        elif len(listofUsers[userperson]) == mostlikes:
            mostlikes = len(listofUsers[userperson])
            mrUser = mrUser + [userperson]
    print 'The user(s) with the most likes is/are" ' + str(mrUser) + '\n'
    print 'The liked artists are the following: '
    for userperson in mrUser:
        print userperson + ": " + str(getPrefs(userperson, listofUsers))
        
def artistLikes(listofUsers):
    '''Returns a dictionary containing the artists with the number
    of likes they have between all the users.'''
    votes = {}
    for user in listofUsers:
        for artisto in listofUsers[user]:
            artist = artisto.strip()
            if artist in votes:
                votes[artist] = votes[artist] + 1
            else:
                votes[artist] = 1
    return votes
       
def main():
    '''The main function'''
    listofUsers = My_read()
    print "Welcome to the music recommender system!"
    name = raw_input("Please enter your first name. \n").title()
    mainOptions(name, listofUsers)
main()

