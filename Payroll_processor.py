class Employee:
    def __init__(self,name):
        self.name=name
        
    def calculatePay(self):
        pass
        
class SalariedEmployee(Employee):
    def __init__(self,name,salary):
        super().__init__(name)
        self.salary=salary
        
    def calculatePay(self):
        return self.salary
    
    
class HourlyEmployee(Employee):
    def __init__(self,name,hourly_rate,hours_worked):
        super().__init__(name)
        self.hourly_rate=hourly_rate
        self.hours_worked=hours_worked
        
    def calculatePay(self):
        return self.hourly_rate*self.hours_worked
    
salaried_employee=SalariedEmployee("Rubiga",75000)
print("Monthly salary of Rubiga: ",salaried_employee.calculatePay())

hourly_Employee = HourlyEmployee("Ruby",100,300)
print("Hourly salary of Ruby: ", hourly_Employee.calculatePay())



    