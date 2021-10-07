plt.plot(x,y_svr_rbf, '--', label='SVR_RBF')
plt.plot(x,y_svr_lin, '--', label='SVR_Linear')
plt.plot(x,y_svr_poly, '--', label='SVR Polynomial')

plt.plot(x,y_lin_1, '--', label='Linear Reg 1')
plt.plot(x,y_lin_2, '--', label='Linear Reg 2')
plt.plot(x,y_lin_3, '--', label='Linear Reg 3')