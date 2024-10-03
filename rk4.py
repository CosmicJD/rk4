import numpy as np
import matplotlib.pyplot as plt
def dyn_generator(oper, state):
    """Operador lineal para -i[O,y(t)].

    En este caso, "O" es otro operador lineal, i es la constante compleja, y "y(t)" es una función dependiente del tiempo. Requiere que NumPy sea importado como "np".

Examples:
        oOper es el operador lineal.
        yInit es el estado inicial.

        >>> oOper = np.array([[0, 1], [1, 0]])
        >>> yInit = np.array([[1, 0], [0, 0]])
        >>> dyn_generator(oOper, yInit)
        [[-0.92093156+0.j          0.        +0.38972435j]
         [ 0.        -0.38972435j  0.92093156-0.j        ]]

    Args:
        oper (Numpy array): Primer argumento (opreador lineal).
        state (Numpy array): Segundo argumento (Estado inicial).

    Returns:
        (Numpy array): Retorna el resultado de aplicar el operador -i[A.B] = -i(AB - BA), conocido como el conmutador.
    """
    return (np.dot(oper, state) - np.dot(state, oper)) * (-1.0j)
def rk4(func, oper, state, h):
    """ Runge-Kutta 4, Para una función no dependiente del tiempo.

    Este es el propósito principal de todo el código; desarrolla el método numérico con los siguientes argumentos.:

    Args:
        func (Function):Esta sería la función que se va a usar para ingresar y desarrollar la solución. Para este ejemplo particular, sería dyn_generator
        oper (Numpy array): Segundo argumento: operador lineal.
        state (Numpy array): Tercer argumento: este es un arreglo dinámico que cambiará durante el bucle for con el propósito de modificar el estado inicial, y por lo tanto, cambiar el punto temporal.
        h (float): Paso temporal necesario para el método numérico.

    Returns:
        (Numpy array): Devuelve el estado del sistema en ese tiempo particular.

    Examples:
        >>> oOper = np.array([[0, 1], [1, 0]])
        >>> yInit = np.array([[1, 0], [0, 0]])
        >>> h = 0.01001001001001001
        >>> print(rk4(dyn_generator,oOper, yInit, h))
        [[0.68560521+0.j         0.        +0.46427439j]
         [0.        -0.46427439j 0.31439479+0.j        ]]

    """
    k1 = h*func(oper,state)
    k2 = h*func(oper,state+(k1/2))
    k3 = h*func(oper,state+(k2/2))
    k4 = h*func(oper,state+k3)
    return state + (1/6)*(k1+(2*k2)+(2*k3)+k4)

