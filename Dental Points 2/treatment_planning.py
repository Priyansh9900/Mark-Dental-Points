from required_function import *
from input_parameters import *

def get_treatment_plan_lowerJaw(input):
	if space_required >= 0:
		expand_potential_6 = length6_ - length6
		expand_potential_5 = length5_ - length5
		expand_potential_4 = length4_ - length4
		expand_potential = max(0,expand_potential_4,expand_potential_5,expand_potential_6) * 0.7
		if space_required_after_tipping <= expand_potential:
			expansion = space_required_after_tipping
		else:
			expansion = expand_potential
		space_required_after_expansion = space_required_after_tipping - expansion
		if space_required_after_expansion < 3:
			treatment_plan = (f'tipping_angle = {tipping_angle}, expansion = {expansion}, '
							  f'space_required_after_expansion = {space_required_after_expansion}, {0}')
			print('Treatment_Plan_jaw: ', treatment_plan)
		else:
			space_required_after_treatment = space_required_after_expansion - 3
			treatment_plan = (f'tipping_angle = {tipping_angle} ,expansion = {expansion}, {3},'
							  f' space_required_after_treatment = {space_required_after_treatment}')
			print('Treatment_Plan_lowerjaw: ',treatment_plan)
	elif space_required <0:
		constrict_potential_6 = length6 - length6_
		constrict_potential_4 = length4 - length4_
		constrict_potential_5 = length5 - length5_
		constrict_potential = max(0,constrict_potential_6,constrict_potential_5,constrict_potential_4) * 0.7
		if abs(space_required_after_tipping) <= constrict_potential:
			constriction = space_required_after_tipping
		else:
			constriction = -1 * constrict_potential

		space_required_after_constriction = space_required_after_tipping - constriction
		space_from_tooth_build_up = -1 * space_required_after_constriction

		treatment_plan = (f'tipping_angle = {tipping_angle} ,constriction = {constriction} ,'
						  f'space_from_tooth_build_up = {space_from_tooth_build_up} ,{0}')
		print('Treatment_Plan_lowerjaw: ',treatment_plan)