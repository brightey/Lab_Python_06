import datetime
player_stat={'rooney':(datetime.date(2012,6,4),2),
             'rooney':(datetime.date(2012,6,25),02),
             'ronaldo':(datetime.date(2012,6,19),0),
             ' ronaldo':(datetime.date(2012,6,20),03),
             'torres':(	datetime.date(2012,6,20),0),	
             'torres':(	datetime.date(2012,6,21),1)
                        
        
             }
print  player_stat


def highest_score(player_stats):
 #  for i in 

   #    maximum=max(player_stat,key=player_stat.get)
    #   print maximum
     #inverse = [(value, key) for key, value in  player_stat.items()]
    # print max(inverse)[1]


 print highest_score

a=dict(((1,3),(0,-1),(3,3))); m=max(a,key=a.get)

class Player:
 def __init__(self,firstname,lastname,b=None):
  self.first_name = firstname
  self.last_name = lastname
  self.scores = []
  self.team =b

 def add_score(self,score):
  
  self.scores.append(score)
  print self.scores

 def total_score(self):
  t=0
  for i in self.scores:
    t=t+i
  return t  
  print t

 def average_score(self): 
  return self.total_score()/len(self.scores)

    


soccer=Player('fernando','torres','chelsea')

for i in range(1,6):
    torres=raw_input('enter the scores by Fernado torres: ')
    torres =int(torres)
    soccer.add_score( torres)
print soccer.total_score()
print soccer.average_score()


class Team:
  def __init__(self,name,league,manager_name,points):
    self.name=name
    self.league=league
    self.manager_name=manager_name 
    self.players=[]
    self.points=points
    

  def add_player(self,player):
       self.players.append(player)
       #print self.players
 
  def __str__(self): 

   return "Name of player :" + self.name + '\n name of manager is :' + self.manager_name +'\n the league currently playing  :' + self.league 
                       

    


      
Spain = Team ('chelsea','champions league','Roberto Di Matteo',50)
Portugal = Team ('madrid','copa del rey','José Mourinho',55)


print Spain
print'\n'
print'\n'

#6
torres = Player('torres','fernando',Spain)
print torres.team
ronaldo = Player('christiano','ronaldo',Portugal)

Spain.add_player(torres)
Portugal.add_player(ronaldo)

#8
import datetime
class Match:
 def __init__(self,home_team,away_team,date):
  self.home_team=home_team
  self.away_team=away_team
  self.date=datetime.date
  self.home_score={'Essien' : 2}
  self.away_scores={'Essien':0}

  def home_score(self):
      homescore=0
  for i in (self.home_score.value()):
     homescore=homescore +i
     
  if(homescore==0):
         return 0
        
  else:
     return homescore


    def away_score(self):
           awayscore=0
  for i in (self.away_score.value()):
     awayscore=awayscore +i
     
  if(awayscore==0):
         return 0
        
  else:
     return awayscore

    def winner(self):
     h=0  
     h = self.home_score+self.away.score


#hs=Match('ho','kumasi',(datetime(2012,6,4)))
#print hs.home_score()



