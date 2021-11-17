from threading import Thread
from time import sleep
import sys
import random 

def timer():
    for i in range (60):
        sleep(1)
    print("Sorry, the 1 minute you had to make your way to the Blake House is up! You have to go home and come back tomorrow. Be sure to look up the right bus schedule to give yourself more time.")
    sys.exit()
    
   
def intro():
    print("Welcome to the Blake Garden at UC Berkeley.")
    print("Unfortunately we are closing in 15 minutes, but if you want to try and catch the sunset, you have 1 minute to get to the viewing area.")
    print("Would you still like to come in for a few minutes?")
    
    answer = input("> ")
    
    if answer == "yes":
        sleep(1)
        print("Ok great, once you get to the view in front of the Blake House, you'll have only have 5 minutes before we need you to come back so that we can close the gate promptly at 6:00 p.m.")
        # research how to write a function that allows you to call upon the timer and find out how much time you have left) 
        sleep(2)
        print("Come through the gate and head to the Rose Garden")
        rose_garden()
    else:
        sleep(1)
        print("No problem, please come back tomorrow if you'd like. We'll be open at 9 a.m.")
        sys.exit()
        
def rose_garden():
    sleep(1)
    print("You'll notice that in the Rose Garden, you're catching the last blooms of October before we let them rest for winter.")
    sleep(1)
    print("Since you probably don't remember the exact orientation of the Blake Garden, do you want to stop by the office to grab a map first? Or do you want to head to the fruit patch, or forest?")
    
    while True:
    
        answer = input("> ")
        substring_1 = "office"
        substring_2 = "fruit patch"
        substring_3 = "forest"
    
        if substring_1 in answer:
            print("Great, let's stop by the office first and grab a map.")
            sleep(2)
            office() 
        elif substring_2 in answer:
            print("Ok we'll make our way to the fruit patch and try to figure out our way to the Blake House.")
            sleep(2)
            Fruit_Patch().from_rose_garden()
        elif substring_3 in answer:
            print("Great, we'll head to the forest.")
            sleep(2)
            forest()
        else: 
            print("Sorry, those aren't one of the three options, try again between stopping by the office, going to the fruit patch, or going to the forest")
            sleep(1)
       
    
def office():
    print("It's helpful that now you can pick up a map of the garden to better navigate.")
    sleep(1)
    print("Turns out Meghan, the program coordinator, is also here so naturally you'll want to catch up with her for a little bit on how you both are.") 
    # look up code to knock off 30 seconds off your clock 
    sleep(15) 
    print("It's great catching up but you still need to catch the sunset before the garden closes, so where would you like to go now? You can go to the fruit patch, or to the forest.")
    sleep(1)
    
    while True:
    
        answer = input("> ")
        substring_1 = "fruit patch"
        substring_2 = "forest"
        
        if substring_1 in answer:
            sleep(1)
            print("Ok, we'll head to the fruit patch.")
            sleep(2)
            Fruit_Patch().from_office()
            # the point here is that we're trying to call on a function within the class(fruit_patch)
            # will it also print the self.statement? Or will we need to manually add that too ? 
        elif substring_2 in answer:
            sleep(1)
            print("Great, to the forest we go.")
            sleep(5)
            forest() 
        else: 
            sleep(1)
            print("Sorry, that's not connected to the office. We can only go to the fruit patch or forest from here.") 
            

class Fruit_Patch(object):
    
    def __init__(self):
        self.statement = "Now you are in the fruit patch. Unfortunately, the other Blake Garden staff are also here since they're making their way back to the office."
        print(self.statement)
        sleep(2)

    
    def from_office(self):
    # this method needs 'self' as a parameter, since it is a class method and not a function. 
        
        n = random.radint(1,3)
        
        if n == 1:
            print("You only see Meghan in your path, whom you already said hello to in the office so you can keep making your way to the desert patch quickly.")
            sleep(2)
            Desert().from_fruit_patch()
        elif n == 2:
            print("You see Theresa, who is eager to show you how the plants you potted in the Meditteranean patch have done. She insists that you go see them together.")
            sleep(1)
            print("You leave the fruit patch together and head to the Mediterranean patch, through the desert patch, which is a short walk.")
            sleep(15)
            Mediterranean().with_theresa()
        else:
            print("Thomas is in the patch and wants to continue the conversation about California fuel policy that you left off on last time you worked together.")
            sleep(1)
            print("This conversation takes a little bit longer than you expected so you hang out here for a minute before eventually making your way to the desert patch.")
            sleep(30)
            Desert().from_fruit_patch()
        
 
    def from_rose_garden(self):
        
        n = random.radint(1,3)
        
        if n == 1:
            print("You see Meghan here and even though you weren't planning on it, you're very glad to see her and spend a few seconds catching up on how both of your families are doing.")
            sleep(15)
            print("After doing so, you let her know you're trying to catch the view so she encourages you to make haste to the Blake house by going through the desert patch.")
            sleep(1)
            Desert().from_fruit_patch()
        elif n == 2:
            print("You see Theresa, who is eager to show you how the plants you potted in the Meditteranean patch have done. She insists that you go see them together.")
            sleep(1)
            print("You leave the fruit ptach together and head to the Mediterranean patch, through the desert patch, which is a short walk.")
            sleep(15)
            Mediterranean().with_theresa()
        else:
            print("Thomas is in the patch and wants to continue the conversation about California fuel policy that you left off on last time you worked together.")
            sleep(1)
            print("This conversation takes a little bit longer than you expected so you hang out here for a minute before eventually making your way to the desert patch.")
            sleep(30)
            Desert().from_fruit_patch()     
 
class Mediterranean(object):

    #__init__()
    # pass for now as don't have anything I feel we need to add to every instance of this class 
    
    def with_theresa(self):
        # this is if you entered into Mediterranean patch with Theresa from the fruit_patch, and passed through the desert patch 
        print("Since you came with Theresa here, she's able to show you the olive plants you potted last year which have now grown into beautiful shrubs.")
        sleep(1)
        print("She realizes that it is getting close to sunset and doesn't want you to miss the view either, so she sends you along the path to the Blake House.")
        sleep(2)
        Blake_House()
        

    def from_forest(self):
        # this implies you came from the Forest, and before that you came from the office because if you had gone to the fruit patch, you would no longer go to the forest from there. 
        # so you either only ran into Meghan at the office, or you haven't seen any staff at all. 
        print("Here in the mediterranean patch, you're excited to see that the olive plant you potted last year has turned into a full shrub.")
        sleep(1)
        print("You also see Meghan in the near distance on the corner exit to the Blake House.")
        sleep(1)
        print("While you really want to say hello, you also think she will likely want to chat for a bit and you have very little time left to catch the sunset.")
        sleep(1)
        print("You decide it's probably better to go to the desert patch, and then from there, the Blake House, so you won't have to pass by her.")
        sleep(3)
        Desert().from_mediterannean()
        
    #def from_desert():
        # pass
        # you would not have come from the desert patch to here -- you would go from desert patch directly to the Blake House 
    
def forest():
     
    print("On our way to the forest, we're stopped right outside the Koi pond by a neighbor who wants to know the name of the 16 koi fish.")
    sleep(1)
    print("Even though you're in a hurry, you don't want to disappoint that neighbor's two grandchildren who are obviously eager to know which fish is whom.")
    sleep(1)
    print("You stop for a few seconds to tell them the fish names, and then walk quickly to the Forest.")
    sleep(10)
    print("In the forest, you appreciate the delightful pine scent and majestic height of the trees.")
    sleep(1)
    print("There's only one path from here, so you take it to enter the Mediterannean patch.")
    sleep(2)
    Mediterranean().from_forest()    
    
    # you could have arrived at the fruit patch from the rose garden, or the office. If you came from the Rose Garden, you didn't see Meghan. If you came from the office, you did see Meghan.
    # one way to go about this is to create a class(fruit_patch) and then create functions within class(fruit_patch) so that depending on what your starting point was, you can call on different functions 

class Desert(object):

    # init
    
    def from_fruit_patch(self):
        # if you came from fruit patch, you either talked to Meghan or Thomas, not Theresa because she would have taken you to the mediteranean patch. 
        # assume that in both cases - Meghan or Thomas - you've done your share of running into volunteers so its free and clear to go to the Blake House; 
        print("Luckily it looks completely empty in the desert patch right now and you can see a small path to the Blake House which you take.")
        sleep(2)
        Blake_House()
        
    def from_mediterannean(self):
        print("Whew, that was a close call running into Theresa! You'll have to come back another day to see her when you have more time to see the olive shrubs.")
        sleep(2)
        print("Looks free and clear here in the desert patch, make your way to the Blake House!") 
        Blake_House() 
        
def Blake_House():
    print("Congrats for making it here! You narrowly made it with only X time left to go. Hope you can enjoy the wonderful view of San Francisco.") 
    # print the remaining time 
    sys.exit() 
  
t1 = Thread(target=timer)
t2 = Thread(target=intro)
t1.start()
t2.start()
		

	
	
	# assume you would not have an option of coming from the dessert patch because you would have simply gone to the Blake House directly from the desert patch as opposed to coming here. 
	# assume that you only come to mediteranean patch either through forest, or via passthrough desert patch because you're walking with Theresa, but not an active choice of going from desert to here 
	
		
# (Desert Patch)
# you can get here only from coming from the fruit patch, of which you either talked to Meghan or Thomas, or from teh Mediterranean patch if you backtracked
# assume that in both cases, you've done your time of running into the volunteers so it's free and clear to go to the Blake House 
# Luckily it looks completely empty in the Desert patch right now and you can see a small path to the Blake House which you take. 

# (Blake House) 
# Congrats for making it here! You narrowly made it with only (time) left to go. Hope you can enjoy the wonderful view of San Francisco. 


## If timer gets to zero at any point: 
	# Sorry! The 5 minutes you had to get there is up! Unfortunately you need to make your way back to the gate and try again tomorrow. Be sure to look up the right bus schedule
	# to give yourself more time. 

	# (could have arrived here from the Rose Garden or the Office) 