import matplotlib.pyplot as plt
import numpy as np
#Define datasets
temperatures = [298.15,300,400,500,600,700,800,900,1000,1100,1200,1300]
G1 = [228.582,228.5,223.9,219.05,214.008,208.814,203.501,198.091,192.603,187.052,181.45,175.807] #kJ/mol * -1
G2 = [228.582,228.5,223.901,219.051,214.007,208.812,203.496,198.083,192.59,187.033,181.425,175.774]
G = []
for i in range(len(G1)):
   G.append(((G1[i]+G2[i])/2)*1000) #Average and convert to J/mol
inverse_temperatures = [1/i for i in temperatures] #inverse temperatures
lnk = []
R = 8.31
 
#Calculate all k values
for i in range(len(temperatures)):
   lnk.append(G[i]/(R * temperatures[i]))
 
print(G)
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
plt.errorbar(inverse_temperatures, lnk, yerr=0.017,elinewidth=0.01,ecolor="green")
plt.xlim([0,1/min(temperatures)]) #Range of Values
plt.xlabel("1/T")
plt.ylabel("ln(k)")
plt.title(f"Van't Hoff Plot for an LHV Hydrogen Fuel Cell, {equation}")
plt.show()
