#!/usr/bin/env python


import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi, np.pi, 256,endpoint=True)

C = np.cos(X)
S = np.sin(X)

fig = plt.figure()
ax = fig.add_subplot(111)

# Plot cosine using blue color with a continuous line of width 1 (pixels)
ax.plot(X, C, color="blue", linewidth=1.0, linestyle="-", label='cos')

# Plot sine using green color with a continuous line of width 1 (pixels)
ax.plot(X, S, color="green", linewidth=1.0, linestyle="-", label='sin')

# Set x limits
ax.set_xlim(-4.0,4.0)

# Set x ticks
ax.set_xticks(np.linspace(-4,4,9,endpoint=True))

# Set y limits
ax.set_ylim(-1.05,1.05)

# Set y ticks
ax.set_yticks(np.linspace(-1,1,5,endpoint=True))

# Move left y-axis and bottom x-axis to centre, passing through (0,0)
ax.spines['left'].set_position('center')     # we want the left spline to be centered
ax.spines['bottom'].set_position('center')   # we want the bottom spline to be centered

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks on the left and lower axes only
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.legend(loc='upper left', framealpha=0.0)
t = 2*np.pi/3
plt.plot([t,t],[0,np.cos(t)], color ='blue', linewidth=1.5, linestyle="--")
plt.scatter([t,],[np.cos(t),], 50, color ='blue')

plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t, np.sin(t)), xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.plot([t,t],[0,np.sin(t)], color ='green', linewidth=1.5, linestyle="--")
plt.scatter([t,],[np.sin(t),], 50, color ='green')

plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy=(t, np.cos(t)), xycoords='data',
             xytext=(+24, -35), textcoords='offset points', fontsize=14,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.192"))
plt.savefig("fig_annotate2.png")
