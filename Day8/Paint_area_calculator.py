## Paint Area Calculator 

## Instructions

# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

# number of cans = (wall height X wall width)/ coverage per can.
#e.g. Height = 2, Width = 4, Coverage = 5

# number of cans = (2x4)/5 = 1.6

# But because you can't buy 0.6 of can of paint, the result should be rounded up to 2 cans.

## Define a function for paint calculator

print("******** Welcome to Paint Area Calculator.*********\n")

def paint_cal(h,w,c):
    number_of_cans = round((h * w)/c)
    print(f"\n You need {number_of_cans} cans to Paint your wall.")


height = int(input("Height of the wall: "))
Width = int(input("Width of the wall: "))
coverage = 5

paint_cal(h = height, w = Width, c = coverage)

