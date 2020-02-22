def proverka_str(str1,str2): 


  if type(str1) == str and type(str2) == str: 


  if str1 == str2: 
     return 1 
  elif str2 == 'learn': 
     return 3 
  elif len(str1) > len(str2) :
     return 2 
  elif len(str1) < (str2): 
     return - 
  else: 
return 0 

print(proverka_str("programm", "programm")) 
print(proverka_str("programm", "waitwhat")) 
print(proverka_str("programm", "learn")) 
print(proverka_str("waitwhat", "programm")) 
print(proverka_str("wait", 6))
