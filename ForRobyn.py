import time, random, os
import numpy as np
from tkinter import *
import matplotlib.pyplot as plt
from PIL import Image


progressBar = 'LiamsLove ### Thisisus #### Piano ####### Cactuses #### Tik Tok ##### dance ####### breakfast ### Massage ##### Ottawa ###### Fish ######### Gift card!!'

#Functions
  
def questions():
  Question = []
  Options= []
  Answer = []
  MultipleQuestions = ['How many years of competitive basketball did liam play?', ['5', '6', '7', '8'], '7',  
  'Where was liams first job?', ['NoFrills', 'Walmart', 'Tim Hortons', 'Camp Counsellor'], 'NoFrills', 
  'What is our home song?', ['Im yours', 'I wont give up', 'Banana Pancakes', 'Channel'], 'I wont give up',
  'Where was the first place we held hands?', ['Movie Theatre', 'Library', 'Ski Hill', 'Other'], 'Ski Hill',
  'How many houses did Liam live in as a child (to 18)?', ['2', '3', '4', '5'], '4',
  'What is Liams favourite instrument?', ['Guitar', 'Chello', 'Piano', 'Violin'], 'Piano',
  'What was the name of the artist of the first country album Liam listened to?', ['Eric Church', 'Luke Bryan', 'Thomas Rhett', 'Zac brown Band'], 'Thomas Rhett',
  'What NBA basketball team did liam see in person?', ['Miami Heat', 'Milwaukee Bucks', 'Los Angeles Lakers', 'Toronto Raptors'], 'Toronto Raptors',
  'Which superpower would liam pick?', ['Super Strength', 'Super Speed', 'Flight', 'laser eyes'], 'Super Speed',
  'What was the first thing Liam sketched in his notepad?', ['Cow', 'Sword', 'Samourai', 'Mountains'], 'Samourai',
  'Does Liam or Robyn love the other person more?', ['Liam', 'LIAM in all caps', 'Still Liam', 'Robyn'], 'all',
  'If Liam could improve one aspect of his boyfriend skills, which would it be?', ['Listening', 'Memory', 'Being more fun', 'better planner'], 'all',
  'What is liams favourite kind of jewelery?', ['Anklet', 'Necklace', 'Earring', 'Bracelet'], 'Bracelet',
  'What is Liams favourite drink of all time?', ['Ginger Ale', 'Mango-apple-ginger ale mix', 'chocolate milk', 'pops cream soda'], 'Mango-apple-ginger ale mix']
  Array = range(int(len(MultipleQuestions)/3))
  multiplequestion = random.sample(Array, 8)
  for x in multiplequestion:
    Question.append(MultipleQuestions[x*3])
    Options.append(MultipleQuestions[x*3+1])
    Answer.append(MultipleQuestions[x*3+2])
    
  #Long Answer
  LongQuestions = ['what was the name of the suburb we lived in back in Brisbane?', 'kangaroo,point', 'what was the name of the #1 food place in South Bank?', 'gnocchi,brothers', 
  'What was the name of the Hobbit workshop we visited in new Zealand?', 'weta', 'What was the name of Liams competitive basketball team?', 'hornets']
  Array = range(int(len(LongQuestions)/2))
  longquestion = random.sample(Array, 2)
  for x in longquestion:
    Question.append(LongQuestions[x*2])
    Answer.append(LongQuestions[x*2+1])

  return(Question, Options, Answer)



def picture():
  pictures = []
  for file in os.listdir("pictures/"):
    if file.endswith(".JPG"):
      pictures.append(os.path.join("pictures/", file))
    if file.endswith('.PNG'):
      pictures.append(os.path.join("pictures/", file))
  ImageAddress = random.choice(pictures)
  ImageItself = Image.open(ImageAddress)
  ImageNumpyFormat = np.asarray(ImageItself)
  plt.imshow(ImageNumpyFormat)
  plt.draw()
  plt.pause(3) # pause how many seconds
  plt.close()



def Check(Option, Answer):
  global correct
  global guess  
  correct = False
  if guess == 0:
    if Option == Answer:
      correct = True
      print('Yayyyy, you got it baby, great work!!\n')
    elif Answer == 'all':
      correct = True
      print('Yayyyy, you got it baby, great work!! They were all the right answer... Ill be sure to record that for future use though hehe\n')
    else:
      print('Oh darn it, nice try my love. You got the next one\n')
  else:
    print('You have already guessed')
  guess = 1
  
  
  
def BoxMaker(Question, Options, Answer):
  global guess
  global correct
  guess = 0
  top = Tk()  
  top.geometry("1200x400")  

  b1 = Button(top,text = Options[0],command = lambda: Check(Options[0], Answer),activeforeground = "red",activebackground = "pink",pady=10)  

  b2 = Button(top, text = Options[1],command = lambda: Check(Options[1], Answer),activeforeground = "blue",activebackground = "pink",pady=10)  

  b3 = Button(top, text = Options[2],command = lambda: Check(Options[2], Answer),activeforeground = "green",activebackground = "pink",pady = 10)  

  b4 = Button(top, text = Options[3],command = lambda: Check(Options[3], Answer),activeforeground = "yellow",activebackground = "pink",pady = 10)

  b5 = Button(top, text = 'Next Question' ,command = top.destroy,activeforeground = "yellow",activebackground = "pink",pady = 10, padx = 40)
  
  b6 = Button(top, text = Question, activeforeground = "yellow", activebackground = "pink", pady = 10, padx = 40)
  
  b7 = Button(top, text = 'suprise button', command = lambda: picture(),activeforeground = "yellow",activebackground = "pink",pady = 10)

  b1.pack(side = LEFT)  

  b2.pack(side = LEFT)  

  b3.pack(side = RIGHT)  

  b4.pack(side = RIGHT)

  b5.pack(side = BOTTOM)
  
  b6.pack(side = TOP)
  
  b7.pack(side = BOTTOM)

  top.mainloop() 



#Instantiate variables
adjectives = []
count = 0
questionssofar = 0
progress = '--'
Arrow= '>'

#Script
print('Loading...')
time.sleep(0.5)
print('       $¦$¦$¦$ ____ $¦$¦$¦$')
time.sleep(0.5)
print('      $¦$_____$$__$$_____$¦$')
time.sleep(0.5)
print('     $¦$________$$________$¦$')
time.sleep(0.5)
print('    $¦$____________________$¦$')
time.sleep(0.5)
print('     $¦$__________________$¦$')
time.sleep(0.5)
print('      $¦$_______________$¦$')
time.sleep(0.5)
print(' (¯`.´¯)$¦$___________$¦$(¯`.´¯)')
time.sleep(0.5)
print('(¯≻ ✦ ≺¯) $¦$_______$¦$ (¯≻ ✦ ≺¯)')
time.sleep(0.5)
print(' (_.^._)____$¦$___$¦$____(_.^._)')
time.sleep(0.5)
print('     (¯`.´¯) __$¦$__ (¯`.´¯)')
time.sleep(0.5)
print('    (¯≻ ✦ ≺¯) _ $_  (¯≻ ✦ ≺¯)')
time.sleep(0.5)
print('     (_.^._) (¯`.´¯)_(_.^._)')
time.sleep(0.5)
print('            (¯≻ ✦ ≺¯)')
time.sleep(0.5)
print('     (¯`.´¯) (_.^._) (¯`.´¯)')
time.sleep(0.5)
print('    (¯≻ ✦ ≺¯) _____ (¯≻ ✦ ≺¯)')
time.sleep(0.5)
print('     (_.^._) ______  (_.^._)')


garb = input("Hello My beautiful Angel, Happy 4 and a half years my love. Please hit enter to continue \n")
garb = input("Today, we will be doing a fun quiz for some fun prizes!!!\n")

garb = input('You will have 10 questions, 8 multiple choice and 2 written answer ones. The prizes are based on your score.\nYou get to win all the prizes at and below your score. if you are excited, type yayyyyyy and hit enter\n')
if "yay" in garb.lower():
  garb = input("whooooh, glad we are excited my love. here are some of the great prizes you can win. Don't forget you win all the prizes at and below your score!! \n")
else: 
  garb = input("whaat?? not excited... well no worries my love we can fix that with prizes :). Don't forget you win all the prizes at and below your score!! \n")

garb = input("0 questions right --> a great big hug and Liam's love forever \n1 question right --> 1 full episode of This is us without Liam getting up or fidgeting at all \n(Hit enter)")
garb = input("2 questions right --> 1 priority song request on the piano \n3 questions right --> 1 new cactus from Needhams for both of us \n(Hit enter)")
garb = input("4 questions right --> 1 short tik tok video of your choice \n5 questions right --> We will learn 1 dance together just in case there is ever an impromptu dance battle \n(Hit enter)")
garb = input("6 questions right --> 5 get up for breakfast tickets \n7 questions right --> 1 hour of massage of your choice \n(Hit enter)")
garb = input("8 questions right --> Day trip to Ottawa (museums? Parliament hill? Shopping? fun?) \n9 questions right --> we will buy a beta fish in sudbury \n(Hit enter)")
garb = input("Grand Prize!!!! We look on scene and find out what we want to redeem for 100$ hehehe \n(Hit enter)")

garb = input("Awesome my love, do you have any questions? (yes/no)\n")
put = garb

if put.lower() == 'no':
  garb = input("Alrighty, now that everything has been explained, we can continue to the quiz. \n(Hit enter when ready to start)")
elif put.lower() == 'yes':
  garb = input("Well, you better go ask the real Liam cause I am just a simple computer program, cant really interpret my own input now can I?\n\n I'll wait for you to get those questions clarified. Just hit enter when you are ready\n")
else:
  garb = input("That wasn't a yes or no answer... so unfortunately you missed your chance. Here comes the real quiz \n(Hit enter when ready to start)")
Question, Options, Answer = questions()
# print(Question)
# print(Options)
# print(Answer)







#Beginning of quiz loops
for z in range(8):
  BoxMaker(Question[z], Options[z], Answer[z])
  questionssofar +=1
  if correct == True:
    count += 1
    progress = progress + '--------------'
  print(progressBar)
  garb = input(progress + Arrow +'\n Here is your progress love. you are currently {} for {}. Good luck with the next question, hit enter when you are ready!!\n'.format(count,questionssofar))

garb = input('At the end of the multiple choice, you are currently {} for {}. Good luck with the short answer questions, my love hit enter when you are ready!!\n'.format(count,questionssofar))

for z in range(2):
  answer1 = Answer[8+z]
  answer = input(Question[8+z] +'\n')
  correct = 0
  questionssofar +=1
  for x in answer1.split(','):
    if x in answer.lower():
      count += 1
      progress = progress + '--------------'
      correct = 1
      print('Great work love!! on a tough long answer question too!!')
      break
  if correct == 0:
    print('Better luck next time my angel')
  if z == 1:
    print(progressBar)
    garb = input(progress + Arrow +'\n Here is how you did my love! you ended up {} for {}. Please see Liam to redeem for your prizes with proof, hit enter when you are ready!!\n'.format(count,questionssofar))
  else:
    print(progressBar)
    garb = input(progress + Arrow +'\n Here is your progress love. you are currently {} for {}. Good luck with the next question, hit enter when you are ready!!'.format(count,questionssofar))  
  
print('Thanks for playing!!!')
print('____________________██████\n' +
'_________║║║║____█████████\n'+
'__  Ӝ̵Ʒ║║║║=║____║=║║║║║\n'+
'__ ║║║_║║║║▀●____●▀▀║║║║\n'+
'_║║║║_║║║║║▀▀__▀▀▀▀║║║║\n'+
'_ ║║║║_║║║║▀▀♥__♥▀▀▀║║║\n'+
'__ ║║║___║║▀▀_____▀▀▀║║\n'+
'║║║║║____║▀▀_____▀▀║\n'+
'_ ║║____ █║█║█___ ████\n'+
'_______ █║█║█║█_ ██████\n'+
' _______█║█║█║█__████████\n'+
'  _____ █║█║█║█__██████ ███\n'+
'   _ ___█║█║█║█__██████ _███\n'+
'   _║║X║║║║║║║___██████_ ███\n'+
'   ║║_██████║║___██████_ ███\n'+
'   ║_███████║║___██████_ ███\n'+
'   _████████║║___██████ _███\n'+
'   _████████║║___║║║║║║_██\n'+
'   _████████║║___║║║║║║\n'+
'   _████████║║___║║║║║║\n'+
'   __████████║___║║║║║║\n'+
' _______█████____║║║║║║\n'+
'_______█████ _____║║║║║\n'+
'_______█████_____ ║║║║║\n'+
'_______█████ _____║║║║║\n'+
'________████______║║║║║\n'+
'________█████____█████\n'+
'_▀█║────────────▄▄───────────​─▄──▄_\n'+
'──█║───────▄─▄─█▄▄█║──────▄▄──​█  █║\n'+
'──█║───▄▄──█║█║█║─▄║▄──▄║█║─█║​█║▄█║\n'+
'──█║──█║─█║█║█║─▀▀──█║─█║█║─█║​─▀─▀\n'+
'──█║▄║█║─█║─▀───────█║▄█║─▀▀\n'+
'──▀▀▀──▀▀────────────▀─█║\n'+
'───────▄▄─▄▄▀▀▄▀▀▄──▀▄▄▀\n'+
'──────███████───▄▀\n'+
'──────▀█████▀▀▄▀\n'+
'────────▀█▀\n'+
'Final score of {}'.format(count))


