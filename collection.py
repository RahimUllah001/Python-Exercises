#collections: 1 counter, 2 namedtuple,orderdict,defautdict,deque

from collections import Counter, namedtuple, OrderedDict,   defaultdict,deque

'''This module implements specialized container datatypes providing alternatives to Python's general purpose built-in containers, dict, list, set, and tuple.

namedtuple factory function for creating tuple subclasses with named fields
deque list-like container with fast appends and pops on either end
ChainMap dict-like class for creating a single view of multiple mappings
Counter dict subclass for counting hashable objects
OrderedDict dict subclass that remembers the order entries were added
defaultdict dict subclass that calls a factory function to supply missing values
UserDict wrapper around dictionary objects for easier dict subclassing
UserList wrapper around list objects for easier list subclassing
UserString wrapper around string objects for easier string subclassing'''



a = 'aaaaaaaaaaannnnnnnnnnnnnnnnbbbbbbbbbbbbbbbbcccccccccccccccccc'

b = Counter(a)
print(b)        #Counter({'c': 18, 'n': 16, 'b': 16, 'a': 11})
print(b.items())        #dict_items([('a', 11), ('n', 16), ('b', 16), ('c', 18)])

print(b.keys())     #dict_keys(['a', 'n', 'b', 'c'])
print(b.values())   #dict_values([11, 16, 16, 18])
print(b.most_common(2))    #[('c', 18), ('n', 16)]
print(list(a) )   #['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c']

# /////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////

# namedTuple

point = namedtuple('point','x,y')
pt = point(1,9)     #point(x=1, y=9)        actually this create a point class
print(pt)
print(pt.x,pt.y)


# ///////////////////////////////////////
# ///////////////////////////////////////
# ///////////////////////////////////////
# ///////////////////////////////////////
ordered_dict = OrderedDict()
ordered_dict = {}       # both above and this is same}
ordered_dict['d'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['a'] = 4

print(ordered_dict)     #OrderedDict([('d', 1), ('b', 2), ('c', 3), ('a', 4)])


# //////////////////////////////////////////////////
# //////////////////////////////////////////////////
# //////////////////////////////////////////////////
# //////////////////////////////////////////////////
# defaultdict
d = defaultdict(int)

d['a'] = 1
d['b'] = 2
d['c'] = 3

print(d)    #defaultdict(<class 'int'>, {'a': 1, 'b': 2, 'c': 3})
print(d['e'])       #so as here it is declared as default so it will not give an error but will give zeroa sin integer


# //////////////////////////////////////////////////
# //////////////////////////////////////////////////
# //////////////////////////////////////////////////
# //////////////////////////////////////////////////
# deque : double ended que i.e actually a list upon which we can do opeerration from bith sides


d1 = deque()

d1.append(1)
d1.append(2)
d1.append(3)
d1.append(3)
d1.append(3)

print(d1)
d1.appendleft(4)

print(d1)

d1.pop()        #delete one element
d1.pop()

print(d1)

d1.popleft()

print(d1)

d1.extend([6,7,8])      #deque([1, 2, 3, 6, 7, 8])


print(d1)


d1.extendleft([9,11])       #deque([11, 9, 1, 2, 3, 6, 7, 8])

print(d1)

d1.rotate()     #deque([8, 11, 9, 1, 2, 3, 6, 7])

d1.rotate(2)        #i.e rotate two place deque([6, 7, 8, 11, 9, 1, 2, 3])
d1.rotate(-1)#from left side

# d1.clear()
print(d1)