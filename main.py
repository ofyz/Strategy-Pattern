import random
#from abc import ABC, abstractmethod

#context class?
class Assignment: 

  #3 types of assignments and time calculation
  _cs240 =6
  _cs342=5
  _seniorProject=10
  _completedPercentage=0

  def work_on_cs240(self):
    self._cs240=self._cs240-1
    self._completedPercentage=100-((100*self._cs240)/6)
    print("Worked 1 hour on cs240, completed percentage:" + str(self._completedPercentage))

  def work_on_cs342(self):
    self._cs342=self._cs342-1
    self._completedPercentage=100-((100*self._cs342)/5)
    print("Worked 1 hour on cs342, completed percentage:" + str (self._completedPercentage))


  def work_on_seniorProject(self):
    self._seniorProject=self._seniorProject-1
    self._completedPercentage=100-((100*self._seniorProject)/10)
    print("Worked 1 hour on seniorProject, completed percentage:" + str (self._completedPercentage))

  def showRemainingHours(self):
    print("Remaining CS240: ",self._cs240)
    print("Remaining CS342: ",self._cs342)
    print("Remaining Senior Project: ",self._seniorProject)


 
#abstract strategy class?
class Student():

  availableHours=0
  totalHours=24

  #students attributes
  healthLevel=random.randrange(1,11, 1)
  nutritionLevel=random.randrange(1,11, 1)
  restLevel=random.randrange(1,11, 1)
  anxietyLevel=random.randrange(1,11, 1)
  efficiencyLevel=random.randrange(1,11, 1)
  

  schedule={'Monday':{'sleep':7,'classes':5,'exercise':2,'eating':2,'commuting':2},
            'Tuesday':{'sleep':7,'classes':6,'exercise':2,'eating':2,'commuting':2},
            'Wednesday':{'sleep':7,'classes':2,'exercise':2,'eating':2,'commuting':2,'study':3,'rest':3},
            'Thursday':{'sleep':7,'classes':6,'exercise':2,'eating':2,'commuting':2,'study':3,'rest':1},
            'Friday':{'sleep':7,'classes':3,'recreation':10,'eating':2,'commuting':2},
            'Saturday':{'sleep':7,'classes':0,'employment':6,'eating':2,'commuting':2},
            'Sunday':{'sleep':7,'classes':0,'employment':6,'eating':2,'commuting':2,'movie':2}
            }
  #takes day as a argument calculates avaiable hours that can be worked on assignment for corresponding day
  def calculate_daily_available_hours(self,day):
    allocatedHours=0

    for key, value in self.schedule.items():
      if key==day:
        for key in value:
          allocatedHours+= value[key]
    self.availableHours=self.totalHours-allocatedHours

    return self.availableHours

  #chooses strategy that defined in strategy class
  def choose_strategy(self,strategy):
    if strategy=='1':
      st=OptismisticStrategy()
      st.work_on_assignment()


  #to adjust the number of hours of work the student can accomplish given the daily time available to work on assignments if efficiency is 10 student can work 10 hour on assignment else can work 5 houron assignment
  def manage_attributes(self):

    if self.efficiencyLevel==10:
      self.availableHours=self.availableHours
    if self.efficiencyLevel<10:
      self.availableHours=int(self.availableHours/2)

  #adds new activity to dictionary
  def add_activity(self, day, activity ,hour):
    self.schedule[day][activity]=hour

  #removes activity from dictionary
  def remove_activity(self,day,activity):
    del(self.schedule[day][activity])

  #@abstractmethod
  def work_on_assignment():
    pass

#concretestrategy class??
class OptismisticStrategy(Student):
  
  def work_on_assignment(self):
    
    print("This is optimistic strategy")
    obj.showRemainingHours()
    hour=student.calculate_daily_available_hours("Monday")
    print("Today you have ",hour," hours available to work on assignment")

    
    student.manage_attributes()
    print("Due to the your attributes you can work just ",student.availableHours,"hours")

    if obj._cs240>=student.availableHours:
      for i in range(1,student.availableHours+1):
        obj.work_on_cs240()
    else:
      for i in range(1,obj._cs240+1):
        obj.work_on_cs240()

    obj.showRemainingHours()
 
class LessSleepStategy(Student):

  def work_on_assignment():
    a=10








#for testing functions now
if __name__ == '__main__':

    student=Student()
    obj = Assignment()

    print("Welcome to the strategy center. Please select strategy!")
    val=input("Enter 1 for optimistic strategy:")
    if val=="1":
      
      student.choose_strategy("1")
    else:
      print("Wrong choice")

  

    print("------------------")
    obj = Assignment()

    print(obj._cs240)
    obj.work_on_cs240()
    print(obj._cs240)

    print(obj._cs342)
    obj.work_on_cs342()
    print(obj._cs342)

    print(obj._seniorProject)
    obj.work_on_seniorProject()
    print(obj._seniorProject)

    obj2 = Student()
    baba=obj2.calculate_daily_available_hours('Sunday')
    print(baba)

    obj3=Student()
    print(obj3.schedule)
    obj3.add_activity("Monday","iceCream",5)
    print(obj3.schedule)
    obj3.remove_activity("Monday","iceCream")
    print(obj3.schedule)


