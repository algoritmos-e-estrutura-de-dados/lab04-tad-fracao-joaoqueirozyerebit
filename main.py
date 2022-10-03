class Fracao:
 numerado = 1
 denominador = 1
 
 def __init__(self, numerador, denominador):
   self.numerador = numerador
   self.denominador = denominador

    
 def add(self, fracao):
   num =(self.numerador * fracao.numerador)\
   +(fracao.numerador * self.denominador)
   den = self.numerador * fracao.denominador
   return Fracao(num, den)
   
 def sub(self, fracao):
   num =(self.numerador * fracao.numerador)\
   -(fracao.numerador * self.denominador)
   den = self.numerador * fracao.denominador
   return Fracao(num, den)

   
  
 def solve(self):
   return self.numerador/self.denominador
   
 def simpl(self):        
      loop = True
      x = 2
      
      while loop == True:               
        controle = False
        if self.numerador / x == 1 or self.denominador / x == 1:
          loop = False
        
        if self.numerador % x == 0 and self.denominador % x == 0:       
          self.numerador = self.numerador / x
          self.denominador = self.denominador / x
          controle = True
          
        else:          
          x += 1
          controle = True

        if controle == False:
          loop = False
          
          
      return Fracao(self.numerador,self.denominador)
   
 def __str__(self):
   return f"{self.numerador} / {self.denominador}"

fracao1 = Fracao (2, 3) 
fracao2 = Fracao (1, 3)
fracao3 = fracao1.add(fracao2)
fracao4 = fracao1.sub(fracao2)
fracao5 = fracao1.simpl(fracao2)
fracao6 = fracao1.sub(fracao2)
print(f"fracao1: {fracao1}")
print(f"fracao2: {fracao2}")
print(f"fracao3: {fracao3}")
print(f"fracao4: {fracao4}")
print(f"fracao5: {fracao5}")
print(f"fracao6: {fracao6}")
