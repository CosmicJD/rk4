## Método Runge-Kutta de orden 4 (RK4)

EL método de RK4 es la solución para un punto temporal con lo siguiente:
\begin{equation}
Y_{n+1} = Y_{n} + \frac{1}{6} (k_{1}+2k_{2}+2k_{3}+k_{4}) 
\end{equation}
donde tenemos los siguientes valores para los coeficientes:

$$
\begin{aligned}
k_{1} = h f(t_{n},y_{n}) \\
k_{2} = h f(t_{n} + \frac{h}{2},y_{n} + \frac{k_{1}}{2}) \\
k_{3} = h f(t_{n} + \frac{h}{2},y_{n} + \frac{k_{2}}{2}) \\
k_{4} = h f(t_{n} + {h},y_{n} + k_{3}) \\
\end{aligned}
$$

Donde $h$ es el espaciamiento temporal.
