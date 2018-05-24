import math

expression = ''
f_xi = []

def get_integral(a, b, exp, n=None, h=None):
    """
        a   -> Limite inferior de la integral
        b   -> Limite superior de la integral

        exp -> Es f(x) en la integral
        n   -> Numero de intervalos
        h   -> El espaciado que se toma de 'a' hasta 'b'

        No es posible poner el valor de n y h, a menos 
        que estos esten bien calculados. Solo n o h.
    """
    if n==None:
        n = int((b-a)/h)
    if h==None:
        h = float(b-a)/n

    expression = exp.replace(' ','')
    
    x = a
    for i in range(0, n+1):
        new_exp = expression.replace('x', '('+str(x)+')')
        f_xi.append(eval(new_exp))
        print 'f(X_'+str(i)+') =', new_exp, '=', f_xi[i]
        x += h

    I = 0
    print ''
    print 'I = ',
    for i in range(0, len(f_xi)):
        if i==0 or i==(len(f_xi)-1):
            I += f_xi[i]
            print '+ '+str(f_xi[i]),
        else:
            I += 2*f_xi[i]
            print '+ 2 * '+str(f_xi[i]),
    print '= '+str(h)+' *',I,
    I = I*(h/3)
    print '/2 =',I

def main():
    exp = 'x**3-x+1'
    get_integral(1, 3, exp, h=0.5)

if __name__ == '__main__':
    main()