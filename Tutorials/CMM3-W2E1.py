import math

def bisection(f,a,b,N,error_limit):
    # Check if a and b bound a root
    if f(a)*f(b) >= 0:
       print("a and b do not bound a root")
       return None 
    a_n = a
    b_n = b
    rel_error = error_limit + 1
    result_buffer = 0
    while abs(rel_error) > error_limit:
        m_n = (a_n + b_n)/2
        rel_error = (abs(m_n - result_buffer) / m_n) * 100
        result_buffer = m_n
        f_m_n = f(m_n)
        if f(a_n)*f_m_n < 0:
           a_n = a_n
           b_n = m_n
        elif f(b_n)*f_m_n < 0:
           a_n = m_n
           b_n = b_n
        elif f_m_n == 0:
           print("Found exact solution.")
           return m_n
        else:
           print("Bisection method fails.")
           return None
    return (a_n + b_n)/2

# we solve equation f(x)=0
f = lambda x: math.sin(x) * math.exp(x ** 0.1)

# first root
approx_phi = bisection(f,2,4,500, 0.01) 
print(approx_phi)
# second root
#approx_phi = bisection(f,0,10,50) 
#print(approx_phi)
