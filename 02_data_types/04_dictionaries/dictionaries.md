# Dictionaries:

Dictionaries can be represent as key:value pair. This should be declared in the curly braces with colon between key and value.
If you enter the wrong key, then it will show keyerror.

e.g. countries = {"asian":"india", "european":"london", "asia_pacific":"australia"}

- Enter the key: When you want to retrieve the value of the key, you can simply enter the key and it will print the value.
            e.g. countries["asian"]
        Then it will print the answer as india. If we enter the index in the bracket, then it will show an error.

- get(): You can either enter the key in the square brackets or use get to know the value of the key.
            e.g. countries.get("asia_pacific")
        Then it will print the answer as australia.

- Change the value: If you wish to change the value in the dictionary, then you can enter the key and define the new value.
            e.g. countries["asia_pacific"] = "new_zealand"
        Then the output will be {"asian":"india", "european":"london", "asia_pacific":"new_zealand"}

- Get the key from dictionary: If you want to get only keys from the dictionary then, you will have to use for loop to retrieve the keys.
            e.g. for country in countries:
                     print(country)
        Then the result will be only keys like below: 
                asian
                european
                asia_pacific

- Get only value from the dictionary: If you want to retrieve all the values only, you will have to use the for loop with different print function.
            e.g. for country in countries:
                     print(countries[country])
        Then it will show the below result:
                india
                london
                australia

- Get the key and value from the dictionary: If you want to retrieve all the keys with associated values, you will have to use the for loop with different print function.
            e.g. for country in countries:
                     print(country, countries[country])
        Then it will print the result like below:
                asian india
                european london
                asia_pacific australia

                                                OR

- Using items: Another way to print all the keys and values together is, you can add items in for loop.
            e.g. for key, value in countries.items():
                     print(key, value)
        Then it will print the same result as above:
                asian india
                european london
                asia_pacific australia

- Find value using if condition: If you want to find a value using if condition then follow the below syntax:
            e.g. if "asian" in countries:
                     print("India is an asian country")
        If the asian is present in the dictionary, then it will print "India is an asian country" or it will show empty response. We can also add "else" using print option.

- Length of the dictionary: We can count the length of the dictionary. The length will be the number of items (key:values)
            e.g. print(len(countries))
        Then the result will be 3 as the number of items are 3 i.e. key:value pair.

- Add values: You can add the extra key:value pair.
            e.g. countries["african"] = "nigeria"
        If you print the result then african as a key and nigeria as a value will be added to the dictionary.

- pop the item: You can remove any item using pop. You have to provide key if only pop is used to remove the key from any location.
            e.g. countries.pop("europian")
        It will remove europian key with value from the dictionary.
    Also, if you wish to remove the last item from the dictionary, then use the below code.
            e.g. countries.popitem()
        It will show the last item you have added and that will be removed from the dictionary.

                                                OR

- delete option: You can also use a delete operation to remove the item.
            e.g. del countries["asia_pacific"]                                    
        It will remove asia_pacific item from your dictionary as well as python backend memory.

- Add single value for multiple keys: Yes, you can add single value for multiple keys like below:
            e.g. countries = ["India", "Nepal", "Bhutan"]
                 default_value = "Asian"
                 new_dict = dict.fromkeys(countries, default_value)
        Then it will print the anwer like below:
                 print(new_dict) >>> answer: {'India':'Asian', 'Nepal':'Asian', 'Bhutan':'Asian'}

                                                IF

- You add the countries instead of default_value while definining new_dict:
           e.g.  countries = ["India", "Nepal", "Bhutan"]
                 default_value = "Asian"
                 new_dict = dict.fromkeys(countries, countries)
        Then the result will be like below:
                 print(new_dict) 
        >>> answer: {'India': ['India', 'Nepal', 'Bhutan'], 'Nepal': ['India', 'Nepal', 'Bhutan'], 'Bhutan': ['India', 'Nepal', 'Bhutan']}
