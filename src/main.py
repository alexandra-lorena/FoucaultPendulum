from vpython import *
from src.solve_ode import *


# User input functions
def disable_trail(evt):
    global is_bob_trail
    if evt.checked:
        is_bob_trail = True
    else:
        bob.clear_trail()
        is_bob_trail = False

def reset_values():
    global initial_conditions, i, x, y, z
    i = 0
    initial_conditions[0] = a_0
    x, y, z = get_values(initial_conditions)

def change_alpha(evt):
    global a_0
    a_0 = np.radians(evt.value)
    alpha_slider_text.text = "{:1.1f}".format(evt.value) + "\n\n"

def change_rate(evt):
    global rate_value
    rate_value = evt.value
    rate_slider_text.text = "{:1.0f}".format(evt.value) + "\n\n"


# Initialize objects
is_bob_trail = True
canvas(height = 550, width = 1550, color = color.black)
scene.userpin = True
earth = sphere(pos = vec(0, 0, 0), radius = 42, texture = textures.earth)
earth.rotate(axis = vec(0, 0, 1), origin = vec(0, 0, 0), angle = pi/4)
roof = box( pos = vec(0, 67, 0), axis = vec(1, 0, 0), length = 10, height = 1, width = 5 )
rod = cylinder (pos = vec(0, 67, 0), axis = vec(0, -1, 0), length = 24, radius = 0.1)
bob = sphere(pos = vec( 0, 45, 0), radius = 1, color = color.red, make_trail = is_bob_trail, trail_radius = 0.1)


# Initialize user inputs
commit_button = button(bind =reset_values, text ="Apply changes")
space = wtext(text = "   ")

trail_checkbox = checkbox(bind = disable_trail, text = "Trail", checked = True)
new_line = wtext(text = "\n\n")

alpha_slider_title = wtext(text = "Change alpha:  ")
alpha_slider = slider(bind =change_alpha, min = 0, max = 90, step = 0.5, value = 10)
alpha_slider_text = wtext(text = "{:1.1f}".format(alpha_slider.value) + "\n\n")

rate_slider_title = wtext(text = "Change rate:   ")
rate_slider = slider(bind =change_rate, min = 0, max = 1000, step = 10, value = 100)
rate_slider_text = wtext(text = "{:1.0f}".format(rate_slider.value) + "\n\n")



def main():
    global i, x, y, z, rate_value

    i = 0
    rate_value = 100
    x, y, z = get_values(initial_conditions)

    while i < len(time_values):
        rate(rate_value)
        bob.make_trail = is_bob_trail
        bob.pos = vec(x[i], y[i], z[i])
        rod.axis = bob.pos - rod.pos
        i += 1


main()