#we build list with square bracket
#name  a collection of values
#contain different types
#specific fuctionality and behavior
hall = 11.25
kit = 18.0
_bed = 10.75
bed = 111.96
#create list areas
areas = [11.5," Church", _bed]
#print(areas)
#subsets of list
areas2 = [
    ["value", 334],
    ["value2", 449]
]
#print(areas2[1])

fam = ['lisa',1.74, 'emma,', 1.68, 'mom', 1.83]
#removes 'emma'

del(fam[2])
fam_ext = fam + ['dad', 3.5 ]
#print(fam_ext)


a = [2, 3, 4, 5, 7]
y = list(a)
del(y[2])
y[3]= "34"
print(y)