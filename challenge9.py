import math

def paint_calc(height, width, cover):
    cans_num = (height * width) / cover
    roundup = math.ceil(cans_num)
    print(f"you'll need {roundup} of paint.")


test_h = int(input("height :"))
test_w = int(input("width :"))
coverage = 5

paint_calc(height=test_h ,width=test_w ,cover=coverage)
