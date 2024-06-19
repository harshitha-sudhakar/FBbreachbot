#Breach Bot Starter Code
breachYear = 2019

#Greets user
print("Hello! I'm Breachbot.\n")
userName = input("What is your name?\n")
print("\nNice to meet you " + userName + "\n")

#Recounts year of breach
todaysYear = input("What year is it?\n")
timePassed = int(todaysYear) - breachYear
print("\nWow! That means it has been " + str(timePassed) + " years since the Facebook Breach.\n")


#Introduces breach
print("Would you like to learn about the 2019 Facebook Breach? \n")
giveInfo = input("\nType 'yes' or 'no'\n")

#Explains breach
while giveInfo.lower() == "yes":
  print("\nWhat would you like to learn more about? Enter the lowercase letter of the following options: \n(a) breach details, \n(b) organization's response, \n(c) i would like to hear your reflection, or \n(d) none\n")
  topic = input()
  
  if topic.lower() == "a":
    print("\nSensitive information such as phone numbers, full names, locations, email addresses were posted to a hacking forum. Hackers breached data by exploiting a feature on Facebook that allowed users to find others through phone numbers.\n")
  
  elif topic.lower() == "b":
    print("\nThe company fixed the issue in August 2019, ensuring that data could not be breached from the same route. Facebook did not notify users of the breach, considering that people could not take further action on information that had already been made public.\n")
  
  elif topic.lower() == "c":
    break
    
  else:
    print("\nSorry, I didn't catch that. Choose one of the options listed.\n")
  
  input("\nPress enter to continue\n")

#Introduces my take
print("\n I'm excited to share my perspective with you. Are you ready to hear my take?")
giveInfo = input("Type 'yes' or 'no'\n")

#Shares my take
while giveInfo.lower() == "yes":
  print("\nWhat would you like to learn more about? Enter the lowercase letter of the following options: \n(a) relation to CIA Triad, \n(b) my reaction, \n(c) my advice, \n(d) none\n")
  topic = input()

  if topic.lower() == "a":
    print("\nSensitive information such as phone numbers, full names, locations, email addresses were posted to a hacking forum. Hackers breached data by exploiting a feature on Facebook that allowed users to find others through phone numbers.\n")

  elif topic.lower() == "b":
    print("\nThe company fixed the issue in August 2019, ensuring that data could not be breached from the same route. Facebook did not notify users of the breach, considering that people could not take further action on information that had already been made public.\n")

  elif topic.lower() == "c":
    print("\nI would convince victims to take action by creating a new strong password with a password manager so they can keep track of it\n")
    
  elif topic.lower() == "d":
    break
  else:
    print("\nSorry, I didn't catch that. Choose one of the options listed.\n")

  input("\nPress enter to continue\n")
#Chatbot ends conversation
print("\nThanks for chatting with me, and I hope you learned something new!\n")