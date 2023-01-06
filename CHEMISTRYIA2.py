#CHEMISTRY IA - Investigating the thermodynamic efficiency of an LHV hydrogen fuel cell (%) at standard conditions using a Van't Hoff Plot
import matplotlib.pyplot as plt
import numpy as np

#Define datasets
temperatures = [298,300,400,500,600,700,800,900,1000,1100,1200,1300] 
G            = [228.582,228.5,223.9,219.05,214.008,208.814,203.501,198.091,192.603,187.052,181.45,175.807] #kJ/mol * -1
G = [i*1000 for i in G] #J/mol
inverse_temperatures = [1/i for i in temperatures] #inverse temperatures
lnk = []
R = 8.31

#Calculate all k values with partial pressure
for i in range(len(temperatures)):
    lnk.append(G[i]/(R * temperatures[i]))

print(lnk)
print(inverse_temperatures)

#Calculate Trendline
z = np.polyfit(inverse_temperatures, lnk, 1)
p = np.poly1d(z)
plt.plot(inverse_temperatures, p(inverse_temperatures), "r--")
equation = "y=%.6fx+(%.6f)"%(z[0],z[1])
print(equation)

#Create Van't Hoff Plot
plt.scatter(inverse_temperatures, lnk)
plt.xlim([0,1/min(temperatures)]) #Range of Values
plt.xlabel("Inverse Temperature (1/K)")
plt.ylabel("ln(k)")
plt.title(f"Van't Hoff Plot for an LHV Hydrogen Fuel Cell, {equation}")
plt.show()


#CHEMISTRY IA - Investigating the thermodynamic efficiency of an LHV hydrogen fuel cell (%) at standard conditions using a Van't Hoff Plot
import matplotlib.pyplot as plt
import numpy as np

#Define datasets
temperatures = [100,110,120,130,140,150,160,180,200,220,240,260,280,300,320,340,360,370]
temperatures = [i+273 for i in temperatures] #change to kelvin
inverse_temperatures = [1/i for i in temperatures] #inverse temperatures
water_pressure = [101.42,143.38,198.67,270.28,361.54,476.16,618.23,1002.8,1554.9,2319.6,3346.9,4692.3,6416.6,8587.9,11284,14601,18666,21044] #kpa
fraction_H2 = 2/3
fraction_O2 = 1/3
k = []

#Define square root
def sqrt(n):
    return n**(1/2)

#Define k function
def calculate_k(h2o, h2, o2):
    return (h2o) / (h2 * sqrt(o2))

#Calculate all k values with partial pressure
for i in range(len(water_pressure)):
    pH2 = fraction_H2 * water_pressure[i]
    pO2 = fraction_O2 * water_pressure[i]
    k.append(np.log(calculate_k(water_pressure[i], pH2, pO2))) #log function refers to ln

print(k)
print(inverse_temperatures)

#Calculate Trendline
z = np.polyfit(inverse_temperatures, k, 1)
p = np.poly1d(z)
plt.plot(inverse_temperatures, p(inverse_temperatures), "r--")
equation = "y=%.6fx+(%.6f)"%(z[0],z[1])
print(equation)

#Create Van't Hoff Plot
plt.scatter(inverse_temperatures, k)
plt.xlim([0,1/min(temperatures)]) #Range of Values
plt.xlabel("Inverse Temperature (1/K)")
plt.ylabel("ln(k)")
plt.title(f"Van't Hoff Plot for an LHV Hydrogen Fuel Cell, {equation}")
plt.show()