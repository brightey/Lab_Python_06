"""
Lab_Python_06
Part 1
"""

import datetime

"""
Whatever the datastructure you choose,
it should represent the following data:

player		| date		| score
_______________________________________
rooney		| 6/23/2012	| 2
rooney		| 6/25/2012	| 2
ronaldo		| 6/19/2012	| 0
ronaldo		| 6/20/2012	| 3
torres		| 6/21/2012	| 0
torres		| 6/21/2012	| 1
"""

## create the player_stats data structure
import datetime
player_stat={'rooney':(datetime.date(2012,6,4),2),
             'rooney':(datetime.date(2012,6,25),02),
             'ronaldo':(datetime.date(2012,6,19),0),
             ' ronaldo':(datetime.date(2012,6,20),03),
             'torres':(	datetime.date(2012,6,20),0),	
             'torres':(	datetime.date(2012,6,21),1)
                        

## implement highest_score


## implement highest_score_for_player



## implement highest_scorer


##the one for the class

import datetime
#import time

player_stat={'rooney':(datetime.date(2012,6,4),2),
             'rooney':(datetime.date(2012,6,25),02),
             'ronaldo':(datetime.date(2012,6,19),0),
             ' ronaldo':(datetime.date(2012,6,20),03),
             'torres':(	datetime.date(2012,6,20),0),	
             'torres':(	datetime.date(2012,6,21),1)
                        
        
             }
print  player_stat


#def highest_score(player_stats):
 #  for i in 

   #    maximum=max(player_stat,key=player_stat.get)
    #   print maximum
     #inverse = [(value, key) for key, value in  player_stat.items()]
    # print max(inverse)[1]

#print highest_score

#a=dict(((1,3),(0,-1),(3,3))); m=max(a,key=a.get)

class Player:
 def __init__(self,firstname,lastname,team=None):
  self.first_name = firstname
  self.last_name = lastname
  self.scores = [3,4,2]
  self.team = team

 def add_score(self,score):
  #  self.scores.append(datetime.date())
  self.scores.append(score)
  print self.scores

 def total_score(self):
  t=0
  for i in self.scores:
    t=t+i
  print t

 def average_score(self) 
   k= t/len(self.scores)
 print k
    


soccer=Player('jasper','topaz','anointingAnnointed')
soccer.add_score(1)
soccer.total_score()
soccer.average_score()


