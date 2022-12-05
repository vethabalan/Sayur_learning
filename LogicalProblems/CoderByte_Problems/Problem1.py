def CodelandUsernameValidation(strParam):

  # code goes here
  if ((strParam[0].isalpha()) and (len(strParam) > 4 and len(strParam) < 25) and (strParam[0] != "_" and strParam[-1] != "_")):
    print("valid username")
  elif( (len(strParam) < 4 or len(strParam) > 25) and (strParam[0] == "_" or strParam[-1] == "_")):
    print("UserName should be above 4 and Below 25 characters")
    print("UserName does not support special character in first or last index")
  elif( (strParam[0] == "_" or strParam[-1] == "_")):
    print("UserName does not support special character in first or last index")
  elif( strParam[0].isnumeric()):
    print("UserName should not start with Numbers")
  # else:
  #   return False

  #return strParam

# keep this function call here 
CodelandUsernameValidation(input())