# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random
import decimal
import leaderboard as lb

#-----game configuration----
spotColor = "pink"
turtleSize = 2
turtleShape = "circle"
fontSetup = ("Arial", 20, "normal")
scoring = 0
timerMax = 3.0
timer = 3.0
counter_interval = 100
timer_up = False
leaderboardFile = "a122_leaderboard.txt"
playerName = input("What's your name? ")

#-----initialize turtle-----
clickMe = trtl.Turtle()
clickMe.shape(turtleShape)
clickMe.shapesize(turtleSize)
clickMe.fillcolor(spotColor)
scoreWriter = trtl.Turtle()
scoreWriter.hideturtle()
scoreWriter.penup()
scoreWriter.goto(150, 150)
scoreWriter.pendown()
counter =  trtl.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(-150, 150)
counter.pendown()
#-----game functions--------
def UpdateScore():
  global scoring
  scoring += 1
  scoreWriter.clear()
  scoreWriter.write(scoring, font=fontSetup)
  
def ChangePos(x, y):
  global timer_up
  if (timer_up == False):
    global timer, timerMax
    timerMax -= 0.1
    timer = timerMax
    timer = round(timer, 2)
    tooClose = True
    xCompareTwo = 0
    yCompareTwo = 0
    while (tooClose == True):
      xCompare = x
      yCompare = y
      xCompareTwo = random.randint(-150, 150)
      yCompareTwo = random.randint(-150, 150)
      if (abs(xCompareTwo - xCompare) > 50):
        tooClose = False
      if (abs(yCompareTwo - yCompare) > 50):
        tooClose = False
    clickMe.penup()
    clickMe.goto(xCompareTwo, yCompareTwo)
    UpdateScore()
  
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=fontSetup)
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=fontSetup)
    timer -= 0.1
    timer = round(timer, 2)
    counter.getscreen().ontimer(countdown, counter_interval) 

def manage_leaderboard():

  global scoring
  global clickMe

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboardFile)
  leader_scores_list = lb.get_scores(leaderboardFile)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or scoring >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboardFile, leader_names_list, leader_scores_list, playerName, scoring)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, clickMe, scoring)

  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, clickMe, scoring)
#-----events----------------
clickMe.onclick(ChangePos)
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval)
wn.mainloop()