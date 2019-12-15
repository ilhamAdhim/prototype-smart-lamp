import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# =======================================================
#  PROGRAM FOR AUTO ADJUST YOUR HOME'S LAMPS BRIGHTNESS
# =======================================================    

def main(electricity):
    # The universe of variables and membership functions
    electricity_used = ctrl.Antecedent(np.arange(0,1000,5), 'electricity_used')
    brightness = ctrl.Consequent(np.arange(0,100,1), 'brightness')

    # Rules
    electricity_used['very_low'] = fuzz.trapmf(electricity_used.universe, [0,0,100,150])
    electricity_used['low'] = fuzz.trimf(electricity_used.universe, [100,225,350])
    electricity_used['medium'] = fuzz.trimf(electricity_used.universe, [300,475,650])
    electricity_used['high'] = fuzz.trimf(electricity_used.universe, [550,675,800])
    electricity_used['very_high'] = fuzz.trapmf(electricity_used.universe, [700,750,850,950])


    brightness['very_low'] = fuzz.trapmf(brightness.universe, [0,0,15,30])
    brightness['low'] = fuzz.trimf(brightness.universe, [15,30,45])
    brightness['medium'] = fuzz.trimf(brightness.universe, [35,55,75])
    brightness['high'] = fuzz.trimf(brightness.universe, [60,75,90])
    brightness['very_high'] = fuzz.trapmf(brightness.universe, [80,85,90,100])

# electricity_used.view()
# brightness.view()

# RULES
    rule1 = ctrl.Rule(electricity_used['very_low'] , brightness['very_high'])
    rule2 = ctrl.Rule(electricity_used['low'] , brightness['high'])
    rule3 = ctrl.Rule(electricity_used['medium'] , brightness['medium'])
    rule4 = ctrl.Rule(electricity_used['high'] , brightness['low'])
    rule5 = ctrl.Rule(electricity_used['very_high'] , brightness['very_low'])
    brightness_ctrl = ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5])

    adjusting = ctrl.ControlSystemSimulation(brightness_ctrl)

    # input = input('Enter the electricity : ')
    adjusting.input['electricity_used'] = int(electricity)

    try:
        adjusting.compute()
        output = adjusting.output['brightness']

        print("With electricity used : ", electricity, " KWH")
        print("Output of brightness is : ", '%.2f' % output, "%")

        brightness.view(sim=adjusting)
        # plt.show()
    except Exception:
        print("Electricity out of bound")
    return output

