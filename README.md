## Foucault's pendulum simulation
This started out as a university project on the Coriolis effect, but I'm hoping to be able to 
continue extending it. The project simulates the movement of the infamous Foucault pendulum as 
seen by someone standing on Earth in order to visualize its trajectory, which demonstrates the
Earth's rotation.

The simulation uses the <code>vpython</code> library in order to create the 3D animation and the 
function <code>odeint()</code> in order to solve the coupled second order differential equations
that are used to compute the pendulum's coordinates:
> $\ddot{\alpha}  -  \sin\alpha \cos\alpha \dot{\beta}^2  -  2 \omega \sin\alpha (\cos\phi 
 \sin\alpha \cos\beta + \sin\phi \cos\alpha) \dot{\beta}  +  \frac{g}{l} \sin\alpha$ = 0

> $\sin\alpha \ddot{\beta}  +  \cos\alpha  \dot{\alpha} \dot{\beta}  +  2 \omega 
 (\cos\phi \sin\alpha \cos\beta + \sin\phi \cos\alpha) \dot{\alpha}$ = 0

For more information regarding the derivation of these equations check out the paper: <i> Analysis 
on the Foucault pendulum by De Alembert Principle and Numerical Simulation </i> by Zhiwu Zheng, which
linked lower down.


### Documantation
For a more detailed explanation of the code, check out the <code>FoucaultPendulum.ipynb</code> found
in the file <code>docs</code> or click this link [FoucaultPendulum.ipynb](docs/FoucaultPendulum.ipynb).


### Papers
1. <i> Analysis on the Foucault pendulum by De Alembert Principle and Numerical Simulation </i>, Zhiwu Zheng [[Link text](https://website-name.com)](https://arxiv.org/pdf/1504.03873)
