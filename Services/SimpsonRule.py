import math
import json

class SimpsonRule:
    def __init__(self):
        self.expression = ''
        self.f_xi = []
        self.vjson = {}

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
        vjson['a'] = a
        vjson['b'] = b
        vjson['exp'] = exp
        if n==None:
            n = int((b-a)/h)
        if h==None:
            h = float(b-a)/n
        
        vjson['n'] = n
        vjson['h'] = h

        expression = exp.replace(' ','')
        
        vjson['f(X_n)'] = ''

        x = a
        for i in range(0, n+1):
            new_exp = expression.replace('x', '('+str(x)+')')
            f_xi.append(eval(new_exp))
            #print 'f(X_'+str(i)+') =', new_exp, '=', f_xi[i]
            vjson['f(X_n)'] += 'f(X_'+str(i)+') =' + new_exp + '=' + str(f_xi[i]) + '\n'
            x += h

        I = 0
        #print ''
        #print 'I = ',
        vjson['I'] = ''
        for i in range(0, len(f_xi)):
            if i==0 or i==(len(f_xi)-1):
                I += f_xi[i]
                #print '+ '+str(f_xi[i]),
                vjson['I'] += '+ ' + str(f_xi[i]) + ' '
            elif (i%2)!=0 and i!=0 and i!=(len(f_xi)-1):
                I += 4*f_xi[i]
                #print '+ 4 * '+str(f_xi[i]),
                vjson['I'] += '+ 4 * ' + str(f_xi[i]) + ' '
            else:
                I += 2*f_xi[i]
                #print '+ 2 * '+str(f_xi[i]),
                vjson['I'] += '+ 2 * ' + str(f_xi[i]) + ' '
        #print '= '+str(h)+' *',I,
        vjson['I'] += '= ' + str(h) + ' * ' + I + ' '
        I = I*(h/3)
        #print '/3 =',I
        vjson['I'] += '/3 = ' + I

        return json.dump(vjson)

if __name__ == '__main__':
    print SimpsonRule().get_integral(
        1, 3, 'x**3-x+1', None, 0.5
    )