from consoleServices import *
from extendedMath import *

weight:int=getIntNum("kerem a sulyat(kg)")
height:float=getFloatNum("kerem a magassagat(m)")
bmi:float=bmiCalculator(height,weight)
healthStatus=healthBmiCalculator(bmi)

print(f"A{weight} kg és {height} m BMI értéke {bmi:2f}")
print(f"A BMI index alapján Ön {healthStatus}")