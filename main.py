class Assignment: 
  
  def __init__(self, cs240,cs342,seniorProject,completedPercentage): 
    self._cs240 =cs240 
    self._cs342=cs342
    self._seniorProject=seniorProject
    self._completedPercentage=completedPercentage

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

#for testing functions now
if __name__ == '__main__':
  
    obj = Assignment(6,5,10,0)

    print(obj._cs240)
    obj.work_on_cs240()
    print(obj._cs240)

    print(obj._cs342)
    obj.work_on_cs342()
    print(obj._cs342)

    print(obj._seniorProject)
    obj.work_on_seniorProject()
    print(obj._seniorProject)


