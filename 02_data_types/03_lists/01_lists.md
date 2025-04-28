# Lists:

- append: This will add the value in the list on the last spot.
            e.g. country = ["India", "USA", "Germany", "Australia"]
               country.append("England")
            Then the result will be country = ["India", "USA", "Germany", "Australia", "England"]

- Questions: We can ask python a question like below example using conditional statement. It will print the result as per the print function mentioned in the condition.
            e.g. country = ["india", "usa", "russia", "UK"]
                    if "England" in country:
                        print("England is present in the list")
            The result will be: NULL as England is not in the list

                 country = ["india", "usa", "russia", "UK", "England"]
                    if "England in country":
                        print("England is present in the list")
            The result will be: England is present in the list

- pop: To remove the last item in the list, we uses pop method.
            e.g. country = ["india", "usa", "russia", "UK", "England"]
                    country.pop()
            It will print the result: 'England'  >>> The country "England" will be removed from the list as it is present in the last position.

- remove: If you want to remove the country from the middle of the list then we can use remove method.
            e.g. country = ["india", "usa", "russia", "UK", "England"]
                    country.remove("usa")
            The result will be: country = ["india", "russia", "UK", "England"]

- insert: If you want to add any value at any position, then we will use insert method.
            e.g. country = ["india", "russia", "UK"]
                    country.insert(3, "England")
            Then the result will be country = ['india', 'russia', 'UK', 'England']

- copy: If you want to copy the list, you can use the copy method.
            e.g. country = ["india", "russia", "UK"]
                 international_countries = country
            >>> Then it will add the reference of international_countries to country in the memory. Therefore, both the list will point to the same value in the memory. It will not create a copy of the list

                 country = ["india", "russia", "UK"]
                 international_countries = country.copy()
            >>> Then it will create another list in the python memory. Therefore, both the lists will reference the different lists in the python memory.