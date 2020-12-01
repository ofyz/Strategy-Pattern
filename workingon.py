import random
import abc
from abc import ABC, abstractmethod




class Assignment(object):
  def __init__(self, strategy= None,assignment= None):
    self.strategy = strategy
    self._cs240 =4
    self._cs342=5
    self._seniorProject=10
    self._completedPercentage=0
    self.assignment= assignment
  


  def work(self,day):
    self.strategy.work_on_assignment(self.assignment,day)

    

  def showRemainingHours(self):
    print("Remaining CS240: ",self._cs240)
    print("Remaining CS342: ",self._cs342)
    print("Remaining Senior Project: ",self._seniorProject)
 

  def work_on_cs240(self):
    self._cs240=self._cs240-1
    self._completedPercentage=100-((100*self._cs240)/4)
    print("Worked 1 hour on cs240, completed percentage:" + str(self._completedPercentage))

  def work_on_cs342(self):
    self._cs342=self._cs342-1
    self._completedPercentage=100-((100*self._cs342)/5)
    print("Worked 1 hour on cs342, completed percentage:" + str (self._completedPercentage))


  def work_on_seniorProject(self):
    self._seniorProject=self._seniorProject-1
    self._completedPercentage=100-((100*self._seniorProject)/10)
    print("Worked 1 hour on seniorProject, completed percentage:" + str (self._completedPercentage))

  #types of assignments
class cs240(Assignment):
  def __init__(self,strategy):
    super(cs240,self).__init__(strategy, "cs240")
    

class cs342(Assignment):
  def __init__(self,strategy):
    super(cs342,self).__init__(strategy, "cs342")


class seniorProject(Assignment):
  def __init__(self,strategy):
    super(seniorProject,self).__init__(strategy, "seniorProject")




class Student(object):

  availableHours=0
  totalHours=24
  worked = 0
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def work_on_assignment(self):
    pass
 

  #students attributes
  healthLevel=random.randrange(1,11, 1)
  nutritionLevel=random.randrange(1,11, 1)
  restLevel=random.randrange(1,11, 1)
  anxietyLevel=random.randrange(1,11, 1)
  efficiencyLevel=random.randrange(1,11, 1)
  def displayStats(self):
 
    print("Your Stats")
    print("healthLevel: ",st.healthLevel)
    print("nutritionLevel: ",st.nutritionLevel)
    print("restLevel: ",st.restLevel)
    print("anxietyLevel: ",st.anxietyLevel)
    print("efficiencyLevel: ",st.efficiencyLevel)

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
  def choose_strategy(self,strategy,day):
    if strategy=='1':
     
      cs240(OptismisticStrategy()).work(day)
     
      cs342(OptismisticStrategy()).work(day)
    
      seniorProject(OptismisticStrategy()).work(day)
    if strategy == '2':
      cs240(LessSleepStategy()).work(day)
     
      cs342(LessSleepStategy()).work(day)
    
      seniorProject(LessSleepStategy()).work(day)
      
    else:
      cs240(ProcrastinatorStrategy()).work(day)
     
      cs342(ProcrastinatorStrategy()).work(day)
    
      seniorProject(ProcrastinatorStrategy()).work(day)
    

  #to adjust the number of hours of work the student can accomplish given the daily time available to work on assignments if efficiency is 10 student can work 10 hour on assignment else can work 5 houron assignment
  def manage_attributes(self,val):

    if st.efficiencyLevel==10:
      st.availableHours=st.availableHours
      st.efficiencyLevel = st.efficiencyLevel/2
    if self.efficiencyLevel<10:
      st.availableHours=int(st.availableHours/2)
    if st.nutritionLevel > 7:
      st.nutritionLevel = st.nutritionLevel- 2

    if st.restLevel > 8:
      st.restLevel = st.restLevel- 3
    if st.healthLevel > 7:
      st.healthLevel = st.healthLevel- 2
    if val == 1:
      if st.anxietyLevel > 5:
        st.anxietyLevel = st.anxietyLevel - 1
    if val == 2:
      st.restLevel = st.restLevel - (st.restLevel-1)
      st.healthLevel = st.healthLevel - (st.healthLevel-1)
      st.efficiencyLevel = 10
    if val == 3:
      if st.healthLevel <= 5:
        st.healthLevel = st.healthLevel +5

      if st.nutritionLevel <= 6:
        st.nutritionLevel = st.nutritionLevel + 4



  #adds new activity to dictionary
  def add_activity(self, day, activity ,hour):
    self.schedule[day][activity]=hour

  #removes activity from dictionary
  def remove_activity(self,day,activity):
    del(self.schedule[day][activity])

  def remainingHour(self,day,availableHours):
     
    if (st.calculate_daily_available_hours(day) <= availableHours):
      self.remaining = st.calculate_daily_available_hours(day) - self.worked
   
    else:
      self.remaining = availableHours - self.worked

      st.availableHours = availableHours

      print(self.remaining)
  
    return self.remaining 
    
  def workedHour(self):
    self.worked = self.worked + 1
  
    
class OptismisticStrategy(Student):
  
  def work_on_assignment(self,assignment,day):
    
  
    st.remainingHour(day,st.availableHours)

 

    if (st.remaining ) > 0: 
      if(assignment == 'cs240'):
        if assingn._cs240>= st.remaining:
          for i in range(1, st.remaining+1):
            assingn.work_on_cs240()
            st.workedHour()
        else:
          for i in range(1, assingn._cs240+1):
            assingn.work_on_cs240()
            st.workedHour()

      if(assignment == 'cs342'):
        if assingn._cs342>= st.remaining:
          for i in range(1,st.remaining+1):
            assingn.work_on_cs342()
            st.workedHour()
        else:
          for i in range(1, assingn._cs342+1):
            assingn.work_on_cs342()
            st.workedHour()


      if(assignment == 'seniorProject'):
        if assingn._seniorProject>= st.remaining:
          for i in range(1, st.remaining+1):
            assingn.work_on_seniorProject()
            st.workedHour()
        else:
          for i in range(1, assingn._seniorProject+1):
            assingn.work_on_seniorProject()
            st.workedHour()
    else:
      print("I cannot work more")
     
 
class LessSleepStategy(Student):

  def work_on_assignment(self,assignment,day):


    st.remainingHour(day,st.availableHours)
    


    if (st.remaining ) > 0: 
      if(assignment == 'cs240'):
        if assingn._cs240>= st.remaining:
          for i in range(1, st.remaining+1):
            assingn.work_on_cs240()
            st.workedHour()
        else:
          for i in range(1, assingn._cs240+1):
            assingn.work_on_cs240()
            st.workedHour()

      if(assignment == 'cs342'):
        if assingn._cs342>= st.remaining:
          for i in range(1,st.remaining+1):
            assingn.work_on_cs342()
            st.workedHour()
        else:
          for i in range(1, assingn._cs342+1):
            assingn.work_on_cs342()
            st.workedHour()


      if(assignment == 'seniorProject'):
        if assingn._seniorProject>= st.remaining:
          for i in range(1, st.remaining+1):
            assingn.work_on_seniorProject()
            st.workedHour()
        else:
          for i in range(1, assingn._seniorProject+1):
            assingn.work_on_seniorProject()
            st.workedHour()
    else:
      print("I cannot work more")
   
    #efficiency dusukken
class ProcrastinatorStrategy(Student):
  def work_on_assignment(self,assignment,day):
    #heeath anxite dusukken
    st.remainingHour(day,st.availableHours)
    if(st.remaining > 1):
      st.remaining = st.remaining - 1
    if (st.remaining ) > 0: 
      if(assignment == 'cs240'):
        if assingn._cs240>= st.remaining:
          for i in range(1, st.remaining+1):
            assingn.work_on_cs240()
            st.workedHour()
        else:
          for i in range(1, assingn._cs240+1):
            assingn.work_on_cs240()
            st.workedHour()

      if(assignment == 'cs342'):
        if assingn._cs342>= st.remaining:
          for i in range(1,st.remaining+1):
            assingn.work_on_cs342()
            st.workedHour()
        else:
          for i in range(1, assingn._cs342+1):
            assingn.work_on_cs342()
            st.workedHour()


      if(assignment == 'seniorProject'):
        if assingn._seniorProject>= st.remaining:
          for i in range(1, st.remaining+1):
            assingn.work_on_seniorProject()
            st.workedHour()
        else:
          for i in range(1, assingn._seniorProject+1):
            assingn.work_on_seniorProject()
            st.workedHour()
    else:
      print("I cannot work more")



#def main():
if __name__ == '__main__': 
  st=Student()
  assingn = Assignment()    

  print("Welcome to the strategy center. Please select strategy!")
  print(" Press 1 for Optimal Strategy (low anxiety level high efficiency level)")
  print(" Press 2 for Less Sleep Strategy (low efficiency level high rest level)")
  print(" Press 3 for  Procrastinator Strategy (high anxiety level low health level)")
  Week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  
  for day in Week:
    print("----------------------------"+ day + "------------------------------")
    st.displayStats()
    hour=st.calculate_daily_available_hours(day)
    print("Today you have ",hour," hours available to work on assignment")   
    
    print("Due to the your attributes you can work just ",st.availableHours,"hours")
    val=input("Enter a number for choosing a strategy:")
    st.choose_strategy(val,day)
    st.manage_attributes(val)
    
    
    
    assingn.showRemainingHours()
    st.worked = 0
    print("")


  



