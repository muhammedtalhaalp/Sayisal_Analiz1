import math 


a=math.pi/5
taylorbir=(math.pow((-1),0))*(a**(2*0))/(math.factorial((2*0)))


tayloriki=(-1**1)*(a**(2*1))/(math.factorial((2*1)))
cosa=math.cos(a)


birincikesmehata=taylorbir-cosa

ikincikesmehata=taylorbir+tayloriki-cosa

print(taylorbir)
print(tayloriki+taylorbir)
print(birincikesmehata)  
print(ikincikesmehata)
