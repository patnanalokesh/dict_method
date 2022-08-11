# book={
#     1:"Pthon Programming",
#     2:"Core Python Programming",
#     3:"Advance Python Programming",
#     5.7:'7pm',
#     'p':'Python'
# }
# print(book[3])
# print(book[10])   # KeyError: 10

# g={1:"",2:"Python",3:7,4:6.5,5:[1,4],6:(4,2),7:{4,5},8:{3:"world"}}
# # print(g[1],type(g[1]))
# # print(g[2],type(g[2]))
# print(g,type(g))  #{1: '', 2: 'Python', 3: 7, 4: 6.5, 5: [1, 4], 6: (4, 2), 7: {4, 5}, 8: {3: 'world'}} <class 'dict'>
# print(g.keys())  #  dict_keys([1, 2, 3, 4, 5, 6, 7, 8])
# print(g.values())  # dict_values(['', 'Python', 7, 6.5, [1, 4], (4, 2), {4, 5}, {3: 'world'}])
# print(g.items())  #  dict_items([(1, ''), (2, 'Python'), (3, 7), (4, 6.5), (5, [1, 4]), (6, (4, 2)), (7, {4, 5}), (8, {3: 'world'})])

# g={1:"",2:"Python",3:7,4:6.5,5:[1,4],6:(4,2),7:{4,5},8:{3:"world"}}
# g.clear()
# print(g)  #{}

# a=[120,122,123,125,128,130]
# print(dict.fromkeys(a,'p'))
# print(dict.fromkeys(a,54))
# print(dict.fromkeys(a,"a"))

# g={1:"",2:"Python",3:7,4:6.5,5:[1,4],6:(4,2),7:{4,5},8:{3:"world"}}
# # print(g.get(4))
# # print(g.get(45)) #None
# # print(g[44])  #KeyError:44
# # g.pop(2)
# # print(g)
# g.popitem()
# print(g)

# g={1:"",2:"Python",3:7,4:6.5,5:[1,4],6:(4,2),7:{4,5},8:{3:"world"}}
# g.update({7: 'Lokesh'})
# print(g)
# g.update({9:'lokesh143'})
# print(g)

# g={1:"",2:"Python",3:7,4:6.5,5:[1,4],6:(4,2),7:{4,5},8:{3:"world"}}
# g.setdefault(8,'lokesh')
# print(g)
# g.setdefault(10,'loki')
# print(g)

# print(dir(dict()))