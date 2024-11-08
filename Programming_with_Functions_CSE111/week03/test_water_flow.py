"""Verify that the prefix and suffix functions work correctly."""

from pytest import approx
import pytest

import water_flow

def test_water_column_height():
	# Test case 1: Tower height 0, tank wall height 0, expected water column height 0
	assert water_flow.water_column_height(0.0, 0.0) == 0.0
	
	# Test case 2: Tower height 10, tank wall height 7.5, expected water column height 25
	assert water_flow.water_column_height(0.0, 10.0) == 7.5
	
	# Test case 3: Tower height 0, tank wall height 25, expected water column height 48.3
	assert water_flow.water_column_height(25.0, 0.0) == 25.0
	
	# Test case 4: Tower height 12.8, tank wall height 57.9, expected water column height 75.15
	assert water_flow.water_column_height(48.3, 12.8) == 57.9


import water_flow

def test_pressure_gain_from_water_height():
    # Test case 1: Height 0, expected pressure 0
	assert abs(water_flow.pressure_gain_from_water_height(0.0) - 0.000) < 0.001
	
	# Test case 2: Height 30.2, expected pressure 295.628
	assert abs(water_flow.pressure_gain_from_water_height(30.2) - 295.628) < 0.001
	
	# Test case 3: Height 50.0, expected pressure 489.450
	assert abs(water_flow.pressure_gain_from_water_height(50.0) - 489.450) < 0.001



import water_flow

def test_pressure_loss_from_pipe():
    # Test case 1: Pipe diameter 0.048692, length 0, friction factor 0.018, fluid velocity 1.75, expected pressure loss 0
	assert abs(water_flow.pressure_loss_from_pipe(0.048692, 0.00, 0.018, 1.75) - 0.000) < 0.001
	
	# Test case 2: Pipe diameter 0.048692, length 200, friction factor 0, fluid velocity 1.75, expected pressure loss 0
	assert abs(water_flow.pressure_loss_from_pipe(0.048692, 200.00, 0.000, 1.75) - 0.000) < 0.001
	
	# Test case 3: Pipe diameter 0.048692, length 200, friction factor 0.018, fluid velocity 0, expected pressure loss 0
	assert abs(water_flow.pressure_loss_from_pipe(0.048692, 200.00, 0.018, 0.00) - 0.000) < 0.001
	
	# Test case 4: Pipe diameter 0.048692, length 200, friction factor 0.018, fluid velocity 1.75, expected pressure loss -113.008
	assert abs(water_flow.pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.75) - (-113.008)) < 0.001
	
	# Test case 5: Pipe diameter 0.048692, length 200, friction factor 0.018, fluid velocity 1.65, expected pressure loss -100.462
	assert abs(water_flow.pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.65) - (-100.462)) < 0.001
	
	# Test case 6: Pipe diameter 0.286870, length 1000, friction factor 0.013, fluid velocity 1.65, expected pressure loss -61.576
	assert abs(water_flow.pressure_loss_from_pipe(0.286870, 1000.00, 0.013, 1.65) - (-61.576)) < 0.001
	
	# Test case 7: Pipe diameter 0.286870, length 1800.75, friction factor 0.013, fluid velocity 1.65, expected pressure loss -110.884
	assert abs(water_flow.pressure_loss_from_pipe(0.286870, 1800.75, 0.013, 1.65) - (-110.884)) < 0.001



import water_flow

def test_pressure_loss_from_fittings():
	# Test case 1: Fluid velocity 0, quantity of fittings 3, expected pressure loss 0
	assert abs(water_flow.pressure_loss_from_fittings(0.00, 3) - 0.000) < 0.001
	
	# Test case 2: Fluid velocity 1.65, quantity of fittings 0, expected pressure loss 0
	assert abs(water_flow.pressure_loss_from_fittings(1.65, 0) - 0.000) < 0.001
	
	# Test case 3: Fluid velocity 1.65, quantity of fittings 2, expected pressure loss -0.109
	assert abs(water_flow.pressure_loss_from_fittings(1.65, 2) - (-0.109)) < 0.001
	
	# Test case 4: Fluid velocity 1.75, quantity of fittings 2, expected pressure loss -0.122
	assert abs(water_flow.pressure_loss_from_fittings(1.75, 2) - (-0.122)) < 0.001
	
	# Test case 5: Fluid velocity 1.75, quantity of fittings 5, expected pressure loss -0.306
	assert abs(water_flow.pressure_loss_from_fittings(1.75, 5) - (-0.306)) < 0.001
	


import water_flow

def test_reynolds_number():
	# Test case 1: Hydraulic diameter 0.048692, fluid velocity 0, expected Reynolds number 0
	assert abs(water_flow.reynolds_number(0.048692, 0.00) - 0) < 1
	
	# Test case 2: Hydraulic diameter 0.048692, fluid velocity 1.65, expected Reynolds number 80069
	assert abs(water_flow.reynolds_number(0.048692, 1.65) - 80069) < 1
	
	# Test case 3: Hydraulic diameter 0.048692, fluid velocity 1.75, expected Reynolds number 84922
	assert abs(water_flow.reynolds_number(0.048692, 1.75) - 84922) < 1
	
	# Test case 4: Hydraulic diameter 0.286870, fluid velocity 1.65, expected Reynolds number 471729
	assert abs(water_flow.reynolds_number(0.286870, 1.65) - 471729) < 1
	
	# Test case 5: Hydraulic diameter 0.286870, fluid velocity 1.75, expected Reynolds number 500318
	assert abs(water_flow.reynolds_number(0.286870, 1.75) - 500318) < 1
	


import water_flow

def test_pressure_loss_from_pipe_reduction():
	# Test case 1: Larger diameter 0.28687, fluid velocity 0, Reynolds number 1, smaller diameter 0.048692, expected pressure loss 0
	assert abs(water_flow.pressure_loss_from_pipe_reduction(0.28687, 0.00, 1, 0.048692) - 0.000) < 0.001
	
	# Test case 2: Larger diameter 0.28687, fluid velocity 1.65, Reynolds number 471729, smaller diameter 0.048692, expected pressure loss -163.744
	assert abs(water_flow.pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692) - (-163.744)) < 0.001
	
	# Test case 3: Larger diameter 0.28687, fluid velocity 1.75, Reynolds number 500318, smaller diameter 0.048692, expected pressure loss -184.182
	assert abs(water_flow.pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692) - (-184.182)) < 0.001
    
	

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
        



