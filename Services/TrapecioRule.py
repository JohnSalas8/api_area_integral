import math
import ExpMath

class TrapecioRule:
    def __init__(self, *args):
        self.f_xi = []

    def get_integral(self, a, b, exp, n=None, h=None):
        """
            a   -> Limite inferior de la integral
            b   -> Limite superior de la integral

            exp -> Es f(x) en la integral
            n   -> Numero de intervalos
            h   -> El espaciado que se toma de 'a' hasta 'b'

            No es posible poner el valor de n y h, a menos 
            que estos esten bien calculados. Solo n o h.
        """
        vjson = {}
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

        for i in ExpMath.exp_math:
            expression = expression.replace(i[0] , i[1])

        vjson['f(X_n)'] = []
        
        x = a
        for i in range(0, n+1):
            new_exp = expression.replace('x', '('+str(x)+')')
            self.f_xi.append(eval(new_exp))
            vjson['f(X_n)'].append('f(X_' + str(i) + ') = ' + new_exp + ' = ' + str(self.f_xi[i]))
            x += h

        I = 0
        
        vjson['I'] = '(' + str(h) + '/2)('
        
        for i in range(0, len(self.f_xi)):
            if i==0 or i==(len(self.f_xi)-1):
                I += self.f_xi[i]
                vjson['I'] += ' + '+ str(self.f_xi[i]) + ' '
            else:
                I += 2*self.f_xi[i]
                vjson['I'] += ' + 2 * ' + str(self.f_xi[i]) + ' '
        vjson['I'] += ') = (' + str(h) + '/2) * ' + str(I) + ' '
        I = I*(h/2)
        vjson['I'] += ' = ' + str(I)

        return vjson

if __name__ == '__main__':
    print TrapecioRule().get_integral(
        1, 3, 'x**3-x+1', None, 0.5
    )