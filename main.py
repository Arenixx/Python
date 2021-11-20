import os

#input your pw list name including the file extension
pwlist = input("PW Name?")
pass_file = open(pwlist, "r")

#read password, remove space, select command and print password once found
for password in pass_file:
  password = password.replace("\n","")
  cmd = "unzip -P " + password + " goal.zip"
  print(f"Password is: {password}")
  print(cmd)
  os.system(cmd)