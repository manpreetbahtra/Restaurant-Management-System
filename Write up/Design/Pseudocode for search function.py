function searchItem()
    if typed == "" then
        print(listOfItems)
    else
        data = []
        for item in listOfItems:
            data.append(item)
        next item
        print(data)
    endif
endfunction


listOfItems = ["chips", "vegBurger", "cinnamonRolls", "pepsi", "coke", "BeefStew"]
