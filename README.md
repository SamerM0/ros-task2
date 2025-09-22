# How to use

Running joystick node will start listening to joystick input which get sent to the navigation node which then maps them to the correct pwm values and linearly or exponentially interpolates between the old value and the new value and sending the result to the thruster controller 


# Libraries

threading -> run code on separate threads

pygame -> read joystick input
