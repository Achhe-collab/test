class student:
    rise = 0.25
    count = 0
    def __init__(self,hesru,krama_sanke,masika,anka,vvethana):
        self.name = hesru
        self.id  = krama_sanke
        self.sem = masika
        self.marks = anka
        self.email = self.name+'.'+str(self.id)+'@pes.com'
        self.ammount = vvethana
        student.count = student.count+1

    def extra_activities(self,havsaya):
        self.hobby = havsaya

    def hike(self):
        self.hike_in =(1+student.rise)*self.ammount
        print(self.hike_in )
        return self.hike_in
    def account_balance(self):
        intial = 1000
        final_ammont = intial+self.hike_in
        print(final_ammont)

    @classmethod
    def rise_percentage(cls,rise):
        cls.rise=rise
        return cls.rise

    @classmethod
    def from_string(cls,data):
        data = data.split('-')
        hesru, krama_sanke, masika, anka, vvethana = data[0], int(data[1]), int(data[2]), float(data[3]), int(data[4])
        return cls(hesru, krama_sanke, masika, anka, vvethana)
    @staticmethod
    def announcement():
        return print('hello You are suspended')



class pg_student(student):
    # pass
    def __init__(self,hesru,krama_sanke,masika,anka,vvethana,paper,plants = []):
        super().__init__(hesru,krama_sanke,masika,anka,vvethana)


        self.paper = paper
        self.plants = plants
    def add_plants(self,plant_name):
        if plant_name not in self.plants:
            self.plants.append(plant_name)
    def remove_plants(self,plant_name):
        if plant_name in self.plants:
            self.plants.remove(plant_name)
    def print_plant_names(self):
        print(self.plants)

    def pg_hike(self):
        if len(self.plants)>2:
            student.rise_percentage(0.6)
            print(self.hike())
            return self.hike()
        else:
            return self.hike()


pg_s1 = pg_student('rani',11,11,0.2,2000,'maths')
# print(pg_s1.hike())
pg_s1.add_plants('abc')
pg_s1.add_plants('mango')
pg_s1.add_plants('cjed')
# pg_s1.remove_plants('abc')
# pg_s1.remove_plants('mango')

print(pg_s1.pg_hike())

# pg_s1.remove_plants('abc')

# print(pg_s1.print_plant_names())
# pg_s2 = pg_student('anuj',13,5,0.5,3000,'LA')
# print(pg_s1.paper)
# print(pg_s2.paper)

# print(help(pg_student))
exit()


# stud1 = student('raju',12,4,.8,1000)
data = 'raju-12-4-0.8-2000'
stud1_using_string = student.from_string(data)
stud1_using_string.rise = .4
print(stud1_using_string.hike())
print(stud1_using_string.announcement())

# print(stud1)
exit()
stud2 = student('rani',11,13,0.9,2000)
stud3 = student('anuj',13,5,0.5,3000)
print(student.count)


print(student.__dict__)
# student.rise = 0.5
# print(student.__dict__)


# stud1 = student('raju',12,4,0.8,2000)

data = 'raju-12-4-0.8-2000'
data = data.split('-')
name,num1,num2,num3,num4 = data[0],int(data[1]),int(data[2]),float(data[3]),int(data[4])
print(data)
stud1 = student(name,num1,num2,num3,num4)
print(stud1.hike())




# stud1.rise_percentage(.1)
# print(stud1.hike())
# stud1.rise = 0.9
# print(stud1.__dict__)
# print(stud1.hike())
# # print(stud1.hike())
# # exit()
# stud1.rise = .1
# print(stud1.__dict__)
#
# exit()
#
# stud2 = student('rani',15,4,0.9,2000)

#stud3  = student('kiran',16,8,.5,2000)

# print(stud1.hike())
# print(stud2.hike())
# print(stud3.hike())
#
# exit()
#
# print(stud1.name)
# print(stud1.email)
#
# stud1.extra_activities('singing')
#
# print(stud1.hike())
# print(stud1.__dict__)