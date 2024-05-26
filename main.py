import numpy as np
import matplotlib.pyplot as plt
import json

dataset = json.load(open('../dataset-maker/dataset.json'))

train = np.array(dataset['red'])
test = np.array(dataset['blue'])
mu = train.mean(axis=0)
temp_param = np.square(train - mu)
sigma_sq = temp_param.mean(axis=0)
sigma = sigma_sq**(1/2)

xs = train[:, 0]
ys = train[:, 1]
x = test[:, 0][0]
y = test[:, 1][0]

px = np.e**(-((x-mu[0])**2)/(2*sigma_sq[0]))/(sigma[0]*(2*np.pi)**(1/2))
py = np.e**(-((y-mu[1])**2)/(2*sigma_sq[1]))/(sigma[1]*(2*np.pi)**(1/2))

p = px*py
print(p)

if p > 0.00010561510437583416:
    output = "Not anomalous"
else:
    output = "Anomalous"

fig1, ax1 = plt.subplots()
ax1.scatter(xs, ys, color='red', label='Data')
ax1.scatter(x, y, color='blue', label='To be tested')
ax1.scatter(mu[0], mu[1], color='purple', label='Mean point')
ax1.set_xlabel(output)
ax1.legend()

fig2, ax2 = plt.subplots()
ax2.set_title("Histogram of xs")
ax2.hist(xs, bins=25)


fig3, ax3 = plt.subplots()
ax3.set_title("Histogram of ys")
ax3.hist(ys, bins=25)


plt.show()
# 0.003270820470618132 -> Center
# 0.00010561510437583416 -> Boarder
