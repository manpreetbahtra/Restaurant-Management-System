function registerUser()
    username = input("Enter username:")
    password = input("Enter password:")
    confirmPassword = input("Re-type password for confirmation:")
    if username == '' then //validations so that valid login details can be created
        print ("error")
    else if password == "" then
        print ("error")
    else if confirmPassword =="" then
        print ("error")
    else if password != confirmPassword then
        print ("error") //Validation check to ensure password has been entered correctly
    else if len(username) <=4 then
        print ("error")
    else if len(password) <= 7 or len(password) >= 14  then
        print ("error")
    else
        myFile = openWrite(username) //opens and writes username and password to a new file 
        myFile.writeLine(username)
        myFile.writeLine(password)
        myFile.close()
        print("Registered!") 
    endif
endfunction


