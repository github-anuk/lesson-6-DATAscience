import matplotlib.pyplot as mp
import numpy as np

ages = [22,55,36,45,21,67,45,23,11,89,33,67,88,89,67,12,6,9,48,68,18]
bins =[0,10,20,30,40,50,60,70,80,90,100]

mp.hist(ages,bins,histtype="bar",rwidth=0.8)
mp.xlabel("Age interval")
mp.ylabel("Frequency")
mp.title("Histogram")
mp.show()

x=[1,2,3,4,5,6,7,8,9,10]
y=[1,0,1,0,0,1,1,1,0,0]
mp.scatter(x,y,label="Scatter plot",color="red",marker="o",s=50)
mp.xlabel("IDK")
mp.ylabel("i don't know")
mp.show()

activites=["sleeping","eating","working","netflix","workout n friends"]
slices=[11,1,7,1,3]
clr=["c","m","r","b","g"]
mp.pie(slices,labels=activites,colors=clr,startangle=90,shadow=True)
mp.show()

days=[1,2,3,4,5]

eating = [2,3,4,3,2]
sleeping = [10,7,6,7,10]
working = [8,8,8,8,5]
freetime = [4,6,5,6,8]

mp.plot([],[],color ="m",label = "eating",linewidth = 5)
mp.plot([],[],color ="b",label = "sleeping",linewidth = 5)
mp.plot([],[],color ="g",label = "working",linewidth = 5)
mp.plot([],[],color ="r",label = "freetime",linewidth = 5)
mp.stackplot(days,eating,sleeping,working,freetime,colors=["m","b","g","r"])
mp.xlabel("ddsfdsffsdfdfsdd")
mp.ylabel("lorem")
mp.show()

def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

t1=np.arange(0,5,0.1)
mp.figure()
mp.subplot(221)
mp.plot(t1,f(t1),"bo")
t2=np.arange(0,5,0.02)
mp.subplot(224)
mp.plot(t2,np.cos(2*np.pi*t2))
mp.show()