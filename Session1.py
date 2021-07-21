"""
    This is session 2 and is suppose to explore Model
    Here we will see Single Value Container and Multi Value Container
    This documentation comment should always be in the beginning

    :Data

"""
print(__doc__)     # MAGIC VARIABLE


"""
Multi line comment

"""

"""
MODEL
1. Single Value Container      (Engagement box)
    holds a single value
    
2. Multi Value Container       (Kaju Katli Box) (Homogeneous)
    holds multiple values
     2.1 homogeneous
     2.2 heterogeneous
     
"""

# create a single value container in RAM
# stores 10 in it
# put the hash code in a
# hence, a is a reference variable which will hold HashCode of 10
# Create/ Update
a = 10
b = 10

# READ
print("a is :", a, type(a), id(a), hex(int(a)), oct(int(a)), bin(int(a)))
print("b is :", b, type(b), id(b), hex(b), oct(b), bin(b))
