# Strings:
Below are the different methods you can use with strings.
- strip(): Use to remove the extra spaces before and after the string.
        e.g. a = "  Hello World    "
                 print(a.strip())
        This will remove the extra spaces before and after the string like a=Hello World

- split(): This converts the strings into lists 
        e.g. a = "I love my country"
                 print(a.split(", "))
        This will convert the string into list like a=["I", "love", "my", "country"]

- format(): This is used to add the reference of the variable to the string
        e.g. Country = "India"
             Ethnicity = "Asian"
             Description = "{} is an {} country"
        Description     >>> (If we enter the Description variable then it will show the output as it is)
         '{} is an {} country'

            print(Description.format(Country, Ethnicity)) >>> (This will add the reference of the above variables to the string and will show the full output)
         The result will be "India is an Asian country"

- "".join(): This used to convert the list into string
        e.g. a=["I", "love", "my", "country"] >>> (This is a list)
             print("".join(a))
        This will show the string like "Ilovemycountry".
        If you wish to add the space, then we can add the space in the double quotes before join like below
             print(" ".join(a))  >>> (This will add the space in between the words)
        The result will be "I love my country" >>> (Note: You can add any character like #,$,% etc )

- len(): This will count the length of the string or list or tuple
        e.g. a="India"
             print(len(a))
        The result will be 5 as it starts length counting from 1 and indexes starts from 0.


# Different things we can use with strings:
- raw-string: It also named as rstring and when we are working on windows OS, we uses this string type.
              e.g. when we are trying to print a path in windows
                   a = "c:\users\system32"  
        >>> This will print an error when we will try to give value of the path to the variable
              To resolve this, we uses raw string by adding r before string like,
                   a = r"c:\users\system32"
                   print(a)
              The result will be: c:\users\system32

- slashing: We can use slashing while adding strings into the string.
              e.g. If we enter the below code 
                    a = "He said, "He loves his country""
        >>> This will print an error that the syntax is invalid. It will consider the double quotes after comma as a end of the string. To avoid this we can use the string like below.
                    a = "He said, \"He loves his country\" "
              The result will be: 'He said, "He loves his country"'

- Enter: This is denoted by \n. To add the enter in the programming, we can add the \n after each line where code completes.

- Questions: We can ask python a question like below example. It will print the result in the boolean value.
            e.g. List:
                 country = ["india", "usa", "russia", "UK"]
                 print("usa" in country)
            The result will be: True

            e.g. String
                 country= "india, usa, russia, uk"
                 print("usa" in country)
            The result will be: True
                 print("germany" in country)
            The result will be: False