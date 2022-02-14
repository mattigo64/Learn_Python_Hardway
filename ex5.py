my_name = 'Matt'
my_age = 26
my_height  = 74
height_cm = my_height*2.54
my_weight = 260
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Black'

print "Lets talk about %r." % my_name
print "He's %r inches tall." % my_height
print "He's %r cm tall." % height_cm
print "He's %d pounds heavy." % my_weight
print "Actually thats not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age+ my_height + my_weight)
