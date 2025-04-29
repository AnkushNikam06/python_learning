# Tuple: 

- Tuple indicates using parantheses and are immutable (Unchanged)

- You can read the tuple objects using indexes like list.

- You can perform slicing with tuples. 

- Can measure the length of the tuple.

- append and insert methods will not work as tuples are immutable.

- You can concatenate the tuples together like below:
        e.g. tuple1 = ('a', 'b', 'c')
             tuple2 = ('x', 'y', 'z')
        result = tuple1 + tuple2
        print(result)
    Then the result will be result = ('a','b','c','x','y','z')

- Ask the question: You can ask questions similar to lists for tuple using if condition.
        e.g. result = ('a','b','c','x','y','z')
             if c in result:
                print("variable c is present in the tuple")

- Duplication: You can check the count if the duplicate values are available in the tuple.
        e.g. tuple = ('a','b','c','x','c','z')
             tuple.count('c')
    Then the output will be: 2 as there are two variables c in the tuple.

- Tuple to tuple assignment: You can assign the values of one tuple to another tuple. 
        e.g. tuple1 = ('a','b','c')
             (x,y,z) = tuple1
        If you print the x, then the result will be a.

- Nesting tuple: You can perform the nesting with tuples similar to lists.
        e.g. tuple1 = ("string1", (1,2,3), "string2")
