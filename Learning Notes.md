# Learning Notes

## np.tile 
repeat some array for n times to create another array
e.g. np.tile([0,0,0], (m,n)) 

1. take out all the elements in the list
2. start from the last digit in the tuple, repeat n times
3. then repeat the whole list for m times

e.g. np.tile([0,0,0], (3,2)) 
Ans = array([[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]])

### Exercise 
1. np.tile([0],(3,3))                 Ans:array([[0, 0, 0],[0, 0, 0],[0, 0, 0]])

2. np.tile([1,2,3],(3,1))             Ans:array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])

## np.histogram 

e.g. np.histogram (array-like list, bins=array-like stuff) 
return (array(histogram value), array(the bins))

**Note:**
1. the elements in bins should better be even, otherwise some of the elements might not be able to go into the bins

2. the number in bins must be arranged in ascending order

3. bins 
e.g. np.histogram([0,1,3,4,7,8,9], bins = [0,1,2,3,4])
- the first bin is [0,1 **)** ... 
- the last bins is [3,4 **]**

4. call the result 
- np.histogram (array-like list, bins=array-like stuff)[0].astype(dtype=float64) => add the last func to change the data type in the list 

### Exercise 
1. np.histogram([0,1,3,4,5,6,7],bins=[0,1,2,4])               Ans:(array([1, 1, 2], dtype=int64), array([0, 1, 2, 4]))

## matplotlib.pyplot.scatter([] , [])
import matplotlib.pyplot as plt
a = plt.scatter(list that stores the x-values , list that stores the y-values)

### Exercise - list all the x-y value
1. matplotlib.pyplot.scatter([1,2,3],[1,2,3])                  Ans: (1,1),(2,2),(3,3)

## some useful function for manupulation of array 
### Example 
1. np.mean([ [1,2,3],[4,5,6],[7,8,9] ],axis=0)
- take mean of the array
- => array([4., 5., 6.])

2. np.max([ [1,2,3],[4,5,6],[7,8,9] ])
- return the largest value in numpy
- => 9

## matplotlib.pyplot
e.g. 
fig, (ax,ax2) = plt.subplots(figsize=(5,9), nrows = 2)
- fig => big window
- ax, ax2 => 2 subplot window 
- figsize -> the size of the whole window
- Number of rows of graph 

## matplotlib.pyplot.bar

x = [1,2,3,4,5]
y = [4,5,6,7,8]
e.g. 
 matplotlib.pyplot.bar(x,y)
 matplotlib.pyplot.show()
 
- first list denotes the centre position of the bar
- second list denotes the value of the correspoding position of the bar

### Use for-loop to set the value of the bar 

e.g.1
```
import numpy as np
import matplotlib.pyplot as plt

fig,ax = plt.subplots()
vs = np.linspace(0,1000,25)
list1 = []
bar = ax.bar(vs,[0]*len(vs), width=0.9*np.gradient(vs), align="edge", alpha = 0.8)

#Operation
for i in range(0,25):
    list1.append(i)

for rect, height in zip(bar.patches,list1):          
    rect.set_height(height)

ax.set_xlim(vs[0],vs[-1])
ax.set_ylim(list1[0],list1[-1])
plt.show()
```
