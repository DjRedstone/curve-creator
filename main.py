# ------ SETUP -------

# IMPORTS
import numpy as np
import matplotlib.pyplot as plt

# VARS
points = [(-2, 0), (0, -1), (1,2), (2,-3), (3, 6), (4, -1)]
letters = "abcdefghijklmnopqrstuvwyz"
assert len(points) <= len(letters)

# ------ CREATING INCONNUS -------

inconnus = {}
for i in range(len(points)):
  inconnus[letters[i]] = 0

# ----- CALCULATE INCONNUS ------

n = len(points)
A = []
for i in range(n):
	l = []
	for j in range(1, n+1):
		l.append(points[i][0]**(n-j))
	A.append(l)
A = np.matrix(A)

B = []
for i in range(n):
	B.append([points[i][1]])
B = np.matrix(B)

X = A.I * B
x = np.array(X).ravel()

for i in range(len(x)):
	inconnus[letters[i]] = x[i]

# ------ CREATING CURVE -------

x = np.linspace(-np.pi,np.pi,100)

puissance = len(inconnus) - 1
y = 0
name = "y = "
for inconnu in inconnus.values():
	if inconnu != 0:
	  y += inconnu * x ** puissance
	  name += "" if inconnu < 0 or puissance == len(inconnus)-1 else "+"
	  name += str(round(inconnu))
	  name += "x" if puissance >= 1 else ""
	  name += f"^{puissance}" if puissance >= 2 else ""
	puissance -= 1

print(name)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

plt.plot(x, y, 'r', label=name)
for point in points:
	plt.plot(point[0], point[1], "go", str(point))

plt.legend(loc='upper left')

print("done!")
plt.show()
