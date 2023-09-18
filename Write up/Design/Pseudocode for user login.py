function login()
    username = input("Enter username:")
    password = input("Enter password:")
    file = openRead("usernameAndPasswords.txt")
    found = false
    while NOT file.endOfFile() do 
        loginDetails = file.readline() //file is read until its end 
        if loginDetails[0] == username AND loginDetails[1] == password then
            found = True //if the entered username and password both correspond to the same row, i.e. correspond to the same user, the login is successful. 
            print("Login successful")
            session()
        elseif loginDetails[0] == username then
            print("Password Incorrect")//if the entered username exists but the corresponding password does not match, login is unsuccessful.  
        else
            print("Username entered is not found, register the user before logging in")
            // if the entered username does not exist in the database, this means that the user has not registered, and login is unsuccessful. 
        endif
    endwhile
endfunction
