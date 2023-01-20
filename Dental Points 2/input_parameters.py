space_required = float(input('enter space_required: '))
max_tipping_angle = float(input('enter max_tipping_angle: '))
inputs = space_required,max_tipping_angle

def find_tipping_angle(inputs):
    if (space_required > 0 and max_tipping_angle < 0) or (space_required < 0 and max_tipping_angle > 0):
        tipping_angle = 0
        space_required_after_tipping = space_required
        return tipping_angle,space_required_after_tipping
    elif (space_required > 0 and max_tipping_angle > 0) or (space_required < 0 and max_tipping_angle < 0):
        max_space_recovered = max_tipping_angle / 5

        if (space_required <= max_space_recovered):
            tipping_angle = space_required * 5
            treatment_plan = (f'tipping_angle = {tipping_angle}', 0, 0, 0)
            # return  # everything completed, no need to do the rest
            print(treatment_plan)

        else:
            tipping_angle = max_tipping_angle
            space_required_after_tipping = space_required - max_space_recovered
            return tipping_angle,space_required_after_tipping

tipping_angle = find_tipping_angle(inputs)[0]
space_required_after_tipping = find_tipping_angle(inputs)[1]
