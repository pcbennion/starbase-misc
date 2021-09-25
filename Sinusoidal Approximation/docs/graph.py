import matplotlib.pyplot as plt
import numpy as np

# Sine Approximation
t1 = np.arange(-180, 180, 0.1)

sin = np.sin(np.pi/180 * t1)
sin_approx = 4*(t1/180)*(1-abs(t1/180))

fig1, ax1 = plt.subplots()
ax1.plot(t1, sin, label="sin(x)")
ax1.plot(t1, sin_approx, label="approx")
ax1.set(xlabel='x (deg)', ylabel='y',
        title='Sin vs Approximation')
ax1.legend()
ax1.grid()
fig1.savefig("sin_approx.png")

# Cosine Approximation
t2 = np.arange(-180, 180, 0.1)

cos = np.cos(np.pi/180 * t2)
cos_approx = pow(t2/180, 2)*(4*abs(t2/180) - 6) + 1

fig2, ax2 = plt.subplots()
ax2.plot(t2, cos, label="cos(x)")
ax2.plot(t2, cos_approx, label="approx")
ax2.plot(t2-90, sin_approx, label="sin approx at x+90")
ax2.set(xlabel='x (deg)', ylabel='y',
        title='Cos vs Approximation')
ax2.set_ybound(-1.1, 1.1)
ax2.legend()
ax2.grid()
fig2.savefig("cos_approx.png")

# Arcsine approximation
t3 = np.arange(-1, 1, 0.01)

arcsin = np.arcsin(t3)*180/np.pi
arcsin_approx = 40*pow(t3, 3) + 50*t3

fig3, ax3 = plt.subplots()
ax3.plot(t3, arcsin, label="asin(x)")
ax3.plot(t3, arcsin_approx, label="approx")
ax3.set(xlabel='x', ylabel='y (deg)',
        title='Arcsin vs Approximation')
ax3.legend()
ax3.grid()
fig3.savefig("arcsin_approx.png")

# Arccosine approximation
t4 = np.arange(-1, 1, 0.01)

arccos = np.arccos(t4)*180/np.pi
arccos_approx = -40*pow(t4, 3) - 50*t4 + 90

fig4, ax4 = plt.subplots()
ax4.plot(t4, arccos, label="acos(x)")
ax4.plot(t4, arccos_approx, label="approx")

ax4.set(xlabel='x', ylabel='y (deg)',
        title='Arccos vs Approximation')
ax4.legend()
ax4.grid()
fig4.savefig("arccos_approx.png")

# Show all plots
plt.show()
