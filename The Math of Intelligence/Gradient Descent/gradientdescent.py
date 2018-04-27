"""
Author : Shyam Sunder Kumar
Objective : Gradient Descent algorithm
So first of all you have to understand the components you need to write gradient
descent algorithm.

Think it as a straight line: Y = mX+b
We have to find optimal m and b.
See readme file for full details
"""

def gradient_descent(m,b,X,y,learning_rate):
    m_dy = 0
    b_dy = 0
    N = len(X)
    for i in range(N):
        # Calculate partial derivatives of the cost function
        # -2x(y - (mx + b))
        m_dy = -2* X[i] * * (Y[i] - (m*X[i] + b))

        # -2(y - (mx + b))
        b_deriv += -2*(Y[i] - (m*X[i] + b))

    m -= (m_deriv / float(N)) * learning_rate
    b -= (b_deriv / float(N)) * learning_rate

    return m,b
