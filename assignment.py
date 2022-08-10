class Planet:
    def _init_(self, name,s_gases, no_of_moon ,rings):
        self.name= name
        self.s_gases= s_gases
        self.no_of_moon= no_of_moon
        self.rings= rings
        
    def table(self, Name,S_gases, No_of_moon ,Rings):
        
        x = Planet(Name,S_gases, No_of_moon ,Rings)
        ls.append(x)
        
    def display(self,x):
        print("Name :",x.name)
        print("Gases :",x.s_gases)
        print("No of moons :",x.no_of_moons)
        print("Rings :",x.rings)
        print("\n")
        
    def check(self):
        sum=0
        for i in range(ls._len_()):
            if(ls[i].rings=="yes"):
                
             sum= sum + no_of_moon
        
        print("Total no of moons",sum)
        
    ls=[]
  
    obj=Planet('',[],0,0)
    print("enter the no of table :")
    m=input(int)
    for s in range (m):
      obj.table()
     
    for i in range (ls._len_()):
         obj.display(ls[i])
    
    obj.check()
  
    
        
        
