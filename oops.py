# data = [1,2,3,4]
# data2 = [3,4,5,6]
# data_tuple = 1,2,3,4,'shreaya'
#
# data.append(12)
# # print(data_tuple)
# # print(data_tuple)
# data[3] = 'shreya'
# print(data)
#
# print(data_tuple)
# print(type(data_tuple))
# print(type(data))
#
# data.append(12)
#
# exit()
# # data_tuple.append(1)
#


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# print(type(data))




# data.append(12)
#
# print(data)




class shetty:
    thande = 'rishab'
    def __init__(self,father,mother,child):
        self.thande = father
        self.thayi = mother
        self.kusu = child
        self.full_family_names = father + ', '+mother+' and ' +child


    def name_leghth(self,threshold):
        len1 = len(self.thande)
        len2 = len(self.thayi)
        len3 = len(self.kusu)
        return len1+threshold,len2+threshold,len3+threshold



shetty.thande = 'rakshith'
# fam1.thande = 'name'
fam1 = shetty('raj shetty','sheetal shetty','prajwal shetty')
fam2 = shetty('shetty','shetty','shetty')
fam1.thande = 'name'
print(fam1.thande)
print(fam2.thande)

# print(shetty.thande)
exit()
#
print(fam1.name_leghth(1))
print(fam2.name_leghth(1))
# exit()


data = [1,2,3]
data.append(2)
print(data)



fam2 = shetty('a','d','k')
print(fam2.full_family_names)


exit()
fam2 = shetty()

fam2.father = 'rishab'
fam2.mother = 'pragathi'
fam2.doughter = 'ira'


print(fam1.son)
print(fam2.mother)


d = fam1.name_leghth(1)
print(d)
