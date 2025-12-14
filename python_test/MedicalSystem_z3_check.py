from z3 import *

def to_real(x):
    if isinstance(x, int):
        return RealVal(x)
    if isinstance(x, float):
        return RealVal(x)
    if is_int(x):
        return ToReal(x)
    return x

# Custom Functions
def predict_next(val):
    return ((val + 5) % 150)

sensor_current_bpm_0 = Int('sensor_current_bpm_0')
sensor_OUT_value_0 = Int('sensor_OUT_value_0')
sensor_OUT_reqRead_0 = Bool('sensor_OUT_reqRead_0')
sensor_OUT_reqWrite_0 = Bool('sensor_OUT_reqWrite_0')
monitor_IN_value_0 = Int('monitor_IN_value_0')
monitor_IN_reqRead_0 = Bool('monitor_IN_reqRead_0')
monitor_IN_reqWrite_0 = Bool('monitor_IN_reqWrite_0')
_SafetyController_0_buffered_status_0 = Int('_SafetyController_0_buffered_status_0')
_SafetyController_0_has_data_0 = Int('_SafetyController_0_has_data_0')

sensor_current_bpm_1 = Int('sensor_current_bpm_1')
sensor_OUT_value_1 = Int('sensor_OUT_value_1')
sensor_OUT_reqRead_1 = Bool('sensor_OUT_reqRead_1')
sensor_OUT_reqWrite_1 = Bool('sensor_OUT_reqWrite_1')
monitor_IN_value_1 = Int('monitor_IN_value_1')
monitor_IN_reqRead_1 = Bool('monitor_IN_reqRead_1')
monitor_IN_reqWrite_1 = Bool('monitor_IN_reqWrite_1')
_SafetyController_0_buffered_status_1 = Int('_SafetyController_0_buffered_status_1')
_SafetyController_0_has_data_1 = Int('_SafetyController_0_has_data_1')

sensor_current_bpm_2 = Int('sensor_current_bpm_2')
sensor_OUT_value_2 = Int('sensor_OUT_value_2')
sensor_OUT_reqRead_2 = Bool('sensor_OUT_reqRead_2')
sensor_OUT_reqWrite_2 = Bool('sensor_OUT_reqWrite_2')
monitor_IN_value_2 = Int('monitor_IN_value_2')
monitor_IN_reqRead_2 = Bool('monitor_IN_reqRead_2')
monitor_IN_reqWrite_2 = Bool('monitor_IN_reqWrite_2')
_SafetyController_0_buffered_status_2 = Int('_SafetyController_0_buffered_status_2')
_SafetyController_0_has_data_2 = Int('_SafetyController_0_has_data_2')

sensor_current_bpm_3 = Int('sensor_current_bpm_3')
sensor_OUT_value_3 = Int('sensor_OUT_value_3')
sensor_OUT_reqRead_3 = Bool('sensor_OUT_reqRead_3')
sensor_OUT_reqWrite_3 = Bool('sensor_OUT_reqWrite_3')
monitor_IN_value_3 = Int('monitor_IN_value_3')
monitor_IN_reqRead_3 = Bool('monitor_IN_reqRead_3')
monitor_IN_reqWrite_3 = Bool('monitor_IN_reqWrite_3')
_SafetyController_0_buffered_status_3 = Int('_SafetyController_0_buffered_status_3')
_SafetyController_0_has_data_3 = Int('_SafetyController_0_has_data_3')

sensor_current_bpm_4 = Int('sensor_current_bpm_4')
sensor_OUT_value_4 = Int('sensor_OUT_value_4')
sensor_OUT_reqRead_4 = Bool('sensor_OUT_reqRead_4')
sensor_OUT_reqWrite_4 = Bool('sensor_OUT_reqWrite_4')
monitor_IN_value_4 = Int('monitor_IN_value_4')
monitor_IN_reqRead_4 = Bool('monitor_IN_reqRead_4')
monitor_IN_reqWrite_4 = Bool('monitor_IN_reqWrite_4')
_SafetyController_0_buffered_status_4 = Int('_SafetyController_0_buffered_status_4')
_SafetyController_0_has_data_4 = Int('_SafetyController_0_has_data_4')

sensor_current_bpm_5 = Int('sensor_current_bpm_5')
sensor_OUT_value_5 = Int('sensor_OUT_value_5')
sensor_OUT_reqRead_5 = Bool('sensor_OUT_reqRead_5')
sensor_OUT_reqWrite_5 = Bool('sensor_OUT_reqWrite_5')
monitor_IN_value_5 = Int('monitor_IN_value_5')
monitor_IN_reqRead_5 = Bool('monitor_IN_reqRead_5')
monitor_IN_reqWrite_5 = Bool('monitor_IN_reqWrite_5')
_SafetyController_0_buffered_status_5 = Int('_SafetyController_0_buffered_status_5')
_SafetyController_0_has_data_5 = Int('_SafetyController_0_has_data_5')

sensor_current_bpm_6 = Int('sensor_current_bpm_6')
sensor_OUT_value_6 = Int('sensor_OUT_value_6')
sensor_OUT_reqRead_6 = Bool('sensor_OUT_reqRead_6')
sensor_OUT_reqWrite_6 = Bool('sensor_OUT_reqWrite_6')
monitor_IN_value_6 = Int('monitor_IN_value_6')
monitor_IN_reqRead_6 = Bool('monitor_IN_reqRead_6')
monitor_IN_reqWrite_6 = Bool('monitor_IN_reqWrite_6')
_SafetyController_0_buffered_status_6 = Int('_SafetyController_0_buffered_status_6')
_SafetyController_0_has_data_6 = Int('_SafetyController_0_has_data_6')

sensor_current_bpm_7 = Int('sensor_current_bpm_7')
sensor_OUT_value_7 = Int('sensor_OUT_value_7')
sensor_OUT_reqRead_7 = Bool('sensor_OUT_reqRead_7')
sensor_OUT_reqWrite_7 = Bool('sensor_OUT_reqWrite_7')
monitor_IN_value_7 = Int('monitor_IN_value_7')
monitor_IN_reqRead_7 = Bool('monitor_IN_reqRead_7')
monitor_IN_reqWrite_7 = Bool('monitor_IN_reqWrite_7')
_SafetyController_0_buffered_status_7 = Int('_SafetyController_0_buffered_status_7')
_SafetyController_0_has_data_7 = Int('_SafetyController_0_has_data_7')

sensor_current_bpm_8 = Int('sensor_current_bpm_8')
sensor_OUT_value_8 = Int('sensor_OUT_value_8')
sensor_OUT_reqRead_8 = Bool('sensor_OUT_reqRead_8')
sensor_OUT_reqWrite_8 = Bool('sensor_OUT_reqWrite_8')
monitor_IN_value_8 = Int('monitor_IN_value_8')
monitor_IN_reqRead_8 = Bool('monitor_IN_reqRead_8')
monitor_IN_reqWrite_8 = Bool('monitor_IN_reqWrite_8')
_SafetyController_0_buffered_status_8 = Int('_SafetyController_0_buffered_status_8')
_SafetyController_0_has_data_8 = Int('_SafetyController_0_has_data_8')

sensor_current_bpm_9 = Int('sensor_current_bpm_9')
sensor_OUT_value_9 = Int('sensor_OUT_value_9')
sensor_OUT_reqRead_9 = Bool('sensor_OUT_reqRead_9')
sensor_OUT_reqWrite_9 = Bool('sensor_OUT_reqWrite_9')
monitor_IN_value_9 = Int('monitor_IN_value_9')
monitor_IN_reqRead_9 = Bool('monitor_IN_reqRead_9')
monitor_IN_reqWrite_9 = Bool('monitor_IN_reqWrite_9')
_SafetyController_0_buffered_status_9 = Int('_SafetyController_0_buffered_status_9')
_SafetyController_0_has_data_9 = Int('_SafetyController_0_has_data_9')

sensor_current_bpm_10 = Int('sensor_current_bpm_10')
sensor_OUT_value_10 = Int('sensor_OUT_value_10')
sensor_OUT_reqRead_10 = Bool('sensor_OUT_reqRead_10')
sensor_OUT_reqWrite_10 = Bool('sensor_OUT_reqWrite_10')
monitor_IN_value_10 = Int('monitor_IN_value_10')
monitor_IN_reqRead_10 = Bool('monitor_IN_reqRead_10')
monitor_IN_reqWrite_10 = Bool('monitor_IN_reqWrite_10')
_SafetyController_0_buffered_status_10 = Int('_SafetyController_0_buffered_status_10')
_SafetyController_0_has_data_10 = Int('_SafetyController_0_has_data_10')

sensor_current_bpm_11 = Int('sensor_current_bpm_11')
sensor_OUT_value_11 = Int('sensor_OUT_value_11')
sensor_OUT_reqRead_11 = Bool('sensor_OUT_reqRead_11')
sensor_OUT_reqWrite_11 = Bool('sensor_OUT_reqWrite_11')
monitor_IN_value_11 = Int('monitor_IN_value_11')
monitor_IN_reqRead_11 = Bool('monitor_IN_reqRead_11')
monitor_IN_reqWrite_11 = Bool('monitor_IN_reqWrite_11')
_SafetyController_0_buffered_status_11 = Int('_SafetyController_0_buffered_status_11')
_SafetyController_0_has_data_11 = Int('_SafetyController_0_has_data_11')

sensor_current_bpm_12 = Int('sensor_current_bpm_12')
sensor_OUT_value_12 = Int('sensor_OUT_value_12')
sensor_OUT_reqRead_12 = Bool('sensor_OUT_reqRead_12')
sensor_OUT_reqWrite_12 = Bool('sensor_OUT_reqWrite_12')
monitor_IN_value_12 = Int('monitor_IN_value_12')
monitor_IN_reqRead_12 = Bool('monitor_IN_reqRead_12')
monitor_IN_reqWrite_12 = Bool('monitor_IN_reqWrite_12')
_SafetyController_0_buffered_status_12 = Int('_SafetyController_0_buffered_status_12')
_SafetyController_0_has_data_12 = Int('_SafetyController_0_has_data_12')

sensor_current_bpm_13 = Int('sensor_current_bpm_13')
sensor_OUT_value_13 = Int('sensor_OUT_value_13')
sensor_OUT_reqRead_13 = Bool('sensor_OUT_reqRead_13')
sensor_OUT_reqWrite_13 = Bool('sensor_OUT_reqWrite_13')
monitor_IN_value_13 = Int('monitor_IN_value_13')
monitor_IN_reqRead_13 = Bool('monitor_IN_reqRead_13')
monitor_IN_reqWrite_13 = Bool('monitor_IN_reqWrite_13')
_SafetyController_0_buffered_status_13 = Int('_SafetyController_0_buffered_status_13')
_SafetyController_0_has_data_13 = Int('_SafetyController_0_has_data_13')

sensor_current_bpm_14 = Int('sensor_current_bpm_14')
sensor_OUT_value_14 = Int('sensor_OUT_value_14')
sensor_OUT_reqRead_14 = Bool('sensor_OUT_reqRead_14')
sensor_OUT_reqWrite_14 = Bool('sensor_OUT_reqWrite_14')
monitor_IN_value_14 = Int('monitor_IN_value_14')
monitor_IN_reqRead_14 = Bool('monitor_IN_reqRead_14')
monitor_IN_reqWrite_14 = Bool('monitor_IN_reqWrite_14')
_SafetyController_0_buffered_status_14 = Int('_SafetyController_0_buffered_status_14')
_SafetyController_0_has_data_14 = Int('_SafetyController_0_has_data_14')

sensor_current_bpm_15 = Int('sensor_current_bpm_15')
sensor_OUT_value_15 = Int('sensor_OUT_value_15')
sensor_OUT_reqRead_15 = Bool('sensor_OUT_reqRead_15')
sensor_OUT_reqWrite_15 = Bool('sensor_OUT_reqWrite_15')
monitor_IN_value_15 = Int('monitor_IN_value_15')
monitor_IN_reqRead_15 = Bool('monitor_IN_reqRead_15')
monitor_IN_reqWrite_15 = Bool('monitor_IN_reqWrite_15')
_SafetyController_0_buffered_status_15 = Int('_SafetyController_0_buffered_status_15')
_SafetyController_0_has_data_15 = Int('_SafetyController_0_has_data_15')

sensor_current_bpm_16 = Int('sensor_current_bpm_16')
sensor_OUT_value_16 = Int('sensor_OUT_value_16')
sensor_OUT_reqRead_16 = Bool('sensor_OUT_reqRead_16')
sensor_OUT_reqWrite_16 = Bool('sensor_OUT_reqWrite_16')
monitor_IN_value_16 = Int('monitor_IN_value_16')
monitor_IN_reqRead_16 = Bool('monitor_IN_reqRead_16')
monitor_IN_reqWrite_16 = Bool('monitor_IN_reqWrite_16')
_SafetyController_0_buffered_status_16 = Int('_SafetyController_0_buffered_status_16')
_SafetyController_0_has_data_16 = Int('_SafetyController_0_has_data_16')

sensor_current_bpm_17 = Int('sensor_current_bpm_17')
sensor_OUT_value_17 = Int('sensor_OUT_value_17')
sensor_OUT_reqRead_17 = Bool('sensor_OUT_reqRead_17')
sensor_OUT_reqWrite_17 = Bool('sensor_OUT_reqWrite_17')
monitor_IN_value_17 = Int('monitor_IN_value_17')
monitor_IN_reqRead_17 = Bool('monitor_IN_reqRead_17')
monitor_IN_reqWrite_17 = Bool('monitor_IN_reqWrite_17')
_SafetyController_0_buffered_status_17 = Int('_SafetyController_0_buffered_status_17')
_SafetyController_0_has_data_17 = Int('_SafetyController_0_has_data_17')

sensor_current_bpm_18 = Int('sensor_current_bpm_18')
sensor_OUT_value_18 = Int('sensor_OUT_value_18')
sensor_OUT_reqRead_18 = Bool('sensor_OUT_reqRead_18')
sensor_OUT_reqWrite_18 = Bool('sensor_OUT_reqWrite_18')
monitor_IN_value_18 = Int('monitor_IN_value_18')
monitor_IN_reqRead_18 = Bool('monitor_IN_reqRead_18')
monitor_IN_reqWrite_18 = Bool('monitor_IN_reqWrite_18')
_SafetyController_0_buffered_status_18 = Int('_SafetyController_0_buffered_status_18')
_SafetyController_0_has_data_18 = Int('_SafetyController_0_has_data_18')

sensor_current_bpm_19 = Int('sensor_current_bpm_19')
sensor_OUT_value_19 = Int('sensor_OUT_value_19')
sensor_OUT_reqRead_19 = Bool('sensor_OUT_reqRead_19')
sensor_OUT_reqWrite_19 = Bool('sensor_OUT_reqWrite_19')
monitor_IN_value_19 = Int('monitor_IN_value_19')
monitor_IN_reqRead_19 = Bool('monitor_IN_reqRead_19')
monitor_IN_reqWrite_19 = Bool('monitor_IN_reqWrite_19')
_SafetyController_0_buffered_status_19 = Int('_SafetyController_0_buffered_status_19')
_SafetyController_0_has_data_19 = Int('_SafetyController_0_has_data_19')

sensor_current_bpm_20 = Int('sensor_current_bpm_20')
sensor_OUT_value_20 = Int('sensor_OUT_value_20')
sensor_OUT_reqRead_20 = Bool('sensor_OUT_reqRead_20')
sensor_OUT_reqWrite_20 = Bool('sensor_OUT_reqWrite_20')
monitor_IN_value_20 = Int('monitor_IN_value_20')
monitor_IN_reqRead_20 = Bool('monitor_IN_reqRead_20')
monitor_IN_reqWrite_20 = Bool('monitor_IN_reqWrite_20')
_SafetyController_0_buffered_status_20 = Int('_SafetyController_0_buffered_status_20')
_SafetyController_0_has_data_20 = Int('_SafetyController_0_has_data_20')

sensor_current_bpm_21 = Int('sensor_current_bpm_21')
sensor_OUT_value_21 = Int('sensor_OUT_value_21')
sensor_OUT_reqRead_21 = Bool('sensor_OUT_reqRead_21')
sensor_OUT_reqWrite_21 = Bool('sensor_OUT_reqWrite_21')
monitor_IN_value_21 = Int('monitor_IN_value_21')
monitor_IN_reqRead_21 = Bool('monitor_IN_reqRead_21')
monitor_IN_reqWrite_21 = Bool('monitor_IN_reqWrite_21')
_SafetyController_0_buffered_status_21 = Int('_SafetyController_0_buffered_status_21')
_SafetyController_0_has_data_21 = Int('_SafetyController_0_has_data_21')

sensor_current_bpm_22 = Int('sensor_current_bpm_22')
sensor_OUT_value_22 = Int('sensor_OUT_value_22')
sensor_OUT_reqRead_22 = Bool('sensor_OUT_reqRead_22')
sensor_OUT_reqWrite_22 = Bool('sensor_OUT_reqWrite_22')
monitor_IN_value_22 = Int('monitor_IN_value_22')
monitor_IN_reqRead_22 = Bool('monitor_IN_reqRead_22')
monitor_IN_reqWrite_22 = Bool('monitor_IN_reqWrite_22')
_SafetyController_0_buffered_status_22 = Int('_SafetyController_0_buffered_status_22')
_SafetyController_0_has_data_22 = Int('_SafetyController_0_has_data_22')

sensor_current_bpm_23 = Int('sensor_current_bpm_23')
sensor_OUT_value_23 = Int('sensor_OUT_value_23')
sensor_OUT_reqRead_23 = Bool('sensor_OUT_reqRead_23')
sensor_OUT_reqWrite_23 = Bool('sensor_OUT_reqWrite_23')
monitor_IN_value_23 = Int('monitor_IN_value_23')
monitor_IN_reqRead_23 = Bool('monitor_IN_reqRead_23')
monitor_IN_reqWrite_23 = Bool('monitor_IN_reqWrite_23')
_SafetyController_0_buffered_status_23 = Int('_SafetyController_0_buffered_status_23')
_SafetyController_0_has_data_23 = Int('_SafetyController_0_has_data_23')

sensor_current_bpm_24 = Int('sensor_current_bpm_24')
sensor_OUT_value_24 = Int('sensor_OUT_value_24')
sensor_OUT_reqRead_24 = Bool('sensor_OUT_reqRead_24')
sensor_OUT_reqWrite_24 = Bool('sensor_OUT_reqWrite_24')
monitor_IN_value_24 = Int('monitor_IN_value_24')
monitor_IN_reqRead_24 = Bool('monitor_IN_reqRead_24')
monitor_IN_reqWrite_24 = Bool('monitor_IN_reqWrite_24')
_SafetyController_0_buffered_status_24 = Int('_SafetyController_0_buffered_status_24')
_SafetyController_0_has_data_24 = Int('_SafetyController_0_has_data_24')

sensor_current_bpm_25 = Int('sensor_current_bpm_25')
sensor_OUT_value_25 = Int('sensor_OUT_value_25')
sensor_OUT_reqRead_25 = Bool('sensor_OUT_reqRead_25')
sensor_OUT_reqWrite_25 = Bool('sensor_OUT_reqWrite_25')
monitor_IN_value_25 = Int('monitor_IN_value_25')
monitor_IN_reqRead_25 = Bool('monitor_IN_reqRead_25')
monitor_IN_reqWrite_25 = Bool('monitor_IN_reqWrite_25')
_SafetyController_0_buffered_status_25 = Int('_SafetyController_0_buffered_status_25')
_SafetyController_0_has_data_25 = Int('_SafetyController_0_has_data_25')

sensor_current_bpm_26 = Int('sensor_current_bpm_26')
sensor_OUT_value_26 = Int('sensor_OUT_value_26')
sensor_OUT_reqRead_26 = Bool('sensor_OUT_reqRead_26')
sensor_OUT_reqWrite_26 = Bool('sensor_OUT_reqWrite_26')
monitor_IN_value_26 = Int('monitor_IN_value_26')
monitor_IN_reqRead_26 = Bool('monitor_IN_reqRead_26')
monitor_IN_reqWrite_26 = Bool('monitor_IN_reqWrite_26')
_SafetyController_0_buffered_status_26 = Int('_SafetyController_0_buffered_status_26')
_SafetyController_0_has_data_26 = Int('_SafetyController_0_has_data_26')

sensor_current_bpm_27 = Int('sensor_current_bpm_27')
sensor_OUT_value_27 = Int('sensor_OUT_value_27')
sensor_OUT_reqRead_27 = Bool('sensor_OUT_reqRead_27')
sensor_OUT_reqWrite_27 = Bool('sensor_OUT_reqWrite_27')
monitor_IN_value_27 = Int('monitor_IN_value_27')
monitor_IN_reqRead_27 = Bool('monitor_IN_reqRead_27')
monitor_IN_reqWrite_27 = Bool('monitor_IN_reqWrite_27')
_SafetyController_0_buffered_status_27 = Int('_SafetyController_0_buffered_status_27')
_SafetyController_0_has_data_27 = Int('_SafetyController_0_has_data_27')

sensor_current_bpm_28 = Int('sensor_current_bpm_28')
sensor_OUT_value_28 = Int('sensor_OUT_value_28')
sensor_OUT_reqRead_28 = Bool('sensor_OUT_reqRead_28')
sensor_OUT_reqWrite_28 = Bool('sensor_OUT_reqWrite_28')
monitor_IN_value_28 = Int('monitor_IN_value_28')
monitor_IN_reqRead_28 = Bool('monitor_IN_reqRead_28')
monitor_IN_reqWrite_28 = Bool('monitor_IN_reqWrite_28')
_SafetyController_0_buffered_status_28 = Int('_SafetyController_0_buffered_status_28')
_SafetyController_0_has_data_28 = Int('_SafetyController_0_has_data_28')

sensor_current_bpm_29 = Int('sensor_current_bpm_29')
sensor_OUT_value_29 = Int('sensor_OUT_value_29')
sensor_OUT_reqRead_29 = Bool('sensor_OUT_reqRead_29')
sensor_OUT_reqWrite_29 = Bool('sensor_OUT_reqWrite_29')
monitor_IN_value_29 = Int('monitor_IN_value_29')
monitor_IN_reqRead_29 = Bool('monitor_IN_reqRead_29')
monitor_IN_reqWrite_29 = Bool('monitor_IN_reqWrite_29')
_SafetyController_0_buffered_status_29 = Int('_SafetyController_0_buffered_status_29')
_SafetyController_0_has_data_29 = Int('_SafetyController_0_has_data_29')

sensor_current_bpm_30 = Int('sensor_current_bpm_30')
sensor_OUT_value_30 = Int('sensor_OUT_value_30')
sensor_OUT_reqRead_30 = Bool('sensor_OUT_reqRead_30')
sensor_OUT_reqWrite_30 = Bool('sensor_OUT_reqWrite_30')
monitor_IN_value_30 = Int('monitor_IN_value_30')
monitor_IN_reqRead_30 = Bool('monitor_IN_reqRead_30')
monitor_IN_reqWrite_30 = Bool('monitor_IN_reqWrite_30')
_SafetyController_0_buffered_status_30 = Int('_SafetyController_0_buffered_status_30')
_SafetyController_0_has_data_30 = Int('_SafetyController_0_has_data_30')

sensor_current_bpm_31 = Int('sensor_current_bpm_31')
sensor_OUT_value_31 = Int('sensor_OUT_value_31')
sensor_OUT_reqRead_31 = Bool('sensor_OUT_reqRead_31')
sensor_OUT_reqWrite_31 = Bool('sensor_OUT_reqWrite_31')
monitor_IN_value_31 = Int('monitor_IN_value_31')
monitor_IN_reqRead_31 = Bool('monitor_IN_reqRead_31')
monitor_IN_reqWrite_31 = Bool('monitor_IN_reqWrite_31')
_SafetyController_0_buffered_status_31 = Int('_SafetyController_0_buffered_status_31')
_SafetyController_0_has_data_31 = Int('_SafetyController_0_has_data_31')

sensor_current_bpm_32 = Int('sensor_current_bpm_32')
sensor_OUT_value_32 = Int('sensor_OUT_value_32')
sensor_OUT_reqRead_32 = Bool('sensor_OUT_reqRead_32')
sensor_OUT_reqWrite_32 = Bool('sensor_OUT_reqWrite_32')
monitor_IN_value_32 = Int('monitor_IN_value_32')
monitor_IN_reqRead_32 = Bool('monitor_IN_reqRead_32')
monitor_IN_reqWrite_32 = Bool('monitor_IN_reqWrite_32')
_SafetyController_0_buffered_status_32 = Int('_SafetyController_0_buffered_status_32')
_SafetyController_0_has_data_32 = Int('_SafetyController_0_has_data_32')

sensor_current_bpm_33 = Int('sensor_current_bpm_33')
sensor_OUT_value_33 = Int('sensor_OUT_value_33')
sensor_OUT_reqRead_33 = Bool('sensor_OUT_reqRead_33')
sensor_OUT_reqWrite_33 = Bool('sensor_OUT_reqWrite_33')
monitor_IN_value_33 = Int('monitor_IN_value_33')
monitor_IN_reqRead_33 = Bool('monitor_IN_reqRead_33')
monitor_IN_reqWrite_33 = Bool('monitor_IN_reqWrite_33')
_SafetyController_0_buffered_status_33 = Int('_SafetyController_0_buffered_status_33')
_SafetyController_0_has_data_33 = Int('_SafetyController_0_has_data_33')

sensor_current_bpm_34 = Int('sensor_current_bpm_34')
sensor_OUT_value_34 = Int('sensor_OUT_value_34')
sensor_OUT_reqRead_34 = Bool('sensor_OUT_reqRead_34')
sensor_OUT_reqWrite_34 = Bool('sensor_OUT_reqWrite_34')
monitor_IN_value_34 = Int('monitor_IN_value_34')
monitor_IN_reqRead_34 = Bool('monitor_IN_reqRead_34')
monitor_IN_reqWrite_34 = Bool('monitor_IN_reqWrite_34')
_SafetyController_0_buffered_status_34 = Int('_SafetyController_0_buffered_status_34')
_SafetyController_0_has_data_34 = Int('_SafetyController_0_has_data_34')

sensor_current_bpm_35 = Int('sensor_current_bpm_35')
sensor_OUT_value_35 = Int('sensor_OUT_value_35')
sensor_OUT_reqRead_35 = Bool('sensor_OUT_reqRead_35')
sensor_OUT_reqWrite_35 = Bool('sensor_OUT_reqWrite_35')
monitor_IN_value_35 = Int('monitor_IN_value_35')
monitor_IN_reqRead_35 = Bool('monitor_IN_reqRead_35')
monitor_IN_reqWrite_35 = Bool('monitor_IN_reqWrite_35')
_SafetyController_0_buffered_status_35 = Int('_SafetyController_0_buffered_status_35')
_SafetyController_0_has_data_35 = Int('_SafetyController_0_has_data_35')

sensor_current_bpm_36 = Int('sensor_current_bpm_36')
sensor_OUT_value_36 = Int('sensor_OUT_value_36')
sensor_OUT_reqRead_36 = Bool('sensor_OUT_reqRead_36')
sensor_OUT_reqWrite_36 = Bool('sensor_OUT_reqWrite_36')
monitor_IN_value_36 = Int('monitor_IN_value_36')
monitor_IN_reqRead_36 = Bool('monitor_IN_reqRead_36')
monitor_IN_reqWrite_36 = Bool('monitor_IN_reqWrite_36')
_SafetyController_0_buffered_status_36 = Int('_SafetyController_0_buffered_status_36')
_SafetyController_0_has_data_36 = Int('_SafetyController_0_has_data_36')

sensor_current_bpm_37 = Int('sensor_current_bpm_37')
sensor_OUT_value_37 = Int('sensor_OUT_value_37')
sensor_OUT_reqRead_37 = Bool('sensor_OUT_reqRead_37')
sensor_OUT_reqWrite_37 = Bool('sensor_OUT_reqWrite_37')
monitor_IN_value_37 = Int('monitor_IN_value_37')
monitor_IN_reqRead_37 = Bool('monitor_IN_reqRead_37')
monitor_IN_reqWrite_37 = Bool('monitor_IN_reqWrite_37')
_SafetyController_0_buffered_status_37 = Int('_SafetyController_0_buffered_status_37')
_SafetyController_0_has_data_37 = Int('_SafetyController_0_has_data_37')

sensor_current_bpm_38 = Int('sensor_current_bpm_38')
sensor_OUT_value_38 = Int('sensor_OUT_value_38')
sensor_OUT_reqRead_38 = Bool('sensor_OUT_reqRead_38')
sensor_OUT_reqWrite_38 = Bool('sensor_OUT_reqWrite_38')
monitor_IN_value_38 = Int('monitor_IN_value_38')
monitor_IN_reqRead_38 = Bool('monitor_IN_reqRead_38')
monitor_IN_reqWrite_38 = Bool('monitor_IN_reqWrite_38')
_SafetyController_0_buffered_status_38 = Int('_SafetyController_0_buffered_status_38')
_SafetyController_0_has_data_38 = Int('_SafetyController_0_has_data_38')

sensor_current_bpm_39 = Int('sensor_current_bpm_39')
sensor_OUT_value_39 = Int('sensor_OUT_value_39')
sensor_OUT_reqRead_39 = Bool('sensor_OUT_reqRead_39')
sensor_OUT_reqWrite_39 = Bool('sensor_OUT_reqWrite_39')
monitor_IN_value_39 = Int('monitor_IN_value_39')
monitor_IN_reqRead_39 = Bool('monitor_IN_reqRead_39')
monitor_IN_reqWrite_39 = Bool('monitor_IN_reqWrite_39')
_SafetyController_0_buffered_status_39 = Int('_SafetyController_0_buffered_status_39')
_SafetyController_0_has_data_39 = Int('_SafetyController_0_has_data_39')

sensor_current_bpm_40 = Int('sensor_current_bpm_40')
sensor_OUT_value_40 = Int('sensor_OUT_value_40')
sensor_OUT_reqRead_40 = Bool('sensor_OUT_reqRead_40')
sensor_OUT_reqWrite_40 = Bool('sensor_OUT_reqWrite_40')
monitor_IN_value_40 = Int('monitor_IN_value_40')
monitor_IN_reqRead_40 = Bool('monitor_IN_reqRead_40')
monitor_IN_reqWrite_40 = Bool('monitor_IN_reqWrite_40')
_SafetyController_0_buffered_status_40 = Int('_SafetyController_0_buffered_status_40')
_SafetyController_0_has_data_40 = Int('_SafetyController_0_has_data_40')

sensor_current_bpm_41 = Int('sensor_current_bpm_41')
sensor_OUT_value_41 = Int('sensor_OUT_value_41')
sensor_OUT_reqRead_41 = Bool('sensor_OUT_reqRead_41')
sensor_OUT_reqWrite_41 = Bool('sensor_OUT_reqWrite_41')
monitor_IN_value_41 = Int('monitor_IN_value_41')
monitor_IN_reqRead_41 = Bool('monitor_IN_reqRead_41')
monitor_IN_reqWrite_41 = Bool('monitor_IN_reqWrite_41')
_SafetyController_0_buffered_status_41 = Int('_SafetyController_0_buffered_status_41')
_SafetyController_0_has_data_41 = Int('_SafetyController_0_has_data_41')

sensor_current_bpm_42 = Int('sensor_current_bpm_42')
sensor_OUT_value_42 = Int('sensor_OUT_value_42')
sensor_OUT_reqRead_42 = Bool('sensor_OUT_reqRead_42')
sensor_OUT_reqWrite_42 = Bool('sensor_OUT_reqWrite_42')
monitor_IN_value_42 = Int('monitor_IN_value_42')
monitor_IN_reqRead_42 = Bool('monitor_IN_reqRead_42')
monitor_IN_reqWrite_42 = Bool('monitor_IN_reqWrite_42')
_SafetyController_0_buffered_status_42 = Int('_SafetyController_0_buffered_status_42')
_SafetyController_0_has_data_42 = Int('_SafetyController_0_has_data_42')

sensor_current_bpm_43 = Int('sensor_current_bpm_43')
sensor_OUT_value_43 = Int('sensor_OUT_value_43')
sensor_OUT_reqRead_43 = Bool('sensor_OUT_reqRead_43')
sensor_OUT_reqWrite_43 = Bool('sensor_OUT_reqWrite_43')
monitor_IN_value_43 = Int('monitor_IN_value_43')
monitor_IN_reqRead_43 = Bool('monitor_IN_reqRead_43')
monitor_IN_reqWrite_43 = Bool('monitor_IN_reqWrite_43')
_SafetyController_0_buffered_status_43 = Int('_SafetyController_0_buffered_status_43')
_SafetyController_0_has_data_43 = Int('_SafetyController_0_has_data_43')

sensor_current_bpm_44 = Int('sensor_current_bpm_44')
sensor_OUT_value_44 = Int('sensor_OUT_value_44')
sensor_OUT_reqRead_44 = Bool('sensor_OUT_reqRead_44')
sensor_OUT_reqWrite_44 = Bool('sensor_OUT_reqWrite_44')
monitor_IN_value_44 = Int('monitor_IN_value_44')
monitor_IN_reqRead_44 = Bool('monitor_IN_reqRead_44')
monitor_IN_reqWrite_44 = Bool('monitor_IN_reqWrite_44')
_SafetyController_0_buffered_status_44 = Int('_SafetyController_0_buffered_status_44')
_SafetyController_0_has_data_44 = Int('_SafetyController_0_has_data_44')

sensor_current_bpm_45 = Int('sensor_current_bpm_45')
sensor_OUT_value_45 = Int('sensor_OUT_value_45')
sensor_OUT_reqRead_45 = Bool('sensor_OUT_reqRead_45')
sensor_OUT_reqWrite_45 = Bool('sensor_OUT_reqWrite_45')
monitor_IN_value_45 = Int('monitor_IN_value_45')
monitor_IN_reqRead_45 = Bool('monitor_IN_reqRead_45')
monitor_IN_reqWrite_45 = Bool('monitor_IN_reqWrite_45')
_SafetyController_0_buffered_status_45 = Int('_SafetyController_0_buffered_status_45')
_SafetyController_0_has_data_45 = Int('_SafetyController_0_has_data_45')

sensor_current_bpm_46 = Int('sensor_current_bpm_46')
sensor_OUT_value_46 = Int('sensor_OUT_value_46')
sensor_OUT_reqRead_46 = Bool('sensor_OUT_reqRead_46')
sensor_OUT_reqWrite_46 = Bool('sensor_OUT_reqWrite_46')
monitor_IN_value_46 = Int('monitor_IN_value_46')
monitor_IN_reqRead_46 = Bool('monitor_IN_reqRead_46')
monitor_IN_reqWrite_46 = Bool('monitor_IN_reqWrite_46')
_SafetyController_0_buffered_status_46 = Int('_SafetyController_0_buffered_status_46')
_SafetyController_0_has_data_46 = Int('_SafetyController_0_has_data_46')

sensor_current_bpm_47 = Int('sensor_current_bpm_47')
sensor_OUT_value_47 = Int('sensor_OUT_value_47')
sensor_OUT_reqRead_47 = Bool('sensor_OUT_reqRead_47')
sensor_OUT_reqWrite_47 = Bool('sensor_OUT_reqWrite_47')
monitor_IN_value_47 = Int('monitor_IN_value_47')
monitor_IN_reqRead_47 = Bool('monitor_IN_reqRead_47')
monitor_IN_reqWrite_47 = Bool('monitor_IN_reqWrite_47')
_SafetyController_0_buffered_status_47 = Int('_SafetyController_0_buffered_status_47')
_SafetyController_0_has_data_47 = Int('_SafetyController_0_has_data_47')

sensor_current_bpm_48 = Int('sensor_current_bpm_48')
sensor_OUT_value_48 = Int('sensor_OUT_value_48')
sensor_OUT_reqRead_48 = Bool('sensor_OUT_reqRead_48')
sensor_OUT_reqWrite_48 = Bool('sensor_OUT_reqWrite_48')
monitor_IN_value_48 = Int('monitor_IN_value_48')
monitor_IN_reqRead_48 = Bool('monitor_IN_reqRead_48')
monitor_IN_reqWrite_48 = Bool('monitor_IN_reqWrite_48')
_SafetyController_0_buffered_status_48 = Int('_SafetyController_0_buffered_status_48')
_SafetyController_0_has_data_48 = Int('_SafetyController_0_has_data_48')

sensor_current_bpm_49 = Int('sensor_current_bpm_49')
sensor_OUT_value_49 = Int('sensor_OUT_value_49')
sensor_OUT_reqRead_49 = Bool('sensor_OUT_reqRead_49')
sensor_OUT_reqWrite_49 = Bool('sensor_OUT_reqWrite_49')
monitor_IN_value_49 = Int('monitor_IN_value_49')
monitor_IN_reqRead_49 = Bool('monitor_IN_reqRead_49')
monitor_IN_reqWrite_49 = Bool('monitor_IN_reqWrite_49')
_SafetyController_0_buffered_status_49 = Int('_SafetyController_0_buffered_status_49')
_SafetyController_0_has_data_49 = Int('_SafetyController_0_has_data_49')

sensor_current_bpm_50 = Int('sensor_current_bpm_50')
sensor_OUT_value_50 = Int('sensor_OUT_value_50')
sensor_OUT_reqRead_50 = Bool('sensor_OUT_reqRead_50')
sensor_OUT_reqWrite_50 = Bool('sensor_OUT_reqWrite_50')
monitor_IN_value_50 = Int('monitor_IN_value_50')
monitor_IN_reqRead_50 = Bool('monitor_IN_reqRead_50')
monitor_IN_reqWrite_50 = Bool('monitor_IN_reqWrite_50')
_SafetyController_0_buffered_status_50 = Int('_SafetyController_0_buffered_status_50')
_SafetyController_0_has_data_50 = Int('_SafetyController_0_has_data_50')

sensor_current_bpm_51 = Int('sensor_current_bpm_51')
sensor_OUT_value_51 = Int('sensor_OUT_value_51')
sensor_OUT_reqRead_51 = Bool('sensor_OUT_reqRead_51')
sensor_OUT_reqWrite_51 = Bool('sensor_OUT_reqWrite_51')
monitor_IN_value_51 = Int('monitor_IN_value_51')
monitor_IN_reqRead_51 = Bool('monitor_IN_reqRead_51')
monitor_IN_reqWrite_51 = Bool('monitor_IN_reqWrite_51')
_SafetyController_0_buffered_status_51 = Int('_SafetyController_0_buffered_status_51')
_SafetyController_0_has_data_51 = Int('_SafetyController_0_has_data_51')

sensor_current_bpm_52 = Int('sensor_current_bpm_52')
sensor_OUT_value_52 = Int('sensor_OUT_value_52')
sensor_OUT_reqRead_52 = Bool('sensor_OUT_reqRead_52')
sensor_OUT_reqWrite_52 = Bool('sensor_OUT_reqWrite_52')
monitor_IN_value_52 = Int('monitor_IN_value_52')
monitor_IN_reqRead_52 = Bool('monitor_IN_reqRead_52')
monitor_IN_reqWrite_52 = Bool('monitor_IN_reqWrite_52')
_SafetyController_0_buffered_status_52 = Int('_SafetyController_0_buffered_status_52')
_SafetyController_0_has_data_52 = Int('_SafetyController_0_has_data_52')

sensor_current_bpm_53 = Int('sensor_current_bpm_53')
sensor_OUT_value_53 = Int('sensor_OUT_value_53')
sensor_OUT_reqRead_53 = Bool('sensor_OUT_reqRead_53')
sensor_OUT_reqWrite_53 = Bool('sensor_OUT_reqWrite_53')
monitor_IN_value_53 = Int('monitor_IN_value_53')
monitor_IN_reqRead_53 = Bool('monitor_IN_reqRead_53')
monitor_IN_reqWrite_53 = Bool('monitor_IN_reqWrite_53')
_SafetyController_0_buffered_status_53 = Int('_SafetyController_0_buffered_status_53')
_SafetyController_0_has_data_53 = Int('_SafetyController_0_has_data_53')

sensor_current_bpm_54 = Int('sensor_current_bpm_54')
sensor_OUT_value_54 = Int('sensor_OUT_value_54')
sensor_OUT_reqRead_54 = Bool('sensor_OUT_reqRead_54')
sensor_OUT_reqWrite_54 = Bool('sensor_OUT_reqWrite_54')
monitor_IN_value_54 = Int('monitor_IN_value_54')
monitor_IN_reqRead_54 = Bool('monitor_IN_reqRead_54')
monitor_IN_reqWrite_54 = Bool('monitor_IN_reqWrite_54')
_SafetyController_0_buffered_status_54 = Int('_SafetyController_0_buffered_status_54')
_SafetyController_0_has_data_54 = Int('_SafetyController_0_has_data_54')

sensor_current_bpm_55 = Int('sensor_current_bpm_55')
sensor_OUT_value_55 = Int('sensor_OUT_value_55')
sensor_OUT_reqRead_55 = Bool('sensor_OUT_reqRead_55')
sensor_OUT_reqWrite_55 = Bool('sensor_OUT_reqWrite_55')
monitor_IN_value_55 = Int('monitor_IN_value_55')
monitor_IN_reqRead_55 = Bool('monitor_IN_reqRead_55')
monitor_IN_reqWrite_55 = Bool('monitor_IN_reqWrite_55')
_SafetyController_0_buffered_status_55 = Int('_SafetyController_0_buffered_status_55')
_SafetyController_0_has_data_55 = Int('_SafetyController_0_has_data_55')

sensor_current_bpm_56 = Int('sensor_current_bpm_56')
sensor_OUT_value_56 = Int('sensor_OUT_value_56')
sensor_OUT_reqRead_56 = Bool('sensor_OUT_reqRead_56')
sensor_OUT_reqWrite_56 = Bool('sensor_OUT_reqWrite_56')
monitor_IN_value_56 = Int('monitor_IN_value_56')
monitor_IN_reqRead_56 = Bool('monitor_IN_reqRead_56')
monitor_IN_reqWrite_56 = Bool('monitor_IN_reqWrite_56')
_SafetyController_0_buffered_status_56 = Int('_SafetyController_0_buffered_status_56')
_SafetyController_0_has_data_56 = Int('_SafetyController_0_has_data_56')

sensor_current_bpm_57 = Int('sensor_current_bpm_57')
sensor_OUT_value_57 = Int('sensor_OUT_value_57')
sensor_OUT_reqRead_57 = Bool('sensor_OUT_reqRead_57')
sensor_OUT_reqWrite_57 = Bool('sensor_OUT_reqWrite_57')
monitor_IN_value_57 = Int('monitor_IN_value_57')
monitor_IN_reqRead_57 = Bool('monitor_IN_reqRead_57')
monitor_IN_reqWrite_57 = Bool('monitor_IN_reqWrite_57')
_SafetyController_0_buffered_status_57 = Int('_SafetyController_0_buffered_status_57')
_SafetyController_0_has_data_57 = Int('_SafetyController_0_has_data_57')

sensor_current_bpm_58 = Int('sensor_current_bpm_58')
sensor_OUT_value_58 = Int('sensor_OUT_value_58')
sensor_OUT_reqRead_58 = Bool('sensor_OUT_reqRead_58')
sensor_OUT_reqWrite_58 = Bool('sensor_OUT_reqWrite_58')
monitor_IN_value_58 = Int('monitor_IN_value_58')
monitor_IN_reqRead_58 = Bool('monitor_IN_reqRead_58')
monitor_IN_reqWrite_58 = Bool('monitor_IN_reqWrite_58')
_SafetyController_0_buffered_status_58 = Int('_SafetyController_0_buffered_status_58')
_SafetyController_0_has_data_58 = Int('_SafetyController_0_has_data_58')

sensor_current_bpm_59 = Int('sensor_current_bpm_59')
sensor_OUT_value_59 = Int('sensor_OUT_value_59')
sensor_OUT_reqRead_59 = Bool('sensor_OUT_reqRead_59')
sensor_OUT_reqWrite_59 = Bool('sensor_OUT_reqWrite_59')
monitor_IN_value_59 = Int('monitor_IN_value_59')
monitor_IN_reqRead_59 = Bool('monitor_IN_reqRead_59')
monitor_IN_reqWrite_59 = Bool('monitor_IN_reqWrite_59')
_SafetyController_0_buffered_status_59 = Int('_SafetyController_0_buffered_status_59')
_SafetyController_0_has_data_59 = Int('_SafetyController_0_has_data_59')

sensor_current_bpm_60 = Int('sensor_current_bpm_60')
sensor_OUT_value_60 = Int('sensor_OUT_value_60')
sensor_OUT_reqRead_60 = Bool('sensor_OUT_reqRead_60')
sensor_OUT_reqWrite_60 = Bool('sensor_OUT_reqWrite_60')
monitor_IN_value_60 = Int('monitor_IN_value_60')
monitor_IN_reqRead_60 = Bool('monitor_IN_reqRead_60')
monitor_IN_reqWrite_60 = Bool('monitor_IN_reqWrite_60')
_SafetyController_0_buffered_status_60 = Int('_SafetyController_0_buffered_status_60')
_SafetyController_0_has_data_60 = Int('_SafetyController_0_has_data_60')

sensor_current_bpm_61 = Int('sensor_current_bpm_61')
sensor_OUT_value_61 = Int('sensor_OUT_value_61')
sensor_OUT_reqRead_61 = Bool('sensor_OUT_reqRead_61')
sensor_OUT_reqWrite_61 = Bool('sensor_OUT_reqWrite_61')
monitor_IN_value_61 = Int('monitor_IN_value_61')
monitor_IN_reqRead_61 = Bool('monitor_IN_reqRead_61')
monitor_IN_reqWrite_61 = Bool('monitor_IN_reqWrite_61')
_SafetyController_0_buffered_status_61 = Int('_SafetyController_0_buffered_status_61')
_SafetyController_0_has_data_61 = Int('_SafetyController_0_has_data_61')

sensor_current_bpm_62 = Int('sensor_current_bpm_62')
sensor_OUT_value_62 = Int('sensor_OUT_value_62')
sensor_OUT_reqRead_62 = Bool('sensor_OUT_reqRead_62')
sensor_OUT_reqWrite_62 = Bool('sensor_OUT_reqWrite_62')
monitor_IN_value_62 = Int('monitor_IN_value_62')
monitor_IN_reqRead_62 = Bool('monitor_IN_reqRead_62')
monitor_IN_reqWrite_62 = Bool('monitor_IN_reqWrite_62')
_SafetyController_0_buffered_status_62 = Int('_SafetyController_0_buffered_status_62')
_SafetyController_0_has_data_62 = Int('_SafetyController_0_has_data_62')

sensor_current_bpm_63 = Int('sensor_current_bpm_63')
sensor_OUT_value_63 = Int('sensor_OUT_value_63')
sensor_OUT_reqRead_63 = Bool('sensor_OUT_reqRead_63')
sensor_OUT_reqWrite_63 = Bool('sensor_OUT_reqWrite_63')
monitor_IN_value_63 = Int('monitor_IN_value_63')
monitor_IN_reqRead_63 = Bool('monitor_IN_reqRead_63')
monitor_IN_reqWrite_63 = Bool('monitor_IN_reqWrite_63')
_SafetyController_0_buffered_status_63 = Int('_SafetyController_0_buffered_status_63')
_SafetyController_0_has_data_63 = Int('_SafetyController_0_has_data_63')

sensor_current_bpm_64 = Int('sensor_current_bpm_64')
sensor_OUT_value_64 = Int('sensor_OUT_value_64')
sensor_OUT_reqRead_64 = Bool('sensor_OUT_reqRead_64')
sensor_OUT_reqWrite_64 = Bool('sensor_OUT_reqWrite_64')
monitor_IN_value_64 = Int('monitor_IN_value_64')
monitor_IN_reqRead_64 = Bool('monitor_IN_reqRead_64')
monitor_IN_reqWrite_64 = Bool('monitor_IN_reqWrite_64')
_SafetyController_0_buffered_status_64 = Int('_SafetyController_0_buffered_status_64')
_SafetyController_0_has_data_64 = Int('_SafetyController_0_has_data_64')

sensor_current_bpm_65 = Int('sensor_current_bpm_65')
sensor_OUT_value_65 = Int('sensor_OUT_value_65')
sensor_OUT_reqRead_65 = Bool('sensor_OUT_reqRead_65')
sensor_OUT_reqWrite_65 = Bool('sensor_OUT_reqWrite_65')
monitor_IN_value_65 = Int('monitor_IN_value_65')
monitor_IN_reqRead_65 = Bool('monitor_IN_reqRead_65')
monitor_IN_reqWrite_65 = Bool('monitor_IN_reqWrite_65')
_SafetyController_0_buffered_status_65 = Int('_SafetyController_0_buffered_status_65')
_SafetyController_0_has_data_65 = Int('_SafetyController_0_has_data_65')

sensor_current_bpm_66 = Int('sensor_current_bpm_66')
sensor_OUT_value_66 = Int('sensor_OUT_value_66')
sensor_OUT_reqRead_66 = Bool('sensor_OUT_reqRead_66')
sensor_OUT_reqWrite_66 = Bool('sensor_OUT_reqWrite_66')
monitor_IN_value_66 = Int('monitor_IN_value_66')
monitor_IN_reqRead_66 = Bool('monitor_IN_reqRead_66')
monitor_IN_reqWrite_66 = Bool('monitor_IN_reqWrite_66')
_SafetyController_0_buffered_status_66 = Int('_SafetyController_0_buffered_status_66')
_SafetyController_0_has_data_66 = Int('_SafetyController_0_has_data_66')

sensor_current_bpm_67 = Int('sensor_current_bpm_67')
sensor_OUT_value_67 = Int('sensor_OUT_value_67')
sensor_OUT_reqRead_67 = Bool('sensor_OUT_reqRead_67')
sensor_OUT_reqWrite_67 = Bool('sensor_OUT_reqWrite_67')
monitor_IN_value_67 = Int('monitor_IN_value_67')
monitor_IN_reqRead_67 = Bool('monitor_IN_reqRead_67')
monitor_IN_reqWrite_67 = Bool('monitor_IN_reqWrite_67')
_SafetyController_0_buffered_status_67 = Int('_SafetyController_0_buffered_status_67')
_SafetyController_0_has_data_67 = Int('_SafetyController_0_has_data_67')

sensor_current_bpm_68 = Int('sensor_current_bpm_68')
sensor_OUT_value_68 = Int('sensor_OUT_value_68')
sensor_OUT_reqRead_68 = Bool('sensor_OUT_reqRead_68')
sensor_OUT_reqWrite_68 = Bool('sensor_OUT_reqWrite_68')
monitor_IN_value_68 = Int('monitor_IN_value_68')
monitor_IN_reqRead_68 = Bool('monitor_IN_reqRead_68')
monitor_IN_reqWrite_68 = Bool('monitor_IN_reqWrite_68')
_SafetyController_0_buffered_status_68 = Int('_SafetyController_0_buffered_status_68')
_SafetyController_0_has_data_68 = Int('_SafetyController_0_has_data_68')

sensor_current_bpm_69 = Int('sensor_current_bpm_69')
sensor_OUT_value_69 = Int('sensor_OUT_value_69')
sensor_OUT_reqRead_69 = Bool('sensor_OUT_reqRead_69')
sensor_OUT_reqWrite_69 = Bool('sensor_OUT_reqWrite_69')
monitor_IN_value_69 = Int('monitor_IN_value_69')
monitor_IN_reqRead_69 = Bool('monitor_IN_reqRead_69')
monitor_IN_reqWrite_69 = Bool('monitor_IN_reqWrite_69')
_SafetyController_0_buffered_status_69 = Int('_SafetyController_0_buffered_status_69')
_SafetyController_0_has_data_69 = Int('_SafetyController_0_has_data_69')

sensor_current_bpm_70 = Int('sensor_current_bpm_70')
sensor_OUT_value_70 = Int('sensor_OUT_value_70')
sensor_OUT_reqRead_70 = Bool('sensor_OUT_reqRead_70')
sensor_OUT_reqWrite_70 = Bool('sensor_OUT_reqWrite_70')
monitor_IN_value_70 = Int('monitor_IN_value_70')
monitor_IN_reqRead_70 = Bool('monitor_IN_reqRead_70')
monitor_IN_reqWrite_70 = Bool('monitor_IN_reqWrite_70')
_SafetyController_0_buffered_status_70 = Int('_SafetyController_0_buffered_status_70')
_SafetyController_0_has_data_70 = Int('_SafetyController_0_has_data_70')

sensor_current_bpm_71 = Int('sensor_current_bpm_71')
sensor_OUT_value_71 = Int('sensor_OUT_value_71')
sensor_OUT_reqRead_71 = Bool('sensor_OUT_reqRead_71')
sensor_OUT_reqWrite_71 = Bool('sensor_OUT_reqWrite_71')
monitor_IN_value_71 = Int('monitor_IN_value_71')
monitor_IN_reqRead_71 = Bool('monitor_IN_reqRead_71')
monitor_IN_reqWrite_71 = Bool('monitor_IN_reqWrite_71')
_SafetyController_0_buffered_status_71 = Int('_SafetyController_0_buffered_status_71')
_SafetyController_0_has_data_71 = Int('_SafetyController_0_has_data_71')

sensor_current_bpm_72 = Int('sensor_current_bpm_72')
sensor_OUT_value_72 = Int('sensor_OUT_value_72')
sensor_OUT_reqRead_72 = Bool('sensor_OUT_reqRead_72')
sensor_OUT_reqWrite_72 = Bool('sensor_OUT_reqWrite_72')
monitor_IN_value_72 = Int('monitor_IN_value_72')
monitor_IN_reqRead_72 = Bool('monitor_IN_reqRead_72')
monitor_IN_reqWrite_72 = Bool('monitor_IN_reqWrite_72')
_SafetyController_0_buffered_status_72 = Int('_SafetyController_0_buffered_status_72')
_SafetyController_0_has_data_72 = Int('_SafetyController_0_has_data_72')

sensor_current_bpm_73 = Int('sensor_current_bpm_73')
sensor_OUT_value_73 = Int('sensor_OUT_value_73')
sensor_OUT_reqRead_73 = Bool('sensor_OUT_reqRead_73')
sensor_OUT_reqWrite_73 = Bool('sensor_OUT_reqWrite_73')
monitor_IN_value_73 = Int('monitor_IN_value_73')
monitor_IN_reqRead_73 = Bool('monitor_IN_reqRead_73')
monitor_IN_reqWrite_73 = Bool('monitor_IN_reqWrite_73')
_SafetyController_0_buffered_status_73 = Int('_SafetyController_0_buffered_status_73')
_SafetyController_0_has_data_73 = Int('_SafetyController_0_has_data_73')

sensor_current_bpm_74 = Int('sensor_current_bpm_74')
sensor_OUT_value_74 = Int('sensor_OUT_value_74')
sensor_OUT_reqRead_74 = Bool('sensor_OUT_reqRead_74')
sensor_OUT_reqWrite_74 = Bool('sensor_OUT_reqWrite_74')
monitor_IN_value_74 = Int('monitor_IN_value_74')
monitor_IN_reqRead_74 = Bool('monitor_IN_reqRead_74')
monitor_IN_reqWrite_74 = Bool('monitor_IN_reqWrite_74')
_SafetyController_0_buffered_status_74 = Int('_SafetyController_0_buffered_status_74')
_SafetyController_0_has_data_74 = Int('_SafetyController_0_has_data_74')

sensor_current_bpm_75 = Int('sensor_current_bpm_75')
sensor_OUT_value_75 = Int('sensor_OUT_value_75')
sensor_OUT_reqRead_75 = Bool('sensor_OUT_reqRead_75')
sensor_OUT_reqWrite_75 = Bool('sensor_OUT_reqWrite_75')
monitor_IN_value_75 = Int('monitor_IN_value_75')
monitor_IN_reqRead_75 = Bool('monitor_IN_reqRead_75')
monitor_IN_reqWrite_75 = Bool('monitor_IN_reqWrite_75')
_SafetyController_0_buffered_status_75 = Int('_SafetyController_0_buffered_status_75')
_SafetyController_0_has_data_75 = Int('_SafetyController_0_has_data_75')

sensor_current_bpm_76 = Int('sensor_current_bpm_76')
sensor_OUT_value_76 = Int('sensor_OUT_value_76')
sensor_OUT_reqRead_76 = Bool('sensor_OUT_reqRead_76')
sensor_OUT_reqWrite_76 = Bool('sensor_OUT_reqWrite_76')
monitor_IN_value_76 = Int('monitor_IN_value_76')
monitor_IN_reqRead_76 = Bool('monitor_IN_reqRead_76')
monitor_IN_reqWrite_76 = Bool('monitor_IN_reqWrite_76')
_SafetyController_0_buffered_status_76 = Int('_SafetyController_0_buffered_status_76')
_SafetyController_0_has_data_76 = Int('_SafetyController_0_has_data_76')

sensor_current_bpm_77 = Int('sensor_current_bpm_77')
sensor_OUT_value_77 = Int('sensor_OUT_value_77')
sensor_OUT_reqRead_77 = Bool('sensor_OUT_reqRead_77')
sensor_OUT_reqWrite_77 = Bool('sensor_OUT_reqWrite_77')
monitor_IN_value_77 = Int('monitor_IN_value_77')
monitor_IN_reqRead_77 = Bool('monitor_IN_reqRead_77')
monitor_IN_reqWrite_77 = Bool('monitor_IN_reqWrite_77')
_SafetyController_0_buffered_status_77 = Int('_SafetyController_0_buffered_status_77')
_SafetyController_0_has_data_77 = Int('_SafetyController_0_has_data_77')

sensor_current_bpm_78 = Int('sensor_current_bpm_78')
sensor_OUT_value_78 = Int('sensor_OUT_value_78')
sensor_OUT_reqRead_78 = Bool('sensor_OUT_reqRead_78')
sensor_OUT_reqWrite_78 = Bool('sensor_OUT_reqWrite_78')
monitor_IN_value_78 = Int('monitor_IN_value_78')
monitor_IN_reqRead_78 = Bool('monitor_IN_reqRead_78')
monitor_IN_reqWrite_78 = Bool('monitor_IN_reqWrite_78')
_SafetyController_0_buffered_status_78 = Int('_SafetyController_0_buffered_status_78')
_SafetyController_0_has_data_78 = Int('_SafetyController_0_has_data_78')

sensor_current_bpm_79 = Int('sensor_current_bpm_79')
sensor_OUT_value_79 = Int('sensor_OUT_value_79')
sensor_OUT_reqRead_79 = Bool('sensor_OUT_reqRead_79')
sensor_OUT_reqWrite_79 = Bool('sensor_OUT_reqWrite_79')
monitor_IN_value_79 = Int('monitor_IN_value_79')
monitor_IN_reqRead_79 = Bool('monitor_IN_reqRead_79')
monitor_IN_reqWrite_79 = Bool('monitor_IN_reqWrite_79')
_SafetyController_0_buffered_status_79 = Int('_SafetyController_0_buffered_status_79')
_SafetyController_0_has_data_79 = Int('_SafetyController_0_has_data_79')

sensor_current_bpm_80 = Int('sensor_current_bpm_80')
sensor_OUT_value_80 = Int('sensor_OUT_value_80')
sensor_OUT_reqRead_80 = Bool('sensor_OUT_reqRead_80')
sensor_OUT_reqWrite_80 = Bool('sensor_OUT_reqWrite_80')
monitor_IN_value_80 = Int('monitor_IN_value_80')
monitor_IN_reqRead_80 = Bool('monitor_IN_reqRead_80')
monitor_IN_reqWrite_80 = Bool('monitor_IN_reqWrite_80')
_SafetyController_0_buffered_status_80 = Int('_SafetyController_0_buffered_status_80')
_SafetyController_0_has_data_80 = Int('_SafetyController_0_has_data_80')

sensor_current_bpm_81 = Int('sensor_current_bpm_81')
sensor_OUT_value_81 = Int('sensor_OUT_value_81')
sensor_OUT_reqRead_81 = Bool('sensor_OUT_reqRead_81')
sensor_OUT_reqWrite_81 = Bool('sensor_OUT_reqWrite_81')
monitor_IN_value_81 = Int('monitor_IN_value_81')
monitor_IN_reqRead_81 = Bool('monitor_IN_reqRead_81')
monitor_IN_reqWrite_81 = Bool('monitor_IN_reqWrite_81')
_SafetyController_0_buffered_status_81 = Int('_SafetyController_0_buffered_status_81')
_SafetyController_0_has_data_81 = Int('_SafetyController_0_has_data_81')

sensor_current_bpm_82 = Int('sensor_current_bpm_82')
sensor_OUT_value_82 = Int('sensor_OUT_value_82')
sensor_OUT_reqRead_82 = Bool('sensor_OUT_reqRead_82')
sensor_OUT_reqWrite_82 = Bool('sensor_OUT_reqWrite_82')
monitor_IN_value_82 = Int('monitor_IN_value_82')
monitor_IN_reqRead_82 = Bool('monitor_IN_reqRead_82')
monitor_IN_reqWrite_82 = Bool('monitor_IN_reqWrite_82')
_SafetyController_0_buffered_status_82 = Int('_SafetyController_0_buffered_status_82')
_SafetyController_0_has_data_82 = Int('_SafetyController_0_has_data_82')

sensor_current_bpm_83 = Int('sensor_current_bpm_83')
sensor_OUT_value_83 = Int('sensor_OUT_value_83')
sensor_OUT_reqRead_83 = Bool('sensor_OUT_reqRead_83')
sensor_OUT_reqWrite_83 = Bool('sensor_OUT_reqWrite_83')
monitor_IN_value_83 = Int('monitor_IN_value_83')
monitor_IN_reqRead_83 = Bool('monitor_IN_reqRead_83')
monitor_IN_reqWrite_83 = Bool('monitor_IN_reqWrite_83')
_SafetyController_0_buffered_status_83 = Int('_SafetyController_0_buffered_status_83')
_SafetyController_0_has_data_83 = Int('_SafetyController_0_has_data_83')

sensor_current_bpm_84 = Int('sensor_current_bpm_84')
sensor_OUT_value_84 = Int('sensor_OUT_value_84')
sensor_OUT_reqRead_84 = Bool('sensor_OUT_reqRead_84')
sensor_OUT_reqWrite_84 = Bool('sensor_OUT_reqWrite_84')
monitor_IN_value_84 = Int('monitor_IN_value_84')
monitor_IN_reqRead_84 = Bool('monitor_IN_reqRead_84')
monitor_IN_reqWrite_84 = Bool('monitor_IN_reqWrite_84')
_SafetyController_0_buffered_status_84 = Int('_SafetyController_0_buffered_status_84')
_SafetyController_0_has_data_84 = Int('_SafetyController_0_has_data_84')

sensor_current_bpm_85 = Int('sensor_current_bpm_85')
sensor_OUT_value_85 = Int('sensor_OUT_value_85')
sensor_OUT_reqRead_85 = Bool('sensor_OUT_reqRead_85')
sensor_OUT_reqWrite_85 = Bool('sensor_OUT_reqWrite_85')
monitor_IN_value_85 = Int('monitor_IN_value_85')
monitor_IN_reqRead_85 = Bool('monitor_IN_reqRead_85')
monitor_IN_reqWrite_85 = Bool('monitor_IN_reqWrite_85')
_SafetyController_0_buffered_status_85 = Int('_SafetyController_0_buffered_status_85')
_SafetyController_0_has_data_85 = Int('_SafetyController_0_has_data_85')

sensor_current_bpm_86 = Int('sensor_current_bpm_86')
sensor_OUT_value_86 = Int('sensor_OUT_value_86')
sensor_OUT_reqRead_86 = Bool('sensor_OUT_reqRead_86')
sensor_OUT_reqWrite_86 = Bool('sensor_OUT_reqWrite_86')
monitor_IN_value_86 = Int('monitor_IN_value_86')
monitor_IN_reqRead_86 = Bool('monitor_IN_reqRead_86')
monitor_IN_reqWrite_86 = Bool('monitor_IN_reqWrite_86')
_SafetyController_0_buffered_status_86 = Int('_SafetyController_0_buffered_status_86')
_SafetyController_0_has_data_86 = Int('_SafetyController_0_has_data_86')

sensor_current_bpm_87 = Int('sensor_current_bpm_87')
sensor_OUT_value_87 = Int('sensor_OUT_value_87')
sensor_OUT_reqRead_87 = Bool('sensor_OUT_reqRead_87')
sensor_OUT_reqWrite_87 = Bool('sensor_OUT_reqWrite_87')
monitor_IN_value_87 = Int('monitor_IN_value_87')
monitor_IN_reqRead_87 = Bool('monitor_IN_reqRead_87')
monitor_IN_reqWrite_87 = Bool('monitor_IN_reqWrite_87')
_SafetyController_0_buffered_status_87 = Int('_SafetyController_0_buffered_status_87')
_SafetyController_0_has_data_87 = Int('_SafetyController_0_has_data_87')

sensor_current_bpm_88 = Int('sensor_current_bpm_88')
sensor_OUT_value_88 = Int('sensor_OUT_value_88')
sensor_OUT_reqRead_88 = Bool('sensor_OUT_reqRead_88')
sensor_OUT_reqWrite_88 = Bool('sensor_OUT_reqWrite_88')
monitor_IN_value_88 = Int('monitor_IN_value_88')
monitor_IN_reqRead_88 = Bool('monitor_IN_reqRead_88')
monitor_IN_reqWrite_88 = Bool('monitor_IN_reqWrite_88')
_SafetyController_0_buffered_status_88 = Int('_SafetyController_0_buffered_status_88')
_SafetyController_0_has_data_88 = Int('_SafetyController_0_has_data_88')

sensor_current_bpm_89 = Int('sensor_current_bpm_89')
sensor_OUT_value_89 = Int('sensor_OUT_value_89')
sensor_OUT_reqRead_89 = Bool('sensor_OUT_reqRead_89')
sensor_OUT_reqWrite_89 = Bool('sensor_OUT_reqWrite_89')
monitor_IN_value_89 = Int('monitor_IN_value_89')
monitor_IN_reqRead_89 = Bool('monitor_IN_reqRead_89')
monitor_IN_reqWrite_89 = Bool('monitor_IN_reqWrite_89')
_SafetyController_0_buffered_status_89 = Int('_SafetyController_0_buffered_status_89')
_SafetyController_0_has_data_89 = Int('_SafetyController_0_has_data_89')

sensor_current_bpm_90 = Int('sensor_current_bpm_90')
sensor_OUT_value_90 = Int('sensor_OUT_value_90')
sensor_OUT_reqRead_90 = Bool('sensor_OUT_reqRead_90')
sensor_OUT_reqWrite_90 = Bool('sensor_OUT_reqWrite_90')
monitor_IN_value_90 = Int('monitor_IN_value_90')
monitor_IN_reqRead_90 = Bool('monitor_IN_reqRead_90')
monitor_IN_reqWrite_90 = Bool('monitor_IN_reqWrite_90')
_SafetyController_0_buffered_status_90 = Int('_SafetyController_0_buffered_status_90')
_SafetyController_0_has_data_90 = Int('_SafetyController_0_has_data_90')

sensor_current_bpm_91 = Int('sensor_current_bpm_91')
sensor_OUT_value_91 = Int('sensor_OUT_value_91')
sensor_OUT_reqRead_91 = Bool('sensor_OUT_reqRead_91')
sensor_OUT_reqWrite_91 = Bool('sensor_OUT_reqWrite_91')
monitor_IN_value_91 = Int('monitor_IN_value_91')
monitor_IN_reqRead_91 = Bool('monitor_IN_reqRead_91')
monitor_IN_reqWrite_91 = Bool('monitor_IN_reqWrite_91')
_SafetyController_0_buffered_status_91 = Int('_SafetyController_0_buffered_status_91')
_SafetyController_0_has_data_91 = Int('_SafetyController_0_has_data_91')

sensor_current_bpm_92 = Int('sensor_current_bpm_92')
sensor_OUT_value_92 = Int('sensor_OUT_value_92')
sensor_OUT_reqRead_92 = Bool('sensor_OUT_reqRead_92')
sensor_OUT_reqWrite_92 = Bool('sensor_OUT_reqWrite_92')
monitor_IN_value_92 = Int('monitor_IN_value_92')
monitor_IN_reqRead_92 = Bool('monitor_IN_reqRead_92')
monitor_IN_reqWrite_92 = Bool('monitor_IN_reqWrite_92')
_SafetyController_0_buffered_status_92 = Int('_SafetyController_0_buffered_status_92')
_SafetyController_0_has_data_92 = Int('_SafetyController_0_has_data_92')

sensor_current_bpm_93 = Int('sensor_current_bpm_93')
sensor_OUT_value_93 = Int('sensor_OUT_value_93')
sensor_OUT_reqRead_93 = Bool('sensor_OUT_reqRead_93')
sensor_OUT_reqWrite_93 = Bool('sensor_OUT_reqWrite_93')
monitor_IN_value_93 = Int('monitor_IN_value_93')
monitor_IN_reqRead_93 = Bool('monitor_IN_reqRead_93')
monitor_IN_reqWrite_93 = Bool('monitor_IN_reqWrite_93')
_SafetyController_0_buffered_status_93 = Int('_SafetyController_0_buffered_status_93')
_SafetyController_0_has_data_93 = Int('_SafetyController_0_has_data_93')

sensor_current_bpm_94 = Int('sensor_current_bpm_94')
sensor_OUT_value_94 = Int('sensor_OUT_value_94')
sensor_OUT_reqRead_94 = Bool('sensor_OUT_reqRead_94')
sensor_OUT_reqWrite_94 = Bool('sensor_OUT_reqWrite_94')
monitor_IN_value_94 = Int('monitor_IN_value_94')
monitor_IN_reqRead_94 = Bool('monitor_IN_reqRead_94')
monitor_IN_reqWrite_94 = Bool('monitor_IN_reqWrite_94')
_SafetyController_0_buffered_status_94 = Int('_SafetyController_0_buffered_status_94')
_SafetyController_0_has_data_94 = Int('_SafetyController_0_has_data_94')

sensor_current_bpm_95 = Int('sensor_current_bpm_95')
sensor_OUT_value_95 = Int('sensor_OUT_value_95')
sensor_OUT_reqRead_95 = Bool('sensor_OUT_reqRead_95')
sensor_OUT_reqWrite_95 = Bool('sensor_OUT_reqWrite_95')
monitor_IN_value_95 = Int('monitor_IN_value_95')
monitor_IN_reqRead_95 = Bool('monitor_IN_reqRead_95')
monitor_IN_reqWrite_95 = Bool('monitor_IN_reqWrite_95')
_SafetyController_0_buffered_status_95 = Int('_SafetyController_0_buffered_status_95')
_SafetyController_0_has_data_95 = Int('_SafetyController_0_has_data_95')

sensor_current_bpm_96 = Int('sensor_current_bpm_96')
sensor_OUT_value_96 = Int('sensor_OUT_value_96')
sensor_OUT_reqRead_96 = Bool('sensor_OUT_reqRead_96')
sensor_OUT_reqWrite_96 = Bool('sensor_OUT_reqWrite_96')
monitor_IN_value_96 = Int('monitor_IN_value_96')
monitor_IN_reqRead_96 = Bool('monitor_IN_reqRead_96')
monitor_IN_reqWrite_96 = Bool('monitor_IN_reqWrite_96')
_SafetyController_0_buffered_status_96 = Int('_SafetyController_0_buffered_status_96')
_SafetyController_0_has_data_96 = Int('_SafetyController_0_has_data_96')

sensor_current_bpm_97 = Int('sensor_current_bpm_97')
sensor_OUT_value_97 = Int('sensor_OUT_value_97')
sensor_OUT_reqRead_97 = Bool('sensor_OUT_reqRead_97')
sensor_OUT_reqWrite_97 = Bool('sensor_OUT_reqWrite_97')
monitor_IN_value_97 = Int('monitor_IN_value_97')
monitor_IN_reqRead_97 = Bool('monitor_IN_reqRead_97')
monitor_IN_reqWrite_97 = Bool('monitor_IN_reqWrite_97')
_SafetyController_0_buffered_status_97 = Int('_SafetyController_0_buffered_status_97')
_SafetyController_0_has_data_97 = Int('_SafetyController_0_has_data_97')

sensor_current_bpm_98 = Int('sensor_current_bpm_98')
sensor_OUT_value_98 = Int('sensor_OUT_value_98')
sensor_OUT_reqRead_98 = Bool('sensor_OUT_reqRead_98')
sensor_OUT_reqWrite_98 = Bool('sensor_OUT_reqWrite_98')
monitor_IN_value_98 = Int('monitor_IN_value_98')
monitor_IN_reqRead_98 = Bool('monitor_IN_reqRead_98')
monitor_IN_reqWrite_98 = Bool('monitor_IN_reqWrite_98')
_SafetyController_0_buffered_status_98 = Int('_SafetyController_0_buffered_status_98')
_SafetyController_0_has_data_98 = Int('_SafetyController_0_has_data_98')

sensor_current_bpm_99 = Int('sensor_current_bpm_99')
sensor_OUT_value_99 = Int('sensor_OUT_value_99')
sensor_OUT_reqRead_99 = Bool('sensor_OUT_reqRead_99')
sensor_OUT_reqWrite_99 = Bool('sensor_OUT_reqWrite_99')
monitor_IN_value_99 = Int('monitor_IN_value_99')
monitor_IN_reqRead_99 = Bool('monitor_IN_reqRead_99')
monitor_IN_reqWrite_99 = Bool('monitor_IN_reqWrite_99')
_SafetyController_0_buffered_status_99 = Int('_SafetyController_0_buffered_status_99')
_SafetyController_0_has_data_99 = Int('_SafetyController_0_has_data_99')

sensor_current_bpm_100 = Int('sensor_current_bpm_100')
sensor_OUT_value_100 = Int('sensor_OUT_value_100')
sensor_OUT_reqRead_100 = Bool('sensor_OUT_reqRead_100')
sensor_OUT_reqWrite_100 = Bool('sensor_OUT_reqWrite_100')
monitor_IN_value_100 = Int('monitor_IN_value_100')
monitor_IN_reqRead_100 = Bool('monitor_IN_reqRead_100')
monitor_IN_reqWrite_100 = Bool('monitor_IN_reqWrite_100')
_SafetyController_0_buffered_status_100 = Int('_SafetyController_0_buffered_status_100')
_SafetyController_0_has_data_100 = Int('_SafetyController_0_has_data_100')

s = Solver()
s.add(sensor_current_bpm_0 == 60)
s.add(sensor_OUT_value_0 == 0)
s.add(sensor_OUT_reqRead_0 == False)
s.add(sensor_OUT_reqWrite_0 == False)
s.add(monitor_IN_value_0 == 0)
s.add(monitor_IN_reqRead_0 == False)
s.add(monitor_IN_reqWrite_0 == False)
s.add(_SafetyController_0_buffered_status_0 == 0)
s.add(_SafetyController_0_has_data_0 == 0)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_0) == (sensor_OUT_reqWrite_0))), sensor_OUT_reqWrite_1 == (sensor_OUT_reqRead_0), sensor_current_bpm_1 == sensor_current_bpm_0, sensor_OUT_value_1 == sensor_OUT_value_0, sensor_OUT_reqRead_1 == sensor_OUT_reqRead_0, monitor_IN_value_1 == monitor_IN_value_0, monitor_IN_reqRead_1 == monitor_IN_reqRead_0, monitor_IN_reqWrite_1 == monitor_IN_reqWrite_0, _SafetyController_0_buffered_status_1 == _SafetyController_0_buffered_status_0, _SafetyController_0_has_data_1 == _SafetyController_0_has_data_0), 
    And(And(Not(False), (monitor_IN_reqRead_0) == (False)), monitor_IN_reqRead_1 == (True), sensor_current_bpm_1 == sensor_current_bpm_0, sensor_OUT_value_1 == sensor_OUT_value_0, sensor_OUT_reqRead_1 == sensor_OUT_reqRead_0, sensor_OUT_reqWrite_1 == sensor_OUT_reqWrite_0, monitor_IN_value_1 == monitor_IN_value_0, monitor_IN_reqWrite_1 == monitor_IN_reqWrite_0, _SafetyController_0_buffered_status_1 == _SafetyController_0_buffered_status_0, _SafetyController_0_has_data_1 == _SafetyController_0_has_data_0), 
    And(And(Not(False), Not((sensor_OUT_reqRead_0) == ((_SafetyController_0_has_data_0) == (0)))), sensor_OUT_reqRead_1 == ((_SafetyController_0_has_data_0) == (0)), sensor_current_bpm_1 == sensor_current_bpm_0, sensor_OUT_value_1 == sensor_OUT_value_0, sensor_OUT_reqWrite_1 == sensor_OUT_reqWrite_0, monitor_IN_value_1 == monitor_IN_value_0, monitor_IN_reqRead_1 == monitor_IN_reqRead_0, monitor_IN_reqWrite_1 == monitor_IN_reqWrite_0, _SafetyController_0_buffered_status_1 == _SafetyController_0_buffered_status_0, _SafetyController_0_has_data_1 == _SafetyController_0_has_data_0), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_0) == ((_SafetyController_0_has_data_0) == (0))))), Not((monitor_IN_reqWrite_0) == (And(monitor_IN_reqRead_0, (_SafetyController_0_has_data_0) == (1))))), monitor_IN_reqWrite_1 == (And(monitor_IN_reqRead_0, (_SafetyController_0_has_data_0) == (1))), sensor_current_bpm_1 == sensor_current_bpm_0, sensor_OUT_value_1 == sensor_OUT_value_0, sensor_OUT_reqRead_1 == sensor_OUT_reqRead_0, sensor_OUT_reqWrite_1 == sensor_OUT_reqWrite_0, monitor_IN_value_1 == monitor_IN_value_0, monitor_IN_reqRead_1 == monitor_IN_reqRead_0, _SafetyController_0_buffered_status_1 == _SafetyController_0_buffered_status_0, _SafetyController_0_has_data_1 == _SafetyController_0_has_data_0), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_0) == (sensor_OUT_reqWrite_0)))), sensor_OUT_reqWrite_0), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_0) == ((_SafetyController_0_has_data_0) == (0)))), Not((monitor_IN_reqWrite_0) == (And(monitor_IN_reqRead_0, (_SafetyController_0_has_data_0) == (1)))))), sensor_OUT_reqRead_0)), _SafetyController_0_buffered_status_1 == (If((sensor_current_bpm_0 > 100), 1, 0)), sensor_current_bpm_1 == (predict_next(sensor_current_bpm_0)), sensor_OUT_reqWrite_1 == (False), _SafetyController_0_has_data_1 == (1), sensor_OUT_reqRead_1 == (False), sensor_OUT_value_1 == (sensor_current_bpm_0), monitor_IN_value_1 == monitor_IN_value_0, monitor_IN_reqRead_1 == monitor_IN_reqRead_0, monitor_IN_reqWrite_1 == monitor_IN_reqWrite_0), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_0) == (False))), monitor_IN_reqWrite_0), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_0) == ((_SafetyController_0_has_data_0) == (0)))), Not((monitor_IN_reqWrite_0) == (And(monitor_IN_reqRead_0, (_SafetyController_0_has_data_0) == (1))))), sensor_OUT_reqRead_0)), monitor_IN_reqWrite_0)), monitor_IN_reqWrite_1 == (False), monitor_IN_value_1 == (_SafetyController_0_buffered_status_0), _SafetyController_0_has_data_1 == (0), monitor_IN_reqRead_1 == (False), sensor_current_bpm_1 == sensor_current_bpm_0, sensor_OUT_value_1 == sensor_OUT_value_0, sensor_OUT_reqRead_1 == sensor_OUT_reqRead_0, sensor_OUT_reqWrite_1 == sensor_OUT_reqWrite_0, _SafetyController_0_buffered_status_1 == _SafetyController_0_buffered_status_0)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_1) == (sensor_OUT_reqWrite_1))), sensor_OUT_reqWrite_2 == (sensor_OUT_reqRead_1), sensor_current_bpm_2 == sensor_current_bpm_1, sensor_OUT_value_2 == sensor_OUT_value_1, sensor_OUT_reqRead_2 == sensor_OUT_reqRead_1, monitor_IN_value_2 == monitor_IN_value_1, monitor_IN_reqRead_2 == monitor_IN_reqRead_1, monitor_IN_reqWrite_2 == monitor_IN_reqWrite_1, _SafetyController_0_buffered_status_2 == _SafetyController_0_buffered_status_1, _SafetyController_0_has_data_2 == _SafetyController_0_has_data_1), 
    And(And(Not(False), (monitor_IN_reqRead_1) == (False)), monitor_IN_reqRead_2 == (True), sensor_current_bpm_2 == sensor_current_bpm_1, sensor_OUT_value_2 == sensor_OUT_value_1, sensor_OUT_reqRead_2 == sensor_OUT_reqRead_1, sensor_OUT_reqWrite_2 == sensor_OUT_reqWrite_1, monitor_IN_value_2 == monitor_IN_value_1, monitor_IN_reqWrite_2 == monitor_IN_reqWrite_1, _SafetyController_0_buffered_status_2 == _SafetyController_0_buffered_status_1, _SafetyController_0_has_data_2 == _SafetyController_0_has_data_1), 
    And(And(Not(False), Not((sensor_OUT_reqRead_1) == ((_SafetyController_0_has_data_1) == (0)))), sensor_OUT_reqRead_2 == ((_SafetyController_0_has_data_1) == (0)), sensor_current_bpm_2 == sensor_current_bpm_1, sensor_OUT_value_2 == sensor_OUT_value_1, sensor_OUT_reqWrite_2 == sensor_OUT_reqWrite_1, monitor_IN_value_2 == monitor_IN_value_1, monitor_IN_reqRead_2 == monitor_IN_reqRead_1, monitor_IN_reqWrite_2 == monitor_IN_reqWrite_1, _SafetyController_0_buffered_status_2 == _SafetyController_0_buffered_status_1, _SafetyController_0_has_data_2 == _SafetyController_0_has_data_1), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_1) == ((_SafetyController_0_has_data_1) == (0))))), Not((monitor_IN_reqWrite_1) == (And(monitor_IN_reqRead_1, (_SafetyController_0_has_data_1) == (1))))), monitor_IN_reqWrite_2 == (And(monitor_IN_reqRead_1, (_SafetyController_0_has_data_1) == (1))), sensor_current_bpm_2 == sensor_current_bpm_1, sensor_OUT_value_2 == sensor_OUT_value_1, sensor_OUT_reqRead_2 == sensor_OUT_reqRead_1, sensor_OUT_reqWrite_2 == sensor_OUT_reqWrite_1, monitor_IN_value_2 == monitor_IN_value_1, monitor_IN_reqRead_2 == monitor_IN_reqRead_1, _SafetyController_0_buffered_status_2 == _SafetyController_0_buffered_status_1, _SafetyController_0_has_data_2 == _SafetyController_0_has_data_1), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_1) == (sensor_OUT_reqWrite_1)))), sensor_OUT_reqWrite_1), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_1) == ((_SafetyController_0_has_data_1) == (0)))), Not((monitor_IN_reqWrite_1) == (And(monitor_IN_reqRead_1, (_SafetyController_0_has_data_1) == (1)))))), sensor_OUT_reqRead_1)), _SafetyController_0_buffered_status_2 == (If((sensor_current_bpm_1 > 100), 1, 0)), sensor_current_bpm_2 == (predict_next(sensor_current_bpm_1)), sensor_OUT_reqWrite_2 == (False), _SafetyController_0_has_data_2 == (1), sensor_OUT_reqRead_2 == (False), sensor_OUT_value_2 == (sensor_current_bpm_1), monitor_IN_value_2 == monitor_IN_value_1, monitor_IN_reqRead_2 == monitor_IN_reqRead_1, monitor_IN_reqWrite_2 == monitor_IN_reqWrite_1), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_1) == (False))), monitor_IN_reqWrite_1), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_1) == ((_SafetyController_0_has_data_1) == (0)))), Not((monitor_IN_reqWrite_1) == (And(monitor_IN_reqRead_1, (_SafetyController_0_has_data_1) == (1))))), sensor_OUT_reqRead_1)), monitor_IN_reqWrite_1)), monitor_IN_reqWrite_2 == (False), monitor_IN_value_2 == (_SafetyController_0_buffered_status_1), _SafetyController_0_has_data_2 == (0), monitor_IN_reqRead_2 == (False), sensor_current_bpm_2 == sensor_current_bpm_1, sensor_OUT_value_2 == sensor_OUT_value_1, sensor_OUT_reqRead_2 == sensor_OUT_reqRead_1, sensor_OUT_reqWrite_2 == sensor_OUT_reqWrite_1, _SafetyController_0_buffered_status_2 == _SafetyController_0_buffered_status_1)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_2) == (sensor_OUT_reqWrite_2))), sensor_OUT_reqWrite_3 == (sensor_OUT_reqRead_2), sensor_current_bpm_3 == sensor_current_bpm_2, sensor_OUT_value_3 == sensor_OUT_value_2, sensor_OUT_reqRead_3 == sensor_OUT_reqRead_2, monitor_IN_value_3 == monitor_IN_value_2, monitor_IN_reqRead_3 == monitor_IN_reqRead_2, monitor_IN_reqWrite_3 == monitor_IN_reqWrite_2, _SafetyController_0_buffered_status_3 == _SafetyController_0_buffered_status_2, _SafetyController_0_has_data_3 == _SafetyController_0_has_data_2), 
    And(And(Not(False), (monitor_IN_reqRead_2) == (False)), monitor_IN_reqRead_3 == (True), sensor_current_bpm_3 == sensor_current_bpm_2, sensor_OUT_value_3 == sensor_OUT_value_2, sensor_OUT_reqRead_3 == sensor_OUT_reqRead_2, sensor_OUT_reqWrite_3 == sensor_OUT_reqWrite_2, monitor_IN_value_3 == monitor_IN_value_2, monitor_IN_reqWrite_3 == monitor_IN_reqWrite_2, _SafetyController_0_buffered_status_3 == _SafetyController_0_buffered_status_2, _SafetyController_0_has_data_3 == _SafetyController_0_has_data_2), 
    And(And(Not(False), Not((sensor_OUT_reqRead_2) == ((_SafetyController_0_has_data_2) == (0)))), sensor_OUT_reqRead_3 == ((_SafetyController_0_has_data_2) == (0)), sensor_current_bpm_3 == sensor_current_bpm_2, sensor_OUT_value_3 == sensor_OUT_value_2, sensor_OUT_reqWrite_3 == sensor_OUT_reqWrite_2, monitor_IN_value_3 == monitor_IN_value_2, monitor_IN_reqRead_3 == monitor_IN_reqRead_2, monitor_IN_reqWrite_3 == monitor_IN_reqWrite_2, _SafetyController_0_buffered_status_3 == _SafetyController_0_buffered_status_2, _SafetyController_0_has_data_3 == _SafetyController_0_has_data_2), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_2) == ((_SafetyController_0_has_data_2) == (0))))), Not((monitor_IN_reqWrite_2) == (And(monitor_IN_reqRead_2, (_SafetyController_0_has_data_2) == (1))))), monitor_IN_reqWrite_3 == (And(monitor_IN_reqRead_2, (_SafetyController_0_has_data_2) == (1))), sensor_current_bpm_3 == sensor_current_bpm_2, sensor_OUT_value_3 == sensor_OUT_value_2, sensor_OUT_reqRead_3 == sensor_OUT_reqRead_2, sensor_OUT_reqWrite_3 == sensor_OUT_reqWrite_2, monitor_IN_value_3 == monitor_IN_value_2, monitor_IN_reqRead_3 == monitor_IN_reqRead_2, _SafetyController_0_buffered_status_3 == _SafetyController_0_buffered_status_2, _SafetyController_0_has_data_3 == _SafetyController_0_has_data_2), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_2) == (sensor_OUT_reqWrite_2)))), sensor_OUT_reqWrite_2), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_2) == ((_SafetyController_0_has_data_2) == (0)))), Not((monitor_IN_reqWrite_2) == (And(monitor_IN_reqRead_2, (_SafetyController_0_has_data_2) == (1)))))), sensor_OUT_reqRead_2)), _SafetyController_0_buffered_status_3 == (If((sensor_current_bpm_2 > 100), 1, 0)), sensor_current_bpm_3 == (predict_next(sensor_current_bpm_2)), sensor_OUT_reqWrite_3 == (False), _SafetyController_0_has_data_3 == (1), sensor_OUT_reqRead_3 == (False), sensor_OUT_value_3 == (sensor_current_bpm_2), monitor_IN_value_3 == monitor_IN_value_2, monitor_IN_reqRead_3 == monitor_IN_reqRead_2, monitor_IN_reqWrite_3 == monitor_IN_reqWrite_2), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_2) == (False))), monitor_IN_reqWrite_2), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_2) == ((_SafetyController_0_has_data_2) == (0)))), Not((monitor_IN_reqWrite_2) == (And(monitor_IN_reqRead_2, (_SafetyController_0_has_data_2) == (1))))), sensor_OUT_reqRead_2)), monitor_IN_reqWrite_2)), monitor_IN_reqWrite_3 == (False), monitor_IN_value_3 == (_SafetyController_0_buffered_status_2), _SafetyController_0_has_data_3 == (0), monitor_IN_reqRead_3 == (False), sensor_current_bpm_3 == sensor_current_bpm_2, sensor_OUT_value_3 == sensor_OUT_value_2, sensor_OUT_reqRead_3 == sensor_OUT_reqRead_2, sensor_OUT_reqWrite_3 == sensor_OUT_reqWrite_2, _SafetyController_0_buffered_status_3 == _SafetyController_0_buffered_status_2)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_3) == (sensor_OUT_reqWrite_3))), sensor_OUT_reqWrite_4 == (sensor_OUT_reqRead_3), sensor_current_bpm_4 == sensor_current_bpm_3, sensor_OUT_value_4 == sensor_OUT_value_3, sensor_OUT_reqRead_4 == sensor_OUT_reqRead_3, monitor_IN_value_4 == monitor_IN_value_3, monitor_IN_reqRead_4 == monitor_IN_reqRead_3, monitor_IN_reqWrite_4 == monitor_IN_reqWrite_3, _SafetyController_0_buffered_status_4 == _SafetyController_0_buffered_status_3, _SafetyController_0_has_data_4 == _SafetyController_0_has_data_3), 
    And(And(Not(False), (monitor_IN_reqRead_3) == (False)), monitor_IN_reqRead_4 == (True), sensor_current_bpm_4 == sensor_current_bpm_3, sensor_OUT_value_4 == sensor_OUT_value_3, sensor_OUT_reqRead_4 == sensor_OUT_reqRead_3, sensor_OUT_reqWrite_4 == sensor_OUT_reqWrite_3, monitor_IN_value_4 == monitor_IN_value_3, monitor_IN_reqWrite_4 == monitor_IN_reqWrite_3, _SafetyController_0_buffered_status_4 == _SafetyController_0_buffered_status_3, _SafetyController_0_has_data_4 == _SafetyController_0_has_data_3), 
    And(And(Not(False), Not((sensor_OUT_reqRead_3) == ((_SafetyController_0_has_data_3) == (0)))), sensor_OUT_reqRead_4 == ((_SafetyController_0_has_data_3) == (0)), sensor_current_bpm_4 == sensor_current_bpm_3, sensor_OUT_value_4 == sensor_OUT_value_3, sensor_OUT_reqWrite_4 == sensor_OUT_reqWrite_3, monitor_IN_value_4 == monitor_IN_value_3, monitor_IN_reqRead_4 == monitor_IN_reqRead_3, monitor_IN_reqWrite_4 == monitor_IN_reqWrite_3, _SafetyController_0_buffered_status_4 == _SafetyController_0_buffered_status_3, _SafetyController_0_has_data_4 == _SafetyController_0_has_data_3), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_3) == ((_SafetyController_0_has_data_3) == (0))))), Not((monitor_IN_reqWrite_3) == (And(monitor_IN_reqRead_3, (_SafetyController_0_has_data_3) == (1))))), monitor_IN_reqWrite_4 == (And(monitor_IN_reqRead_3, (_SafetyController_0_has_data_3) == (1))), sensor_current_bpm_4 == sensor_current_bpm_3, sensor_OUT_value_4 == sensor_OUT_value_3, sensor_OUT_reqRead_4 == sensor_OUT_reqRead_3, sensor_OUT_reqWrite_4 == sensor_OUT_reqWrite_3, monitor_IN_value_4 == monitor_IN_value_3, monitor_IN_reqRead_4 == monitor_IN_reqRead_3, _SafetyController_0_buffered_status_4 == _SafetyController_0_buffered_status_3, _SafetyController_0_has_data_4 == _SafetyController_0_has_data_3), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_3) == (sensor_OUT_reqWrite_3)))), sensor_OUT_reqWrite_3), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_3) == ((_SafetyController_0_has_data_3) == (0)))), Not((monitor_IN_reqWrite_3) == (And(monitor_IN_reqRead_3, (_SafetyController_0_has_data_3) == (1)))))), sensor_OUT_reqRead_3)), _SafetyController_0_buffered_status_4 == (If((sensor_current_bpm_3 > 100), 1, 0)), sensor_current_bpm_4 == (predict_next(sensor_current_bpm_3)), sensor_OUT_reqWrite_4 == (False), _SafetyController_0_has_data_4 == (1), sensor_OUT_reqRead_4 == (False), sensor_OUT_value_4 == (sensor_current_bpm_3), monitor_IN_value_4 == monitor_IN_value_3, monitor_IN_reqRead_4 == monitor_IN_reqRead_3, monitor_IN_reqWrite_4 == monitor_IN_reqWrite_3), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_3) == (False))), monitor_IN_reqWrite_3), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_3) == ((_SafetyController_0_has_data_3) == (0)))), Not((monitor_IN_reqWrite_3) == (And(monitor_IN_reqRead_3, (_SafetyController_0_has_data_3) == (1))))), sensor_OUT_reqRead_3)), monitor_IN_reqWrite_3)), monitor_IN_reqWrite_4 == (False), monitor_IN_value_4 == (_SafetyController_0_buffered_status_3), _SafetyController_0_has_data_4 == (0), monitor_IN_reqRead_4 == (False), sensor_current_bpm_4 == sensor_current_bpm_3, sensor_OUT_value_4 == sensor_OUT_value_3, sensor_OUT_reqRead_4 == sensor_OUT_reqRead_3, sensor_OUT_reqWrite_4 == sensor_OUT_reqWrite_3, _SafetyController_0_buffered_status_4 == _SafetyController_0_buffered_status_3)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_4) == (sensor_OUT_reqWrite_4))), sensor_OUT_reqWrite_5 == (sensor_OUT_reqRead_4), sensor_current_bpm_5 == sensor_current_bpm_4, sensor_OUT_value_5 == sensor_OUT_value_4, sensor_OUT_reqRead_5 == sensor_OUT_reqRead_4, monitor_IN_value_5 == monitor_IN_value_4, monitor_IN_reqRead_5 == monitor_IN_reqRead_4, monitor_IN_reqWrite_5 == monitor_IN_reqWrite_4, _SafetyController_0_buffered_status_5 == _SafetyController_0_buffered_status_4, _SafetyController_0_has_data_5 == _SafetyController_0_has_data_4), 
    And(And(Not(False), (monitor_IN_reqRead_4) == (False)), monitor_IN_reqRead_5 == (True), sensor_current_bpm_5 == sensor_current_bpm_4, sensor_OUT_value_5 == sensor_OUT_value_4, sensor_OUT_reqRead_5 == sensor_OUT_reqRead_4, sensor_OUT_reqWrite_5 == sensor_OUT_reqWrite_4, monitor_IN_value_5 == monitor_IN_value_4, monitor_IN_reqWrite_5 == monitor_IN_reqWrite_4, _SafetyController_0_buffered_status_5 == _SafetyController_0_buffered_status_4, _SafetyController_0_has_data_5 == _SafetyController_0_has_data_4), 
    And(And(Not(False), Not((sensor_OUT_reqRead_4) == ((_SafetyController_0_has_data_4) == (0)))), sensor_OUT_reqRead_5 == ((_SafetyController_0_has_data_4) == (0)), sensor_current_bpm_5 == sensor_current_bpm_4, sensor_OUT_value_5 == sensor_OUT_value_4, sensor_OUT_reqWrite_5 == sensor_OUT_reqWrite_4, monitor_IN_value_5 == monitor_IN_value_4, monitor_IN_reqRead_5 == monitor_IN_reqRead_4, monitor_IN_reqWrite_5 == monitor_IN_reqWrite_4, _SafetyController_0_buffered_status_5 == _SafetyController_0_buffered_status_4, _SafetyController_0_has_data_5 == _SafetyController_0_has_data_4), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_4) == ((_SafetyController_0_has_data_4) == (0))))), Not((monitor_IN_reqWrite_4) == (And(monitor_IN_reqRead_4, (_SafetyController_0_has_data_4) == (1))))), monitor_IN_reqWrite_5 == (And(monitor_IN_reqRead_4, (_SafetyController_0_has_data_4) == (1))), sensor_current_bpm_5 == sensor_current_bpm_4, sensor_OUT_value_5 == sensor_OUT_value_4, sensor_OUT_reqRead_5 == sensor_OUT_reqRead_4, sensor_OUT_reqWrite_5 == sensor_OUT_reqWrite_4, monitor_IN_value_5 == monitor_IN_value_4, monitor_IN_reqRead_5 == monitor_IN_reqRead_4, _SafetyController_0_buffered_status_5 == _SafetyController_0_buffered_status_4, _SafetyController_0_has_data_5 == _SafetyController_0_has_data_4), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_4) == (sensor_OUT_reqWrite_4)))), sensor_OUT_reqWrite_4), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_4) == ((_SafetyController_0_has_data_4) == (0)))), Not((monitor_IN_reqWrite_4) == (And(monitor_IN_reqRead_4, (_SafetyController_0_has_data_4) == (1)))))), sensor_OUT_reqRead_4)), _SafetyController_0_buffered_status_5 == (If((sensor_current_bpm_4 > 100), 1, 0)), sensor_current_bpm_5 == (predict_next(sensor_current_bpm_4)), sensor_OUT_reqWrite_5 == (False), _SafetyController_0_has_data_5 == (1), sensor_OUT_reqRead_5 == (False), sensor_OUT_value_5 == (sensor_current_bpm_4), monitor_IN_value_5 == monitor_IN_value_4, monitor_IN_reqRead_5 == monitor_IN_reqRead_4, monitor_IN_reqWrite_5 == monitor_IN_reqWrite_4), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_4) == (False))), monitor_IN_reqWrite_4), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_4) == ((_SafetyController_0_has_data_4) == (0)))), Not((monitor_IN_reqWrite_4) == (And(monitor_IN_reqRead_4, (_SafetyController_0_has_data_4) == (1))))), sensor_OUT_reqRead_4)), monitor_IN_reqWrite_4)), monitor_IN_reqWrite_5 == (False), monitor_IN_value_5 == (_SafetyController_0_buffered_status_4), _SafetyController_0_has_data_5 == (0), monitor_IN_reqRead_5 == (False), sensor_current_bpm_5 == sensor_current_bpm_4, sensor_OUT_value_5 == sensor_OUT_value_4, sensor_OUT_reqRead_5 == sensor_OUT_reqRead_4, sensor_OUT_reqWrite_5 == sensor_OUT_reqWrite_4, _SafetyController_0_buffered_status_5 == _SafetyController_0_buffered_status_4)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_5) == (sensor_OUT_reqWrite_5))), sensor_OUT_reqWrite_6 == (sensor_OUT_reqRead_5), sensor_current_bpm_6 == sensor_current_bpm_5, sensor_OUT_value_6 == sensor_OUT_value_5, sensor_OUT_reqRead_6 == sensor_OUT_reqRead_5, monitor_IN_value_6 == monitor_IN_value_5, monitor_IN_reqRead_6 == monitor_IN_reqRead_5, monitor_IN_reqWrite_6 == monitor_IN_reqWrite_5, _SafetyController_0_buffered_status_6 == _SafetyController_0_buffered_status_5, _SafetyController_0_has_data_6 == _SafetyController_0_has_data_5), 
    And(And(Not(False), (monitor_IN_reqRead_5) == (False)), monitor_IN_reqRead_6 == (True), sensor_current_bpm_6 == sensor_current_bpm_5, sensor_OUT_value_6 == sensor_OUT_value_5, sensor_OUT_reqRead_6 == sensor_OUT_reqRead_5, sensor_OUT_reqWrite_6 == sensor_OUT_reqWrite_5, monitor_IN_value_6 == monitor_IN_value_5, monitor_IN_reqWrite_6 == monitor_IN_reqWrite_5, _SafetyController_0_buffered_status_6 == _SafetyController_0_buffered_status_5, _SafetyController_0_has_data_6 == _SafetyController_0_has_data_5), 
    And(And(Not(False), Not((sensor_OUT_reqRead_5) == ((_SafetyController_0_has_data_5) == (0)))), sensor_OUT_reqRead_6 == ((_SafetyController_0_has_data_5) == (0)), sensor_current_bpm_6 == sensor_current_bpm_5, sensor_OUT_value_6 == sensor_OUT_value_5, sensor_OUT_reqWrite_6 == sensor_OUT_reqWrite_5, monitor_IN_value_6 == monitor_IN_value_5, monitor_IN_reqRead_6 == monitor_IN_reqRead_5, monitor_IN_reqWrite_6 == monitor_IN_reqWrite_5, _SafetyController_0_buffered_status_6 == _SafetyController_0_buffered_status_5, _SafetyController_0_has_data_6 == _SafetyController_0_has_data_5), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_5) == ((_SafetyController_0_has_data_5) == (0))))), Not((monitor_IN_reqWrite_5) == (And(monitor_IN_reqRead_5, (_SafetyController_0_has_data_5) == (1))))), monitor_IN_reqWrite_6 == (And(monitor_IN_reqRead_5, (_SafetyController_0_has_data_5) == (1))), sensor_current_bpm_6 == sensor_current_bpm_5, sensor_OUT_value_6 == sensor_OUT_value_5, sensor_OUT_reqRead_6 == sensor_OUT_reqRead_5, sensor_OUT_reqWrite_6 == sensor_OUT_reqWrite_5, monitor_IN_value_6 == monitor_IN_value_5, monitor_IN_reqRead_6 == monitor_IN_reqRead_5, _SafetyController_0_buffered_status_6 == _SafetyController_0_buffered_status_5, _SafetyController_0_has_data_6 == _SafetyController_0_has_data_5), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_5) == (sensor_OUT_reqWrite_5)))), sensor_OUT_reqWrite_5), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_5) == ((_SafetyController_0_has_data_5) == (0)))), Not((monitor_IN_reqWrite_5) == (And(monitor_IN_reqRead_5, (_SafetyController_0_has_data_5) == (1)))))), sensor_OUT_reqRead_5)), _SafetyController_0_buffered_status_6 == (If((sensor_current_bpm_5 > 100), 1, 0)), sensor_current_bpm_6 == (predict_next(sensor_current_bpm_5)), sensor_OUT_reqWrite_6 == (False), _SafetyController_0_has_data_6 == (1), sensor_OUT_reqRead_6 == (False), sensor_OUT_value_6 == (sensor_current_bpm_5), monitor_IN_value_6 == monitor_IN_value_5, monitor_IN_reqRead_6 == monitor_IN_reqRead_5, monitor_IN_reqWrite_6 == monitor_IN_reqWrite_5), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_5) == (False))), monitor_IN_reqWrite_5), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_5) == ((_SafetyController_0_has_data_5) == (0)))), Not((monitor_IN_reqWrite_5) == (And(monitor_IN_reqRead_5, (_SafetyController_0_has_data_5) == (1))))), sensor_OUT_reqRead_5)), monitor_IN_reqWrite_5)), monitor_IN_reqWrite_6 == (False), monitor_IN_value_6 == (_SafetyController_0_buffered_status_5), _SafetyController_0_has_data_6 == (0), monitor_IN_reqRead_6 == (False), sensor_current_bpm_6 == sensor_current_bpm_5, sensor_OUT_value_6 == sensor_OUT_value_5, sensor_OUT_reqRead_6 == sensor_OUT_reqRead_5, sensor_OUT_reqWrite_6 == sensor_OUT_reqWrite_5, _SafetyController_0_buffered_status_6 == _SafetyController_0_buffered_status_5)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_6) == (sensor_OUT_reqWrite_6))), sensor_OUT_reqWrite_7 == (sensor_OUT_reqRead_6), sensor_current_bpm_7 == sensor_current_bpm_6, sensor_OUT_value_7 == sensor_OUT_value_6, sensor_OUT_reqRead_7 == sensor_OUT_reqRead_6, monitor_IN_value_7 == monitor_IN_value_6, monitor_IN_reqRead_7 == monitor_IN_reqRead_6, monitor_IN_reqWrite_7 == monitor_IN_reqWrite_6, _SafetyController_0_buffered_status_7 == _SafetyController_0_buffered_status_6, _SafetyController_0_has_data_7 == _SafetyController_0_has_data_6), 
    And(And(Not(False), (monitor_IN_reqRead_6) == (False)), monitor_IN_reqRead_7 == (True), sensor_current_bpm_7 == sensor_current_bpm_6, sensor_OUT_value_7 == sensor_OUT_value_6, sensor_OUT_reqRead_7 == sensor_OUT_reqRead_6, sensor_OUT_reqWrite_7 == sensor_OUT_reqWrite_6, monitor_IN_value_7 == monitor_IN_value_6, monitor_IN_reqWrite_7 == monitor_IN_reqWrite_6, _SafetyController_0_buffered_status_7 == _SafetyController_0_buffered_status_6, _SafetyController_0_has_data_7 == _SafetyController_0_has_data_6), 
    And(And(Not(False), Not((sensor_OUT_reqRead_6) == ((_SafetyController_0_has_data_6) == (0)))), sensor_OUT_reqRead_7 == ((_SafetyController_0_has_data_6) == (0)), sensor_current_bpm_7 == sensor_current_bpm_6, sensor_OUT_value_7 == sensor_OUT_value_6, sensor_OUT_reqWrite_7 == sensor_OUT_reqWrite_6, monitor_IN_value_7 == monitor_IN_value_6, monitor_IN_reqRead_7 == monitor_IN_reqRead_6, monitor_IN_reqWrite_7 == monitor_IN_reqWrite_6, _SafetyController_0_buffered_status_7 == _SafetyController_0_buffered_status_6, _SafetyController_0_has_data_7 == _SafetyController_0_has_data_6), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_6) == ((_SafetyController_0_has_data_6) == (0))))), Not((monitor_IN_reqWrite_6) == (And(monitor_IN_reqRead_6, (_SafetyController_0_has_data_6) == (1))))), monitor_IN_reqWrite_7 == (And(monitor_IN_reqRead_6, (_SafetyController_0_has_data_6) == (1))), sensor_current_bpm_7 == sensor_current_bpm_6, sensor_OUT_value_7 == sensor_OUT_value_6, sensor_OUT_reqRead_7 == sensor_OUT_reqRead_6, sensor_OUT_reqWrite_7 == sensor_OUT_reqWrite_6, monitor_IN_value_7 == monitor_IN_value_6, monitor_IN_reqRead_7 == monitor_IN_reqRead_6, _SafetyController_0_buffered_status_7 == _SafetyController_0_buffered_status_6, _SafetyController_0_has_data_7 == _SafetyController_0_has_data_6), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_6) == (sensor_OUT_reqWrite_6)))), sensor_OUT_reqWrite_6), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_6) == ((_SafetyController_0_has_data_6) == (0)))), Not((monitor_IN_reqWrite_6) == (And(monitor_IN_reqRead_6, (_SafetyController_0_has_data_6) == (1)))))), sensor_OUT_reqRead_6)), _SafetyController_0_buffered_status_7 == (If((sensor_current_bpm_6 > 100), 1, 0)), sensor_current_bpm_7 == (predict_next(sensor_current_bpm_6)), sensor_OUT_reqWrite_7 == (False), _SafetyController_0_has_data_7 == (1), sensor_OUT_reqRead_7 == (False), sensor_OUT_value_7 == (sensor_current_bpm_6), monitor_IN_value_7 == monitor_IN_value_6, monitor_IN_reqRead_7 == monitor_IN_reqRead_6, monitor_IN_reqWrite_7 == monitor_IN_reqWrite_6), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_6) == (False))), monitor_IN_reqWrite_6), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_6) == ((_SafetyController_0_has_data_6) == (0)))), Not((monitor_IN_reqWrite_6) == (And(monitor_IN_reqRead_6, (_SafetyController_0_has_data_6) == (1))))), sensor_OUT_reqRead_6)), monitor_IN_reqWrite_6)), monitor_IN_reqWrite_7 == (False), monitor_IN_value_7 == (_SafetyController_0_buffered_status_6), _SafetyController_0_has_data_7 == (0), monitor_IN_reqRead_7 == (False), sensor_current_bpm_7 == sensor_current_bpm_6, sensor_OUT_value_7 == sensor_OUT_value_6, sensor_OUT_reqRead_7 == sensor_OUT_reqRead_6, sensor_OUT_reqWrite_7 == sensor_OUT_reqWrite_6, _SafetyController_0_buffered_status_7 == _SafetyController_0_buffered_status_6)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_7) == (sensor_OUT_reqWrite_7))), sensor_OUT_reqWrite_8 == (sensor_OUT_reqRead_7), sensor_current_bpm_8 == sensor_current_bpm_7, sensor_OUT_value_8 == sensor_OUT_value_7, sensor_OUT_reqRead_8 == sensor_OUT_reqRead_7, monitor_IN_value_8 == monitor_IN_value_7, monitor_IN_reqRead_8 == monitor_IN_reqRead_7, monitor_IN_reqWrite_8 == monitor_IN_reqWrite_7, _SafetyController_0_buffered_status_8 == _SafetyController_0_buffered_status_7, _SafetyController_0_has_data_8 == _SafetyController_0_has_data_7), 
    And(And(Not(False), (monitor_IN_reqRead_7) == (False)), monitor_IN_reqRead_8 == (True), sensor_current_bpm_8 == sensor_current_bpm_7, sensor_OUT_value_8 == sensor_OUT_value_7, sensor_OUT_reqRead_8 == sensor_OUT_reqRead_7, sensor_OUT_reqWrite_8 == sensor_OUT_reqWrite_7, monitor_IN_value_8 == monitor_IN_value_7, monitor_IN_reqWrite_8 == monitor_IN_reqWrite_7, _SafetyController_0_buffered_status_8 == _SafetyController_0_buffered_status_7, _SafetyController_0_has_data_8 == _SafetyController_0_has_data_7), 
    And(And(Not(False), Not((sensor_OUT_reqRead_7) == ((_SafetyController_0_has_data_7) == (0)))), sensor_OUT_reqRead_8 == ((_SafetyController_0_has_data_7) == (0)), sensor_current_bpm_8 == sensor_current_bpm_7, sensor_OUT_value_8 == sensor_OUT_value_7, sensor_OUT_reqWrite_8 == sensor_OUT_reqWrite_7, monitor_IN_value_8 == monitor_IN_value_7, monitor_IN_reqRead_8 == monitor_IN_reqRead_7, monitor_IN_reqWrite_8 == monitor_IN_reqWrite_7, _SafetyController_0_buffered_status_8 == _SafetyController_0_buffered_status_7, _SafetyController_0_has_data_8 == _SafetyController_0_has_data_7), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_7) == ((_SafetyController_0_has_data_7) == (0))))), Not((monitor_IN_reqWrite_7) == (And(monitor_IN_reqRead_7, (_SafetyController_0_has_data_7) == (1))))), monitor_IN_reqWrite_8 == (And(monitor_IN_reqRead_7, (_SafetyController_0_has_data_7) == (1))), sensor_current_bpm_8 == sensor_current_bpm_7, sensor_OUT_value_8 == sensor_OUT_value_7, sensor_OUT_reqRead_8 == sensor_OUT_reqRead_7, sensor_OUT_reqWrite_8 == sensor_OUT_reqWrite_7, monitor_IN_value_8 == monitor_IN_value_7, monitor_IN_reqRead_8 == monitor_IN_reqRead_7, _SafetyController_0_buffered_status_8 == _SafetyController_0_buffered_status_7, _SafetyController_0_has_data_8 == _SafetyController_0_has_data_7), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_7) == (sensor_OUT_reqWrite_7)))), sensor_OUT_reqWrite_7), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_7) == ((_SafetyController_0_has_data_7) == (0)))), Not((monitor_IN_reqWrite_7) == (And(monitor_IN_reqRead_7, (_SafetyController_0_has_data_7) == (1)))))), sensor_OUT_reqRead_7)), _SafetyController_0_buffered_status_8 == (If((sensor_current_bpm_7 > 100), 1, 0)), sensor_current_bpm_8 == (predict_next(sensor_current_bpm_7)), sensor_OUT_reqWrite_8 == (False), _SafetyController_0_has_data_8 == (1), sensor_OUT_reqRead_8 == (False), sensor_OUT_value_8 == (sensor_current_bpm_7), monitor_IN_value_8 == monitor_IN_value_7, monitor_IN_reqRead_8 == monitor_IN_reqRead_7, monitor_IN_reqWrite_8 == monitor_IN_reqWrite_7), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_7) == (False))), monitor_IN_reqWrite_7), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_7) == ((_SafetyController_0_has_data_7) == (0)))), Not((monitor_IN_reqWrite_7) == (And(monitor_IN_reqRead_7, (_SafetyController_0_has_data_7) == (1))))), sensor_OUT_reqRead_7)), monitor_IN_reqWrite_7)), monitor_IN_reqWrite_8 == (False), monitor_IN_value_8 == (_SafetyController_0_buffered_status_7), _SafetyController_0_has_data_8 == (0), monitor_IN_reqRead_8 == (False), sensor_current_bpm_8 == sensor_current_bpm_7, sensor_OUT_value_8 == sensor_OUT_value_7, sensor_OUT_reqRead_8 == sensor_OUT_reqRead_7, sensor_OUT_reqWrite_8 == sensor_OUT_reqWrite_7, _SafetyController_0_buffered_status_8 == _SafetyController_0_buffered_status_7)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_8) == (sensor_OUT_reqWrite_8))), sensor_OUT_reqWrite_9 == (sensor_OUT_reqRead_8), sensor_current_bpm_9 == sensor_current_bpm_8, sensor_OUT_value_9 == sensor_OUT_value_8, sensor_OUT_reqRead_9 == sensor_OUT_reqRead_8, monitor_IN_value_9 == monitor_IN_value_8, monitor_IN_reqRead_9 == monitor_IN_reqRead_8, monitor_IN_reqWrite_9 == monitor_IN_reqWrite_8, _SafetyController_0_buffered_status_9 == _SafetyController_0_buffered_status_8, _SafetyController_0_has_data_9 == _SafetyController_0_has_data_8), 
    And(And(Not(False), (monitor_IN_reqRead_8) == (False)), monitor_IN_reqRead_9 == (True), sensor_current_bpm_9 == sensor_current_bpm_8, sensor_OUT_value_9 == sensor_OUT_value_8, sensor_OUT_reqRead_9 == sensor_OUT_reqRead_8, sensor_OUT_reqWrite_9 == sensor_OUT_reqWrite_8, monitor_IN_value_9 == monitor_IN_value_8, monitor_IN_reqWrite_9 == monitor_IN_reqWrite_8, _SafetyController_0_buffered_status_9 == _SafetyController_0_buffered_status_8, _SafetyController_0_has_data_9 == _SafetyController_0_has_data_8), 
    And(And(Not(False), Not((sensor_OUT_reqRead_8) == ((_SafetyController_0_has_data_8) == (0)))), sensor_OUT_reqRead_9 == ((_SafetyController_0_has_data_8) == (0)), sensor_current_bpm_9 == sensor_current_bpm_8, sensor_OUT_value_9 == sensor_OUT_value_8, sensor_OUT_reqWrite_9 == sensor_OUT_reqWrite_8, monitor_IN_value_9 == monitor_IN_value_8, monitor_IN_reqRead_9 == monitor_IN_reqRead_8, monitor_IN_reqWrite_9 == monitor_IN_reqWrite_8, _SafetyController_0_buffered_status_9 == _SafetyController_0_buffered_status_8, _SafetyController_0_has_data_9 == _SafetyController_0_has_data_8), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_8) == ((_SafetyController_0_has_data_8) == (0))))), Not((monitor_IN_reqWrite_8) == (And(monitor_IN_reqRead_8, (_SafetyController_0_has_data_8) == (1))))), monitor_IN_reqWrite_9 == (And(monitor_IN_reqRead_8, (_SafetyController_0_has_data_8) == (1))), sensor_current_bpm_9 == sensor_current_bpm_8, sensor_OUT_value_9 == sensor_OUT_value_8, sensor_OUT_reqRead_9 == sensor_OUT_reqRead_8, sensor_OUT_reqWrite_9 == sensor_OUT_reqWrite_8, monitor_IN_value_9 == monitor_IN_value_8, monitor_IN_reqRead_9 == monitor_IN_reqRead_8, _SafetyController_0_buffered_status_9 == _SafetyController_0_buffered_status_8, _SafetyController_0_has_data_9 == _SafetyController_0_has_data_8), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_8) == (sensor_OUT_reqWrite_8)))), sensor_OUT_reqWrite_8), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_8) == ((_SafetyController_0_has_data_8) == (0)))), Not((monitor_IN_reqWrite_8) == (And(monitor_IN_reqRead_8, (_SafetyController_0_has_data_8) == (1)))))), sensor_OUT_reqRead_8)), _SafetyController_0_buffered_status_9 == (If((sensor_current_bpm_8 > 100), 1, 0)), sensor_current_bpm_9 == (predict_next(sensor_current_bpm_8)), sensor_OUT_reqWrite_9 == (False), _SafetyController_0_has_data_9 == (1), sensor_OUT_reqRead_9 == (False), sensor_OUT_value_9 == (sensor_current_bpm_8), monitor_IN_value_9 == monitor_IN_value_8, monitor_IN_reqRead_9 == monitor_IN_reqRead_8, monitor_IN_reqWrite_9 == monitor_IN_reqWrite_8), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_8) == (False))), monitor_IN_reqWrite_8), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_8) == ((_SafetyController_0_has_data_8) == (0)))), Not((monitor_IN_reqWrite_8) == (And(monitor_IN_reqRead_8, (_SafetyController_0_has_data_8) == (1))))), sensor_OUT_reqRead_8)), monitor_IN_reqWrite_8)), monitor_IN_reqWrite_9 == (False), monitor_IN_value_9 == (_SafetyController_0_buffered_status_8), _SafetyController_0_has_data_9 == (0), monitor_IN_reqRead_9 == (False), sensor_current_bpm_9 == sensor_current_bpm_8, sensor_OUT_value_9 == sensor_OUT_value_8, sensor_OUT_reqRead_9 == sensor_OUT_reqRead_8, sensor_OUT_reqWrite_9 == sensor_OUT_reqWrite_8, _SafetyController_0_buffered_status_9 == _SafetyController_0_buffered_status_8)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_9) == (sensor_OUT_reqWrite_9))), sensor_OUT_reqWrite_10 == (sensor_OUT_reqRead_9), sensor_current_bpm_10 == sensor_current_bpm_9, sensor_OUT_value_10 == sensor_OUT_value_9, sensor_OUT_reqRead_10 == sensor_OUT_reqRead_9, monitor_IN_value_10 == monitor_IN_value_9, monitor_IN_reqRead_10 == monitor_IN_reqRead_9, monitor_IN_reqWrite_10 == monitor_IN_reqWrite_9, _SafetyController_0_buffered_status_10 == _SafetyController_0_buffered_status_9, _SafetyController_0_has_data_10 == _SafetyController_0_has_data_9), 
    And(And(Not(False), (monitor_IN_reqRead_9) == (False)), monitor_IN_reqRead_10 == (True), sensor_current_bpm_10 == sensor_current_bpm_9, sensor_OUT_value_10 == sensor_OUT_value_9, sensor_OUT_reqRead_10 == sensor_OUT_reqRead_9, sensor_OUT_reqWrite_10 == sensor_OUT_reqWrite_9, monitor_IN_value_10 == monitor_IN_value_9, monitor_IN_reqWrite_10 == monitor_IN_reqWrite_9, _SafetyController_0_buffered_status_10 == _SafetyController_0_buffered_status_9, _SafetyController_0_has_data_10 == _SafetyController_0_has_data_9), 
    And(And(Not(False), Not((sensor_OUT_reqRead_9) == ((_SafetyController_0_has_data_9) == (0)))), sensor_OUT_reqRead_10 == ((_SafetyController_0_has_data_9) == (0)), sensor_current_bpm_10 == sensor_current_bpm_9, sensor_OUT_value_10 == sensor_OUT_value_9, sensor_OUT_reqWrite_10 == sensor_OUT_reqWrite_9, monitor_IN_value_10 == monitor_IN_value_9, monitor_IN_reqRead_10 == monitor_IN_reqRead_9, monitor_IN_reqWrite_10 == monitor_IN_reqWrite_9, _SafetyController_0_buffered_status_10 == _SafetyController_0_buffered_status_9, _SafetyController_0_has_data_10 == _SafetyController_0_has_data_9), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_9) == ((_SafetyController_0_has_data_9) == (0))))), Not((monitor_IN_reqWrite_9) == (And(monitor_IN_reqRead_9, (_SafetyController_0_has_data_9) == (1))))), monitor_IN_reqWrite_10 == (And(monitor_IN_reqRead_9, (_SafetyController_0_has_data_9) == (1))), sensor_current_bpm_10 == sensor_current_bpm_9, sensor_OUT_value_10 == sensor_OUT_value_9, sensor_OUT_reqRead_10 == sensor_OUT_reqRead_9, sensor_OUT_reqWrite_10 == sensor_OUT_reqWrite_9, monitor_IN_value_10 == monitor_IN_value_9, monitor_IN_reqRead_10 == monitor_IN_reqRead_9, _SafetyController_0_buffered_status_10 == _SafetyController_0_buffered_status_9, _SafetyController_0_has_data_10 == _SafetyController_0_has_data_9), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_9) == (sensor_OUT_reqWrite_9)))), sensor_OUT_reqWrite_9), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_9) == ((_SafetyController_0_has_data_9) == (0)))), Not((monitor_IN_reqWrite_9) == (And(monitor_IN_reqRead_9, (_SafetyController_0_has_data_9) == (1)))))), sensor_OUT_reqRead_9)), _SafetyController_0_buffered_status_10 == (If((sensor_current_bpm_9 > 100), 1, 0)), sensor_current_bpm_10 == (predict_next(sensor_current_bpm_9)), sensor_OUT_reqWrite_10 == (False), _SafetyController_0_has_data_10 == (1), sensor_OUT_reqRead_10 == (False), sensor_OUT_value_10 == (sensor_current_bpm_9), monitor_IN_value_10 == monitor_IN_value_9, monitor_IN_reqRead_10 == monitor_IN_reqRead_9, monitor_IN_reqWrite_10 == monitor_IN_reqWrite_9), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_9) == (False))), monitor_IN_reqWrite_9), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_9) == ((_SafetyController_0_has_data_9) == (0)))), Not((monitor_IN_reqWrite_9) == (And(monitor_IN_reqRead_9, (_SafetyController_0_has_data_9) == (1))))), sensor_OUT_reqRead_9)), monitor_IN_reqWrite_9)), monitor_IN_reqWrite_10 == (False), monitor_IN_value_10 == (_SafetyController_0_buffered_status_9), _SafetyController_0_has_data_10 == (0), monitor_IN_reqRead_10 == (False), sensor_current_bpm_10 == sensor_current_bpm_9, sensor_OUT_value_10 == sensor_OUT_value_9, sensor_OUT_reqRead_10 == sensor_OUT_reqRead_9, sensor_OUT_reqWrite_10 == sensor_OUT_reqWrite_9, _SafetyController_0_buffered_status_10 == _SafetyController_0_buffered_status_9)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_10) == (sensor_OUT_reqWrite_10))), sensor_OUT_reqWrite_11 == (sensor_OUT_reqRead_10), sensor_current_bpm_11 == sensor_current_bpm_10, sensor_OUT_value_11 == sensor_OUT_value_10, sensor_OUT_reqRead_11 == sensor_OUT_reqRead_10, monitor_IN_value_11 == monitor_IN_value_10, monitor_IN_reqRead_11 == monitor_IN_reqRead_10, monitor_IN_reqWrite_11 == monitor_IN_reqWrite_10, _SafetyController_0_buffered_status_11 == _SafetyController_0_buffered_status_10, _SafetyController_0_has_data_11 == _SafetyController_0_has_data_10), 
    And(And(Not(False), (monitor_IN_reqRead_10) == (False)), monitor_IN_reqRead_11 == (True), sensor_current_bpm_11 == sensor_current_bpm_10, sensor_OUT_value_11 == sensor_OUT_value_10, sensor_OUT_reqRead_11 == sensor_OUT_reqRead_10, sensor_OUT_reqWrite_11 == sensor_OUT_reqWrite_10, monitor_IN_value_11 == monitor_IN_value_10, monitor_IN_reqWrite_11 == monitor_IN_reqWrite_10, _SafetyController_0_buffered_status_11 == _SafetyController_0_buffered_status_10, _SafetyController_0_has_data_11 == _SafetyController_0_has_data_10), 
    And(And(Not(False), Not((sensor_OUT_reqRead_10) == ((_SafetyController_0_has_data_10) == (0)))), sensor_OUT_reqRead_11 == ((_SafetyController_0_has_data_10) == (0)), sensor_current_bpm_11 == sensor_current_bpm_10, sensor_OUT_value_11 == sensor_OUT_value_10, sensor_OUT_reqWrite_11 == sensor_OUT_reqWrite_10, monitor_IN_value_11 == monitor_IN_value_10, monitor_IN_reqRead_11 == monitor_IN_reqRead_10, monitor_IN_reqWrite_11 == monitor_IN_reqWrite_10, _SafetyController_0_buffered_status_11 == _SafetyController_0_buffered_status_10, _SafetyController_0_has_data_11 == _SafetyController_0_has_data_10), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_10) == ((_SafetyController_0_has_data_10) == (0))))), Not((monitor_IN_reqWrite_10) == (And(monitor_IN_reqRead_10, (_SafetyController_0_has_data_10) == (1))))), monitor_IN_reqWrite_11 == (And(monitor_IN_reqRead_10, (_SafetyController_0_has_data_10) == (1))), sensor_current_bpm_11 == sensor_current_bpm_10, sensor_OUT_value_11 == sensor_OUT_value_10, sensor_OUT_reqRead_11 == sensor_OUT_reqRead_10, sensor_OUT_reqWrite_11 == sensor_OUT_reqWrite_10, monitor_IN_value_11 == monitor_IN_value_10, monitor_IN_reqRead_11 == monitor_IN_reqRead_10, _SafetyController_0_buffered_status_11 == _SafetyController_0_buffered_status_10, _SafetyController_0_has_data_11 == _SafetyController_0_has_data_10), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_10) == (sensor_OUT_reqWrite_10)))), sensor_OUT_reqWrite_10), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_10) == ((_SafetyController_0_has_data_10) == (0)))), Not((monitor_IN_reqWrite_10) == (And(monitor_IN_reqRead_10, (_SafetyController_0_has_data_10) == (1)))))), sensor_OUT_reqRead_10)), _SafetyController_0_buffered_status_11 == (If((sensor_current_bpm_10 > 100), 1, 0)), sensor_current_bpm_11 == (predict_next(sensor_current_bpm_10)), sensor_OUT_reqWrite_11 == (False), _SafetyController_0_has_data_11 == (1), sensor_OUT_reqRead_11 == (False), sensor_OUT_value_11 == (sensor_current_bpm_10), monitor_IN_value_11 == monitor_IN_value_10, monitor_IN_reqRead_11 == monitor_IN_reqRead_10, monitor_IN_reqWrite_11 == monitor_IN_reqWrite_10), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_10) == (False))), monitor_IN_reqWrite_10), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_10) == ((_SafetyController_0_has_data_10) == (0)))), Not((monitor_IN_reqWrite_10) == (And(monitor_IN_reqRead_10, (_SafetyController_0_has_data_10) == (1))))), sensor_OUT_reqRead_10)), monitor_IN_reqWrite_10)), monitor_IN_reqWrite_11 == (False), monitor_IN_value_11 == (_SafetyController_0_buffered_status_10), _SafetyController_0_has_data_11 == (0), monitor_IN_reqRead_11 == (False), sensor_current_bpm_11 == sensor_current_bpm_10, sensor_OUT_value_11 == sensor_OUT_value_10, sensor_OUT_reqRead_11 == sensor_OUT_reqRead_10, sensor_OUT_reqWrite_11 == sensor_OUT_reqWrite_10, _SafetyController_0_buffered_status_11 == _SafetyController_0_buffered_status_10)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_11) == (sensor_OUT_reqWrite_11))), sensor_OUT_reqWrite_12 == (sensor_OUT_reqRead_11), sensor_current_bpm_12 == sensor_current_bpm_11, sensor_OUT_value_12 == sensor_OUT_value_11, sensor_OUT_reqRead_12 == sensor_OUT_reqRead_11, monitor_IN_value_12 == monitor_IN_value_11, monitor_IN_reqRead_12 == monitor_IN_reqRead_11, monitor_IN_reqWrite_12 == monitor_IN_reqWrite_11, _SafetyController_0_buffered_status_12 == _SafetyController_0_buffered_status_11, _SafetyController_0_has_data_12 == _SafetyController_0_has_data_11), 
    And(And(Not(False), (monitor_IN_reqRead_11) == (False)), monitor_IN_reqRead_12 == (True), sensor_current_bpm_12 == sensor_current_bpm_11, sensor_OUT_value_12 == sensor_OUT_value_11, sensor_OUT_reqRead_12 == sensor_OUT_reqRead_11, sensor_OUT_reqWrite_12 == sensor_OUT_reqWrite_11, monitor_IN_value_12 == monitor_IN_value_11, monitor_IN_reqWrite_12 == monitor_IN_reqWrite_11, _SafetyController_0_buffered_status_12 == _SafetyController_0_buffered_status_11, _SafetyController_0_has_data_12 == _SafetyController_0_has_data_11), 
    And(And(Not(False), Not((sensor_OUT_reqRead_11) == ((_SafetyController_0_has_data_11) == (0)))), sensor_OUT_reqRead_12 == ((_SafetyController_0_has_data_11) == (0)), sensor_current_bpm_12 == sensor_current_bpm_11, sensor_OUT_value_12 == sensor_OUT_value_11, sensor_OUT_reqWrite_12 == sensor_OUT_reqWrite_11, monitor_IN_value_12 == monitor_IN_value_11, monitor_IN_reqRead_12 == monitor_IN_reqRead_11, monitor_IN_reqWrite_12 == monitor_IN_reqWrite_11, _SafetyController_0_buffered_status_12 == _SafetyController_0_buffered_status_11, _SafetyController_0_has_data_12 == _SafetyController_0_has_data_11), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_11) == ((_SafetyController_0_has_data_11) == (0))))), Not((monitor_IN_reqWrite_11) == (And(monitor_IN_reqRead_11, (_SafetyController_0_has_data_11) == (1))))), monitor_IN_reqWrite_12 == (And(monitor_IN_reqRead_11, (_SafetyController_0_has_data_11) == (1))), sensor_current_bpm_12 == sensor_current_bpm_11, sensor_OUT_value_12 == sensor_OUT_value_11, sensor_OUT_reqRead_12 == sensor_OUT_reqRead_11, sensor_OUT_reqWrite_12 == sensor_OUT_reqWrite_11, monitor_IN_value_12 == monitor_IN_value_11, monitor_IN_reqRead_12 == monitor_IN_reqRead_11, _SafetyController_0_buffered_status_12 == _SafetyController_0_buffered_status_11, _SafetyController_0_has_data_12 == _SafetyController_0_has_data_11), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_11) == (sensor_OUT_reqWrite_11)))), sensor_OUT_reqWrite_11), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_11) == ((_SafetyController_0_has_data_11) == (0)))), Not((monitor_IN_reqWrite_11) == (And(monitor_IN_reqRead_11, (_SafetyController_0_has_data_11) == (1)))))), sensor_OUT_reqRead_11)), _SafetyController_0_buffered_status_12 == (If((sensor_current_bpm_11 > 100), 1, 0)), sensor_current_bpm_12 == (predict_next(sensor_current_bpm_11)), sensor_OUT_reqWrite_12 == (False), _SafetyController_0_has_data_12 == (1), sensor_OUT_reqRead_12 == (False), sensor_OUT_value_12 == (sensor_current_bpm_11), monitor_IN_value_12 == monitor_IN_value_11, monitor_IN_reqRead_12 == monitor_IN_reqRead_11, monitor_IN_reqWrite_12 == monitor_IN_reqWrite_11), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_11) == (False))), monitor_IN_reqWrite_11), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_11) == ((_SafetyController_0_has_data_11) == (0)))), Not((monitor_IN_reqWrite_11) == (And(monitor_IN_reqRead_11, (_SafetyController_0_has_data_11) == (1))))), sensor_OUT_reqRead_11)), monitor_IN_reqWrite_11)), monitor_IN_reqWrite_12 == (False), monitor_IN_value_12 == (_SafetyController_0_buffered_status_11), _SafetyController_0_has_data_12 == (0), monitor_IN_reqRead_12 == (False), sensor_current_bpm_12 == sensor_current_bpm_11, sensor_OUT_value_12 == sensor_OUT_value_11, sensor_OUT_reqRead_12 == sensor_OUT_reqRead_11, sensor_OUT_reqWrite_12 == sensor_OUT_reqWrite_11, _SafetyController_0_buffered_status_12 == _SafetyController_0_buffered_status_11)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_12) == (sensor_OUT_reqWrite_12))), sensor_OUT_reqWrite_13 == (sensor_OUT_reqRead_12), sensor_current_bpm_13 == sensor_current_bpm_12, sensor_OUT_value_13 == sensor_OUT_value_12, sensor_OUT_reqRead_13 == sensor_OUT_reqRead_12, monitor_IN_value_13 == monitor_IN_value_12, monitor_IN_reqRead_13 == monitor_IN_reqRead_12, monitor_IN_reqWrite_13 == monitor_IN_reqWrite_12, _SafetyController_0_buffered_status_13 == _SafetyController_0_buffered_status_12, _SafetyController_0_has_data_13 == _SafetyController_0_has_data_12), 
    And(And(Not(False), (monitor_IN_reqRead_12) == (False)), monitor_IN_reqRead_13 == (True), sensor_current_bpm_13 == sensor_current_bpm_12, sensor_OUT_value_13 == sensor_OUT_value_12, sensor_OUT_reqRead_13 == sensor_OUT_reqRead_12, sensor_OUT_reqWrite_13 == sensor_OUT_reqWrite_12, monitor_IN_value_13 == monitor_IN_value_12, monitor_IN_reqWrite_13 == monitor_IN_reqWrite_12, _SafetyController_0_buffered_status_13 == _SafetyController_0_buffered_status_12, _SafetyController_0_has_data_13 == _SafetyController_0_has_data_12), 
    And(And(Not(False), Not((sensor_OUT_reqRead_12) == ((_SafetyController_0_has_data_12) == (0)))), sensor_OUT_reqRead_13 == ((_SafetyController_0_has_data_12) == (0)), sensor_current_bpm_13 == sensor_current_bpm_12, sensor_OUT_value_13 == sensor_OUT_value_12, sensor_OUT_reqWrite_13 == sensor_OUT_reqWrite_12, monitor_IN_value_13 == monitor_IN_value_12, monitor_IN_reqRead_13 == monitor_IN_reqRead_12, monitor_IN_reqWrite_13 == monitor_IN_reqWrite_12, _SafetyController_0_buffered_status_13 == _SafetyController_0_buffered_status_12, _SafetyController_0_has_data_13 == _SafetyController_0_has_data_12), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_12) == ((_SafetyController_0_has_data_12) == (0))))), Not((monitor_IN_reqWrite_12) == (And(monitor_IN_reqRead_12, (_SafetyController_0_has_data_12) == (1))))), monitor_IN_reqWrite_13 == (And(monitor_IN_reqRead_12, (_SafetyController_0_has_data_12) == (1))), sensor_current_bpm_13 == sensor_current_bpm_12, sensor_OUT_value_13 == sensor_OUT_value_12, sensor_OUT_reqRead_13 == sensor_OUT_reqRead_12, sensor_OUT_reqWrite_13 == sensor_OUT_reqWrite_12, monitor_IN_value_13 == monitor_IN_value_12, monitor_IN_reqRead_13 == monitor_IN_reqRead_12, _SafetyController_0_buffered_status_13 == _SafetyController_0_buffered_status_12, _SafetyController_0_has_data_13 == _SafetyController_0_has_data_12), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_12) == (sensor_OUT_reqWrite_12)))), sensor_OUT_reqWrite_12), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_12) == ((_SafetyController_0_has_data_12) == (0)))), Not((monitor_IN_reqWrite_12) == (And(monitor_IN_reqRead_12, (_SafetyController_0_has_data_12) == (1)))))), sensor_OUT_reqRead_12)), _SafetyController_0_buffered_status_13 == (If((sensor_current_bpm_12 > 100), 1, 0)), sensor_current_bpm_13 == (predict_next(sensor_current_bpm_12)), sensor_OUT_reqWrite_13 == (False), _SafetyController_0_has_data_13 == (1), sensor_OUT_reqRead_13 == (False), sensor_OUT_value_13 == (sensor_current_bpm_12), monitor_IN_value_13 == monitor_IN_value_12, monitor_IN_reqRead_13 == monitor_IN_reqRead_12, monitor_IN_reqWrite_13 == monitor_IN_reqWrite_12), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_12) == (False))), monitor_IN_reqWrite_12), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_12) == ((_SafetyController_0_has_data_12) == (0)))), Not((monitor_IN_reqWrite_12) == (And(monitor_IN_reqRead_12, (_SafetyController_0_has_data_12) == (1))))), sensor_OUT_reqRead_12)), monitor_IN_reqWrite_12)), monitor_IN_reqWrite_13 == (False), monitor_IN_value_13 == (_SafetyController_0_buffered_status_12), _SafetyController_0_has_data_13 == (0), monitor_IN_reqRead_13 == (False), sensor_current_bpm_13 == sensor_current_bpm_12, sensor_OUT_value_13 == sensor_OUT_value_12, sensor_OUT_reqRead_13 == sensor_OUT_reqRead_12, sensor_OUT_reqWrite_13 == sensor_OUT_reqWrite_12, _SafetyController_0_buffered_status_13 == _SafetyController_0_buffered_status_12)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_13) == (sensor_OUT_reqWrite_13))), sensor_OUT_reqWrite_14 == (sensor_OUT_reqRead_13), sensor_current_bpm_14 == sensor_current_bpm_13, sensor_OUT_value_14 == sensor_OUT_value_13, sensor_OUT_reqRead_14 == sensor_OUT_reqRead_13, monitor_IN_value_14 == monitor_IN_value_13, monitor_IN_reqRead_14 == monitor_IN_reqRead_13, monitor_IN_reqWrite_14 == monitor_IN_reqWrite_13, _SafetyController_0_buffered_status_14 == _SafetyController_0_buffered_status_13, _SafetyController_0_has_data_14 == _SafetyController_0_has_data_13), 
    And(And(Not(False), (monitor_IN_reqRead_13) == (False)), monitor_IN_reqRead_14 == (True), sensor_current_bpm_14 == sensor_current_bpm_13, sensor_OUT_value_14 == sensor_OUT_value_13, sensor_OUT_reqRead_14 == sensor_OUT_reqRead_13, sensor_OUT_reqWrite_14 == sensor_OUT_reqWrite_13, monitor_IN_value_14 == monitor_IN_value_13, monitor_IN_reqWrite_14 == monitor_IN_reqWrite_13, _SafetyController_0_buffered_status_14 == _SafetyController_0_buffered_status_13, _SafetyController_0_has_data_14 == _SafetyController_0_has_data_13), 
    And(And(Not(False), Not((sensor_OUT_reqRead_13) == ((_SafetyController_0_has_data_13) == (0)))), sensor_OUT_reqRead_14 == ((_SafetyController_0_has_data_13) == (0)), sensor_current_bpm_14 == sensor_current_bpm_13, sensor_OUT_value_14 == sensor_OUT_value_13, sensor_OUT_reqWrite_14 == sensor_OUT_reqWrite_13, monitor_IN_value_14 == monitor_IN_value_13, monitor_IN_reqRead_14 == monitor_IN_reqRead_13, monitor_IN_reqWrite_14 == monitor_IN_reqWrite_13, _SafetyController_0_buffered_status_14 == _SafetyController_0_buffered_status_13, _SafetyController_0_has_data_14 == _SafetyController_0_has_data_13), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_13) == ((_SafetyController_0_has_data_13) == (0))))), Not((monitor_IN_reqWrite_13) == (And(monitor_IN_reqRead_13, (_SafetyController_0_has_data_13) == (1))))), monitor_IN_reqWrite_14 == (And(monitor_IN_reqRead_13, (_SafetyController_0_has_data_13) == (1))), sensor_current_bpm_14 == sensor_current_bpm_13, sensor_OUT_value_14 == sensor_OUT_value_13, sensor_OUT_reqRead_14 == sensor_OUT_reqRead_13, sensor_OUT_reqWrite_14 == sensor_OUT_reqWrite_13, monitor_IN_value_14 == monitor_IN_value_13, monitor_IN_reqRead_14 == monitor_IN_reqRead_13, _SafetyController_0_buffered_status_14 == _SafetyController_0_buffered_status_13, _SafetyController_0_has_data_14 == _SafetyController_0_has_data_13), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_13) == (sensor_OUT_reqWrite_13)))), sensor_OUT_reqWrite_13), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_13) == ((_SafetyController_0_has_data_13) == (0)))), Not((monitor_IN_reqWrite_13) == (And(monitor_IN_reqRead_13, (_SafetyController_0_has_data_13) == (1)))))), sensor_OUT_reqRead_13)), _SafetyController_0_buffered_status_14 == (If((sensor_current_bpm_13 > 100), 1, 0)), sensor_current_bpm_14 == (predict_next(sensor_current_bpm_13)), sensor_OUT_reqWrite_14 == (False), _SafetyController_0_has_data_14 == (1), sensor_OUT_reqRead_14 == (False), sensor_OUT_value_14 == (sensor_current_bpm_13), monitor_IN_value_14 == monitor_IN_value_13, monitor_IN_reqRead_14 == monitor_IN_reqRead_13, monitor_IN_reqWrite_14 == monitor_IN_reqWrite_13), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_13) == (False))), monitor_IN_reqWrite_13), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_13) == ((_SafetyController_0_has_data_13) == (0)))), Not((monitor_IN_reqWrite_13) == (And(monitor_IN_reqRead_13, (_SafetyController_0_has_data_13) == (1))))), sensor_OUT_reqRead_13)), monitor_IN_reqWrite_13)), monitor_IN_reqWrite_14 == (False), monitor_IN_value_14 == (_SafetyController_0_buffered_status_13), _SafetyController_0_has_data_14 == (0), monitor_IN_reqRead_14 == (False), sensor_current_bpm_14 == sensor_current_bpm_13, sensor_OUT_value_14 == sensor_OUT_value_13, sensor_OUT_reqRead_14 == sensor_OUT_reqRead_13, sensor_OUT_reqWrite_14 == sensor_OUT_reqWrite_13, _SafetyController_0_buffered_status_14 == _SafetyController_0_buffered_status_13)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_14) == (sensor_OUT_reqWrite_14))), sensor_OUT_reqWrite_15 == (sensor_OUT_reqRead_14), sensor_current_bpm_15 == sensor_current_bpm_14, sensor_OUT_value_15 == sensor_OUT_value_14, sensor_OUT_reqRead_15 == sensor_OUT_reqRead_14, monitor_IN_value_15 == monitor_IN_value_14, monitor_IN_reqRead_15 == monitor_IN_reqRead_14, monitor_IN_reqWrite_15 == monitor_IN_reqWrite_14, _SafetyController_0_buffered_status_15 == _SafetyController_0_buffered_status_14, _SafetyController_0_has_data_15 == _SafetyController_0_has_data_14), 
    And(And(Not(False), (monitor_IN_reqRead_14) == (False)), monitor_IN_reqRead_15 == (True), sensor_current_bpm_15 == sensor_current_bpm_14, sensor_OUT_value_15 == sensor_OUT_value_14, sensor_OUT_reqRead_15 == sensor_OUT_reqRead_14, sensor_OUT_reqWrite_15 == sensor_OUT_reqWrite_14, monitor_IN_value_15 == monitor_IN_value_14, monitor_IN_reqWrite_15 == monitor_IN_reqWrite_14, _SafetyController_0_buffered_status_15 == _SafetyController_0_buffered_status_14, _SafetyController_0_has_data_15 == _SafetyController_0_has_data_14), 
    And(And(Not(False), Not((sensor_OUT_reqRead_14) == ((_SafetyController_0_has_data_14) == (0)))), sensor_OUT_reqRead_15 == ((_SafetyController_0_has_data_14) == (0)), sensor_current_bpm_15 == sensor_current_bpm_14, sensor_OUT_value_15 == sensor_OUT_value_14, sensor_OUT_reqWrite_15 == sensor_OUT_reqWrite_14, monitor_IN_value_15 == monitor_IN_value_14, monitor_IN_reqRead_15 == monitor_IN_reqRead_14, monitor_IN_reqWrite_15 == monitor_IN_reqWrite_14, _SafetyController_0_buffered_status_15 == _SafetyController_0_buffered_status_14, _SafetyController_0_has_data_15 == _SafetyController_0_has_data_14), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_14) == ((_SafetyController_0_has_data_14) == (0))))), Not((monitor_IN_reqWrite_14) == (And(monitor_IN_reqRead_14, (_SafetyController_0_has_data_14) == (1))))), monitor_IN_reqWrite_15 == (And(monitor_IN_reqRead_14, (_SafetyController_0_has_data_14) == (1))), sensor_current_bpm_15 == sensor_current_bpm_14, sensor_OUT_value_15 == sensor_OUT_value_14, sensor_OUT_reqRead_15 == sensor_OUT_reqRead_14, sensor_OUT_reqWrite_15 == sensor_OUT_reqWrite_14, monitor_IN_value_15 == monitor_IN_value_14, monitor_IN_reqRead_15 == monitor_IN_reqRead_14, _SafetyController_0_buffered_status_15 == _SafetyController_0_buffered_status_14, _SafetyController_0_has_data_15 == _SafetyController_0_has_data_14), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_14) == (sensor_OUT_reqWrite_14)))), sensor_OUT_reqWrite_14), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_14) == ((_SafetyController_0_has_data_14) == (0)))), Not((monitor_IN_reqWrite_14) == (And(monitor_IN_reqRead_14, (_SafetyController_0_has_data_14) == (1)))))), sensor_OUT_reqRead_14)), _SafetyController_0_buffered_status_15 == (If((sensor_current_bpm_14 > 100), 1, 0)), sensor_current_bpm_15 == (predict_next(sensor_current_bpm_14)), sensor_OUT_reqWrite_15 == (False), _SafetyController_0_has_data_15 == (1), sensor_OUT_reqRead_15 == (False), sensor_OUT_value_15 == (sensor_current_bpm_14), monitor_IN_value_15 == monitor_IN_value_14, monitor_IN_reqRead_15 == monitor_IN_reqRead_14, monitor_IN_reqWrite_15 == monitor_IN_reqWrite_14), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_14) == (False))), monitor_IN_reqWrite_14), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_14) == ((_SafetyController_0_has_data_14) == (0)))), Not((monitor_IN_reqWrite_14) == (And(monitor_IN_reqRead_14, (_SafetyController_0_has_data_14) == (1))))), sensor_OUT_reqRead_14)), monitor_IN_reqWrite_14)), monitor_IN_reqWrite_15 == (False), monitor_IN_value_15 == (_SafetyController_0_buffered_status_14), _SafetyController_0_has_data_15 == (0), monitor_IN_reqRead_15 == (False), sensor_current_bpm_15 == sensor_current_bpm_14, sensor_OUT_value_15 == sensor_OUT_value_14, sensor_OUT_reqRead_15 == sensor_OUT_reqRead_14, sensor_OUT_reqWrite_15 == sensor_OUT_reqWrite_14, _SafetyController_0_buffered_status_15 == _SafetyController_0_buffered_status_14)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_15) == (sensor_OUT_reqWrite_15))), sensor_OUT_reqWrite_16 == (sensor_OUT_reqRead_15), sensor_current_bpm_16 == sensor_current_bpm_15, sensor_OUT_value_16 == sensor_OUT_value_15, sensor_OUT_reqRead_16 == sensor_OUT_reqRead_15, monitor_IN_value_16 == monitor_IN_value_15, monitor_IN_reqRead_16 == monitor_IN_reqRead_15, monitor_IN_reqWrite_16 == monitor_IN_reqWrite_15, _SafetyController_0_buffered_status_16 == _SafetyController_0_buffered_status_15, _SafetyController_0_has_data_16 == _SafetyController_0_has_data_15), 
    And(And(Not(False), (monitor_IN_reqRead_15) == (False)), monitor_IN_reqRead_16 == (True), sensor_current_bpm_16 == sensor_current_bpm_15, sensor_OUT_value_16 == sensor_OUT_value_15, sensor_OUT_reqRead_16 == sensor_OUT_reqRead_15, sensor_OUT_reqWrite_16 == sensor_OUT_reqWrite_15, monitor_IN_value_16 == monitor_IN_value_15, monitor_IN_reqWrite_16 == monitor_IN_reqWrite_15, _SafetyController_0_buffered_status_16 == _SafetyController_0_buffered_status_15, _SafetyController_0_has_data_16 == _SafetyController_0_has_data_15), 
    And(And(Not(False), Not((sensor_OUT_reqRead_15) == ((_SafetyController_0_has_data_15) == (0)))), sensor_OUT_reqRead_16 == ((_SafetyController_0_has_data_15) == (0)), sensor_current_bpm_16 == sensor_current_bpm_15, sensor_OUT_value_16 == sensor_OUT_value_15, sensor_OUT_reqWrite_16 == sensor_OUT_reqWrite_15, monitor_IN_value_16 == monitor_IN_value_15, monitor_IN_reqRead_16 == monitor_IN_reqRead_15, monitor_IN_reqWrite_16 == monitor_IN_reqWrite_15, _SafetyController_0_buffered_status_16 == _SafetyController_0_buffered_status_15, _SafetyController_0_has_data_16 == _SafetyController_0_has_data_15), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_15) == ((_SafetyController_0_has_data_15) == (0))))), Not((monitor_IN_reqWrite_15) == (And(monitor_IN_reqRead_15, (_SafetyController_0_has_data_15) == (1))))), monitor_IN_reqWrite_16 == (And(monitor_IN_reqRead_15, (_SafetyController_0_has_data_15) == (1))), sensor_current_bpm_16 == sensor_current_bpm_15, sensor_OUT_value_16 == sensor_OUT_value_15, sensor_OUT_reqRead_16 == sensor_OUT_reqRead_15, sensor_OUT_reqWrite_16 == sensor_OUT_reqWrite_15, monitor_IN_value_16 == monitor_IN_value_15, monitor_IN_reqRead_16 == monitor_IN_reqRead_15, _SafetyController_0_buffered_status_16 == _SafetyController_0_buffered_status_15, _SafetyController_0_has_data_16 == _SafetyController_0_has_data_15), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_15) == (sensor_OUT_reqWrite_15)))), sensor_OUT_reqWrite_15), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_15) == ((_SafetyController_0_has_data_15) == (0)))), Not((monitor_IN_reqWrite_15) == (And(monitor_IN_reqRead_15, (_SafetyController_0_has_data_15) == (1)))))), sensor_OUT_reqRead_15)), _SafetyController_0_buffered_status_16 == (If((sensor_current_bpm_15 > 100), 1, 0)), sensor_current_bpm_16 == (predict_next(sensor_current_bpm_15)), sensor_OUT_reqWrite_16 == (False), _SafetyController_0_has_data_16 == (1), sensor_OUT_reqRead_16 == (False), sensor_OUT_value_16 == (sensor_current_bpm_15), monitor_IN_value_16 == monitor_IN_value_15, monitor_IN_reqRead_16 == monitor_IN_reqRead_15, monitor_IN_reqWrite_16 == monitor_IN_reqWrite_15), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_15) == (False))), monitor_IN_reqWrite_15), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_15) == ((_SafetyController_0_has_data_15) == (0)))), Not((monitor_IN_reqWrite_15) == (And(monitor_IN_reqRead_15, (_SafetyController_0_has_data_15) == (1))))), sensor_OUT_reqRead_15)), monitor_IN_reqWrite_15)), monitor_IN_reqWrite_16 == (False), monitor_IN_value_16 == (_SafetyController_0_buffered_status_15), _SafetyController_0_has_data_16 == (0), monitor_IN_reqRead_16 == (False), sensor_current_bpm_16 == sensor_current_bpm_15, sensor_OUT_value_16 == sensor_OUT_value_15, sensor_OUT_reqRead_16 == sensor_OUT_reqRead_15, sensor_OUT_reqWrite_16 == sensor_OUT_reqWrite_15, _SafetyController_0_buffered_status_16 == _SafetyController_0_buffered_status_15)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_16) == (sensor_OUT_reqWrite_16))), sensor_OUT_reqWrite_17 == (sensor_OUT_reqRead_16), sensor_current_bpm_17 == sensor_current_bpm_16, sensor_OUT_value_17 == sensor_OUT_value_16, sensor_OUT_reqRead_17 == sensor_OUT_reqRead_16, monitor_IN_value_17 == monitor_IN_value_16, monitor_IN_reqRead_17 == monitor_IN_reqRead_16, monitor_IN_reqWrite_17 == monitor_IN_reqWrite_16, _SafetyController_0_buffered_status_17 == _SafetyController_0_buffered_status_16, _SafetyController_0_has_data_17 == _SafetyController_0_has_data_16), 
    And(And(Not(False), (monitor_IN_reqRead_16) == (False)), monitor_IN_reqRead_17 == (True), sensor_current_bpm_17 == sensor_current_bpm_16, sensor_OUT_value_17 == sensor_OUT_value_16, sensor_OUT_reqRead_17 == sensor_OUT_reqRead_16, sensor_OUT_reqWrite_17 == sensor_OUT_reqWrite_16, monitor_IN_value_17 == monitor_IN_value_16, monitor_IN_reqWrite_17 == monitor_IN_reqWrite_16, _SafetyController_0_buffered_status_17 == _SafetyController_0_buffered_status_16, _SafetyController_0_has_data_17 == _SafetyController_0_has_data_16), 
    And(And(Not(False), Not((sensor_OUT_reqRead_16) == ((_SafetyController_0_has_data_16) == (0)))), sensor_OUT_reqRead_17 == ((_SafetyController_0_has_data_16) == (0)), sensor_current_bpm_17 == sensor_current_bpm_16, sensor_OUT_value_17 == sensor_OUT_value_16, sensor_OUT_reqWrite_17 == sensor_OUT_reqWrite_16, monitor_IN_value_17 == monitor_IN_value_16, monitor_IN_reqRead_17 == monitor_IN_reqRead_16, monitor_IN_reqWrite_17 == monitor_IN_reqWrite_16, _SafetyController_0_buffered_status_17 == _SafetyController_0_buffered_status_16, _SafetyController_0_has_data_17 == _SafetyController_0_has_data_16), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_16) == ((_SafetyController_0_has_data_16) == (0))))), Not((monitor_IN_reqWrite_16) == (And(monitor_IN_reqRead_16, (_SafetyController_0_has_data_16) == (1))))), monitor_IN_reqWrite_17 == (And(monitor_IN_reqRead_16, (_SafetyController_0_has_data_16) == (1))), sensor_current_bpm_17 == sensor_current_bpm_16, sensor_OUT_value_17 == sensor_OUT_value_16, sensor_OUT_reqRead_17 == sensor_OUT_reqRead_16, sensor_OUT_reqWrite_17 == sensor_OUT_reqWrite_16, monitor_IN_value_17 == monitor_IN_value_16, monitor_IN_reqRead_17 == monitor_IN_reqRead_16, _SafetyController_0_buffered_status_17 == _SafetyController_0_buffered_status_16, _SafetyController_0_has_data_17 == _SafetyController_0_has_data_16), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_16) == (sensor_OUT_reqWrite_16)))), sensor_OUT_reqWrite_16), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_16) == ((_SafetyController_0_has_data_16) == (0)))), Not((monitor_IN_reqWrite_16) == (And(monitor_IN_reqRead_16, (_SafetyController_0_has_data_16) == (1)))))), sensor_OUT_reqRead_16)), _SafetyController_0_buffered_status_17 == (If((sensor_current_bpm_16 > 100), 1, 0)), sensor_current_bpm_17 == (predict_next(sensor_current_bpm_16)), sensor_OUT_reqWrite_17 == (False), _SafetyController_0_has_data_17 == (1), sensor_OUT_reqRead_17 == (False), sensor_OUT_value_17 == (sensor_current_bpm_16), monitor_IN_value_17 == monitor_IN_value_16, monitor_IN_reqRead_17 == monitor_IN_reqRead_16, monitor_IN_reqWrite_17 == monitor_IN_reqWrite_16), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_16) == (False))), monitor_IN_reqWrite_16), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_16) == ((_SafetyController_0_has_data_16) == (0)))), Not((monitor_IN_reqWrite_16) == (And(monitor_IN_reqRead_16, (_SafetyController_0_has_data_16) == (1))))), sensor_OUT_reqRead_16)), monitor_IN_reqWrite_16)), monitor_IN_reqWrite_17 == (False), monitor_IN_value_17 == (_SafetyController_0_buffered_status_16), _SafetyController_0_has_data_17 == (0), monitor_IN_reqRead_17 == (False), sensor_current_bpm_17 == sensor_current_bpm_16, sensor_OUT_value_17 == sensor_OUT_value_16, sensor_OUT_reqRead_17 == sensor_OUT_reqRead_16, sensor_OUT_reqWrite_17 == sensor_OUT_reqWrite_16, _SafetyController_0_buffered_status_17 == _SafetyController_0_buffered_status_16)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_17) == (sensor_OUT_reqWrite_17))), sensor_OUT_reqWrite_18 == (sensor_OUT_reqRead_17), sensor_current_bpm_18 == sensor_current_bpm_17, sensor_OUT_value_18 == sensor_OUT_value_17, sensor_OUT_reqRead_18 == sensor_OUT_reqRead_17, monitor_IN_value_18 == monitor_IN_value_17, monitor_IN_reqRead_18 == monitor_IN_reqRead_17, monitor_IN_reqWrite_18 == monitor_IN_reqWrite_17, _SafetyController_0_buffered_status_18 == _SafetyController_0_buffered_status_17, _SafetyController_0_has_data_18 == _SafetyController_0_has_data_17), 
    And(And(Not(False), (monitor_IN_reqRead_17) == (False)), monitor_IN_reqRead_18 == (True), sensor_current_bpm_18 == sensor_current_bpm_17, sensor_OUT_value_18 == sensor_OUT_value_17, sensor_OUT_reqRead_18 == sensor_OUT_reqRead_17, sensor_OUT_reqWrite_18 == sensor_OUT_reqWrite_17, monitor_IN_value_18 == monitor_IN_value_17, monitor_IN_reqWrite_18 == monitor_IN_reqWrite_17, _SafetyController_0_buffered_status_18 == _SafetyController_0_buffered_status_17, _SafetyController_0_has_data_18 == _SafetyController_0_has_data_17), 
    And(And(Not(False), Not((sensor_OUT_reqRead_17) == ((_SafetyController_0_has_data_17) == (0)))), sensor_OUT_reqRead_18 == ((_SafetyController_0_has_data_17) == (0)), sensor_current_bpm_18 == sensor_current_bpm_17, sensor_OUT_value_18 == sensor_OUT_value_17, sensor_OUT_reqWrite_18 == sensor_OUT_reqWrite_17, monitor_IN_value_18 == monitor_IN_value_17, monitor_IN_reqRead_18 == monitor_IN_reqRead_17, monitor_IN_reqWrite_18 == monitor_IN_reqWrite_17, _SafetyController_0_buffered_status_18 == _SafetyController_0_buffered_status_17, _SafetyController_0_has_data_18 == _SafetyController_0_has_data_17), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_17) == ((_SafetyController_0_has_data_17) == (0))))), Not((monitor_IN_reqWrite_17) == (And(monitor_IN_reqRead_17, (_SafetyController_0_has_data_17) == (1))))), monitor_IN_reqWrite_18 == (And(monitor_IN_reqRead_17, (_SafetyController_0_has_data_17) == (1))), sensor_current_bpm_18 == sensor_current_bpm_17, sensor_OUT_value_18 == sensor_OUT_value_17, sensor_OUT_reqRead_18 == sensor_OUT_reqRead_17, sensor_OUT_reqWrite_18 == sensor_OUT_reqWrite_17, monitor_IN_value_18 == monitor_IN_value_17, monitor_IN_reqRead_18 == monitor_IN_reqRead_17, _SafetyController_0_buffered_status_18 == _SafetyController_0_buffered_status_17, _SafetyController_0_has_data_18 == _SafetyController_0_has_data_17), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_17) == (sensor_OUT_reqWrite_17)))), sensor_OUT_reqWrite_17), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_17) == ((_SafetyController_0_has_data_17) == (0)))), Not((monitor_IN_reqWrite_17) == (And(monitor_IN_reqRead_17, (_SafetyController_0_has_data_17) == (1)))))), sensor_OUT_reqRead_17)), _SafetyController_0_buffered_status_18 == (If((sensor_current_bpm_17 > 100), 1, 0)), sensor_current_bpm_18 == (predict_next(sensor_current_bpm_17)), sensor_OUT_reqWrite_18 == (False), _SafetyController_0_has_data_18 == (1), sensor_OUT_reqRead_18 == (False), sensor_OUT_value_18 == (sensor_current_bpm_17), monitor_IN_value_18 == monitor_IN_value_17, monitor_IN_reqRead_18 == monitor_IN_reqRead_17, monitor_IN_reqWrite_18 == monitor_IN_reqWrite_17), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_17) == (False))), monitor_IN_reqWrite_17), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_17) == ((_SafetyController_0_has_data_17) == (0)))), Not((monitor_IN_reqWrite_17) == (And(monitor_IN_reqRead_17, (_SafetyController_0_has_data_17) == (1))))), sensor_OUT_reqRead_17)), monitor_IN_reqWrite_17)), monitor_IN_reqWrite_18 == (False), monitor_IN_value_18 == (_SafetyController_0_buffered_status_17), _SafetyController_0_has_data_18 == (0), monitor_IN_reqRead_18 == (False), sensor_current_bpm_18 == sensor_current_bpm_17, sensor_OUT_value_18 == sensor_OUT_value_17, sensor_OUT_reqRead_18 == sensor_OUT_reqRead_17, sensor_OUT_reqWrite_18 == sensor_OUT_reqWrite_17, _SafetyController_0_buffered_status_18 == _SafetyController_0_buffered_status_17)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_18) == (sensor_OUT_reqWrite_18))), sensor_OUT_reqWrite_19 == (sensor_OUT_reqRead_18), sensor_current_bpm_19 == sensor_current_bpm_18, sensor_OUT_value_19 == sensor_OUT_value_18, sensor_OUT_reqRead_19 == sensor_OUT_reqRead_18, monitor_IN_value_19 == monitor_IN_value_18, monitor_IN_reqRead_19 == monitor_IN_reqRead_18, monitor_IN_reqWrite_19 == monitor_IN_reqWrite_18, _SafetyController_0_buffered_status_19 == _SafetyController_0_buffered_status_18, _SafetyController_0_has_data_19 == _SafetyController_0_has_data_18), 
    And(And(Not(False), (monitor_IN_reqRead_18) == (False)), monitor_IN_reqRead_19 == (True), sensor_current_bpm_19 == sensor_current_bpm_18, sensor_OUT_value_19 == sensor_OUT_value_18, sensor_OUT_reqRead_19 == sensor_OUT_reqRead_18, sensor_OUT_reqWrite_19 == sensor_OUT_reqWrite_18, monitor_IN_value_19 == monitor_IN_value_18, monitor_IN_reqWrite_19 == monitor_IN_reqWrite_18, _SafetyController_0_buffered_status_19 == _SafetyController_0_buffered_status_18, _SafetyController_0_has_data_19 == _SafetyController_0_has_data_18), 
    And(And(Not(False), Not((sensor_OUT_reqRead_18) == ((_SafetyController_0_has_data_18) == (0)))), sensor_OUT_reqRead_19 == ((_SafetyController_0_has_data_18) == (0)), sensor_current_bpm_19 == sensor_current_bpm_18, sensor_OUT_value_19 == sensor_OUT_value_18, sensor_OUT_reqWrite_19 == sensor_OUT_reqWrite_18, monitor_IN_value_19 == monitor_IN_value_18, monitor_IN_reqRead_19 == monitor_IN_reqRead_18, monitor_IN_reqWrite_19 == monitor_IN_reqWrite_18, _SafetyController_0_buffered_status_19 == _SafetyController_0_buffered_status_18, _SafetyController_0_has_data_19 == _SafetyController_0_has_data_18), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_18) == ((_SafetyController_0_has_data_18) == (0))))), Not((monitor_IN_reqWrite_18) == (And(monitor_IN_reqRead_18, (_SafetyController_0_has_data_18) == (1))))), monitor_IN_reqWrite_19 == (And(monitor_IN_reqRead_18, (_SafetyController_0_has_data_18) == (1))), sensor_current_bpm_19 == sensor_current_bpm_18, sensor_OUT_value_19 == sensor_OUT_value_18, sensor_OUT_reqRead_19 == sensor_OUT_reqRead_18, sensor_OUT_reqWrite_19 == sensor_OUT_reqWrite_18, monitor_IN_value_19 == monitor_IN_value_18, monitor_IN_reqRead_19 == monitor_IN_reqRead_18, _SafetyController_0_buffered_status_19 == _SafetyController_0_buffered_status_18, _SafetyController_0_has_data_19 == _SafetyController_0_has_data_18), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_18) == (sensor_OUT_reqWrite_18)))), sensor_OUT_reqWrite_18), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_18) == ((_SafetyController_0_has_data_18) == (0)))), Not((monitor_IN_reqWrite_18) == (And(monitor_IN_reqRead_18, (_SafetyController_0_has_data_18) == (1)))))), sensor_OUT_reqRead_18)), _SafetyController_0_buffered_status_19 == (If((sensor_current_bpm_18 > 100), 1, 0)), sensor_current_bpm_19 == (predict_next(sensor_current_bpm_18)), sensor_OUT_reqWrite_19 == (False), _SafetyController_0_has_data_19 == (1), sensor_OUT_reqRead_19 == (False), sensor_OUT_value_19 == (sensor_current_bpm_18), monitor_IN_value_19 == monitor_IN_value_18, monitor_IN_reqRead_19 == monitor_IN_reqRead_18, monitor_IN_reqWrite_19 == monitor_IN_reqWrite_18), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_18) == (False))), monitor_IN_reqWrite_18), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_18) == ((_SafetyController_0_has_data_18) == (0)))), Not((monitor_IN_reqWrite_18) == (And(monitor_IN_reqRead_18, (_SafetyController_0_has_data_18) == (1))))), sensor_OUT_reqRead_18)), monitor_IN_reqWrite_18)), monitor_IN_reqWrite_19 == (False), monitor_IN_value_19 == (_SafetyController_0_buffered_status_18), _SafetyController_0_has_data_19 == (0), monitor_IN_reqRead_19 == (False), sensor_current_bpm_19 == sensor_current_bpm_18, sensor_OUT_value_19 == sensor_OUT_value_18, sensor_OUT_reqRead_19 == sensor_OUT_reqRead_18, sensor_OUT_reqWrite_19 == sensor_OUT_reqWrite_18, _SafetyController_0_buffered_status_19 == _SafetyController_0_buffered_status_18)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_19) == (sensor_OUT_reqWrite_19))), sensor_OUT_reqWrite_20 == (sensor_OUT_reqRead_19), sensor_current_bpm_20 == sensor_current_bpm_19, sensor_OUT_value_20 == sensor_OUT_value_19, sensor_OUT_reqRead_20 == sensor_OUT_reqRead_19, monitor_IN_value_20 == monitor_IN_value_19, monitor_IN_reqRead_20 == monitor_IN_reqRead_19, monitor_IN_reqWrite_20 == monitor_IN_reqWrite_19, _SafetyController_0_buffered_status_20 == _SafetyController_0_buffered_status_19, _SafetyController_0_has_data_20 == _SafetyController_0_has_data_19), 
    And(And(Not(False), (monitor_IN_reqRead_19) == (False)), monitor_IN_reqRead_20 == (True), sensor_current_bpm_20 == sensor_current_bpm_19, sensor_OUT_value_20 == sensor_OUT_value_19, sensor_OUT_reqRead_20 == sensor_OUT_reqRead_19, sensor_OUT_reqWrite_20 == sensor_OUT_reqWrite_19, monitor_IN_value_20 == monitor_IN_value_19, monitor_IN_reqWrite_20 == monitor_IN_reqWrite_19, _SafetyController_0_buffered_status_20 == _SafetyController_0_buffered_status_19, _SafetyController_0_has_data_20 == _SafetyController_0_has_data_19), 
    And(And(Not(False), Not((sensor_OUT_reqRead_19) == ((_SafetyController_0_has_data_19) == (0)))), sensor_OUT_reqRead_20 == ((_SafetyController_0_has_data_19) == (0)), sensor_current_bpm_20 == sensor_current_bpm_19, sensor_OUT_value_20 == sensor_OUT_value_19, sensor_OUT_reqWrite_20 == sensor_OUT_reqWrite_19, monitor_IN_value_20 == monitor_IN_value_19, monitor_IN_reqRead_20 == monitor_IN_reqRead_19, monitor_IN_reqWrite_20 == monitor_IN_reqWrite_19, _SafetyController_0_buffered_status_20 == _SafetyController_0_buffered_status_19, _SafetyController_0_has_data_20 == _SafetyController_0_has_data_19), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_19) == ((_SafetyController_0_has_data_19) == (0))))), Not((monitor_IN_reqWrite_19) == (And(monitor_IN_reqRead_19, (_SafetyController_0_has_data_19) == (1))))), monitor_IN_reqWrite_20 == (And(monitor_IN_reqRead_19, (_SafetyController_0_has_data_19) == (1))), sensor_current_bpm_20 == sensor_current_bpm_19, sensor_OUT_value_20 == sensor_OUT_value_19, sensor_OUT_reqRead_20 == sensor_OUT_reqRead_19, sensor_OUT_reqWrite_20 == sensor_OUT_reqWrite_19, monitor_IN_value_20 == monitor_IN_value_19, monitor_IN_reqRead_20 == monitor_IN_reqRead_19, _SafetyController_0_buffered_status_20 == _SafetyController_0_buffered_status_19, _SafetyController_0_has_data_20 == _SafetyController_0_has_data_19), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_19) == (sensor_OUT_reqWrite_19)))), sensor_OUT_reqWrite_19), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_19) == ((_SafetyController_0_has_data_19) == (0)))), Not((monitor_IN_reqWrite_19) == (And(monitor_IN_reqRead_19, (_SafetyController_0_has_data_19) == (1)))))), sensor_OUT_reqRead_19)), _SafetyController_0_buffered_status_20 == (If((sensor_current_bpm_19 > 100), 1, 0)), sensor_current_bpm_20 == (predict_next(sensor_current_bpm_19)), sensor_OUT_reqWrite_20 == (False), _SafetyController_0_has_data_20 == (1), sensor_OUT_reqRead_20 == (False), sensor_OUT_value_20 == (sensor_current_bpm_19), monitor_IN_value_20 == monitor_IN_value_19, monitor_IN_reqRead_20 == monitor_IN_reqRead_19, monitor_IN_reqWrite_20 == monitor_IN_reqWrite_19), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_19) == (False))), monitor_IN_reqWrite_19), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_19) == ((_SafetyController_0_has_data_19) == (0)))), Not((monitor_IN_reqWrite_19) == (And(monitor_IN_reqRead_19, (_SafetyController_0_has_data_19) == (1))))), sensor_OUT_reqRead_19)), monitor_IN_reqWrite_19)), monitor_IN_reqWrite_20 == (False), monitor_IN_value_20 == (_SafetyController_0_buffered_status_19), _SafetyController_0_has_data_20 == (0), monitor_IN_reqRead_20 == (False), sensor_current_bpm_20 == sensor_current_bpm_19, sensor_OUT_value_20 == sensor_OUT_value_19, sensor_OUT_reqRead_20 == sensor_OUT_reqRead_19, sensor_OUT_reqWrite_20 == sensor_OUT_reqWrite_19, _SafetyController_0_buffered_status_20 == _SafetyController_0_buffered_status_19)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_20) == (sensor_OUT_reqWrite_20))), sensor_OUT_reqWrite_21 == (sensor_OUT_reqRead_20), sensor_current_bpm_21 == sensor_current_bpm_20, sensor_OUT_value_21 == sensor_OUT_value_20, sensor_OUT_reqRead_21 == sensor_OUT_reqRead_20, monitor_IN_value_21 == monitor_IN_value_20, monitor_IN_reqRead_21 == monitor_IN_reqRead_20, monitor_IN_reqWrite_21 == monitor_IN_reqWrite_20, _SafetyController_0_buffered_status_21 == _SafetyController_0_buffered_status_20, _SafetyController_0_has_data_21 == _SafetyController_0_has_data_20), 
    And(And(Not(False), (monitor_IN_reqRead_20) == (False)), monitor_IN_reqRead_21 == (True), sensor_current_bpm_21 == sensor_current_bpm_20, sensor_OUT_value_21 == sensor_OUT_value_20, sensor_OUT_reqRead_21 == sensor_OUT_reqRead_20, sensor_OUT_reqWrite_21 == sensor_OUT_reqWrite_20, monitor_IN_value_21 == monitor_IN_value_20, monitor_IN_reqWrite_21 == monitor_IN_reqWrite_20, _SafetyController_0_buffered_status_21 == _SafetyController_0_buffered_status_20, _SafetyController_0_has_data_21 == _SafetyController_0_has_data_20), 
    And(And(Not(False), Not((sensor_OUT_reqRead_20) == ((_SafetyController_0_has_data_20) == (0)))), sensor_OUT_reqRead_21 == ((_SafetyController_0_has_data_20) == (0)), sensor_current_bpm_21 == sensor_current_bpm_20, sensor_OUT_value_21 == sensor_OUT_value_20, sensor_OUT_reqWrite_21 == sensor_OUT_reqWrite_20, monitor_IN_value_21 == monitor_IN_value_20, monitor_IN_reqRead_21 == monitor_IN_reqRead_20, monitor_IN_reqWrite_21 == monitor_IN_reqWrite_20, _SafetyController_0_buffered_status_21 == _SafetyController_0_buffered_status_20, _SafetyController_0_has_data_21 == _SafetyController_0_has_data_20), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_20) == ((_SafetyController_0_has_data_20) == (0))))), Not((monitor_IN_reqWrite_20) == (And(monitor_IN_reqRead_20, (_SafetyController_0_has_data_20) == (1))))), monitor_IN_reqWrite_21 == (And(monitor_IN_reqRead_20, (_SafetyController_0_has_data_20) == (1))), sensor_current_bpm_21 == sensor_current_bpm_20, sensor_OUT_value_21 == sensor_OUT_value_20, sensor_OUT_reqRead_21 == sensor_OUT_reqRead_20, sensor_OUT_reqWrite_21 == sensor_OUT_reqWrite_20, monitor_IN_value_21 == monitor_IN_value_20, monitor_IN_reqRead_21 == monitor_IN_reqRead_20, _SafetyController_0_buffered_status_21 == _SafetyController_0_buffered_status_20, _SafetyController_0_has_data_21 == _SafetyController_0_has_data_20), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_20) == (sensor_OUT_reqWrite_20)))), sensor_OUT_reqWrite_20), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_20) == ((_SafetyController_0_has_data_20) == (0)))), Not((monitor_IN_reqWrite_20) == (And(monitor_IN_reqRead_20, (_SafetyController_0_has_data_20) == (1)))))), sensor_OUT_reqRead_20)), _SafetyController_0_buffered_status_21 == (If((sensor_current_bpm_20 > 100), 1, 0)), sensor_current_bpm_21 == (predict_next(sensor_current_bpm_20)), sensor_OUT_reqWrite_21 == (False), _SafetyController_0_has_data_21 == (1), sensor_OUT_reqRead_21 == (False), sensor_OUT_value_21 == (sensor_current_bpm_20), monitor_IN_value_21 == monitor_IN_value_20, monitor_IN_reqRead_21 == monitor_IN_reqRead_20, monitor_IN_reqWrite_21 == monitor_IN_reqWrite_20), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_20) == (False))), monitor_IN_reqWrite_20), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_20) == ((_SafetyController_0_has_data_20) == (0)))), Not((monitor_IN_reqWrite_20) == (And(monitor_IN_reqRead_20, (_SafetyController_0_has_data_20) == (1))))), sensor_OUT_reqRead_20)), monitor_IN_reqWrite_20)), monitor_IN_reqWrite_21 == (False), monitor_IN_value_21 == (_SafetyController_0_buffered_status_20), _SafetyController_0_has_data_21 == (0), monitor_IN_reqRead_21 == (False), sensor_current_bpm_21 == sensor_current_bpm_20, sensor_OUT_value_21 == sensor_OUT_value_20, sensor_OUT_reqRead_21 == sensor_OUT_reqRead_20, sensor_OUT_reqWrite_21 == sensor_OUT_reqWrite_20, _SafetyController_0_buffered_status_21 == _SafetyController_0_buffered_status_20)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_21) == (sensor_OUT_reqWrite_21))), sensor_OUT_reqWrite_22 == (sensor_OUT_reqRead_21), sensor_current_bpm_22 == sensor_current_bpm_21, sensor_OUT_value_22 == sensor_OUT_value_21, sensor_OUT_reqRead_22 == sensor_OUT_reqRead_21, monitor_IN_value_22 == monitor_IN_value_21, monitor_IN_reqRead_22 == monitor_IN_reqRead_21, monitor_IN_reqWrite_22 == monitor_IN_reqWrite_21, _SafetyController_0_buffered_status_22 == _SafetyController_0_buffered_status_21, _SafetyController_0_has_data_22 == _SafetyController_0_has_data_21), 
    And(And(Not(False), (monitor_IN_reqRead_21) == (False)), monitor_IN_reqRead_22 == (True), sensor_current_bpm_22 == sensor_current_bpm_21, sensor_OUT_value_22 == sensor_OUT_value_21, sensor_OUT_reqRead_22 == sensor_OUT_reqRead_21, sensor_OUT_reqWrite_22 == sensor_OUT_reqWrite_21, monitor_IN_value_22 == monitor_IN_value_21, monitor_IN_reqWrite_22 == monitor_IN_reqWrite_21, _SafetyController_0_buffered_status_22 == _SafetyController_0_buffered_status_21, _SafetyController_0_has_data_22 == _SafetyController_0_has_data_21), 
    And(And(Not(False), Not((sensor_OUT_reqRead_21) == ((_SafetyController_0_has_data_21) == (0)))), sensor_OUT_reqRead_22 == ((_SafetyController_0_has_data_21) == (0)), sensor_current_bpm_22 == sensor_current_bpm_21, sensor_OUT_value_22 == sensor_OUT_value_21, sensor_OUT_reqWrite_22 == sensor_OUT_reqWrite_21, monitor_IN_value_22 == monitor_IN_value_21, monitor_IN_reqRead_22 == monitor_IN_reqRead_21, monitor_IN_reqWrite_22 == monitor_IN_reqWrite_21, _SafetyController_0_buffered_status_22 == _SafetyController_0_buffered_status_21, _SafetyController_0_has_data_22 == _SafetyController_0_has_data_21), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_21) == ((_SafetyController_0_has_data_21) == (0))))), Not((monitor_IN_reqWrite_21) == (And(monitor_IN_reqRead_21, (_SafetyController_0_has_data_21) == (1))))), monitor_IN_reqWrite_22 == (And(monitor_IN_reqRead_21, (_SafetyController_0_has_data_21) == (1))), sensor_current_bpm_22 == sensor_current_bpm_21, sensor_OUT_value_22 == sensor_OUT_value_21, sensor_OUT_reqRead_22 == sensor_OUT_reqRead_21, sensor_OUT_reqWrite_22 == sensor_OUT_reqWrite_21, monitor_IN_value_22 == monitor_IN_value_21, monitor_IN_reqRead_22 == monitor_IN_reqRead_21, _SafetyController_0_buffered_status_22 == _SafetyController_0_buffered_status_21, _SafetyController_0_has_data_22 == _SafetyController_0_has_data_21), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_21) == (sensor_OUT_reqWrite_21)))), sensor_OUT_reqWrite_21), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_21) == ((_SafetyController_0_has_data_21) == (0)))), Not((monitor_IN_reqWrite_21) == (And(monitor_IN_reqRead_21, (_SafetyController_0_has_data_21) == (1)))))), sensor_OUT_reqRead_21)), _SafetyController_0_buffered_status_22 == (If((sensor_current_bpm_21 > 100), 1, 0)), sensor_current_bpm_22 == (predict_next(sensor_current_bpm_21)), sensor_OUT_reqWrite_22 == (False), _SafetyController_0_has_data_22 == (1), sensor_OUT_reqRead_22 == (False), sensor_OUT_value_22 == (sensor_current_bpm_21), monitor_IN_value_22 == monitor_IN_value_21, monitor_IN_reqRead_22 == monitor_IN_reqRead_21, monitor_IN_reqWrite_22 == monitor_IN_reqWrite_21), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_21) == (False))), monitor_IN_reqWrite_21), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_21) == ((_SafetyController_0_has_data_21) == (0)))), Not((monitor_IN_reqWrite_21) == (And(monitor_IN_reqRead_21, (_SafetyController_0_has_data_21) == (1))))), sensor_OUT_reqRead_21)), monitor_IN_reqWrite_21)), monitor_IN_reqWrite_22 == (False), monitor_IN_value_22 == (_SafetyController_0_buffered_status_21), _SafetyController_0_has_data_22 == (0), monitor_IN_reqRead_22 == (False), sensor_current_bpm_22 == sensor_current_bpm_21, sensor_OUT_value_22 == sensor_OUT_value_21, sensor_OUT_reqRead_22 == sensor_OUT_reqRead_21, sensor_OUT_reqWrite_22 == sensor_OUT_reqWrite_21, _SafetyController_0_buffered_status_22 == _SafetyController_0_buffered_status_21)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_22) == (sensor_OUT_reqWrite_22))), sensor_OUT_reqWrite_23 == (sensor_OUT_reqRead_22), sensor_current_bpm_23 == sensor_current_bpm_22, sensor_OUT_value_23 == sensor_OUT_value_22, sensor_OUT_reqRead_23 == sensor_OUT_reqRead_22, monitor_IN_value_23 == monitor_IN_value_22, monitor_IN_reqRead_23 == monitor_IN_reqRead_22, monitor_IN_reqWrite_23 == monitor_IN_reqWrite_22, _SafetyController_0_buffered_status_23 == _SafetyController_0_buffered_status_22, _SafetyController_0_has_data_23 == _SafetyController_0_has_data_22), 
    And(And(Not(False), (monitor_IN_reqRead_22) == (False)), monitor_IN_reqRead_23 == (True), sensor_current_bpm_23 == sensor_current_bpm_22, sensor_OUT_value_23 == sensor_OUT_value_22, sensor_OUT_reqRead_23 == sensor_OUT_reqRead_22, sensor_OUT_reqWrite_23 == sensor_OUT_reqWrite_22, monitor_IN_value_23 == monitor_IN_value_22, monitor_IN_reqWrite_23 == monitor_IN_reqWrite_22, _SafetyController_0_buffered_status_23 == _SafetyController_0_buffered_status_22, _SafetyController_0_has_data_23 == _SafetyController_0_has_data_22), 
    And(And(Not(False), Not((sensor_OUT_reqRead_22) == ((_SafetyController_0_has_data_22) == (0)))), sensor_OUT_reqRead_23 == ((_SafetyController_0_has_data_22) == (0)), sensor_current_bpm_23 == sensor_current_bpm_22, sensor_OUT_value_23 == sensor_OUT_value_22, sensor_OUT_reqWrite_23 == sensor_OUT_reqWrite_22, monitor_IN_value_23 == monitor_IN_value_22, monitor_IN_reqRead_23 == monitor_IN_reqRead_22, monitor_IN_reqWrite_23 == monitor_IN_reqWrite_22, _SafetyController_0_buffered_status_23 == _SafetyController_0_buffered_status_22, _SafetyController_0_has_data_23 == _SafetyController_0_has_data_22), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_22) == ((_SafetyController_0_has_data_22) == (0))))), Not((monitor_IN_reqWrite_22) == (And(monitor_IN_reqRead_22, (_SafetyController_0_has_data_22) == (1))))), monitor_IN_reqWrite_23 == (And(monitor_IN_reqRead_22, (_SafetyController_0_has_data_22) == (1))), sensor_current_bpm_23 == sensor_current_bpm_22, sensor_OUT_value_23 == sensor_OUT_value_22, sensor_OUT_reqRead_23 == sensor_OUT_reqRead_22, sensor_OUT_reqWrite_23 == sensor_OUT_reqWrite_22, monitor_IN_value_23 == monitor_IN_value_22, monitor_IN_reqRead_23 == monitor_IN_reqRead_22, _SafetyController_0_buffered_status_23 == _SafetyController_0_buffered_status_22, _SafetyController_0_has_data_23 == _SafetyController_0_has_data_22), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_22) == (sensor_OUT_reqWrite_22)))), sensor_OUT_reqWrite_22), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_22) == ((_SafetyController_0_has_data_22) == (0)))), Not((monitor_IN_reqWrite_22) == (And(monitor_IN_reqRead_22, (_SafetyController_0_has_data_22) == (1)))))), sensor_OUT_reqRead_22)), _SafetyController_0_buffered_status_23 == (If((sensor_current_bpm_22 > 100), 1, 0)), sensor_current_bpm_23 == (predict_next(sensor_current_bpm_22)), sensor_OUT_reqWrite_23 == (False), _SafetyController_0_has_data_23 == (1), sensor_OUT_reqRead_23 == (False), sensor_OUT_value_23 == (sensor_current_bpm_22), monitor_IN_value_23 == monitor_IN_value_22, monitor_IN_reqRead_23 == monitor_IN_reqRead_22, monitor_IN_reqWrite_23 == monitor_IN_reqWrite_22), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_22) == (False))), monitor_IN_reqWrite_22), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_22) == ((_SafetyController_0_has_data_22) == (0)))), Not((monitor_IN_reqWrite_22) == (And(monitor_IN_reqRead_22, (_SafetyController_0_has_data_22) == (1))))), sensor_OUT_reqRead_22)), monitor_IN_reqWrite_22)), monitor_IN_reqWrite_23 == (False), monitor_IN_value_23 == (_SafetyController_0_buffered_status_22), _SafetyController_0_has_data_23 == (0), monitor_IN_reqRead_23 == (False), sensor_current_bpm_23 == sensor_current_bpm_22, sensor_OUT_value_23 == sensor_OUT_value_22, sensor_OUT_reqRead_23 == sensor_OUT_reqRead_22, sensor_OUT_reqWrite_23 == sensor_OUT_reqWrite_22, _SafetyController_0_buffered_status_23 == _SafetyController_0_buffered_status_22)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_23) == (sensor_OUT_reqWrite_23))), sensor_OUT_reqWrite_24 == (sensor_OUT_reqRead_23), sensor_current_bpm_24 == sensor_current_bpm_23, sensor_OUT_value_24 == sensor_OUT_value_23, sensor_OUT_reqRead_24 == sensor_OUT_reqRead_23, monitor_IN_value_24 == monitor_IN_value_23, monitor_IN_reqRead_24 == monitor_IN_reqRead_23, monitor_IN_reqWrite_24 == monitor_IN_reqWrite_23, _SafetyController_0_buffered_status_24 == _SafetyController_0_buffered_status_23, _SafetyController_0_has_data_24 == _SafetyController_0_has_data_23), 
    And(And(Not(False), (monitor_IN_reqRead_23) == (False)), monitor_IN_reqRead_24 == (True), sensor_current_bpm_24 == sensor_current_bpm_23, sensor_OUT_value_24 == sensor_OUT_value_23, sensor_OUT_reqRead_24 == sensor_OUT_reqRead_23, sensor_OUT_reqWrite_24 == sensor_OUT_reqWrite_23, monitor_IN_value_24 == monitor_IN_value_23, monitor_IN_reqWrite_24 == monitor_IN_reqWrite_23, _SafetyController_0_buffered_status_24 == _SafetyController_0_buffered_status_23, _SafetyController_0_has_data_24 == _SafetyController_0_has_data_23), 
    And(And(Not(False), Not((sensor_OUT_reqRead_23) == ((_SafetyController_0_has_data_23) == (0)))), sensor_OUT_reqRead_24 == ((_SafetyController_0_has_data_23) == (0)), sensor_current_bpm_24 == sensor_current_bpm_23, sensor_OUT_value_24 == sensor_OUT_value_23, sensor_OUT_reqWrite_24 == sensor_OUT_reqWrite_23, monitor_IN_value_24 == monitor_IN_value_23, monitor_IN_reqRead_24 == monitor_IN_reqRead_23, monitor_IN_reqWrite_24 == monitor_IN_reqWrite_23, _SafetyController_0_buffered_status_24 == _SafetyController_0_buffered_status_23, _SafetyController_0_has_data_24 == _SafetyController_0_has_data_23), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_23) == ((_SafetyController_0_has_data_23) == (0))))), Not((monitor_IN_reqWrite_23) == (And(monitor_IN_reqRead_23, (_SafetyController_0_has_data_23) == (1))))), monitor_IN_reqWrite_24 == (And(monitor_IN_reqRead_23, (_SafetyController_0_has_data_23) == (1))), sensor_current_bpm_24 == sensor_current_bpm_23, sensor_OUT_value_24 == sensor_OUT_value_23, sensor_OUT_reqRead_24 == sensor_OUT_reqRead_23, sensor_OUT_reqWrite_24 == sensor_OUT_reqWrite_23, monitor_IN_value_24 == monitor_IN_value_23, monitor_IN_reqRead_24 == monitor_IN_reqRead_23, _SafetyController_0_buffered_status_24 == _SafetyController_0_buffered_status_23, _SafetyController_0_has_data_24 == _SafetyController_0_has_data_23), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_23) == (sensor_OUT_reqWrite_23)))), sensor_OUT_reqWrite_23), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_23) == ((_SafetyController_0_has_data_23) == (0)))), Not((monitor_IN_reqWrite_23) == (And(monitor_IN_reqRead_23, (_SafetyController_0_has_data_23) == (1)))))), sensor_OUT_reqRead_23)), _SafetyController_0_buffered_status_24 == (If((sensor_current_bpm_23 > 100), 1, 0)), sensor_current_bpm_24 == (predict_next(sensor_current_bpm_23)), sensor_OUT_reqWrite_24 == (False), _SafetyController_0_has_data_24 == (1), sensor_OUT_reqRead_24 == (False), sensor_OUT_value_24 == (sensor_current_bpm_23), monitor_IN_value_24 == monitor_IN_value_23, monitor_IN_reqRead_24 == monitor_IN_reqRead_23, monitor_IN_reqWrite_24 == monitor_IN_reqWrite_23), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_23) == (False))), monitor_IN_reqWrite_23), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_23) == ((_SafetyController_0_has_data_23) == (0)))), Not((monitor_IN_reqWrite_23) == (And(monitor_IN_reqRead_23, (_SafetyController_0_has_data_23) == (1))))), sensor_OUT_reqRead_23)), monitor_IN_reqWrite_23)), monitor_IN_reqWrite_24 == (False), monitor_IN_value_24 == (_SafetyController_0_buffered_status_23), _SafetyController_0_has_data_24 == (0), monitor_IN_reqRead_24 == (False), sensor_current_bpm_24 == sensor_current_bpm_23, sensor_OUT_value_24 == sensor_OUT_value_23, sensor_OUT_reqRead_24 == sensor_OUT_reqRead_23, sensor_OUT_reqWrite_24 == sensor_OUT_reqWrite_23, _SafetyController_0_buffered_status_24 == _SafetyController_0_buffered_status_23)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_24) == (sensor_OUT_reqWrite_24))), sensor_OUT_reqWrite_25 == (sensor_OUT_reqRead_24), sensor_current_bpm_25 == sensor_current_bpm_24, sensor_OUT_value_25 == sensor_OUT_value_24, sensor_OUT_reqRead_25 == sensor_OUT_reqRead_24, monitor_IN_value_25 == monitor_IN_value_24, monitor_IN_reqRead_25 == monitor_IN_reqRead_24, monitor_IN_reqWrite_25 == monitor_IN_reqWrite_24, _SafetyController_0_buffered_status_25 == _SafetyController_0_buffered_status_24, _SafetyController_0_has_data_25 == _SafetyController_0_has_data_24), 
    And(And(Not(False), (monitor_IN_reqRead_24) == (False)), monitor_IN_reqRead_25 == (True), sensor_current_bpm_25 == sensor_current_bpm_24, sensor_OUT_value_25 == sensor_OUT_value_24, sensor_OUT_reqRead_25 == sensor_OUT_reqRead_24, sensor_OUT_reqWrite_25 == sensor_OUT_reqWrite_24, monitor_IN_value_25 == monitor_IN_value_24, monitor_IN_reqWrite_25 == monitor_IN_reqWrite_24, _SafetyController_0_buffered_status_25 == _SafetyController_0_buffered_status_24, _SafetyController_0_has_data_25 == _SafetyController_0_has_data_24), 
    And(And(Not(False), Not((sensor_OUT_reqRead_24) == ((_SafetyController_0_has_data_24) == (0)))), sensor_OUT_reqRead_25 == ((_SafetyController_0_has_data_24) == (0)), sensor_current_bpm_25 == sensor_current_bpm_24, sensor_OUT_value_25 == sensor_OUT_value_24, sensor_OUT_reqWrite_25 == sensor_OUT_reqWrite_24, monitor_IN_value_25 == monitor_IN_value_24, monitor_IN_reqRead_25 == monitor_IN_reqRead_24, monitor_IN_reqWrite_25 == monitor_IN_reqWrite_24, _SafetyController_0_buffered_status_25 == _SafetyController_0_buffered_status_24, _SafetyController_0_has_data_25 == _SafetyController_0_has_data_24), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_24) == ((_SafetyController_0_has_data_24) == (0))))), Not((monitor_IN_reqWrite_24) == (And(monitor_IN_reqRead_24, (_SafetyController_0_has_data_24) == (1))))), monitor_IN_reqWrite_25 == (And(monitor_IN_reqRead_24, (_SafetyController_0_has_data_24) == (1))), sensor_current_bpm_25 == sensor_current_bpm_24, sensor_OUT_value_25 == sensor_OUT_value_24, sensor_OUT_reqRead_25 == sensor_OUT_reqRead_24, sensor_OUT_reqWrite_25 == sensor_OUT_reqWrite_24, monitor_IN_value_25 == monitor_IN_value_24, monitor_IN_reqRead_25 == monitor_IN_reqRead_24, _SafetyController_0_buffered_status_25 == _SafetyController_0_buffered_status_24, _SafetyController_0_has_data_25 == _SafetyController_0_has_data_24), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_24) == (sensor_OUT_reqWrite_24)))), sensor_OUT_reqWrite_24), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_24) == ((_SafetyController_0_has_data_24) == (0)))), Not((monitor_IN_reqWrite_24) == (And(monitor_IN_reqRead_24, (_SafetyController_0_has_data_24) == (1)))))), sensor_OUT_reqRead_24)), _SafetyController_0_buffered_status_25 == (If((sensor_current_bpm_24 > 100), 1, 0)), sensor_current_bpm_25 == (predict_next(sensor_current_bpm_24)), sensor_OUT_reqWrite_25 == (False), _SafetyController_0_has_data_25 == (1), sensor_OUT_reqRead_25 == (False), sensor_OUT_value_25 == (sensor_current_bpm_24), monitor_IN_value_25 == monitor_IN_value_24, monitor_IN_reqRead_25 == monitor_IN_reqRead_24, monitor_IN_reqWrite_25 == monitor_IN_reqWrite_24), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_24) == (False))), monitor_IN_reqWrite_24), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_24) == ((_SafetyController_0_has_data_24) == (0)))), Not((monitor_IN_reqWrite_24) == (And(monitor_IN_reqRead_24, (_SafetyController_0_has_data_24) == (1))))), sensor_OUT_reqRead_24)), monitor_IN_reqWrite_24)), monitor_IN_reqWrite_25 == (False), monitor_IN_value_25 == (_SafetyController_0_buffered_status_24), _SafetyController_0_has_data_25 == (0), monitor_IN_reqRead_25 == (False), sensor_current_bpm_25 == sensor_current_bpm_24, sensor_OUT_value_25 == sensor_OUT_value_24, sensor_OUT_reqRead_25 == sensor_OUT_reqRead_24, sensor_OUT_reqWrite_25 == sensor_OUT_reqWrite_24, _SafetyController_0_buffered_status_25 == _SafetyController_0_buffered_status_24)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_25) == (sensor_OUT_reqWrite_25))), sensor_OUT_reqWrite_26 == (sensor_OUT_reqRead_25), sensor_current_bpm_26 == sensor_current_bpm_25, sensor_OUT_value_26 == sensor_OUT_value_25, sensor_OUT_reqRead_26 == sensor_OUT_reqRead_25, monitor_IN_value_26 == monitor_IN_value_25, monitor_IN_reqRead_26 == monitor_IN_reqRead_25, monitor_IN_reqWrite_26 == monitor_IN_reqWrite_25, _SafetyController_0_buffered_status_26 == _SafetyController_0_buffered_status_25, _SafetyController_0_has_data_26 == _SafetyController_0_has_data_25), 
    And(And(Not(False), (monitor_IN_reqRead_25) == (False)), monitor_IN_reqRead_26 == (True), sensor_current_bpm_26 == sensor_current_bpm_25, sensor_OUT_value_26 == sensor_OUT_value_25, sensor_OUT_reqRead_26 == sensor_OUT_reqRead_25, sensor_OUT_reqWrite_26 == sensor_OUT_reqWrite_25, monitor_IN_value_26 == monitor_IN_value_25, monitor_IN_reqWrite_26 == monitor_IN_reqWrite_25, _SafetyController_0_buffered_status_26 == _SafetyController_0_buffered_status_25, _SafetyController_0_has_data_26 == _SafetyController_0_has_data_25), 
    And(And(Not(False), Not((sensor_OUT_reqRead_25) == ((_SafetyController_0_has_data_25) == (0)))), sensor_OUT_reqRead_26 == ((_SafetyController_0_has_data_25) == (0)), sensor_current_bpm_26 == sensor_current_bpm_25, sensor_OUT_value_26 == sensor_OUT_value_25, sensor_OUT_reqWrite_26 == sensor_OUT_reqWrite_25, monitor_IN_value_26 == monitor_IN_value_25, monitor_IN_reqRead_26 == monitor_IN_reqRead_25, monitor_IN_reqWrite_26 == monitor_IN_reqWrite_25, _SafetyController_0_buffered_status_26 == _SafetyController_0_buffered_status_25, _SafetyController_0_has_data_26 == _SafetyController_0_has_data_25), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_25) == ((_SafetyController_0_has_data_25) == (0))))), Not((monitor_IN_reqWrite_25) == (And(monitor_IN_reqRead_25, (_SafetyController_0_has_data_25) == (1))))), monitor_IN_reqWrite_26 == (And(monitor_IN_reqRead_25, (_SafetyController_0_has_data_25) == (1))), sensor_current_bpm_26 == sensor_current_bpm_25, sensor_OUT_value_26 == sensor_OUT_value_25, sensor_OUT_reqRead_26 == sensor_OUT_reqRead_25, sensor_OUT_reqWrite_26 == sensor_OUT_reqWrite_25, monitor_IN_value_26 == monitor_IN_value_25, monitor_IN_reqRead_26 == monitor_IN_reqRead_25, _SafetyController_0_buffered_status_26 == _SafetyController_0_buffered_status_25, _SafetyController_0_has_data_26 == _SafetyController_0_has_data_25), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_25) == (sensor_OUT_reqWrite_25)))), sensor_OUT_reqWrite_25), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_25) == ((_SafetyController_0_has_data_25) == (0)))), Not((monitor_IN_reqWrite_25) == (And(monitor_IN_reqRead_25, (_SafetyController_0_has_data_25) == (1)))))), sensor_OUT_reqRead_25)), _SafetyController_0_buffered_status_26 == (If((sensor_current_bpm_25 > 100), 1, 0)), sensor_current_bpm_26 == (predict_next(sensor_current_bpm_25)), sensor_OUT_reqWrite_26 == (False), _SafetyController_0_has_data_26 == (1), sensor_OUT_reqRead_26 == (False), sensor_OUT_value_26 == (sensor_current_bpm_25), monitor_IN_value_26 == monitor_IN_value_25, monitor_IN_reqRead_26 == monitor_IN_reqRead_25, monitor_IN_reqWrite_26 == monitor_IN_reqWrite_25), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_25) == (False))), monitor_IN_reqWrite_25), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_25) == ((_SafetyController_0_has_data_25) == (0)))), Not((monitor_IN_reqWrite_25) == (And(monitor_IN_reqRead_25, (_SafetyController_0_has_data_25) == (1))))), sensor_OUT_reqRead_25)), monitor_IN_reqWrite_25)), monitor_IN_reqWrite_26 == (False), monitor_IN_value_26 == (_SafetyController_0_buffered_status_25), _SafetyController_0_has_data_26 == (0), monitor_IN_reqRead_26 == (False), sensor_current_bpm_26 == sensor_current_bpm_25, sensor_OUT_value_26 == sensor_OUT_value_25, sensor_OUT_reqRead_26 == sensor_OUT_reqRead_25, sensor_OUT_reqWrite_26 == sensor_OUT_reqWrite_25, _SafetyController_0_buffered_status_26 == _SafetyController_0_buffered_status_25)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_26) == (sensor_OUT_reqWrite_26))), sensor_OUT_reqWrite_27 == (sensor_OUT_reqRead_26), sensor_current_bpm_27 == sensor_current_bpm_26, sensor_OUT_value_27 == sensor_OUT_value_26, sensor_OUT_reqRead_27 == sensor_OUT_reqRead_26, monitor_IN_value_27 == monitor_IN_value_26, monitor_IN_reqRead_27 == monitor_IN_reqRead_26, monitor_IN_reqWrite_27 == monitor_IN_reqWrite_26, _SafetyController_0_buffered_status_27 == _SafetyController_0_buffered_status_26, _SafetyController_0_has_data_27 == _SafetyController_0_has_data_26), 
    And(And(Not(False), (monitor_IN_reqRead_26) == (False)), monitor_IN_reqRead_27 == (True), sensor_current_bpm_27 == sensor_current_bpm_26, sensor_OUT_value_27 == sensor_OUT_value_26, sensor_OUT_reqRead_27 == sensor_OUT_reqRead_26, sensor_OUT_reqWrite_27 == sensor_OUT_reqWrite_26, monitor_IN_value_27 == monitor_IN_value_26, monitor_IN_reqWrite_27 == monitor_IN_reqWrite_26, _SafetyController_0_buffered_status_27 == _SafetyController_0_buffered_status_26, _SafetyController_0_has_data_27 == _SafetyController_0_has_data_26), 
    And(And(Not(False), Not((sensor_OUT_reqRead_26) == ((_SafetyController_0_has_data_26) == (0)))), sensor_OUT_reqRead_27 == ((_SafetyController_0_has_data_26) == (0)), sensor_current_bpm_27 == sensor_current_bpm_26, sensor_OUT_value_27 == sensor_OUT_value_26, sensor_OUT_reqWrite_27 == sensor_OUT_reqWrite_26, monitor_IN_value_27 == monitor_IN_value_26, monitor_IN_reqRead_27 == monitor_IN_reqRead_26, monitor_IN_reqWrite_27 == monitor_IN_reqWrite_26, _SafetyController_0_buffered_status_27 == _SafetyController_0_buffered_status_26, _SafetyController_0_has_data_27 == _SafetyController_0_has_data_26), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_26) == ((_SafetyController_0_has_data_26) == (0))))), Not((monitor_IN_reqWrite_26) == (And(monitor_IN_reqRead_26, (_SafetyController_0_has_data_26) == (1))))), monitor_IN_reqWrite_27 == (And(monitor_IN_reqRead_26, (_SafetyController_0_has_data_26) == (1))), sensor_current_bpm_27 == sensor_current_bpm_26, sensor_OUT_value_27 == sensor_OUT_value_26, sensor_OUT_reqRead_27 == sensor_OUT_reqRead_26, sensor_OUT_reqWrite_27 == sensor_OUT_reqWrite_26, monitor_IN_value_27 == monitor_IN_value_26, monitor_IN_reqRead_27 == monitor_IN_reqRead_26, _SafetyController_0_buffered_status_27 == _SafetyController_0_buffered_status_26, _SafetyController_0_has_data_27 == _SafetyController_0_has_data_26), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_26) == (sensor_OUT_reqWrite_26)))), sensor_OUT_reqWrite_26), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_26) == ((_SafetyController_0_has_data_26) == (0)))), Not((monitor_IN_reqWrite_26) == (And(monitor_IN_reqRead_26, (_SafetyController_0_has_data_26) == (1)))))), sensor_OUT_reqRead_26)), _SafetyController_0_buffered_status_27 == (If((sensor_current_bpm_26 > 100), 1, 0)), sensor_current_bpm_27 == (predict_next(sensor_current_bpm_26)), sensor_OUT_reqWrite_27 == (False), _SafetyController_0_has_data_27 == (1), sensor_OUT_reqRead_27 == (False), sensor_OUT_value_27 == (sensor_current_bpm_26), monitor_IN_value_27 == monitor_IN_value_26, monitor_IN_reqRead_27 == monitor_IN_reqRead_26, monitor_IN_reqWrite_27 == monitor_IN_reqWrite_26), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_26) == (False))), monitor_IN_reqWrite_26), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_26) == ((_SafetyController_0_has_data_26) == (0)))), Not((monitor_IN_reqWrite_26) == (And(monitor_IN_reqRead_26, (_SafetyController_0_has_data_26) == (1))))), sensor_OUT_reqRead_26)), monitor_IN_reqWrite_26)), monitor_IN_reqWrite_27 == (False), monitor_IN_value_27 == (_SafetyController_0_buffered_status_26), _SafetyController_0_has_data_27 == (0), monitor_IN_reqRead_27 == (False), sensor_current_bpm_27 == sensor_current_bpm_26, sensor_OUT_value_27 == sensor_OUT_value_26, sensor_OUT_reqRead_27 == sensor_OUT_reqRead_26, sensor_OUT_reqWrite_27 == sensor_OUT_reqWrite_26, _SafetyController_0_buffered_status_27 == _SafetyController_0_buffered_status_26)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_27) == (sensor_OUT_reqWrite_27))), sensor_OUT_reqWrite_28 == (sensor_OUT_reqRead_27), sensor_current_bpm_28 == sensor_current_bpm_27, sensor_OUT_value_28 == sensor_OUT_value_27, sensor_OUT_reqRead_28 == sensor_OUT_reqRead_27, monitor_IN_value_28 == monitor_IN_value_27, monitor_IN_reqRead_28 == monitor_IN_reqRead_27, monitor_IN_reqWrite_28 == monitor_IN_reqWrite_27, _SafetyController_0_buffered_status_28 == _SafetyController_0_buffered_status_27, _SafetyController_0_has_data_28 == _SafetyController_0_has_data_27), 
    And(And(Not(False), (monitor_IN_reqRead_27) == (False)), monitor_IN_reqRead_28 == (True), sensor_current_bpm_28 == sensor_current_bpm_27, sensor_OUT_value_28 == sensor_OUT_value_27, sensor_OUT_reqRead_28 == sensor_OUT_reqRead_27, sensor_OUT_reqWrite_28 == sensor_OUT_reqWrite_27, monitor_IN_value_28 == monitor_IN_value_27, monitor_IN_reqWrite_28 == monitor_IN_reqWrite_27, _SafetyController_0_buffered_status_28 == _SafetyController_0_buffered_status_27, _SafetyController_0_has_data_28 == _SafetyController_0_has_data_27), 
    And(And(Not(False), Not((sensor_OUT_reqRead_27) == ((_SafetyController_0_has_data_27) == (0)))), sensor_OUT_reqRead_28 == ((_SafetyController_0_has_data_27) == (0)), sensor_current_bpm_28 == sensor_current_bpm_27, sensor_OUT_value_28 == sensor_OUT_value_27, sensor_OUT_reqWrite_28 == sensor_OUT_reqWrite_27, monitor_IN_value_28 == monitor_IN_value_27, monitor_IN_reqRead_28 == monitor_IN_reqRead_27, monitor_IN_reqWrite_28 == monitor_IN_reqWrite_27, _SafetyController_0_buffered_status_28 == _SafetyController_0_buffered_status_27, _SafetyController_0_has_data_28 == _SafetyController_0_has_data_27), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_27) == ((_SafetyController_0_has_data_27) == (0))))), Not((monitor_IN_reqWrite_27) == (And(monitor_IN_reqRead_27, (_SafetyController_0_has_data_27) == (1))))), monitor_IN_reqWrite_28 == (And(monitor_IN_reqRead_27, (_SafetyController_0_has_data_27) == (1))), sensor_current_bpm_28 == sensor_current_bpm_27, sensor_OUT_value_28 == sensor_OUT_value_27, sensor_OUT_reqRead_28 == sensor_OUT_reqRead_27, sensor_OUT_reqWrite_28 == sensor_OUT_reqWrite_27, monitor_IN_value_28 == monitor_IN_value_27, monitor_IN_reqRead_28 == monitor_IN_reqRead_27, _SafetyController_0_buffered_status_28 == _SafetyController_0_buffered_status_27, _SafetyController_0_has_data_28 == _SafetyController_0_has_data_27), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_27) == (sensor_OUT_reqWrite_27)))), sensor_OUT_reqWrite_27), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_27) == ((_SafetyController_0_has_data_27) == (0)))), Not((monitor_IN_reqWrite_27) == (And(monitor_IN_reqRead_27, (_SafetyController_0_has_data_27) == (1)))))), sensor_OUT_reqRead_27)), _SafetyController_0_buffered_status_28 == (If((sensor_current_bpm_27 > 100), 1, 0)), sensor_current_bpm_28 == (predict_next(sensor_current_bpm_27)), sensor_OUT_reqWrite_28 == (False), _SafetyController_0_has_data_28 == (1), sensor_OUT_reqRead_28 == (False), sensor_OUT_value_28 == (sensor_current_bpm_27), monitor_IN_value_28 == monitor_IN_value_27, monitor_IN_reqRead_28 == monitor_IN_reqRead_27, monitor_IN_reqWrite_28 == monitor_IN_reqWrite_27), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_27) == (False))), monitor_IN_reqWrite_27), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_27) == ((_SafetyController_0_has_data_27) == (0)))), Not((monitor_IN_reqWrite_27) == (And(monitor_IN_reqRead_27, (_SafetyController_0_has_data_27) == (1))))), sensor_OUT_reqRead_27)), monitor_IN_reqWrite_27)), monitor_IN_reqWrite_28 == (False), monitor_IN_value_28 == (_SafetyController_0_buffered_status_27), _SafetyController_0_has_data_28 == (0), monitor_IN_reqRead_28 == (False), sensor_current_bpm_28 == sensor_current_bpm_27, sensor_OUT_value_28 == sensor_OUT_value_27, sensor_OUT_reqRead_28 == sensor_OUT_reqRead_27, sensor_OUT_reqWrite_28 == sensor_OUT_reqWrite_27, _SafetyController_0_buffered_status_28 == _SafetyController_0_buffered_status_27)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_28) == (sensor_OUT_reqWrite_28))), sensor_OUT_reqWrite_29 == (sensor_OUT_reqRead_28), sensor_current_bpm_29 == sensor_current_bpm_28, sensor_OUT_value_29 == sensor_OUT_value_28, sensor_OUT_reqRead_29 == sensor_OUT_reqRead_28, monitor_IN_value_29 == monitor_IN_value_28, monitor_IN_reqRead_29 == monitor_IN_reqRead_28, monitor_IN_reqWrite_29 == monitor_IN_reqWrite_28, _SafetyController_0_buffered_status_29 == _SafetyController_0_buffered_status_28, _SafetyController_0_has_data_29 == _SafetyController_0_has_data_28), 
    And(And(Not(False), (monitor_IN_reqRead_28) == (False)), monitor_IN_reqRead_29 == (True), sensor_current_bpm_29 == sensor_current_bpm_28, sensor_OUT_value_29 == sensor_OUT_value_28, sensor_OUT_reqRead_29 == sensor_OUT_reqRead_28, sensor_OUT_reqWrite_29 == sensor_OUT_reqWrite_28, monitor_IN_value_29 == monitor_IN_value_28, monitor_IN_reqWrite_29 == monitor_IN_reqWrite_28, _SafetyController_0_buffered_status_29 == _SafetyController_0_buffered_status_28, _SafetyController_0_has_data_29 == _SafetyController_0_has_data_28), 
    And(And(Not(False), Not((sensor_OUT_reqRead_28) == ((_SafetyController_0_has_data_28) == (0)))), sensor_OUT_reqRead_29 == ((_SafetyController_0_has_data_28) == (0)), sensor_current_bpm_29 == sensor_current_bpm_28, sensor_OUT_value_29 == sensor_OUT_value_28, sensor_OUT_reqWrite_29 == sensor_OUT_reqWrite_28, monitor_IN_value_29 == monitor_IN_value_28, monitor_IN_reqRead_29 == monitor_IN_reqRead_28, monitor_IN_reqWrite_29 == monitor_IN_reqWrite_28, _SafetyController_0_buffered_status_29 == _SafetyController_0_buffered_status_28, _SafetyController_0_has_data_29 == _SafetyController_0_has_data_28), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_28) == ((_SafetyController_0_has_data_28) == (0))))), Not((monitor_IN_reqWrite_28) == (And(monitor_IN_reqRead_28, (_SafetyController_0_has_data_28) == (1))))), monitor_IN_reqWrite_29 == (And(monitor_IN_reqRead_28, (_SafetyController_0_has_data_28) == (1))), sensor_current_bpm_29 == sensor_current_bpm_28, sensor_OUT_value_29 == sensor_OUT_value_28, sensor_OUT_reqRead_29 == sensor_OUT_reqRead_28, sensor_OUT_reqWrite_29 == sensor_OUT_reqWrite_28, monitor_IN_value_29 == monitor_IN_value_28, monitor_IN_reqRead_29 == monitor_IN_reqRead_28, _SafetyController_0_buffered_status_29 == _SafetyController_0_buffered_status_28, _SafetyController_0_has_data_29 == _SafetyController_0_has_data_28), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_28) == (sensor_OUT_reqWrite_28)))), sensor_OUT_reqWrite_28), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_28) == ((_SafetyController_0_has_data_28) == (0)))), Not((monitor_IN_reqWrite_28) == (And(monitor_IN_reqRead_28, (_SafetyController_0_has_data_28) == (1)))))), sensor_OUT_reqRead_28)), _SafetyController_0_buffered_status_29 == (If((sensor_current_bpm_28 > 100), 1, 0)), sensor_current_bpm_29 == (predict_next(sensor_current_bpm_28)), sensor_OUT_reqWrite_29 == (False), _SafetyController_0_has_data_29 == (1), sensor_OUT_reqRead_29 == (False), sensor_OUT_value_29 == (sensor_current_bpm_28), monitor_IN_value_29 == monitor_IN_value_28, monitor_IN_reqRead_29 == monitor_IN_reqRead_28, monitor_IN_reqWrite_29 == monitor_IN_reqWrite_28), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_28) == (False))), monitor_IN_reqWrite_28), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_28) == ((_SafetyController_0_has_data_28) == (0)))), Not((monitor_IN_reqWrite_28) == (And(monitor_IN_reqRead_28, (_SafetyController_0_has_data_28) == (1))))), sensor_OUT_reqRead_28)), monitor_IN_reqWrite_28)), monitor_IN_reqWrite_29 == (False), monitor_IN_value_29 == (_SafetyController_0_buffered_status_28), _SafetyController_0_has_data_29 == (0), monitor_IN_reqRead_29 == (False), sensor_current_bpm_29 == sensor_current_bpm_28, sensor_OUT_value_29 == sensor_OUT_value_28, sensor_OUT_reqRead_29 == sensor_OUT_reqRead_28, sensor_OUT_reqWrite_29 == sensor_OUT_reqWrite_28, _SafetyController_0_buffered_status_29 == _SafetyController_0_buffered_status_28)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_29) == (sensor_OUT_reqWrite_29))), sensor_OUT_reqWrite_30 == (sensor_OUT_reqRead_29), sensor_current_bpm_30 == sensor_current_bpm_29, sensor_OUT_value_30 == sensor_OUT_value_29, sensor_OUT_reqRead_30 == sensor_OUT_reqRead_29, monitor_IN_value_30 == monitor_IN_value_29, monitor_IN_reqRead_30 == monitor_IN_reqRead_29, monitor_IN_reqWrite_30 == monitor_IN_reqWrite_29, _SafetyController_0_buffered_status_30 == _SafetyController_0_buffered_status_29, _SafetyController_0_has_data_30 == _SafetyController_0_has_data_29), 
    And(And(Not(False), (monitor_IN_reqRead_29) == (False)), monitor_IN_reqRead_30 == (True), sensor_current_bpm_30 == sensor_current_bpm_29, sensor_OUT_value_30 == sensor_OUT_value_29, sensor_OUT_reqRead_30 == sensor_OUT_reqRead_29, sensor_OUT_reqWrite_30 == sensor_OUT_reqWrite_29, monitor_IN_value_30 == monitor_IN_value_29, monitor_IN_reqWrite_30 == monitor_IN_reqWrite_29, _SafetyController_0_buffered_status_30 == _SafetyController_0_buffered_status_29, _SafetyController_0_has_data_30 == _SafetyController_0_has_data_29), 
    And(And(Not(False), Not((sensor_OUT_reqRead_29) == ((_SafetyController_0_has_data_29) == (0)))), sensor_OUT_reqRead_30 == ((_SafetyController_0_has_data_29) == (0)), sensor_current_bpm_30 == sensor_current_bpm_29, sensor_OUT_value_30 == sensor_OUT_value_29, sensor_OUT_reqWrite_30 == sensor_OUT_reqWrite_29, monitor_IN_value_30 == monitor_IN_value_29, monitor_IN_reqRead_30 == monitor_IN_reqRead_29, monitor_IN_reqWrite_30 == monitor_IN_reqWrite_29, _SafetyController_0_buffered_status_30 == _SafetyController_0_buffered_status_29, _SafetyController_0_has_data_30 == _SafetyController_0_has_data_29), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_29) == ((_SafetyController_0_has_data_29) == (0))))), Not((monitor_IN_reqWrite_29) == (And(monitor_IN_reqRead_29, (_SafetyController_0_has_data_29) == (1))))), monitor_IN_reqWrite_30 == (And(monitor_IN_reqRead_29, (_SafetyController_0_has_data_29) == (1))), sensor_current_bpm_30 == sensor_current_bpm_29, sensor_OUT_value_30 == sensor_OUT_value_29, sensor_OUT_reqRead_30 == sensor_OUT_reqRead_29, sensor_OUT_reqWrite_30 == sensor_OUT_reqWrite_29, monitor_IN_value_30 == monitor_IN_value_29, monitor_IN_reqRead_30 == monitor_IN_reqRead_29, _SafetyController_0_buffered_status_30 == _SafetyController_0_buffered_status_29, _SafetyController_0_has_data_30 == _SafetyController_0_has_data_29), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_29) == (sensor_OUT_reqWrite_29)))), sensor_OUT_reqWrite_29), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_29) == ((_SafetyController_0_has_data_29) == (0)))), Not((monitor_IN_reqWrite_29) == (And(monitor_IN_reqRead_29, (_SafetyController_0_has_data_29) == (1)))))), sensor_OUT_reqRead_29)), _SafetyController_0_buffered_status_30 == (If((sensor_current_bpm_29 > 100), 1, 0)), sensor_current_bpm_30 == (predict_next(sensor_current_bpm_29)), sensor_OUT_reqWrite_30 == (False), _SafetyController_0_has_data_30 == (1), sensor_OUT_reqRead_30 == (False), sensor_OUT_value_30 == (sensor_current_bpm_29), monitor_IN_value_30 == monitor_IN_value_29, monitor_IN_reqRead_30 == monitor_IN_reqRead_29, monitor_IN_reqWrite_30 == monitor_IN_reqWrite_29), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_29) == (False))), monitor_IN_reqWrite_29), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_29) == ((_SafetyController_0_has_data_29) == (0)))), Not((monitor_IN_reqWrite_29) == (And(monitor_IN_reqRead_29, (_SafetyController_0_has_data_29) == (1))))), sensor_OUT_reqRead_29)), monitor_IN_reqWrite_29)), monitor_IN_reqWrite_30 == (False), monitor_IN_value_30 == (_SafetyController_0_buffered_status_29), _SafetyController_0_has_data_30 == (0), monitor_IN_reqRead_30 == (False), sensor_current_bpm_30 == sensor_current_bpm_29, sensor_OUT_value_30 == sensor_OUT_value_29, sensor_OUT_reqRead_30 == sensor_OUT_reqRead_29, sensor_OUT_reqWrite_30 == sensor_OUT_reqWrite_29, _SafetyController_0_buffered_status_30 == _SafetyController_0_buffered_status_29)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_30) == (sensor_OUT_reqWrite_30))), sensor_OUT_reqWrite_31 == (sensor_OUT_reqRead_30), sensor_current_bpm_31 == sensor_current_bpm_30, sensor_OUT_value_31 == sensor_OUT_value_30, sensor_OUT_reqRead_31 == sensor_OUT_reqRead_30, monitor_IN_value_31 == monitor_IN_value_30, monitor_IN_reqRead_31 == monitor_IN_reqRead_30, monitor_IN_reqWrite_31 == monitor_IN_reqWrite_30, _SafetyController_0_buffered_status_31 == _SafetyController_0_buffered_status_30, _SafetyController_0_has_data_31 == _SafetyController_0_has_data_30), 
    And(And(Not(False), (monitor_IN_reqRead_30) == (False)), monitor_IN_reqRead_31 == (True), sensor_current_bpm_31 == sensor_current_bpm_30, sensor_OUT_value_31 == sensor_OUT_value_30, sensor_OUT_reqRead_31 == sensor_OUT_reqRead_30, sensor_OUT_reqWrite_31 == sensor_OUT_reqWrite_30, monitor_IN_value_31 == monitor_IN_value_30, monitor_IN_reqWrite_31 == monitor_IN_reqWrite_30, _SafetyController_0_buffered_status_31 == _SafetyController_0_buffered_status_30, _SafetyController_0_has_data_31 == _SafetyController_0_has_data_30), 
    And(And(Not(False), Not((sensor_OUT_reqRead_30) == ((_SafetyController_0_has_data_30) == (0)))), sensor_OUT_reqRead_31 == ((_SafetyController_0_has_data_30) == (0)), sensor_current_bpm_31 == sensor_current_bpm_30, sensor_OUT_value_31 == sensor_OUT_value_30, sensor_OUT_reqWrite_31 == sensor_OUT_reqWrite_30, monitor_IN_value_31 == monitor_IN_value_30, monitor_IN_reqRead_31 == monitor_IN_reqRead_30, monitor_IN_reqWrite_31 == monitor_IN_reqWrite_30, _SafetyController_0_buffered_status_31 == _SafetyController_0_buffered_status_30, _SafetyController_0_has_data_31 == _SafetyController_0_has_data_30), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_30) == ((_SafetyController_0_has_data_30) == (0))))), Not((monitor_IN_reqWrite_30) == (And(monitor_IN_reqRead_30, (_SafetyController_0_has_data_30) == (1))))), monitor_IN_reqWrite_31 == (And(monitor_IN_reqRead_30, (_SafetyController_0_has_data_30) == (1))), sensor_current_bpm_31 == sensor_current_bpm_30, sensor_OUT_value_31 == sensor_OUT_value_30, sensor_OUT_reqRead_31 == sensor_OUT_reqRead_30, sensor_OUT_reqWrite_31 == sensor_OUT_reqWrite_30, monitor_IN_value_31 == monitor_IN_value_30, monitor_IN_reqRead_31 == monitor_IN_reqRead_30, _SafetyController_0_buffered_status_31 == _SafetyController_0_buffered_status_30, _SafetyController_0_has_data_31 == _SafetyController_0_has_data_30), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_30) == (sensor_OUT_reqWrite_30)))), sensor_OUT_reqWrite_30), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_30) == ((_SafetyController_0_has_data_30) == (0)))), Not((monitor_IN_reqWrite_30) == (And(monitor_IN_reqRead_30, (_SafetyController_0_has_data_30) == (1)))))), sensor_OUT_reqRead_30)), _SafetyController_0_buffered_status_31 == (If((sensor_current_bpm_30 > 100), 1, 0)), sensor_current_bpm_31 == (predict_next(sensor_current_bpm_30)), sensor_OUT_reqWrite_31 == (False), _SafetyController_0_has_data_31 == (1), sensor_OUT_reqRead_31 == (False), sensor_OUT_value_31 == (sensor_current_bpm_30), monitor_IN_value_31 == monitor_IN_value_30, monitor_IN_reqRead_31 == monitor_IN_reqRead_30, monitor_IN_reqWrite_31 == monitor_IN_reqWrite_30), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_30) == (False))), monitor_IN_reqWrite_30), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_30) == ((_SafetyController_0_has_data_30) == (0)))), Not((monitor_IN_reqWrite_30) == (And(monitor_IN_reqRead_30, (_SafetyController_0_has_data_30) == (1))))), sensor_OUT_reqRead_30)), monitor_IN_reqWrite_30)), monitor_IN_reqWrite_31 == (False), monitor_IN_value_31 == (_SafetyController_0_buffered_status_30), _SafetyController_0_has_data_31 == (0), monitor_IN_reqRead_31 == (False), sensor_current_bpm_31 == sensor_current_bpm_30, sensor_OUT_value_31 == sensor_OUT_value_30, sensor_OUT_reqRead_31 == sensor_OUT_reqRead_30, sensor_OUT_reqWrite_31 == sensor_OUT_reqWrite_30, _SafetyController_0_buffered_status_31 == _SafetyController_0_buffered_status_30)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_31) == (sensor_OUT_reqWrite_31))), sensor_OUT_reqWrite_32 == (sensor_OUT_reqRead_31), sensor_current_bpm_32 == sensor_current_bpm_31, sensor_OUT_value_32 == sensor_OUT_value_31, sensor_OUT_reqRead_32 == sensor_OUT_reqRead_31, monitor_IN_value_32 == monitor_IN_value_31, monitor_IN_reqRead_32 == monitor_IN_reqRead_31, monitor_IN_reqWrite_32 == monitor_IN_reqWrite_31, _SafetyController_0_buffered_status_32 == _SafetyController_0_buffered_status_31, _SafetyController_0_has_data_32 == _SafetyController_0_has_data_31), 
    And(And(Not(False), (monitor_IN_reqRead_31) == (False)), monitor_IN_reqRead_32 == (True), sensor_current_bpm_32 == sensor_current_bpm_31, sensor_OUT_value_32 == sensor_OUT_value_31, sensor_OUT_reqRead_32 == sensor_OUT_reqRead_31, sensor_OUT_reqWrite_32 == sensor_OUT_reqWrite_31, monitor_IN_value_32 == monitor_IN_value_31, monitor_IN_reqWrite_32 == monitor_IN_reqWrite_31, _SafetyController_0_buffered_status_32 == _SafetyController_0_buffered_status_31, _SafetyController_0_has_data_32 == _SafetyController_0_has_data_31), 
    And(And(Not(False), Not((sensor_OUT_reqRead_31) == ((_SafetyController_0_has_data_31) == (0)))), sensor_OUT_reqRead_32 == ((_SafetyController_0_has_data_31) == (0)), sensor_current_bpm_32 == sensor_current_bpm_31, sensor_OUT_value_32 == sensor_OUT_value_31, sensor_OUT_reqWrite_32 == sensor_OUT_reqWrite_31, monitor_IN_value_32 == monitor_IN_value_31, monitor_IN_reqRead_32 == monitor_IN_reqRead_31, monitor_IN_reqWrite_32 == monitor_IN_reqWrite_31, _SafetyController_0_buffered_status_32 == _SafetyController_0_buffered_status_31, _SafetyController_0_has_data_32 == _SafetyController_0_has_data_31), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_31) == ((_SafetyController_0_has_data_31) == (0))))), Not((monitor_IN_reqWrite_31) == (And(monitor_IN_reqRead_31, (_SafetyController_0_has_data_31) == (1))))), monitor_IN_reqWrite_32 == (And(monitor_IN_reqRead_31, (_SafetyController_0_has_data_31) == (1))), sensor_current_bpm_32 == sensor_current_bpm_31, sensor_OUT_value_32 == sensor_OUT_value_31, sensor_OUT_reqRead_32 == sensor_OUT_reqRead_31, sensor_OUT_reqWrite_32 == sensor_OUT_reqWrite_31, monitor_IN_value_32 == monitor_IN_value_31, monitor_IN_reqRead_32 == monitor_IN_reqRead_31, _SafetyController_0_buffered_status_32 == _SafetyController_0_buffered_status_31, _SafetyController_0_has_data_32 == _SafetyController_0_has_data_31), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_31) == (sensor_OUT_reqWrite_31)))), sensor_OUT_reqWrite_31), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_31) == ((_SafetyController_0_has_data_31) == (0)))), Not((monitor_IN_reqWrite_31) == (And(monitor_IN_reqRead_31, (_SafetyController_0_has_data_31) == (1)))))), sensor_OUT_reqRead_31)), _SafetyController_0_buffered_status_32 == (If((sensor_current_bpm_31 > 100), 1, 0)), sensor_current_bpm_32 == (predict_next(sensor_current_bpm_31)), sensor_OUT_reqWrite_32 == (False), _SafetyController_0_has_data_32 == (1), sensor_OUT_reqRead_32 == (False), sensor_OUT_value_32 == (sensor_current_bpm_31), monitor_IN_value_32 == monitor_IN_value_31, monitor_IN_reqRead_32 == monitor_IN_reqRead_31, monitor_IN_reqWrite_32 == monitor_IN_reqWrite_31), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_31) == (False))), monitor_IN_reqWrite_31), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_31) == ((_SafetyController_0_has_data_31) == (0)))), Not((monitor_IN_reqWrite_31) == (And(monitor_IN_reqRead_31, (_SafetyController_0_has_data_31) == (1))))), sensor_OUT_reqRead_31)), monitor_IN_reqWrite_31)), monitor_IN_reqWrite_32 == (False), monitor_IN_value_32 == (_SafetyController_0_buffered_status_31), _SafetyController_0_has_data_32 == (0), monitor_IN_reqRead_32 == (False), sensor_current_bpm_32 == sensor_current_bpm_31, sensor_OUT_value_32 == sensor_OUT_value_31, sensor_OUT_reqRead_32 == sensor_OUT_reqRead_31, sensor_OUT_reqWrite_32 == sensor_OUT_reqWrite_31, _SafetyController_0_buffered_status_32 == _SafetyController_0_buffered_status_31)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_32) == (sensor_OUT_reqWrite_32))), sensor_OUT_reqWrite_33 == (sensor_OUT_reqRead_32), sensor_current_bpm_33 == sensor_current_bpm_32, sensor_OUT_value_33 == sensor_OUT_value_32, sensor_OUT_reqRead_33 == sensor_OUT_reqRead_32, monitor_IN_value_33 == monitor_IN_value_32, monitor_IN_reqRead_33 == monitor_IN_reqRead_32, monitor_IN_reqWrite_33 == monitor_IN_reqWrite_32, _SafetyController_0_buffered_status_33 == _SafetyController_0_buffered_status_32, _SafetyController_0_has_data_33 == _SafetyController_0_has_data_32), 
    And(And(Not(False), (monitor_IN_reqRead_32) == (False)), monitor_IN_reqRead_33 == (True), sensor_current_bpm_33 == sensor_current_bpm_32, sensor_OUT_value_33 == sensor_OUT_value_32, sensor_OUT_reqRead_33 == sensor_OUT_reqRead_32, sensor_OUT_reqWrite_33 == sensor_OUT_reqWrite_32, monitor_IN_value_33 == monitor_IN_value_32, monitor_IN_reqWrite_33 == monitor_IN_reqWrite_32, _SafetyController_0_buffered_status_33 == _SafetyController_0_buffered_status_32, _SafetyController_0_has_data_33 == _SafetyController_0_has_data_32), 
    And(And(Not(False), Not((sensor_OUT_reqRead_32) == ((_SafetyController_0_has_data_32) == (0)))), sensor_OUT_reqRead_33 == ((_SafetyController_0_has_data_32) == (0)), sensor_current_bpm_33 == sensor_current_bpm_32, sensor_OUT_value_33 == sensor_OUT_value_32, sensor_OUT_reqWrite_33 == sensor_OUT_reqWrite_32, monitor_IN_value_33 == monitor_IN_value_32, monitor_IN_reqRead_33 == monitor_IN_reqRead_32, monitor_IN_reqWrite_33 == monitor_IN_reqWrite_32, _SafetyController_0_buffered_status_33 == _SafetyController_0_buffered_status_32, _SafetyController_0_has_data_33 == _SafetyController_0_has_data_32), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_32) == ((_SafetyController_0_has_data_32) == (0))))), Not((monitor_IN_reqWrite_32) == (And(monitor_IN_reqRead_32, (_SafetyController_0_has_data_32) == (1))))), monitor_IN_reqWrite_33 == (And(monitor_IN_reqRead_32, (_SafetyController_0_has_data_32) == (1))), sensor_current_bpm_33 == sensor_current_bpm_32, sensor_OUT_value_33 == sensor_OUT_value_32, sensor_OUT_reqRead_33 == sensor_OUT_reqRead_32, sensor_OUT_reqWrite_33 == sensor_OUT_reqWrite_32, monitor_IN_value_33 == monitor_IN_value_32, monitor_IN_reqRead_33 == monitor_IN_reqRead_32, _SafetyController_0_buffered_status_33 == _SafetyController_0_buffered_status_32, _SafetyController_0_has_data_33 == _SafetyController_0_has_data_32), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_32) == (sensor_OUT_reqWrite_32)))), sensor_OUT_reqWrite_32), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_32) == ((_SafetyController_0_has_data_32) == (0)))), Not((monitor_IN_reqWrite_32) == (And(monitor_IN_reqRead_32, (_SafetyController_0_has_data_32) == (1)))))), sensor_OUT_reqRead_32)), _SafetyController_0_buffered_status_33 == (If((sensor_current_bpm_32 > 100), 1, 0)), sensor_current_bpm_33 == (predict_next(sensor_current_bpm_32)), sensor_OUT_reqWrite_33 == (False), _SafetyController_0_has_data_33 == (1), sensor_OUT_reqRead_33 == (False), sensor_OUT_value_33 == (sensor_current_bpm_32), monitor_IN_value_33 == monitor_IN_value_32, monitor_IN_reqRead_33 == monitor_IN_reqRead_32, monitor_IN_reqWrite_33 == monitor_IN_reqWrite_32), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_32) == (False))), monitor_IN_reqWrite_32), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_32) == ((_SafetyController_0_has_data_32) == (0)))), Not((monitor_IN_reqWrite_32) == (And(monitor_IN_reqRead_32, (_SafetyController_0_has_data_32) == (1))))), sensor_OUT_reqRead_32)), monitor_IN_reqWrite_32)), monitor_IN_reqWrite_33 == (False), monitor_IN_value_33 == (_SafetyController_0_buffered_status_32), _SafetyController_0_has_data_33 == (0), monitor_IN_reqRead_33 == (False), sensor_current_bpm_33 == sensor_current_bpm_32, sensor_OUT_value_33 == sensor_OUT_value_32, sensor_OUT_reqRead_33 == sensor_OUT_reqRead_32, sensor_OUT_reqWrite_33 == sensor_OUT_reqWrite_32, _SafetyController_0_buffered_status_33 == _SafetyController_0_buffered_status_32)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_33) == (sensor_OUT_reqWrite_33))), sensor_OUT_reqWrite_34 == (sensor_OUT_reqRead_33), sensor_current_bpm_34 == sensor_current_bpm_33, sensor_OUT_value_34 == sensor_OUT_value_33, sensor_OUT_reqRead_34 == sensor_OUT_reqRead_33, monitor_IN_value_34 == monitor_IN_value_33, monitor_IN_reqRead_34 == monitor_IN_reqRead_33, monitor_IN_reqWrite_34 == monitor_IN_reqWrite_33, _SafetyController_0_buffered_status_34 == _SafetyController_0_buffered_status_33, _SafetyController_0_has_data_34 == _SafetyController_0_has_data_33), 
    And(And(Not(False), (monitor_IN_reqRead_33) == (False)), monitor_IN_reqRead_34 == (True), sensor_current_bpm_34 == sensor_current_bpm_33, sensor_OUT_value_34 == sensor_OUT_value_33, sensor_OUT_reqRead_34 == sensor_OUT_reqRead_33, sensor_OUT_reqWrite_34 == sensor_OUT_reqWrite_33, monitor_IN_value_34 == monitor_IN_value_33, monitor_IN_reqWrite_34 == monitor_IN_reqWrite_33, _SafetyController_0_buffered_status_34 == _SafetyController_0_buffered_status_33, _SafetyController_0_has_data_34 == _SafetyController_0_has_data_33), 
    And(And(Not(False), Not((sensor_OUT_reqRead_33) == ((_SafetyController_0_has_data_33) == (0)))), sensor_OUT_reqRead_34 == ((_SafetyController_0_has_data_33) == (0)), sensor_current_bpm_34 == sensor_current_bpm_33, sensor_OUT_value_34 == sensor_OUT_value_33, sensor_OUT_reqWrite_34 == sensor_OUT_reqWrite_33, monitor_IN_value_34 == monitor_IN_value_33, monitor_IN_reqRead_34 == monitor_IN_reqRead_33, monitor_IN_reqWrite_34 == monitor_IN_reqWrite_33, _SafetyController_0_buffered_status_34 == _SafetyController_0_buffered_status_33, _SafetyController_0_has_data_34 == _SafetyController_0_has_data_33), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_33) == ((_SafetyController_0_has_data_33) == (0))))), Not((monitor_IN_reqWrite_33) == (And(monitor_IN_reqRead_33, (_SafetyController_0_has_data_33) == (1))))), monitor_IN_reqWrite_34 == (And(monitor_IN_reqRead_33, (_SafetyController_0_has_data_33) == (1))), sensor_current_bpm_34 == sensor_current_bpm_33, sensor_OUT_value_34 == sensor_OUT_value_33, sensor_OUT_reqRead_34 == sensor_OUT_reqRead_33, sensor_OUT_reqWrite_34 == sensor_OUT_reqWrite_33, monitor_IN_value_34 == monitor_IN_value_33, monitor_IN_reqRead_34 == monitor_IN_reqRead_33, _SafetyController_0_buffered_status_34 == _SafetyController_0_buffered_status_33, _SafetyController_0_has_data_34 == _SafetyController_0_has_data_33), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_33) == (sensor_OUT_reqWrite_33)))), sensor_OUT_reqWrite_33), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_33) == ((_SafetyController_0_has_data_33) == (0)))), Not((monitor_IN_reqWrite_33) == (And(monitor_IN_reqRead_33, (_SafetyController_0_has_data_33) == (1)))))), sensor_OUT_reqRead_33)), _SafetyController_0_buffered_status_34 == (If((sensor_current_bpm_33 > 100), 1, 0)), sensor_current_bpm_34 == (predict_next(sensor_current_bpm_33)), sensor_OUT_reqWrite_34 == (False), _SafetyController_0_has_data_34 == (1), sensor_OUT_reqRead_34 == (False), sensor_OUT_value_34 == (sensor_current_bpm_33), monitor_IN_value_34 == monitor_IN_value_33, monitor_IN_reqRead_34 == monitor_IN_reqRead_33, monitor_IN_reqWrite_34 == monitor_IN_reqWrite_33), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_33) == (False))), monitor_IN_reqWrite_33), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_33) == ((_SafetyController_0_has_data_33) == (0)))), Not((monitor_IN_reqWrite_33) == (And(monitor_IN_reqRead_33, (_SafetyController_0_has_data_33) == (1))))), sensor_OUT_reqRead_33)), monitor_IN_reqWrite_33)), monitor_IN_reqWrite_34 == (False), monitor_IN_value_34 == (_SafetyController_0_buffered_status_33), _SafetyController_0_has_data_34 == (0), monitor_IN_reqRead_34 == (False), sensor_current_bpm_34 == sensor_current_bpm_33, sensor_OUT_value_34 == sensor_OUT_value_33, sensor_OUT_reqRead_34 == sensor_OUT_reqRead_33, sensor_OUT_reqWrite_34 == sensor_OUT_reqWrite_33, _SafetyController_0_buffered_status_34 == _SafetyController_0_buffered_status_33)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_34) == (sensor_OUT_reqWrite_34))), sensor_OUT_reqWrite_35 == (sensor_OUT_reqRead_34), sensor_current_bpm_35 == sensor_current_bpm_34, sensor_OUT_value_35 == sensor_OUT_value_34, sensor_OUT_reqRead_35 == sensor_OUT_reqRead_34, monitor_IN_value_35 == monitor_IN_value_34, monitor_IN_reqRead_35 == monitor_IN_reqRead_34, monitor_IN_reqWrite_35 == monitor_IN_reqWrite_34, _SafetyController_0_buffered_status_35 == _SafetyController_0_buffered_status_34, _SafetyController_0_has_data_35 == _SafetyController_0_has_data_34), 
    And(And(Not(False), (monitor_IN_reqRead_34) == (False)), monitor_IN_reqRead_35 == (True), sensor_current_bpm_35 == sensor_current_bpm_34, sensor_OUT_value_35 == sensor_OUT_value_34, sensor_OUT_reqRead_35 == sensor_OUT_reqRead_34, sensor_OUT_reqWrite_35 == sensor_OUT_reqWrite_34, monitor_IN_value_35 == monitor_IN_value_34, monitor_IN_reqWrite_35 == monitor_IN_reqWrite_34, _SafetyController_0_buffered_status_35 == _SafetyController_0_buffered_status_34, _SafetyController_0_has_data_35 == _SafetyController_0_has_data_34), 
    And(And(Not(False), Not((sensor_OUT_reqRead_34) == ((_SafetyController_0_has_data_34) == (0)))), sensor_OUT_reqRead_35 == ((_SafetyController_0_has_data_34) == (0)), sensor_current_bpm_35 == sensor_current_bpm_34, sensor_OUT_value_35 == sensor_OUT_value_34, sensor_OUT_reqWrite_35 == sensor_OUT_reqWrite_34, monitor_IN_value_35 == monitor_IN_value_34, monitor_IN_reqRead_35 == monitor_IN_reqRead_34, monitor_IN_reqWrite_35 == monitor_IN_reqWrite_34, _SafetyController_0_buffered_status_35 == _SafetyController_0_buffered_status_34, _SafetyController_0_has_data_35 == _SafetyController_0_has_data_34), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_34) == ((_SafetyController_0_has_data_34) == (0))))), Not((monitor_IN_reqWrite_34) == (And(monitor_IN_reqRead_34, (_SafetyController_0_has_data_34) == (1))))), monitor_IN_reqWrite_35 == (And(monitor_IN_reqRead_34, (_SafetyController_0_has_data_34) == (1))), sensor_current_bpm_35 == sensor_current_bpm_34, sensor_OUT_value_35 == sensor_OUT_value_34, sensor_OUT_reqRead_35 == sensor_OUT_reqRead_34, sensor_OUT_reqWrite_35 == sensor_OUT_reqWrite_34, monitor_IN_value_35 == monitor_IN_value_34, monitor_IN_reqRead_35 == monitor_IN_reqRead_34, _SafetyController_0_buffered_status_35 == _SafetyController_0_buffered_status_34, _SafetyController_0_has_data_35 == _SafetyController_0_has_data_34), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_34) == (sensor_OUT_reqWrite_34)))), sensor_OUT_reqWrite_34), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_34) == ((_SafetyController_0_has_data_34) == (0)))), Not((monitor_IN_reqWrite_34) == (And(monitor_IN_reqRead_34, (_SafetyController_0_has_data_34) == (1)))))), sensor_OUT_reqRead_34)), _SafetyController_0_buffered_status_35 == (If((sensor_current_bpm_34 > 100), 1, 0)), sensor_current_bpm_35 == (predict_next(sensor_current_bpm_34)), sensor_OUT_reqWrite_35 == (False), _SafetyController_0_has_data_35 == (1), sensor_OUT_reqRead_35 == (False), sensor_OUT_value_35 == (sensor_current_bpm_34), monitor_IN_value_35 == monitor_IN_value_34, monitor_IN_reqRead_35 == monitor_IN_reqRead_34, monitor_IN_reqWrite_35 == monitor_IN_reqWrite_34), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_34) == (False))), monitor_IN_reqWrite_34), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_34) == ((_SafetyController_0_has_data_34) == (0)))), Not((monitor_IN_reqWrite_34) == (And(monitor_IN_reqRead_34, (_SafetyController_0_has_data_34) == (1))))), sensor_OUT_reqRead_34)), monitor_IN_reqWrite_34)), monitor_IN_reqWrite_35 == (False), monitor_IN_value_35 == (_SafetyController_0_buffered_status_34), _SafetyController_0_has_data_35 == (0), monitor_IN_reqRead_35 == (False), sensor_current_bpm_35 == sensor_current_bpm_34, sensor_OUT_value_35 == sensor_OUT_value_34, sensor_OUT_reqRead_35 == sensor_OUT_reqRead_34, sensor_OUT_reqWrite_35 == sensor_OUT_reqWrite_34, _SafetyController_0_buffered_status_35 == _SafetyController_0_buffered_status_34)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_35) == (sensor_OUT_reqWrite_35))), sensor_OUT_reqWrite_36 == (sensor_OUT_reqRead_35), sensor_current_bpm_36 == sensor_current_bpm_35, sensor_OUT_value_36 == sensor_OUT_value_35, sensor_OUT_reqRead_36 == sensor_OUT_reqRead_35, monitor_IN_value_36 == monitor_IN_value_35, monitor_IN_reqRead_36 == monitor_IN_reqRead_35, monitor_IN_reqWrite_36 == monitor_IN_reqWrite_35, _SafetyController_0_buffered_status_36 == _SafetyController_0_buffered_status_35, _SafetyController_0_has_data_36 == _SafetyController_0_has_data_35), 
    And(And(Not(False), (monitor_IN_reqRead_35) == (False)), monitor_IN_reqRead_36 == (True), sensor_current_bpm_36 == sensor_current_bpm_35, sensor_OUT_value_36 == sensor_OUT_value_35, sensor_OUT_reqRead_36 == sensor_OUT_reqRead_35, sensor_OUT_reqWrite_36 == sensor_OUT_reqWrite_35, monitor_IN_value_36 == monitor_IN_value_35, monitor_IN_reqWrite_36 == monitor_IN_reqWrite_35, _SafetyController_0_buffered_status_36 == _SafetyController_0_buffered_status_35, _SafetyController_0_has_data_36 == _SafetyController_0_has_data_35), 
    And(And(Not(False), Not((sensor_OUT_reqRead_35) == ((_SafetyController_0_has_data_35) == (0)))), sensor_OUT_reqRead_36 == ((_SafetyController_0_has_data_35) == (0)), sensor_current_bpm_36 == sensor_current_bpm_35, sensor_OUT_value_36 == sensor_OUT_value_35, sensor_OUT_reqWrite_36 == sensor_OUT_reqWrite_35, monitor_IN_value_36 == monitor_IN_value_35, monitor_IN_reqRead_36 == monitor_IN_reqRead_35, monitor_IN_reqWrite_36 == monitor_IN_reqWrite_35, _SafetyController_0_buffered_status_36 == _SafetyController_0_buffered_status_35, _SafetyController_0_has_data_36 == _SafetyController_0_has_data_35), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_35) == ((_SafetyController_0_has_data_35) == (0))))), Not((monitor_IN_reqWrite_35) == (And(monitor_IN_reqRead_35, (_SafetyController_0_has_data_35) == (1))))), monitor_IN_reqWrite_36 == (And(monitor_IN_reqRead_35, (_SafetyController_0_has_data_35) == (1))), sensor_current_bpm_36 == sensor_current_bpm_35, sensor_OUT_value_36 == sensor_OUT_value_35, sensor_OUT_reqRead_36 == sensor_OUT_reqRead_35, sensor_OUT_reqWrite_36 == sensor_OUT_reqWrite_35, monitor_IN_value_36 == monitor_IN_value_35, monitor_IN_reqRead_36 == monitor_IN_reqRead_35, _SafetyController_0_buffered_status_36 == _SafetyController_0_buffered_status_35, _SafetyController_0_has_data_36 == _SafetyController_0_has_data_35), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_35) == (sensor_OUT_reqWrite_35)))), sensor_OUT_reqWrite_35), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_35) == ((_SafetyController_0_has_data_35) == (0)))), Not((monitor_IN_reqWrite_35) == (And(monitor_IN_reqRead_35, (_SafetyController_0_has_data_35) == (1)))))), sensor_OUT_reqRead_35)), _SafetyController_0_buffered_status_36 == (If((sensor_current_bpm_35 > 100), 1, 0)), sensor_current_bpm_36 == (predict_next(sensor_current_bpm_35)), sensor_OUT_reqWrite_36 == (False), _SafetyController_0_has_data_36 == (1), sensor_OUT_reqRead_36 == (False), sensor_OUT_value_36 == (sensor_current_bpm_35), monitor_IN_value_36 == monitor_IN_value_35, monitor_IN_reqRead_36 == monitor_IN_reqRead_35, monitor_IN_reqWrite_36 == monitor_IN_reqWrite_35), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_35) == (False))), monitor_IN_reqWrite_35), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_35) == ((_SafetyController_0_has_data_35) == (0)))), Not((monitor_IN_reqWrite_35) == (And(monitor_IN_reqRead_35, (_SafetyController_0_has_data_35) == (1))))), sensor_OUT_reqRead_35)), monitor_IN_reqWrite_35)), monitor_IN_reqWrite_36 == (False), monitor_IN_value_36 == (_SafetyController_0_buffered_status_35), _SafetyController_0_has_data_36 == (0), monitor_IN_reqRead_36 == (False), sensor_current_bpm_36 == sensor_current_bpm_35, sensor_OUT_value_36 == sensor_OUT_value_35, sensor_OUT_reqRead_36 == sensor_OUT_reqRead_35, sensor_OUT_reqWrite_36 == sensor_OUT_reqWrite_35, _SafetyController_0_buffered_status_36 == _SafetyController_0_buffered_status_35)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_36) == (sensor_OUT_reqWrite_36))), sensor_OUT_reqWrite_37 == (sensor_OUT_reqRead_36), sensor_current_bpm_37 == sensor_current_bpm_36, sensor_OUT_value_37 == sensor_OUT_value_36, sensor_OUT_reqRead_37 == sensor_OUT_reqRead_36, monitor_IN_value_37 == monitor_IN_value_36, monitor_IN_reqRead_37 == monitor_IN_reqRead_36, monitor_IN_reqWrite_37 == monitor_IN_reqWrite_36, _SafetyController_0_buffered_status_37 == _SafetyController_0_buffered_status_36, _SafetyController_0_has_data_37 == _SafetyController_0_has_data_36), 
    And(And(Not(False), (monitor_IN_reqRead_36) == (False)), monitor_IN_reqRead_37 == (True), sensor_current_bpm_37 == sensor_current_bpm_36, sensor_OUT_value_37 == sensor_OUT_value_36, sensor_OUT_reqRead_37 == sensor_OUT_reqRead_36, sensor_OUT_reqWrite_37 == sensor_OUT_reqWrite_36, monitor_IN_value_37 == monitor_IN_value_36, monitor_IN_reqWrite_37 == monitor_IN_reqWrite_36, _SafetyController_0_buffered_status_37 == _SafetyController_0_buffered_status_36, _SafetyController_0_has_data_37 == _SafetyController_0_has_data_36), 
    And(And(Not(False), Not((sensor_OUT_reqRead_36) == ((_SafetyController_0_has_data_36) == (0)))), sensor_OUT_reqRead_37 == ((_SafetyController_0_has_data_36) == (0)), sensor_current_bpm_37 == sensor_current_bpm_36, sensor_OUT_value_37 == sensor_OUT_value_36, sensor_OUT_reqWrite_37 == sensor_OUT_reqWrite_36, monitor_IN_value_37 == monitor_IN_value_36, monitor_IN_reqRead_37 == monitor_IN_reqRead_36, monitor_IN_reqWrite_37 == monitor_IN_reqWrite_36, _SafetyController_0_buffered_status_37 == _SafetyController_0_buffered_status_36, _SafetyController_0_has_data_37 == _SafetyController_0_has_data_36), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_36) == ((_SafetyController_0_has_data_36) == (0))))), Not((monitor_IN_reqWrite_36) == (And(monitor_IN_reqRead_36, (_SafetyController_0_has_data_36) == (1))))), monitor_IN_reqWrite_37 == (And(monitor_IN_reqRead_36, (_SafetyController_0_has_data_36) == (1))), sensor_current_bpm_37 == sensor_current_bpm_36, sensor_OUT_value_37 == sensor_OUT_value_36, sensor_OUT_reqRead_37 == sensor_OUT_reqRead_36, sensor_OUT_reqWrite_37 == sensor_OUT_reqWrite_36, monitor_IN_value_37 == monitor_IN_value_36, monitor_IN_reqRead_37 == monitor_IN_reqRead_36, _SafetyController_0_buffered_status_37 == _SafetyController_0_buffered_status_36, _SafetyController_0_has_data_37 == _SafetyController_0_has_data_36), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_36) == (sensor_OUT_reqWrite_36)))), sensor_OUT_reqWrite_36), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_36) == ((_SafetyController_0_has_data_36) == (0)))), Not((monitor_IN_reqWrite_36) == (And(monitor_IN_reqRead_36, (_SafetyController_0_has_data_36) == (1)))))), sensor_OUT_reqRead_36)), _SafetyController_0_buffered_status_37 == (If((sensor_current_bpm_36 > 100), 1, 0)), sensor_current_bpm_37 == (predict_next(sensor_current_bpm_36)), sensor_OUT_reqWrite_37 == (False), _SafetyController_0_has_data_37 == (1), sensor_OUT_reqRead_37 == (False), sensor_OUT_value_37 == (sensor_current_bpm_36), monitor_IN_value_37 == monitor_IN_value_36, monitor_IN_reqRead_37 == monitor_IN_reqRead_36, monitor_IN_reqWrite_37 == monitor_IN_reqWrite_36), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_36) == (False))), monitor_IN_reqWrite_36), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_36) == ((_SafetyController_0_has_data_36) == (0)))), Not((monitor_IN_reqWrite_36) == (And(monitor_IN_reqRead_36, (_SafetyController_0_has_data_36) == (1))))), sensor_OUT_reqRead_36)), monitor_IN_reqWrite_36)), monitor_IN_reqWrite_37 == (False), monitor_IN_value_37 == (_SafetyController_0_buffered_status_36), _SafetyController_0_has_data_37 == (0), monitor_IN_reqRead_37 == (False), sensor_current_bpm_37 == sensor_current_bpm_36, sensor_OUT_value_37 == sensor_OUT_value_36, sensor_OUT_reqRead_37 == sensor_OUT_reqRead_36, sensor_OUT_reqWrite_37 == sensor_OUT_reqWrite_36, _SafetyController_0_buffered_status_37 == _SafetyController_0_buffered_status_36)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_37) == (sensor_OUT_reqWrite_37))), sensor_OUT_reqWrite_38 == (sensor_OUT_reqRead_37), sensor_current_bpm_38 == sensor_current_bpm_37, sensor_OUT_value_38 == sensor_OUT_value_37, sensor_OUT_reqRead_38 == sensor_OUT_reqRead_37, monitor_IN_value_38 == monitor_IN_value_37, monitor_IN_reqRead_38 == monitor_IN_reqRead_37, monitor_IN_reqWrite_38 == monitor_IN_reqWrite_37, _SafetyController_0_buffered_status_38 == _SafetyController_0_buffered_status_37, _SafetyController_0_has_data_38 == _SafetyController_0_has_data_37), 
    And(And(Not(False), (monitor_IN_reqRead_37) == (False)), monitor_IN_reqRead_38 == (True), sensor_current_bpm_38 == sensor_current_bpm_37, sensor_OUT_value_38 == sensor_OUT_value_37, sensor_OUT_reqRead_38 == sensor_OUT_reqRead_37, sensor_OUT_reqWrite_38 == sensor_OUT_reqWrite_37, monitor_IN_value_38 == monitor_IN_value_37, monitor_IN_reqWrite_38 == monitor_IN_reqWrite_37, _SafetyController_0_buffered_status_38 == _SafetyController_0_buffered_status_37, _SafetyController_0_has_data_38 == _SafetyController_0_has_data_37), 
    And(And(Not(False), Not((sensor_OUT_reqRead_37) == ((_SafetyController_0_has_data_37) == (0)))), sensor_OUT_reqRead_38 == ((_SafetyController_0_has_data_37) == (0)), sensor_current_bpm_38 == sensor_current_bpm_37, sensor_OUT_value_38 == sensor_OUT_value_37, sensor_OUT_reqWrite_38 == sensor_OUT_reqWrite_37, monitor_IN_value_38 == monitor_IN_value_37, monitor_IN_reqRead_38 == monitor_IN_reqRead_37, monitor_IN_reqWrite_38 == monitor_IN_reqWrite_37, _SafetyController_0_buffered_status_38 == _SafetyController_0_buffered_status_37, _SafetyController_0_has_data_38 == _SafetyController_0_has_data_37), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_37) == ((_SafetyController_0_has_data_37) == (0))))), Not((monitor_IN_reqWrite_37) == (And(monitor_IN_reqRead_37, (_SafetyController_0_has_data_37) == (1))))), monitor_IN_reqWrite_38 == (And(monitor_IN_reqRead_37, (_SafetyController_0_has_data_37) == (1))), sensor_current_bpm_38 == sensor_current_bpm_37, sensor_OUT_value_38 == sensor_OUT_value_37, sensor_OUT_reqRead_38 == sensor_OUT_reqRead_37, sensor_OUT_reqWrite_38 == sensor_OUT_reqWrite_37, monitor_IN_value_38 == monitor_IN_value_37, monitor_IN_reqRead_38 == monitor_IN_reqRead_37, _SafetyController_0_buffered_status_38 == _SafetyController_0_buffered_status_37, _SafetyController_0_has_data_38 == _SafetyController_0_has_data_37), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_37) == (sensor_OUT_reqWrite_37)))), sensor_OUT_reqWrite_37), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_37) == ((_SafetyController_0_has_data_37) == (0)))), Not((monitor_IN_reqWrite_37) == (And(monitor_IN_reqRead_37, (_SafetyController_0_has_data_37) == (1)))))), sensor_OUT_reqRead_37)), _SafetyController_0_buffered_status_38 == (If((sensor_current_bpm_37 > 100), 1, 0)), sensor_current_bpm_38 == (predict_next(sensor_current_bpm_37)), sensor_OUT_reqWrite_38 == (False), _SafetyController_0_has_data_38 == (1), sensor_OUT_reqRead_38 == (False), sensor_OUT_value_38 == (sensor_current_bpm_37), monitor_IN_value_38 == monitor_IN_value_37, monitor_IN_reqRead_38 == monitor_IN_reqRead_37, monitor_IN_reqWrite_38 == monitor_IN_reqWrite_37), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_37) == (False))), monitor_IN_reqWrite_37), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_37) == ((_SafetyController_0_has_data_37) == (0)))), Not((monitor_IN_reqWrite_37) == (And(monitor_IN_reqRead_37, (_SafetyController_0_has_data_37) == (1))))), sensor_OUT_reqRead_37)), monitor_IN_reqWrite_37)), monitor_IN_reqWrite_38 == (False), monitor_IN_value_38 == (_SafetyController_0_buffered_status_37), _SafetyController_0_has_data_38 == (0), monitor_IN_reqRead_38 == (False), sensor_current_bpm_38 == sensor_current_bpm_37, sensor_OUT_value_38 == sensor_OUT_value_37, sensor_OUT_reqRead_38 == sensor_OUT_reqRead_37, sensor_OUT_reqWrite_38 == sensor_OUT_reqWrite_37, _SafetyController_0_buffered_status_38 == _SafetyController_0_buffered_status_37)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_38) == (sensor_OUT_reqWrite_38))), sensor_OUT_reqWrite_39 == (sensor_OUT_reqRead_38), sensor_current_bpm_39 == sensor_current_bpm_38, sensor_OUT_value_39 == sensor_OUT_value_38, sensor_OUT_reqRead_39 == sensor_OUT_reqRead_38, monitor_IN_value_39 == monitor_IN_value_38, monitor_IN_reqRead_39 == monitor_IN_reqRead_38, monitor_IN_reqWrite_39 == monitor_IN_reqWrite_38, _SafetyController_0_buffered_status_39 == _SafetyController_0_buffered_status_38, _SafetyController_0_has_data_39 == _SafetyController_0_has_data_38), 
    And(And(Not(False), (monitor_IN_reqRead_38) == (False)), monitor_IN_reqRead_39 == (True), sensor_current_bpm_39 == sensor_current_bpm_38, sensor_OUT_value_39 == sensor_OUT_value_38, sensor_OUT_reqRead_39 == sensor_OUT_reqRead_38, sensor_OUT_reqWrite_39 == sensor_OUT_reqWrite_38, monitor_IN_value_39 == monitor_IN_value_38, monitor_IN_reqWrite_39 == monitor_IN_reqWrite_38, _SafetyController_0_buffered_status_39 == _SafetyController_0_buffered_status_38, _SafetyController_0_has_data_39 == _SafetyController_0_has_data_38), 
    And(And(Not(False), Not((sensor_OUT_reqRead_38) == ((_SafetyController_0_has_data_38) == (0)))), sensor_OUT_reqRead_39 == ((_SafetyController_0_has_data_38) == (0)), sensor_current_bpm_39 == sensor_current_bpm_38, sensor_OUT_value_39 == sensor_OUT_value_38, sensor_OUT_reqWrite_39 == sensor_OUT_reqWrite_38, monitor_IN_value_39 == monitor_IN_value_38, monitor_IN_reqRead_39 == monitor_IN_reqRead_38, monitor_IN_reqWrite_39 == monitor_IN_reqWrite_38, _SafetyController_0_buffered_status_39 == _SafetyController_0_buffered_status_38, _SafetyController_0_has_data_39 == _SafetyController_0_has_data_38), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_38) == ((_SafetyController_0_has_data_38) == (0))))), Not((monitor_IN_reqWrite_38) == (And(monitor_IN_reqRead_38, (_SafetyController_0_has_data_38) == (1))))), monitor_IN_reqWrite_39 == (And(monitor_IN_reqRead_38, (_SafetyController_0_has_data_38) == (1))), sensor_current_bpm_39 == sensor_current_bpm_38, sensor_OUT_value_39 == sensor_OUT_value_38, sensor_OUT_reqRead_39 == sensor_OUT_reqRead_38, sensor_OUT_reqWrite_39 == sensor_OUT_reqWrite_38, monitor_IN_value_39 == monitor_IN_value_38, monitor_IN_reqRead_39 == monitor_IN_reqRead_38, _SafetyController_0_buffered_status_39 == _SafetyController_0_buffered_status_38, _SafetyController_0_has_data_39 == _SafetyController_0_has_data_38), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_38) == (sensor_OUT_reqWrite_38)))), sensor_OUT_reqWrite_38), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_38) == ((_SafetyController_0_has_data_38) == (0)))), Not((monitor_IN_reqWrite_38) == (And(monitor_IN_reqRead_38, (_SafetyController_0_has_data_38) == (1)))))), sensor_OUT_reqRead_38)), _SafetyController_0_buffered_status_39 == (If((sensor_current_bpm_38 > 100), 1, 0)), sensor_current_bpm_39 == (predict_next(sensor_current_bpm_38)), sensor_OUT_reqWrite_39 == (False), _SafetyController_0_has_data_39 == (1), sensor_OUT_reqRead_39 == (False), sensor_OUT_value_39 == (sensor_current_bpm_38), monitor_IN_value_39 == monitor_IN_value_38, monitor_IN_reqRead_39 == monitor_IN_reqRead_38, monitor_IN_reqWrite_39 == monitor_IN_reqWrite_38), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_38) == (False))), monitor_IN_reqWrite_38), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_38) == ((_SafetyController_0_has_data_38) == (0)))), Not((monitor_IN_reqWrite_38) == (And(monitor_IN_reqRead_38, (_SafetyController_0_has_data_38) == (1))))), sensor_OUT_reqRead_38)), monitor_IN_reqWrite_38)), monitor_IN_reqWrite_39 == (False), monitor_IN_value_39 == (_SafetyController_0_buffered_status_38), _SafetyController_0_has_data_39 == (0), monitor_IN_reqRead_39 == (False), sensor_current_bpm_39 == sensor_current_bpm_38, sensor_OUT_value_39 == sensor_OUT_value_38, sensor_OUT_reqRead_39 == sensor_OUT_reqRead_38, sensor_OUT_reqWrite_39 == sensor_OUT_reqWrite_38, _SafetyController_0_buffered_status_39 == _SafetyController_0_buffered_status_38)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_39) == (sensor_OUT_reqWrite_39))), sensor_OUT_reqWrite_40 == (sensor_OUT_reqRead_39), sensor_current_bpm_40 == sensor_current_bpm_39, sensor_OUT_value_40 == sensor_OUT_value_39, sensor_OUT_reqRead_40 == sensor_OUT_reqRead_39, monitor_IN_value_40 == monitor_IN_value_39, monitor_IN_reqRead_40 == monitor_IN_reqRead_39, monitor_IN_reqWrite_40 == monitor_IN_reqWrite_39, _SafetyController_0_buffered_status_40 == _SafetyController_0_buffered_status_39, _SafetyController_0_has_data_40 == _SafetyController_0_has_data_39), 
    And(And(Not(False), (monitor_IN_reqRead_39) == (False)), monitor_IN_reqRead_40 == (True), sensor_current_bpm_40 == sensor_current_bpm_39, sensor_OUT_value_40 == sensor_OUT_value_39, sensor_OUT_reqRead_40 == sensor_OUT_reqRead_39, sensor_OUT_reqWrite_40 == sensor_OUT_reqWrite_39, monitor_IN_value_40 == monitor_IN_value_39, monitor_IN_reqWrite_40 == monitor_IN_reqWrite_39, _SafetyController_0_buffered_status_40 == _SafetyController_0_buffered_status_39, _SafetyController_0_has_data_40 == _SafetyController_0_has_data_39), 
    And(And(Not(False), Not((sensor_OUT_reqRead_39) == ((_SafetyController_0_has_data_39) == (0)))), sensor_OUT_reqRead_40 == ((_SafetyController_0_has_data_39) == (0)), sensor_current_bpm_40 == sensor_current_bpm_39, sensor_OUT_value_40 == sensor_OUT_value_39, sensor_OUT_reqWrite_40 == sensor_OUT_reqWrite_39, monitor_IN_value_40 == monitor_IN_value_39, monitor_IN_reqRead_40 == monitor_IN_reqRead_39, monitor_IN_reqWrite_40 == monitor_IN_reqWrite_39, _SafetyController_0_buffered_status_40 == _SafetyController_0_buffered_status_39, _SafetyController_0_has_data_40 == _SafetyController_0_has_data_39), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_39) == ((_SafetyController_0_has_data_39) == (0))))), Not((monitor_IN_reqWrite_39) == (And(monitor_IN_reqRead_39, (_SafetyController_0_has_data_39) == (1))))), monitor_IN_reqWrite_40 == (And(monitor_IN_reqRead_39, (_SafetyController_0_has_data_39) == (1))), sensor_current_bpm_40 == sensor_current_bpm_39, sensor_OUT_value_40 == sensor_OUT_value_39, sensor_OUT_reqRead_40 == sensor_OUT_reqRead_39, sensor_OUT_reqWrite_40 == sensor_OUT_reqWrite_39, monitor_IN_value_40 == monitor_IN_value_39, monitor_IN_reqRead_40 == monitor_IN_reqRead_39, _SafetyController_0_buffered_status_40 == _SafetyController_0_buffered_status_39, _SafetyController_0_has_data_40 == _SafetyController_0_has_data_39), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_39) == (sensor_OUT_reqWrite_39)))), sensor_OUT_reqWrite_39), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_39) == ((_SafetyController_0_has_data_39) == (0)))), Not((monitor_IN_reqWrite_39) == (And(monitor_IN_reqRead_39, (_SafetyController_0_has_data_39) == (1)))))), sensor_OUT_reqRead_39)), _SafetyController_0_buffered_status_40 == (If((sensor_current_bpm_39 > 100), 1, 0)), sensor_current_bpm_40 == (predict_next(sensor_current_bpm_39)), sensor_OUT_reqWrite_40 == (False), _SafetyController_0_has_data_40 == (1), sensor_OUT_reqRead_40 == (False), sensor_OUT_value_40 == (sensor_current_bpm_39), monitor_IN_value_40 == monitor_IN_value_39, monitor_IN_reqRead_40 == monitor_IN_reqRead_39, monitor_IN_reqWrite_40 == monitor_IN_reqWrite_39), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_39) == (False))), monitor_IN_reqWrite_39), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_39) == ((_SafetyController_0_has_data_39) == (0)))), Not((monitor_IN_reqWrite_39) == (And(monitor_IN_reqRead_39, (_SafetyController_0_has_data_39) == (1))))), sensor_OUT_reqRead_39)), monitor_IN_reqWrite_39)), monitor_IN_reqWrite_40 == (False), monitor_IN_value_40 == (_SafetyController_0_buffered_status_39), _SafetyController_0_has_data_40 == (0), monitor_IN_reqRead_40 == (False), sensor_current_bpm_40 == sensor_current_bpm_39, sensor_OUT_value_40 == sensor_OUT_value_39, sensor_OUT_reqRead_40 == sensor_OUT_reqRead_39, sensor_OUT_reqWrite_40 == sensor_OUT_reqWrite_39, _SafetyController_0_buffered_status_40 == _SafetyController_0_buffered_status_39)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_40) == (sensor_OUT_reqWrite_40))), sensor_OUT_reqWrite_41 == (sensor_OUT_reqRead_40), sensor_current_bpm_41 == sensor_current_bpm_40, sensor_OUT_value_41 == sensor_OUT_value_40, sensor_OUT_reqRead_41 == sensor_OUT_reqRead_40, monitor_IN_value_41 == monitor_IN_value_40, monitor_IN_reqRead_41 == monitor_IN_reqRead_40, monitor_IN_reqWrite_41 == monitor_IN_reqWrite_40, _SafetyController_0_buffered_status_41 == _SafetyController_0_buffered_status_40, _SafetyController_0_has_data_41 == _SafetyController_0_has_data_40), 
    And(And(Not(False), (monitor_IN_reqRead_40) == (False)), monitor_IN_reqRead_41 == (True), sensor_current_bpm_41 == sensor_current_bpm_40, sensor_OUT_value_41 == sensor_OUT_value_40, sensor_OUT_reqRead_41 == sensor_OUT_reqRead_40, sensor_OUT_reqWrite_41 == sensor_OUT_reqWrite_40, monitor_IN_value_41 == monitor_IN_value_40, monitor_IN_reqWrite_41 == monitor_IN_reqWrite_40, _SafetyController_0_buffered_status_41 == _SafetyController_0_buffered_status_40, _SafetyController_0_has_data_41 == _SafetyController_0_has_data_40), 
    And(And(Not(False), Not((sensor_OUT_reqRead_40) == ((_SafetyController_0_has_data_40) == (0)))), sensor_OUT_reqRead_41 == ((_SafetyController_0_has_data_40) == (0)), sensor_current_bpm_41 == sensor_current_bpm_40, sensor_OUT_value_41 == sensor_OUT_value_40, sensor_OUT_reqWrite_41 == sensor_OUT_reqWrite_40, monitor_IN_value_41 == monitor_IN_value_40, monitor_IN_reqRead_41 == monitor_IN_reqRead_40, monitor_IN_reqWrite_41 == monitor_IN_reqWrite_40, _SafetyController_0_buffered_status_41 == _SafetyController_0_buffered_status_40, _SafetyController_0_has_data_41 == _SafetyController_0_has_data_40), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_40) == ((_SafetyController_0_has_data_40) == (0))))), Not((monitor_IN_reqWrite_40) == (And(monitor_IN_reqRead_40, (_SafetyController_0_has_data_40) == (1))))), monitor_IN_reqWrite_41 == (And(monitor_IN_reqRead_40, (_SafetyController_0_has_data_40) == (1))), sensor_current_bpm_41 == sensor_current_bpm_40, sensor_OUT_value_41 == sensor_OUT_value_40, sensor_OUT_reqRead_41 == sensor_OUT_reqRead_40, sensor_OUT_reqWrite_41 == sensor_OUT_reqWrite_40, monitor_IN_value_41 == monitor_IN_value_40, monitor_IN_reqRead_41 == monitor_IN_reqRead_40, _SafetyController_0_buffered_status_41 == _SafetyController_0_buffered_status_40, _SafetyController_0_has_data_41 == _SafetyController_0_has_data_40), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_40) == (sensor_OUT_reqWrite_40)))), sensor_OUT_reqWrite_40), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_40) == ((_SafetyController_0_has_data_40) == (0)))), Not((monitor_IN_reqWrite_40) == (And(monitor_IN_reqRead_40, (_SafetyController_0_has_data_40) == (1)))))), sensor_OUT_reqRead_40)), _SafetyController_0_buffered_status_41 == (If((sensor_current_bpm_40 > 100), 1, 0)), sensor_current_bpm_41 == (predict_next(sensor_current_bpm_40)), sensor_OUT_reqWrite_41 == (False), _SafetyController_0_has_data_41 == (1), sensor_OUT_reqRead_41 == (False), sensor_OUT_value_41 == (sensor_current_bpm_40), monitor_IN_value_41 == monitor_IN_value_40, monitor_IN_reqRead_41 == monitor_IN_reqRead_40, monitor_IN_reqWrite_41 == monitor_IN_reqWrite_40), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_40) == (False))), monitor_IN_reqWrite_40), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_40) == ((_SafetyController_0_has_data_40) == (0)))), Not((monitor_IN_reqWrite_40) == (And(monitor_IN_reqRead_40, (_SafetyController_0_has_data_40) == (1))))), sensor_OUT_reqRead_40)), monitor_IN_reqWrite_40)), monitor_IN_reqWrite_41 == (False), monitor_IN_value_41 == (_SafetyController_0_buffered_status_40), _SafetyController_0_has_data_41 == (0), monitor_IN_reqRead_41 == (False), sensor_current_bpm_41 == sensor_current_bpm_40, sensor_OUT_value_41 == sensor_OUT_value_40, sensor_OUT_reqRead_41 == sensor_OUT_reqRead_40, sensor_OUT_reqWrite_41 == sensor_OUT_reqWrite_40, _SafetyController_0_buffered_status_41 == _SafetyController_0_buffered_status_40)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_41) == (sensor_OUT_reqWrite_41))), sensor_OUT_reqWrite_42 == (sensor_OUT_reqRead_41), sensor_current_bpm_42 == sensor_current_bpm_41, sensor_OUT_value_42 == sensor_OUT_value_41, sensor_OUT_reqRead_42 == sensor_OUT_reqRead_41, monitor_IN_value_42 == monitor_IN_value_41, monitor_IN_reqRead_42 == monitor_IN_reqRead_41, monitor_IN_reqWrite_42 == monitor_IN_reqWrite_41, _SafetyController_0_buffered_status_42 == _SafetyController_0_buffered_status_41, _SafetyController_0_has_data_42 == _SafetyController_0_has_data_41), 
    And(And(Not(False), (monitor_IN_reqRead_41) == (False)), monitor_IN_reqRead_42 == (True), sensor_current_bpm_42 == sensor_current_bpm_41, sensor_OUT_value_42 == sensor_OUT_value_41, sensor_OUT_reqRead_42 == sensor_OUT_reqRead_41, sensor_OUT_reqWrite_42 == sensor_OUT_reqWrite_41, monitor_IN_value_42 == monitor_IN_value_41, monitor_IN_reqWrite_42 == monitor_IN_reqWrite_41, _SafetyController_0_buffered_status_42 == _SafetyController_0_buffered_status_41, _SafetyController_0_has_data_42 == _SafetyController_0_has_data_41), 
    And(And(Not(False), Not((sensor_OUT_reqRead_41) == ((_SafetyController_0_has_data_41) == (0)))), sensor_OUT_reqRead_42 == ((_SafetyController_0_has_data_41) == (0)), sensor_current_bpm_42 == sensor_current_bpm_41, sensor_OUT_value_42 == sensor_OUT_value_41, sensor_OUT_reqWrite_42 == sensor_OUT_reqWrite_41, monitor_IN_value_42 == monitor_IN_value_41, monitor_IN_reqRead_42 == monitor_IN_reqRead_41, monitor_IN_reqWrite_42 == monitor_IN_reqWrite_41, _SafetyController_0_buffered_status_42 == _SafetyController_0_buffered_status_41, _SafetyController_0_has_data_42 == _SafetyController_0_has_data_41), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_41) == ((_SafetyController_0_has_data_41) == (0))))), Not((monitor_IN_reqWrite_41) == (And(monitor_IN_reqRead_41, (_SafetyController_0_has_data_41) == (1))))), monitor_IN_reqWrite_42 == (And(monitor_IN_reqRead_41, (_SafetyController_0_has_data_41) == (1))), sensor_current_bpm_42 == sensor_current_bpm_41, sensor_OUT_value_42 == sensor_OUT_value_41, sensor_OUT_reqRead_42 == sensor_OUT_reqRead_41, sensor_OUT_reqWrite_42 == sensor_OUT_reqWrite_41, monitor_IN_value_42 == monitor_IN_value_41, monitor_IN_reqRead_42 == monitor_IN_reqRead_41, _SafetyController_0_buffered_status_42 == _SafetyController_0_buffered_status_41, _SafetyController_0_has_data_42 == _SafetyController_0_has_data_41), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_41) == (sensor_OUT_reqWrite_41)))), sensor_OUT_reqWrite_41), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_41) == ((_SafetyController_0_has_data_41) == (0)))), Not((monitor_IN_reqWrite_41) == (And(monitor_IN_reqRead_41, (_SafetyController_0_has_data_41) == (1)))))), sensor_OUT_reqRead_41)), _SafetyController_0_buffered_status_42 == (If((sensor_current_bpm_41 > 100), 1, 0)), sensor_current_bpm_42 == (predict_next(sensor_current_bpm_41)), sensor_OUT_reqWrite_42 == (False), _SafetyController_0_has_data_42 == (1), sensor_OUT_reqRead_42 == (False), sensor_OUT_value_42 == (sensor_current_bpm_41), monitor_IN_value_42 == monitor_IN_value_41, monitor_IN_reqRead_42 == monitor_IN_reqRead_41, monitor_IN_reqWrite_42 == monitor_IN_reqWrite_41), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_41) == (False))), monitor_IN_reqWrite_41), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_41) == ((_SafetyController_0_has_data_41) == (0)))), Not((monitor_IN_reqWrite_41) == (And(monitor_IN_reqRead_41, (_SafetyController_0_has_data_41) == (1))))), sensor_OUT_reqRead_41)), monitor_IN_reqWrite_41)), monitor_IN_reqWrite_42 == (False), monitor_IN_value_42 == (_SafetyController_0_buffered_status_41), _SafetyController_0_has_data_42 == (0), monitor_IN_reqRead_42 == (False), sensor_current_bpm_42 == sensor_current_bpm_41, sensor_OUT_value_42 == sensor_OUT_value_41, sensor_OUT_reqRead_42 == sensor_OUT_reqRead_41, sensor_OUT_reqWrite_42 == sensor_OUT_reqWrite_41, _SafetyController_0_buffered_status_42 == _SafetyController_0_buffered_status_41)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_42) == (sensor_OUT_reqWrite_42))), sensor_OUT_reqWrite_43 == (sensor_OUT_reqRead_42), sensor_current_bpm_43 == sensor_current_bpm_42, sensor_OUT_value_43 == sensor_OUT_value_42, sensor_OUT_reqRead_43 == sensor_OUT_reqRead_42, monitor_IN_value_43 == monitor_IN_value_42, monitor_IN_reqRead_43 == monitor_IN_reqRead_42, monitor_IN_reqWrite_43 == monitor_IN_reqWrite_42, _SafetyController_0_buffered_status_43 == _SafetyController_0_buffered_status_42, _SafetyController_0_has_data_43 == _SafetyController_0_has_data_42), 
    And(And(Not(False), (monitor_IN_reqRead_42) == (False)), monitor_IN_reqRead_43 == (True), sensor_current_bpm_43 == sensor_current_bpm_42, sensor_OUT_value_43 == sensor_OUT_value_42, sensor_OUT_reqRead_43 == sensor_OUT_reqRead_42, sensor_OUT_reqWrite_43 == sensor_OUT_reqWrite_42, monitor_IN_value_43 == monitor_IN_value_42, monitor_IN_reqWrite_43 == monitor_IN_reqWrite_42, _SafetyController_0_buffered_status_43 == _SafetyController_0_buffered_status_42, _SafetyController_0_has_data_43 == _SafetyController_0_has_data_42), 
    And(And(Not(False), Not((sensor_OUT_reqRead_42) == ((_SafetyController_0_has_data_42) == (0)))), sensor_OUT_reqRead_43 == ((_SafetyController_0_has_data_42) == (0)), sensor_current_bpm_43 == sensor_current_bpm_42, sensor_OUT_value_43 == sensor_OUT_value_42, sensor_OUT_reqWrite_43 == sensor_OUT_reqWrite_42, monitor_IN_value_43 == monitor_IN_value_42, monitor_IN_reqRead_43 == monitor_IN_reqRead_42, monitor_IN_reqWrite_43 == monitor_IN_reqWrite_42, _SafetyController_0_buffered_status_43 == _SafetyController_0_buffered_status_42, _SafetyController_0_has_data_43 == _SafetyController_0_has_data_42), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_42) == ((_SafetyController_0_has_data_42) == (0))))), Not((monitor_IN_reqWrite_42) == (And(monitor_IN_reqRead_42, (_SafetyController_0_has_data_42) == (1))))), monitor_IN_reqWrite_43 == (And(monitor_IN_reqRead_42, (_SafetyController_0_has_data_42) == (1))), sensor_current_bpm_43 == sensor_current_bpm_42, sensor_OUT_value_43 == sensor_OUT_value_42, sensor_OUT_reqRead_43 == sensor_OUT_reqRead_42, sensor_OUT_reqWrite_43 == sensor_OUT_reqWrite_42, monitor_IN_value_43 == monitor_IN_value_42, monitor_IN_reqRead_43 == monitor_IN_reqRead_42, _SafetyController_0_buffered_status_43 == _SafetyController_0_buffered_status_42, _SafetyController_0_has_data_43 == _SafetyController_0_has_data_42), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_42) == (sensor_OUT_reqWrite_42)))), sensor_OUT_reqWrite_42), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_42) == ((_SafetyController_0_has_data_42) == (0)))), Not((monitor_IN_reqWrite_42) == (And(monitor_IN_reqRead_42, (_SafetyController_0_has_data_42) == (1)))))), sensor_OUT_reqRead_42)), _SafetyController_0_buffered_status_43 == (If((sensor_current_bpm_42 > 100), 1, 0)), sensor_current_bpm_43 == (predict_next(sensor_current_bpm_42)), sensor_OUT_reqWrite_43 == (False), _SafetyController_0_has_data_43 == (1), sensor_OUT_reqRead_43 == (False), sensor_OUT_value_43 == (sensor_current_bpm_42), monitor_IN_value_43 == monitor_IN_value_42, monitor_IN_reqRead_43 == monitor_IN_reqRead_42, monitor_IN_reqWrite_43 == monitor_IN_reqWrite_42), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_42) == (False))), monitor_IN_reqWrite_42), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_42) == ((_SafetyController_0_has_data_42) == (0)))), Not((monitor_IN_reqWrite_42) == (And(monitor_IN_reqRead_42, (_SafetyController_0_has_data_42) == (1))))), sensor_OUT_reqRead_42)), monitor_IN_reqWrite_42)), monitor_IN_reqWrite_43 == (False), monitor_IN_value_43 == (_SafetyController_0_buffered_status_42), _SafetyController_0_has_data_43 == (0), monitor_IN_reqRead_43 == (False), sensor_current_bpm_43 == sensor_current_bpm_42, sensor_OUT_value_43 == sensor_OUT_value_42, sensor_OUT_reqRead_43 == sensor_OUT_reqRead_42, sensor_OUT_reqWrite_43 == sensor_OUT_reqWrite_42, _SafetyController_0_buffered_status_43 == _SafetyController_0_buffered_status_42)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_43) == (sensor_OUT_reqWrite_43))), sensor_OUT_reqWrite_44 == (sensor_OUT_reqRead_43), sensor_current_bpm_44 == sensor_current_bpm_43, sensor_OUT_value_44 == sensor_OUT_value_43, sensor_OUT_reqRead_44 == sensor_OUT_reqRead_43, monitor_IN_value_44 == monitor_IN_value_43, monitor_IN_reqRead_44 == monitor_IN_reqRead_43, monitor_IN_reqWrite_44 == monitor_IN_reqWrite_43, _SafetyController_0_buffered_status_44 == _SafetyController_0_buffered_status_43, _SafetyController_0_has_data_44 == _SafetyController_0_has_data_43), 
    And(And(Not(False), (monitor_IN_reqRead_43) == (False)), monitor_IN_reqRead_44 == (True), sensor_current_bpm_44 == sensor_current_bpm_43, sensor_OUT_value_44 == sensor_OUT_value_43, sensor_OUT_reqRead_44 == sensor_OUT_reqRead_43, sensor_OUT_reqWrite_44 == sensor_OUT_reqWrite_43, monitor_IN_value_44 == monitor_IN_value_43, monitor_IN_reqWrite_44 == monitor_IN_reqWrite_43, _SafetyController_0_buffered_status_44 == _SafetyController_0_buffered_status_43, _SafetyController_0_has_data_44 == _SafetyController_0_has_data_43), 
    And(And(Not(False), Not((sensor_OUT_reqRead_43) == ((_SafetyController_0_has_data_43) == (0)))), sensor_OUT_reqRead_44 == ((_SafetyController_0_has_data_43) == (0)), sensor_current_bpm_44 == sensor_current_bpm_43, sensor_OUT_value_44 == sensor_OUT_value_43, sensor_OUT_reqWrite_44 == sensor_OUT_reqWrite_43, monitor_IN_value_44 == monitor_IN_value_43, monitor_IN_reqRead_44 == monitor_IN_reqRead_43, monitor_IN_reqWrite_44 == monitor_IN_reqWrite_43, _SafetyController_0_buffered_status_44 == _SafetyController_0_buffered_status_43, _SafetyController_0_has_data_44 == _SafetyController_0_has_data_43), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_43) == ((_SafetyController_0_has_data_43) == (0))))), Not((monitor_IN_reqWrite_43) == (And(monitor_IN_reqRead_43, (_SafetyController_0_has_data_43) == (1))))), monitor_IN_reqWrite_44 == (And(monitor_IN_reqRead_43, (_SafetyController_0_has_data_43) == (1))), sensor_current_bpm_44 == sensor_current_bpm_43, sensor_OUT_value_44 == sensor_OUT_value_43, sensor_OUT_reqRead_44 == sensor_OUT_reqRead_43, sensor_OUT_reqWrite_44 == sensor_OUT_reqWrite_43, monitor_IN_value_44 == monitor_IN_value_43, monitor_IN_reqRead_44 == monitor_IN_reqRead_43, _SafetyController_0_buffered_status_44 == _SafetyController_0_buffered_status_43, _SafetyController_0_has_data_44 == _SafetyController_0_has_data_43), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_43) == (sensor_OUT_reqWrite_43)))), sensor_OUT_reqWrite_43), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_43) == ((_SafetyController_0_has_data_43) == (0)))), Not((monitor_IN_reqWrite_43) == (And(monitor_IN_reqRead_43, (_SafetyController_0_has_data_43) == (1)))))), sensor_OUT_reqRead_43)), _SafetyController_0_buffered_status_44 == (If((sensor_current_bpm_43 > 100), 1, 0)), sensor_current_bpm_44 == (predict_next(sensor_current_bpm_43)), sensor_OUT_reqWrite_44 == (False), _SafetyController_0_has_data_44 == (1), sensor_OUT_reqRead_44 == (False), sensor_OUT_value_44 == (sensor_current_bpm_43), monitor_IN_value_44 == monitor_IN_value_43, monitor_IN_reqRead_44 == monitor_IN_reqRead_43, monitor_IN_reqWrite_44 == monitor_IN_reqWrite_43), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_43) == (False))), monitor_IN_reqWrite_43), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_43) == ((_SafetyController_0_has_data_43) == (0)))), Not((monitor_IN_reqWrite_43) == (And(monitor_IN_reqRead_43, (_SafetyController_0_has_data_43) == (1))))), sensor_OUT_reqRead_43)), monitor_IN_reqWrite_43)), monitor_IN_reqWrite_44 == (False), monitor_IN_value_44 == (_SafetyController_0_buffered_status_43), _SafetyController_0_has_data_44 == (0), monitor_IN_reqRead_44 == (False), sensor_current_bpm_44 == sensor_current_bpm_43, sensor_OUT_value_44 == sensor_OUT_value_43, sensor_OUT_reqRead_44 == sensor_OUT_reqRead_43, sensor_OUT_reqWrite_44 == sensor_OUT_reqWrite_43, _SafetyController_0_buffered_status_44 == _SafetyController_0_buffered_status_43)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_44) == (sensor_OUT_reqWrite_44))), sensor_OUT_reqWrite_45 == (sensor_OUT_reqRead_44), sensor_current_bpm_45 == sensor_current_bpm_44, sensor_OUT_value_45 == sensor_OUT_value_44, sensor_OUT_reqRead_45 == sensor_OUT_reqRead_44, monitor_IN_value_45 == monitor_IN_value_44, monitor_IN_reqRead_45 == monitor_IN_reqRead_44, monitor_IN_reqWrite_45 == monitor_IN_reqWrite_44, _SafetyController_0_buffered_status_45 == _SafetyController_0_buffered_status_44, _SafetyController_0_has_data_45 == _SafetyController_0_has_data_44), 
    And(And(Not(False), (monitor_IN_reqRead_44) == (False)), monitor_IN_reqRead_45 == (True), sensor_current_bpm_45 == sensor_current_bpm_44, sensor_OUT_value_45 == sensor_OUT_value_44, sensor_OUT_reqRead_45 == sensor_OUT_reqRead_44, sensor_OUT_reqWrite_45 == sensor_OUT_reqWrite_44, monitor_IN_value_45 == monitor_IN_value_44, monitor_IN_reqWrite_45 == monitor_IN_reqWrite_44, _SafetyController_0_buffered_status_45 == _SafetyController_0_buffered_status_44, _SafetyController_0_has_data_45 == _SafetyController_0_has_data_44), 
    And(And(Not(False), Not((sensor_OUT_reqRead_44) == ((_SafetyController_0_has_data_44) == (0)))), sensor_OUT_reqRead_45 == ((_SafetyController_0_has_data_44) == (0)), sensor_current_bpm_45 == sensor_current_bpm_44, sensor_OUT_value_45 == sensor_OUT_value_44, sensor_OUT_reqWrite_45 == sensor_OUT_reqWrite_44, monitor_IN_value_45 == monitor_IN_value_44, monitor_IN_reqRead_45 == monitor_IN_reqRead_44, monitor_IN_reqWrite_45 == monitor_IN_reqWrite_44, _SafetyController_0_buffered_status_45 == _SafetyController_0_buffered_status_44, _SafetyController_0_has_data_45 == _SafetyController_0_has_data_44), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_44) == ((_SafetyController_0_has_data_44) == (0))))), Not((monitor_IN_reqWrite_44) == (And(monitor_IN_reqRead_44, (_SafetyController_0_has_data_44) == (1))))), monitor_IN_reqWrite_45 == (And(monitor_IN_reqRead_44, (_SafetyController_0_has_data_44) == (1))), sensor_current_bpm_45 == sensor_current_bpm_44, sensor_OUT_value_45 == sensor_OUT_value_44, sensor_OUT_reqRead_45 == sensor_OUT_reqRead_44, sensor_OUT_reqWrite_45 == sensor_OUT_reqWrite_44, monitor_IN_value_45 == monitor_IN_value_44, monitor_IN_reqRead_45 == monitor_IN_reqRead_44, _SafetyController_0_buffered_status_45 == _SafetyController_0_buffered_status_44, _SafetyController_0_has_data_45 == _SafetyController_0_has_data_44), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_44) == (sensor_OUT_reqWrite_44)))), sensor_OUT_reqWrite_44), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_44) == ((_SafetyController_0_has_data_44) == (0)))), Not((monitor_IN_reqWrite_44) == (And(monitor_IN_reqRead_44, (_SafetyController_0_has_data_44) == (1)))))), sensor_OUT_reqRead_44)), _SafetyController_0_buffered_status_45 == (If((sensor_current_bpm_44 > 100), 1, 0)), sensor_current_bpm_45 == (predict_next(sensor_current_bpm_44)), sensor_OUT_reqWrite_45 == (False), _SafetyController_0_has_data_45 == (1), sensor_OUT_reqRead_45 == (False), sensor_OUT_value_45 == (sensor_current_bpm_44), monitor_IN_value_45 == monitor_IN_value_44, monitor_IN_reqRead_45 == monitor_IN_reqRead_44, monitor_IN_reqWrite_45 == monitor_IN_reqWrite_44), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_44) == (False))), monitor_IN_reqWrite_44), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_44) == ((_SafetyController_0_has_data_44) == (0)))), Not((monitor_IN_reqWrite_44) == (And(monitor_IN_reqRead_44, (_SafetyController_0_has_data_44) == (1))))), sensor_OUT_reqRead_44)), monitor_IN_reqWrite_44)), monitor_IN_reqWrite_45 == (False), monitor_IN_value_45 == (_SafetyController_0_buffered_status_44), _SafetyController_0_has_data_45 == (0), monitor_IN_reqRead_45 == (False), sensor_current_bpm_45 == sensor_current_bpm_44, sensor_OUT_value_45 == sensor_OUT_value_44, sensor_OUT_reqRead_45 == sensor_OUT_reqRead_44, sensor_OUT_reqWrite_45 == sensor_OUT_reqWrite_44, _SafetyController_0_buffered_status_45 == _SafetyController_0_buffered_status_44)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_45) == (sensor_OUT_reqWrite_45))), sensor_OUT_reqWrite_46 == (sensor_OUT_reqRead_45), sensor_current_bpm_46 == sensor_current_bpm_45, sensor_OUT_value_46 == sensor_OUT_value_45, sensor_OUT_reqRead_46 == sensor_OUT_reqRead_45, monitor_IN_value_46 == monitor_IN_value_45, monitor_IN_reqRead_46 == monitor_IN_reqRead_45, monitor_IN_reqWrite_46 == monitor_IN_reqWrite_45, _SafetyController_0_buffered_status_46 == _SafetyController_0_buffered_status_45, _SafetyController_0_has_data_46 == _SafetyController_0_has_data_45), 
    And(And(Not(False), (monitor_IN_reqRead_45) == (False)), monitor_IN_reqRead_46 == (True), sensor_current_bpm_46 == sensor_current_bpm_45, sensor_OUT_value_46 == sensor_OUT_value_45, sensor_OUT_reqRead_46 == sensor_OUT_reqRead_45, sensor_OUT_reqWrite_46 == sensor_OUT_reqWrite_45, monitor_IN_value_46 == monitor_IN_value_45, monitor_IN_reqWrite_46 == monitor_IN_reqWrite_45, _SafetyController_0_buffered_status_46 == _SafetyController_0_buffered_status_45, _SafetyController_0_has_data_46 == _SafetyController_0_has_data_45), 
    And(And(Not(False), Not((sensor_OUT_reqRead_45) == ((_SafetyController_0_has_data_45) == (0)))), sensor_OUT_reqRead_46 == ((_SafetyController_0_has_data_45) == (0)), sensor_current_bpm_46 == sensor_current_bpm_45, sensor_OUT_value_46 == sensor_OUT_value_45, sensor_OUT_reqWrite_46 == sensor_OUT_reqWrite_45, monitor_IN_value_46 == monitor_IN_value_45, monitor_IN_reqRead_46 == monitor_IN_reqRead_45, monitor_IN_reqWrite_46 == monitor_IN_reqWrite_45, _SafetyController_0_buffered_status_46 == _SafetyController_0_buffered_status_45, _SafetyController_0_has_data_46 == _SafetyController_0_has_data_45), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_45) == ((_SafetyController_0_has_data_45) == (0))))), Not((monitor_IN_reqWrite_45) == (And(monitor_IN_reqRead_45, (_SafetyController_0_has_data_45) == (1))))), monitor_IN_reqWrite_46 == (And(monitor_IN_reqRead_45, (_SafetyController_0_has_data_45) == (1))), sensor_current_bpm_46 == sensor_current_bpm_45, sensor_OUT_value_46 == sensor_OUT_value_45, sensor_OUT_reqRead_46 == sensor_OUT_reqRead_45, sensor_OUT_reqWrite_46 == sensor_OUT_reqWrite_45, monitor_IN_value_46 == monitor_IN_value_45, monitor_IN_reqRead_46 == monitor_IN_reqRead_45, _SafetyController_0_buffered_status_46 == _SafetyController_0_buffered_status_45, _SafetyController_0_has_data_46 == _SafetyController_0_has_data_45), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_45) == (sensor_OUT_reqWrite_45)))), sensor_OUT_reqWrite_45), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_45) == ((_SafetyController_0_has_data_45) == (0)))), Not((monitor_IN_reqWrite_45) == (And(monitor_IN_reqRead_45, (_SafetyController_0_has_data_45) == (1)))))), sensor_OUT_reqRead_45)), _SafetyController_0_buffered_status_46 == (If((sensor_current_bpm_45 > 100), 1, 0)), sensor_current_bpm_46 == (predict_next(sensor_current_bpm_45)), sensor_OUT_reqWrite_46 == (False), _SafetyController_0_has_data_46 == (1), sensor_OUT_reqRead_46 == (False), sensor_OUT_value_46 == (sensor_current_bpm_45), monitor_IN_value_46 == monitor_IN_value_45, monitor_IN_reqRead_46 == monitor_IN_reqRead_45, monitor_IN_reqWrite_46 == monitor_IN_reqWrite_45), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_45) == (False))), monitor_IN_reqWrite_45), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_45) == ((_SafetyController_0_has_data_45) == (0)))), Not((monitor_IN_reqWrite_45) == (And(monitor_IN_reqRead_45, (_SafetyController_0_has_data_45) == (1))))), sensor_OUT_reqRead_45)), monitor_IN_reqWrite_45)), monitor_IN_reqWrite_46 == (False), monitor_IN_value_46 == (_SafetyController_0_buffered_status_45), _SafetyController_0_has_data_46 == (0), monitor_IN_reqRead_46 == (False), sensor_current_bpm_46 == sensor_current_bpm_45, sensor_OUT_value_46 == sensor_OUT_value_45, sensor_OUT_reqRead_46 == sensor_OUT_reqRead_45, sensor_OUT_reqWrite_46 == sensor_OUT_reqWrite_45, _SafetyController_0_buffered_status_46 == _SafetyController_0_buffered_status_45)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_46) == (sensor_OUT_reqWrite_46))), sensor_OUT_reqWrite_47 == (sensor_OUT_reqRead_46), sensor_current_bpm_47 == sensor_current_bpm_46, sensor_OUT_value_47 == sensor_OUT_value_46, sensor_OUT_reqRead_47 == sensor_OUT_reqRead_46, monitor_IN_value_47 == monitor_IN_value_46, monitor_IN_reqRead_47 == monitor_IN_reqRead_46, monitor_IN_reqWrite_47 == monitor_IN_reqWrite_46, _SafetyController_0_buffered_status_47 == _SafetyController_0_buffered_status_46, _SafetyController_0_has_data_47 == _SafetyController_0_has_data_46), 
    And(And(Not(False), (monitor_IN_reqRead_46) == (False)), monitor_IN_reqRead_47 == (True), sensor_current_bpm_47 == sensor_current_bpm_46, sensor_OUT_value_47 == sensor_OUT_value_46, sensor_OUT_reqRead_47 == sensor_OUT_reqRead_46, sensor_OUT_reqWrite_47 == sensor_OUT_reqWrite_46, monitor_IN_value_47 == monitor_IN_value_46, monitor_IN_reqWrite_47 == monitor_IN_reqWrite_46, _SafetyController_0_buffered_status_47 == _SafetyController_0_buffered_status_46, _SafetyController_0_has_data_47 == _SafetyController_0_has_data_46), 
    And(And(Not(False), Not((sensor_OUT_reqRead_46) == ((_SafetyController_0_has_data_46) == (0)))), sensor_OUT_reqRead_47 == ((_SafetyController_0_has_data_46) == (0)), sensor_current_bpm_47 == sensor_current_bpm_46, sensor_OUT_value_47 == sensor_OUT_value_46, sensor_OUT_reqWrite_47 == sensor_OUT_reqWrite_46, monitor_IN_value_47 == monitor_IN_value_46, monitor_IN_reqRead_47 == monitor_IN_reqRead_46, monitor_IN_reqWrite_47 == monitor_IN_reqWrite_46, _SafetyController_0_buffered_status_47 == _SafetyController_0_buffered_status_46, _SafetyController_0_has_data_47 == _SafetyController_0_has_data_46), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_46) == ((_SafetyController_0_has_data_46) == (0))))), Not((monitor_IN_reqWrite_46) == (And(monitor_IN_reqRead_46, (_SafetyController_0_has_data_46) == (1))))), monitor_IN_reqWrite_47 == (And(monitor_IN_reqRead_46, (_SafetyController_0_has_data_46) == (1))), sensor_current_bpm_47 == sensor_current_bpm_46, sensor_OUT_value_47 == sensor_OUT_value_46, sensor_OUT_reqRead_47 == sensor_OUT_reqRead_46, sensor_OUT_reqWrite_47 == sensor_OUT_reqWrite_46, monitor_IN_value_47 == monitor_IN_value_46, monitor_IN_reqRead_47 == monitor_IN_reqRead_46, _SafetyController_0_buffered_status_47 == _SafetyController_0_buffered_status_46, _SafetyController_0_has_data_47 == _SafetyController_0_has_data_46), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_46) == (sensor_OUT_reqWrite_46)))), sensor_OUT_reqWrite_46), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_46) == ((_SafetyController_0_has_data_46) == (0)))), Not((monitor_IN_reqWrite_46) == (And(monitor_IN_reqRead_46, (_SafetyController_0_has_data_46) == (1)))))), sensor_OUT_reqRead_46)), _SafetyController_0_buffered_status_47 == (If((sensor_current_bpm_46 > 100), 1, 0)), sensor_current_bpm_47 == (predict_next(sensor_current_bpm_46)), sensor_OUT_reqWrite_47 == (False), _SafetyController_0_has_data_47 == (1), sensor_OUT_reqRead_47 == (False), sensor_OUT_value_47 == (sensor_current_bpm_46), monitor_IN_value_47 == monitor_IN_value_46, monitor_IN_reqRead_47 == monitor_IN_reqRead_46, monitor_IN_reqWrite_47 == monitor_IN_reqWrite_46), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_46) == (False))), monitor_IN_reqWrite_46), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_46) == ((_SafetyController_0_has_data_46) == (0)))), Not((monitor_IN_reqWrite_46) == (And(monitor_IN_reqRead_46, (_SafetyController_0_has_data_46) == (1))))), sensor_OUT_reqRead_46)), monitor_IN_reqWrite_46)), monitor_IN_reqWrite_47 == (False), monitor_IN_value_47 == (_SafetyController_0_buffered_status_46), _SafetyController_0_has_data_47 == (0), monitor_IN_reqRead_47 == (False), sensor_current_bpm_47 == sensor_current_bpm_46, sensor_OUT_value_47 == sensor_OUT_value_46, sensor_OUT_reqRead_47 == sensor_OUT_reqRead_46, sensor_OUT_reqWrite_47 == sensor_OUT_reqWrite_46, _SafetyController_0_buffered_status_47 == _SafetyController_0_buffered_status_46)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_47) == (sensor_OUT_reqWrite_47))), sensor_OUT_reqWrite_48 == (sensor_OUT_reqRead_47), sensor_current_bpm_48 == sensor_current_bpm_47, sensor_OUT_value_48 == sensor_OUT_value_47, sensor_OUT_reqRead_48 == sensor_OUT_reqRead_47, monitor_IN_value_48 == monitor_IN_value_47, monitor_IN_reqRead_48 == monitor_IN_reqRead_47, monitor_IN_reqWrite_48 == monitor_IN_reqWrite_47, _SafetyController_0_buffered_status_48 == _SafetyController_0_buffered_status_47, _SafetyController_0_has_data_48 == _SafetyController_0_has_data_47), 
    And(And(Not(False), (monitor_IN_reqRead_47) == (False)), monitor_IN_reqRead_48 == (True), sensor_current_bpm_48 == sensor_current_bpm_47, sensor_OUT_value_48 == sensor_OUT_value_47, sensor_OUT_reqRead_48 == sensor_OUT_reqRead_47, sensor_OUT_reqWrite_48 == sensor_OUT_reqWrite_47, monitor_IN_value_48 == monitor_IN_value_47, monitor_IN_reqWrite_48 == monitor_IN_reqWrite_47, _SafetyController_0_buffered_status_48 == _SafetyController_0_buffered_status_47, _SafetyController_0_has_data_48 == _SafetyController_0_has_data_47), 
    And(And(Not(False), Not((sensor_OUT_reqRead_47) == ((_SafetyController_0_has_data_47) == (0)))), sensor_OUT_reqRead_48 == ((_SafetyController_0_has_data_47) == (0)), sensor_current_bpm_48 == sensor_current_bpm_47, sensor_OUT_value_48 == sensor_OUT_value_47, sensor_OUT_reqWrite_48 == sensor_OUT_reqWrite_47, monitor_IN_value_48 == monitor_IN_value_47, monitor_IN_reqRead_48 == monitor_IN_reqRead_47, monitor_IN_reqWrite_48 == monitor_IN_reqWrite_47, _SafetyController_0_buffered_status_48 == _SafetyController_0_buffered_status_47, _SafetyController_0_has_data_48 == _SafetyController_0_has_data_47), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_47) == ((_SafetyController_0_has_data_47) == (0))))), Not((monitor_IN_reqWrite_47) == (And(monitor_IN_reqRead_47, (_SafetyController_0_has_data_47) == (1))))), monitor_IN_reqWrite_48 == (And(monitor_IN_reqRead_47, (_SafetyController_0_has_data_47) == (1))), sensor_current_bpm_48 == sensor_current_bpm_47, sensor_OUT_value_48 == sensor_OUT_value_47, sensor_OUT_reqRead_48 == sensor_OUT_reqRead_47, sensor_OUT_reqWrite_48 == sensor_OUT_reqWrite_47, monitor_IN_value_48 == monitor_IN_value_47, monitor_IN_reqRead_48 == monitor_IN_reqRead_47, _SafetyController_0_buffered_status_48 == _SafetyController_0_buffered_status_47, _SafetyController_0_has_data_48 == _SafetyController_0_has_data_47), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_47) == (sensor_OUT_reqWrite_47)))), sensor_OUT_reqWrite_47), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_47) == ((_SafetyController_0_has_data_47) == (0)))), Not((monitor_IN_reqWrite_47) == (And(monitor_IN_reqRead_47, (_SafetyController_0_has_data_47) == (1)))))), sensor_OUT_reqRead_47)), _SafetyController_0_buffered_status_48 == (If((sensor_current_bpm_47 > 100), 1, 0)), sensor_current_bpm_48 == (predict_next(sensor_current_bpm_47)), sensor_OUT_reqWrite_48 == (False), _SafetyController_0_has_data_48 == (1), sensor_OUT_reqRead_48 == (False), sensor_OUT_value_48 == (sensor_current_bpm_47), monitor_IN_value_48 == monitor_IN_value_47, monitor_IN_reqRead_48 == monitor_IN_reqRead_47, monitor_IN_reqWrite_48 == monitor_IN_reqWrite_47), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_47) == (False))), monitor_IN_reqWrite_47), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_47) == ((_SafetyController_0_has_data_47) == (0)))), Not((monitor_IN_reqWrite_47) == (And(monitor_IN_reqRead_47, (_SafetyController_0_has_data_47) == (1))))), sensor_OUT_reqRead_47)), monitor_IN_reqWrite_47)), monitor_IN_reqWrite_48 == (False), monitor_IN_value_48 == (_SafetyController_0_buffered_status_47), _SafetyController_0_has_data_48 == (0), monitor_IN_reqRead_48 == (False), sensor_current_bpm_48 == sensor_current_bpm_47, sensor_OUT_value_48 == sensor_OUT_value_47, sensor_OUT_reqRead_48 == sensor_OUT_reqRead_47, sensor_OUT_reqWrite_48 == sensor_OUT_reqWrite_47, _SafetyController_0_buffered_status_48 == _SafetyController_0_buffered_status_47)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_48) == (sensor_OUT_reqWrite_48))), sensor_OUT_reqWrite_49 == (sensor_OUT_reqRead_48), sensor_current_bpm_49 == sensor_current_bpm_48, sensor_OUT_value_49 == sensor_OUT_value_48, sensor_OUT_reqRead_49 == sensor_OUT_reqRead_48, monitor_IN_value_49 == monitor_IN_value_48, monitor_IN_reqRead_49 == monitor_IN_reqRead_48, monitor_IN_reqWrite_49 == monitor_IN_reqWrite_48, _SafetyController_0_buffered_status_49 == _SafetyController_0_buffered_status_48, _SafetyController_0_has_data_49 == _SafetyController_0_has_data_48), 
    And(And(Not(False), (monitor_IN_reqRead_48) == (False)), monitor_IN_reqRead_49 == (True), sensor_current_bpm_49 == sensor_current_bpm_48, sensor_OUT_value_49 == sensor_OUT_value_48, sensor_OUT_reqRead_49 == sensor_OUT_reqRead_48, sensor_OUT_reqWrite_49 == sensor_OUT_reqWrite_48, monitor_IN_value_49 == monitor_IN_value_48, monitor_IN_reqWrite_49 == monitor_IN_reqWrite_48, _SafetyController_0_buffered_status_49 == _SafetyController_0_buffered_status_48, _SafetyController_0_has_data_49 == _SafetyController_0_has_data_48), 
    And(And(Not(False), Not((sensor_OUT_reqRead_48) == ((_SafetyController_0_has_data_48) == (0)))), sensor_OUT_reqRead_49 == ((_SafetyController_0_has_data_48) == (0)), sensor_current_bpm_49 == sensor_current_bpm_48, sensor_OUT_value_49 == sensor_OUT_value_48, sensor_OUT_reqWrite_49 == sensor_OUT_reqWrite_48, monitor_IN_value_49 == monitor_IN_value_48, monitor_IN_reqRead_49 == monitor_IN_reqRead_48, monitor_IN_reqWrite_49 == monitor_IN_reqWrite_48, _SafetyController_0_buffered_status_49 == _SafetyController_0_buffered_status_48, _SafetyController_0_has_data_49 == _SafetyController_0_has_data_48), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_48) == ((_SafetyController_0_has_data_48) == (0))))), Not((monitor_IN_reqWrite_48) == (And(monitor_IN_reqRead_48, (_SafetyController_0_has_data_48) == (1))))), monitor_IN_reqWrite_49 == (And(monitor_IN_reqRead_48, (_SafetyController_0_has_data_48) == (1))), sensor_current_bpm_49 == sensor_current_bpm_48, sensor_OUT_value_49 == sensor_OUT_value_48, sensor_OUT_reqRead_49 == sensor_OUT_reqRead_48, sensor_OUT_reqWrite_49 == sensor_OUT_reqWrite_48, monitor_IN_value_49 == monitor_IN_value_48, monitor_IN_reqRead_49 == monitor_IN_reqRead_48, _SafetyController_0_buffered_status_49 == _SafetyController_0_buffered_status_48, _SafetyController_0_has_data_49 == _SafetyController_0_has_data_48), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_48) == (sensor_OUT_reqWrite_48)))), sensor_OUT_reqWrite_48), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_48) == ((_SafetyController_0_has_data_48) == (0)))), Not((monitor_IN_reqWrite_48) == (And(monitor_IN_reqRead_48, (_SafetyController_0_has_data_48) == (1)))))), sensor_OUT_reqRead_48)), _SafetyController_0_buffered_status_49 == (If((sensor_current_bpm_48 > 100), 1, 0)), sensor_current_bpm_49 == (predict_next(sensor_current_bpm_48)), sensor_OUT_reqWrite_49 == (False), _SafetyController_0_has_data_49 == (1), sensor_OUT_reqRead_49 == (False), sensor_OUT_value_49 == (sensor_current_bpm_48), monitor_IN_value_49 == monitor_IN_value_48, monitor_IN_reqRead_49 == monitor_IN_reqRead_48, monitor_IN_reqWrite_49 == monitor_IN_reqWrite_48), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_48) == (False))), monitor_IN_reqWrite_48), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_48) == ((_SafetyController_0_has_data_48) == (0)))), Not((monitor_IN_reqWrite_48) == (And(monitor_IN_reqRead_48, (_SafetyController_0_has_data_48) == (1))))), sensor_OUT_reqRead_48)), monitor_IN_reqWrite_48)), monitor_IN_reqWrite_49 == (False), monitor_IN_value_49 == (_SafetyController_0_buffered_status_48), _SafetyController_0_has_data_49 == (0), monitor_IN_reqRead_49 == (False), sensor_current_bpm_49 == sensor_current_bpm_48, sensor_OUT_value_49 == sensor_OUT_value_48, sensor_OUT_reqRead_49 == sensor_OUT_reqRead_48, sensor_OUT_reqWrite_49 == sensor_OUT_reqWrite_48, _SafetyController_0_buffered_status_49 == _SafetyController_0_buffered_status_48)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_49) == (sensor_OUT_reqWrite_49))), sensor_OUT_reqWrite_50 == (sensor_OUT_reqRead_49), sensor_current_bpm_50 == sensor_current_bpm_49, sensor_OUT_value_50 == sensor_OUT_value_49, sensor_OUT_reqRead_50 == sensor_OUT_reqRead_49, monitor_IN_value_50 == monitor_IN_value_49, monitor_IN_reqRead_50 == monitor_IN_reqRead_49, monitor_IN_reqWrite_50 == monitor_IN_reqWrite_49, _SafetyController_0_buffered_status_50 == _SafetyController_0_buffered_status_49, _SafetyController_0_has_data_50 == _SafetyController_0_has_data_49), 
    And(And(Not(False), (monitor_IN_reqRead_49) == (False)), monitor_IN_reqRead_50 == (True), sensor_current_bpm_50 == sensor_current_bpm_49, sensor_OUT_value_50 == sensor_OUT_value_49, sensor_OUT_reqRead_50 == sensor_OUT_reqRead_49, sensor_OUT_reqWrite_50 == sensor_OUT_reqWrite_49, monitor_IN_value_50 == monitor_IN_value_49, monitor_IN_reqWrite_50 == monitor_IN_reqWrite_49, _SafetyController_0_buffered_status_50 == _SafetyController_0_buffered_status_49, _SafetyController_0_has_data_50 == _SafetyController_0_has_data_49), 
    And(And(Not(False), Not((sensor_OUT_reqRead_49) == ((_SafetyController_0_has_data_49) == (0)))), sensor_OUT_reqRead_50 == ((_SafetyController_0_has_data_49) == (0)), sensor_current_bpm_50 == sensor_current_bpm_49, sensor_OUT_value_50 == sensor_OUT_value_49, sensor_OUT_reqWrite_50 == sensor_OUT_reqWrite_49, monitor_IN_value_50 == monitor_IN_value_49, monitor_IN_reqRead_50 == monitor_IN_reqRead_49, monitor_IN_reqWrite_50 == monitor_IN_reqWrite_49, _SafetyController_0_buffered_status_50 == _SafetyController_0_buffered_status_49, _SafetyController_0_has_data_50 == _SafetyController_0_has_data_49), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_49) == ((_SafetyController_0_has_data_49) == (0))))), Not((monitor_IN_reqWrite_49) == (And(monitor_IN_reqRead_49, (_SafetyController_0_has_data_49) == (1))))), monitor_IN_reqWrite_50 == (And(monitor_IN_reqRead_49, (_SafetyController_0_has_data_49) == (1))), sensor_current_bpm_50 == sensor_current_bpm_49, sensor_OUT_value_50 == sensor_OUT_value_49, sensor_OUT_reqRead_50 == sensor_OUT_reqRead_49, sensor_OUT_reqWrite_50 == sensor_OUT_reqWrite_49, monitor_IN_value_50 == monitor_IN_value_49, monitor_IN_reqRead_50 == monitor_IN_reqRead_49, _SafetyController_0_buffered_status_50 == _SafetyController_0_buffered_status_49, _SafetyController_0_has_data_50 == _SafetyController_0_has_data_49), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_49) == (sensor_OUT_reqWrite_49)))), sensor_OUT_reqWrite_49), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_49) == ((_SafetyController_0_has_data_49) == (0)))), Not((monitor_IN_reqWrite_49) == (And(monitor_IN_reqRead_49, (_SafetyController_0_has_data_49) == (1)))))), sensor_OUT_reqRead_49)), _SafetyController_0_buffered_status_50 == (If((sensor_current_bpm_49 > 100), 1, 0)), sensor_current_bpm_50 == (predict_next(sensor_current_bpm_49)), sensor_OUT_reqWrite_50 == (False), _SafetyController_0_has_data_50 == (1), sensor_OUT_reqRead_50 == (False), sensor_OUT_value_50 == (sensor_current_bpm_49), monitor_IN_value_50 == monitor_IN_value_49, monitor_IN_reqRead_50 == monitor_IN_reqRead_49, monitor_IN_reqWrite_50 == monitor_IN_reqWrite_49), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_49) == (False))), monitor_IN_reqWrite_49), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_49) == ((_SafetyController_0_has_data_49) == (0)))), Not((monitor_IN_reqWrite_49) == (And(monitor_IN_reqRead_49, (_SafetyController_0_has_data_49) == (1))))), sensor_OUT_reqRead_49)), monitor_IN_reqWrite_49)), monitor_IN_reqWrite_50 == (False), monitor_IN_value_50 == (_SafetyController_0_buffered_status_49), _SafetyController_0_has_data_50 == (0), monitor_IN_reqRead_50 == (False), sensor_current_bpm_50 == sensor_current_bpm_49, sensor_OUT_value_50 == sensor_OUT_value_49, sensor_OUT_reqRead_50 == sensor_OUT_reqRead_49, sensor_OUT_reqWrite_50 == sensor_OUT_reqWrite_49, _SafetyController_0_buffered_status_50 == _SafetyController_0_buffered_status_49)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_50) == (sensor_OUT_reqWrite_50))), sensor_OUT_reqWrite_51 == (sensor_OUT_reqRead_50), sensor_current_bpm_51 == sensor_current_bpm_50, sensor_OUT_value_51 == sensor_OUT_value_50, sensor_OUT_reqRead_51 == sensor_OUT_reqRead_50, monitor_IN_value_51 == monitor_IN_value_50, monitor_IN_reqRead_51 == monitor_IN_reqRead_50, monitor_IN_reqWrite_51 == monitor_IN_reqWrite_50, _SafetyController_0_buffered_status_51 == _SafetyController_0_buffered_status_50, _SafetyController_0_has_data_51 == _SafetyController_0_has_data_50), 
    And(And(Not(False), (monitor_IN_reqRead_50) == (False)), monitor_IN_reqRead_51 == (True), sensor_current_bpm_51 == sensor_current_bpm_50, sensor_OUT_value_51 == sensor_OUT_value_50, sensor_OUT_reqRead_51 == sensor_OUT_reqRead_50, sensor_OUT_reqWrite_51 == sensor_OUT_reqWrite_50, monitor_IN_value_51 == monitor_IN_value_50, monitor_IN_reqWrite_51 == monitor_IN_reqWrite_50, _SafetyController_0_buffered_status_51 == _SafetyController_0_buffered_status_50, _SafetyController_0_has_data_51 == _SafetyController_0_has_data_50), 
    And(And(Not(False), Not((sensor_OUT_reqRead_50) == ((_SafetyController_0_has_data_50) == (0)))), sensor_OUT_reqRead_51 == ((_SafetyController_0_has_data_50) == (0)), sensor_current_bpm_51 == sensor_current_bpm_50, sensor_OUT_value_51 == sensor_OUT_value_50, sensor_OUT_reqWrite_51 == sensor_OUT_reqWrite_50, monitor_IN_value_51 == monitor_IN_value_50, monitor_IN_reqRead_51 == monitor_IN_reqRead_50, monitor_IN_reqWrite_51 == monitor_IN_reqWrite_50, _SafetyController_0_buffered_status_51 == _SafetyController_0_buffered_status_50, _SafetyController_0_has_data_51 == _SafetyController_0_has_data_50), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_50) == ((_SafetyController_0_has_data_50) == (0))))), Not((monitor_IN_reqWrite_50) == (And(monitor_IN_reqRead_50, (_SafetyController_0_has_data_50) == (1))))), monitor_IN_reqWrite_51 == (And(monitor_IN_reqRead_50, (_SafetyController_0_has_data_50) == (1))), sensor_current_bpm_51 == sensor_current_bpm_50, sensor_OUT_value_51 == sensor_OUT_value_50, sensor_OUT_reqRead_51 == sensor_OUT_reqRead_50, sensor_OUT_reqWrite_51 == sensor_OUT_reqWrite_50, monitor_IN_value_51 == monitor_IN_value_50, monitor_IN_reqRead_51 == monitor_IN_reqRead_50, _SafetyController_0_buffered_status_51 == _SafetyController_0_buffered_status_50, _SafetyController_0_has_data_51 == _SafetyController_0_has_data_50), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_50) == (sensor_OUT_reqWrite_50)))), sensor_OUT_reqWrite_50), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_50) == ((_SafetyController_0_has_data_50) == (0)))), Not((monitor_IN_reqWrite_50) == (And(monitor_IN_reqRead_50, (_SafetyController_0_has_data_50) == (1)))))), sensor_OUT_reqRead_50)), _SafetyController_0_buffered_status_51 == (If((sensor_current_bpm_50 > 100), 1, 0)), sensor_current_bpm_51 == (predict_next(sensor_current_bpm_50)), sensor_OUT_reqWrite_51 == (False), _SafetyController_0_has_data_51 == (1), sensor_OUT_reqRead_51 == (False), sensor_OUT_value_51 == (sensor_current_bpm_50), monitor_IN_value_51 == monitor_IN_value_50, monitor_IN_reqRead_51 == monitor_IN_reqRead_50, monitor_IN_reqWrite_51 == monitor_IN_reqWrite_50), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_50) == (False))), monitor_IN_reqWrite_50), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_50) == ((_SafetyController_0_has_data_50) == (0)))), Not((monitor_IN_reqWrite_50) == (And(monitor_IN_reqRead_50, (_SafetyController_0_has_data_50) == (1))))), sensor_OUT_reqRead_50)), monitor_IN_reqWrite_50)), monitor_IN_reqWrite_51 == (False), monitor_IN_value_51 == (_SafetyController_0_buffered_status_50), _SafetyController_0_has_data_51 == (0), monitor_IN_reqRead_51 == (False), sensor_current_bpm_51 == sensor_current_bpm_50, sensor_OUT_value_51 == sensor_OUT_value_50, sensor_OUT_reqRead_51 == sensor_OUT_reqRead_50, sensor_OUT_reqWrite_51 == sensor_OUT_reqWrite_50, _SafetyController_0_buffered_status_51 == _SafetyController_0_buffered_status_50)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_51) == (sensor_OUT_reqWrite_51))), sensor_OUT_reqWrite_52 == (sensor_OUT_reqRead_51), sensor_current_bpm_52 == sensor_current_bpm_51, sensor_OUT_value_52 == sensor_OUT_value_51, sensor_OUT_reqRead_52 == sensor_OUT_reqRead_51, monitor_IN_value_52 == monitor_IN_value_51, monitor_IN_reqRead_52 == monitor_IN_reqRead_51, monitor_IN_reqWrite_52 == monitor_IN_reqWrite_51, _SafetyController_0_buffered_status_52 == _SafetyController_0_buffered_status_51, _SafetyController_0_has_data_52 == _SafetyController_0_has_data_51), 
    And(And(Not(False), (monitor_IN_reqRead_51) == (False)), monitor_IN_reqRead_52 == (True), sensor_current_bpm_52 == sensor_current_bpm_51, sensor_OUT_value_52 == sensor_OUT_value_51, sensor_OUT_reqRead_52 == sensor_OUT_reqRead_51, sensor_OUT_reqWrite_52 == sensor_OUT_reqWrite_51, monitor_IN_value_52 == monitor_IN_value_51, monitor_IN_reqWrite_52 == monitor_IN_reqWrite_51, _SafetyController_0_buffered_status_52 == _SafetyController_0_buffered_status_51, _SafetyController_0_has_data_52 == _SafetyController_0_has_data_51), 
    And(And(Not(False), Not((sensor_OUT_reqRead_51) == ((_SafetyController_0_has_data_51) == (0)))), sensor_OUT_reqRead_52 == ((_SafetyController_0_has_data_51) == (0)), sensor_current_bpm_52 == sensor_current_bpm_51, sensor_OUT_value_52 == sensor_OUT_value_51, sensor_OUT_reqWrite_52 == sensor_OUT_reqWrite_51, monitor_IN_value_52 == monitor_IN_value_51, monitor_IN_reqRead_52 == monitor_IN_reqRead_51, monitor_IN_reqWrite_52 == monitor_IN_reqWrite_51, _SafetyController_0_buffered_status_52 == _SafetyController_0_buffered_status_51, _SafetyController_0_has_data_52 == _SafetyController_0_has_data_51), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_51) == ((_SafetyController_0_has_data_51) == (0))))), Not((monitor_IN_reqWrite_51) == (And(monitor_IN_reqRead_51, (_SafetyController_0_has_data_51) == (1))))), monitor_IN_reqWrite_52 == (And(monitor_IN_reqRead_51, (_SafetyController_0_has_data_51) == (1))), sensor_current_bpm_52 == sensor_current_bpm_51, sensor_OUT_value_52 == sensor_OUT_value_51, sensor_OUT_reqRead_52 == sensor_OUT_reqRead_51, sensor_OUT_reqWrite_52 == sensor_OUT_reqWrite_51, monitor_IN_value_52 == monitor_IN_value_51, monitor_IN_reqRead_52 == monitor_IN_reqRead_51, _SafetyController_0_buffered_status_52 == _SafetyController_0_buffered_status_51, _SafetyController_0_has_data_52 == _SafetyController_0_has_data_51), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_51) == (sensor_OUT_reqWrite_51)))), sensor_OUT_reqWrite_51), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_51) == ((_SafetyController_0_has_data_51) == (0)))), Not((monitor_IN_reqWrite_51) == (And(monitor_IN_reqRead_51, (_SafetyController_0_has_data_51) == (1)))))), sensor_OUT_reqRead_51)), _SafetyController_0_buffered_status_52 == (If((sensor_current_bpm_51 > 100), 1, 0)), sensor_current_bpm_52 == (predict_next(sensor_current_bpm_51)), sensor_OUT_reqWrite_52 == (False), _SafetyController_0_has_data_52 == (1), sensor_OUT_reqRead_52 == (False), sensor_OUT_value_52 == (sensor_current_bpm_51), monitor_IN_value_52 == monitor_IN_value_51, monitor_IN_reqRead_52 == monitor_IN_reqRead_51, monitor_IN_reqWrite_52 == monitor_IN_reqWrite_51), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_51) == (False))), monitor_IN_reqWrite_51), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_51) == ((_SafetyController_0_has_data_51) == (0)))), Not((monitor_IN_reqWrite_51) == (And(monitor_IN_reqRead_51, (_SafetyController_0_has_data_51) == (1))))), sensor_OUT_reqRead_51)), monitor_IN_reqWrite_51)), monitor_IN_reqWrite_52 == (False), monitor_IN_value_52 == (_SafetyController_0_buffered_status_51), _SafetyController_0_has_data_52 == (0), monitor_IN_reqRead_52 == (False), sensor_current_bpm_52 == sensor_current_bpm_51, sensor_OUT_value_52 == sensor_OUT_value_51, sensor_OUT_reqRead_52 == sensor_OUT_reqRead_51, sensor_OUT_reqWrite_52 == sensor_OUT_reqWrite_51, _SafetyController_0_buffered_status_52 == _SafetyController_0_buffered_status_51)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_52) == (sensor_OUT_reqWrite_52))), sensor_OUT_reqWrite_53 == (sensor_OUT_reqRead_52), sensor_current_bpm_53 == sensor_current_bpm_52, sensor_OUT_value_53 == sensor_OUT_value_52, sensor_OUT_reqRead_53 == sensor_OUT_reqRead_52, monitor_IN_value_53 == monitor_IN_value_52, monitor_IN_reqRead_53 == monitor_IN_reqRead_52, monitor_IN_reqWrite_53 == monitor_IN_reqWrite_52, _SafetyController_0_buffered_status_53 == _SafetyController_0_buffered_status_52, _SafetyController_0_has_data_53 == _SafetyController_0_has_data_52), 
    And(And(Not(False), (monitor_IN_reqRead_52) == (False)), monitor_IN_reqRead_53 == (True), sensor_current_bpm_53 == sensor_current_bpm_52, sensor_OUT_value_53 == sensor_OUT_value_52, sensor_OUT_reqRead_53 == sensor_OUT_reqRead_52, sensor_OUT_reqWrite_53 == sensor_OUT_reqWrite_52, monitor_IN_value_53 == monitor_IN_value_52, monitor_IN_reqWrite_53 == monitor_IN_reqWrite_52, _SafetyController_0_buffered_status_53 == _SafetyController_0_buffered_status_52, _SafetyController_0_has_data_53 == _SafetyController_0_has_data_52), 
    And(And(Not(False), Not((sensor_OUT_reqRead_52) == ((_SafetyController_0_has_data_52) == (0)))), sensor_OUT_reqRead_53 == ((_SafetyController_0_has_data_52) == (0)), sensor_current_bpm_53 == sensor_current_bpm_52, sensor_OUT_value_53 == sensor_OUT_value_52, sensor_OUT_reqWrite_53 == sensor_OUT_reqWrite_52, monitor_IN_value_53 == monitor_IN_value_52, monitor_IN_reqRead_53 == monitor_IN_reqRead_52, monitor_IN_reqWrite_53 == monitor_IN_reqWrite_52, _SafetyController_0_buffered_status_53 == _SafetyController_0_buffered_status_52, _SafetyController_0_has_data_53 == _SafetyController_0_has_data_52), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_52) == ((_SafetyController_0_has_data_52) == (0))))), Not((monitor_IN_reqWrite_52) == (And(monitor_IN_reqRead_52, (_SafetyController_0_has_data_52) == (1))))), monitor_IN_reqWrite_53 == (And(monitor_IN_reqRead_52, (_SafetyController_0_has_data_52) == (1))), sensor_current_bpm_53 == sensor_current_bpm_52, sensor_OUT_value_53 == sensor_OUT_value_52, sensor_OUT_reqRead_53 == sensor_OUT_reqRead_52, sensor_OUT_reqWrite_53 == sensor_OUT_reqWrite_52, monitor_IN_value_53 == monitor_IN_value_52, monitor_IN_reqRead_53 == monitor_IN_reqRead_52, _SafetyController_0_buffered_status_53 == _SafetyController_0_buffered_status_52, _SafetyController_0_has_data_53 == _SafetyController_0_has_data_52), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_52) == (sensor_OUT_reqWrite_52)))), sensor_OUT_reqWrite_52), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_52) == ((_SafetyController_0_has_data_52) == (0)))), Not((monitor_IN_reqWrite_52) == (And(monitor_IN_reqRead_52, (_SafetyController_0_has_data_52) == (1)))))), sensor_OUT_reqRead_52)), _SafetyController_0_buffered_status_53 == (If((sensor_current_bpm_52 > 100), 1, 0)), sensor_current_bpm_53 == (predict_next(sensor_current_bpm_52)), sensor_OUT_reqWrite_53 == (False), _SafetyController_0_has_data_53 == (1), sensor_OUT_reqRead_53 == (False), sensor_OUT_value_53 == (sensor_current_bpm_52), monitor_IN_value_53 == monitor_IN_value_52, monitor_IN_reqRead_53 == monitor_IN_reqRead_52, monitor_IN_reqWrite_53 == monitor_IN_reqWrite_52), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_52) == (False))), monitor_IN_reqWrite_52), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_52) == ((_SafetyController_0_has_data_52) == (0)))), Not((monitor_IN_reqWrite_52) == (And(monitor_IN_reqRead_52, (_SafetyController_0_has_data_52) == (1))))), sensor_OUT_reqRead_52)), monitor_IN_reqWrite_52)), monitor_IN_reqWrite_53 == (False), monitor_IN_value_53 == (_SafetyController_0_buffered_status_52), _SafetyController_0_has_data_53 == (0), monitor_IN_reqRead_53 == (False), sensor_current_bpm_53 == sensor_current_bpm_52, sensor_OUT_value_53 == sensor_OUT_value_52, sensor_OUT_reqRead_53 == sensor_OUT_reqRead_52, sensor_OUT_reqWrite_53 == sensor_OUT_reqWrite_52, _SafetyController_0_buffered_status_53 == _SafetyController_0_buffered_status_52)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_53) == (sensor_OUT_reqWrite_53))), sensor_OUT_reqWrite_54 == (sensor_OUT_reqRead_53), sensor_current_bpm_54 == sensor_current_bpm_53, sensor_OUT_value_54 == sensor_OUT_value_53, sensor_OUT_reqRead_54 == sensor_OUT_reqRead_53, monitor_IN_value_54 == monitor_IN_value_53, monitor_IN_reqRead_54 == monitor_IN_reqRead_53, monitor_IN_reqWrite_54 == monitor_IN_reqWrite_53, _SafetyController_0_buffered_status_54 == _SafetyController_0_buffered_status_53, _SafetyController_0_has_data_54 == _SafetyController_0_has_data_53), 
    And(And(Not(False), (monitor_IN_reqRead_53) == (False)), monitor_IN_reqRead_54 == (True), sensor_current_bpm_54 == sensor_current_bpm_53, sensor_OUT_value_54 == sensor_OUT_value_53, sensor_OUT_reqRead_54 == sensor_OUT_reqRead_53, sensor_OUT_reqWrite_54 == sensor_OUT_reqWrite_53, monitor_IN_value_54 == monitor_IN_value_53, monitor_IN_reqWrite_54 == monitor_IN_reqWrite_53, _SafetyController_0_buffered_status_54 == _SafetyController_0_buffered_status_53, _SafetyController_0_has_data_54 == _SafetyController_0_has_data_53), 
    And(And(Not(False), Not((sensor_OUT_reqRead_53) == ((_SafetyController_0_has_data_53) == (0)))), sensor_OUT_reqRead_54 == ((_SafetyController_0_has_data_53) == (0)), sensor_current_bpm_54 == sensor_current_bpm_53, sensor_OUT_value_54 == sensor_OUT_value_53, sensor_OUT_reqWrite_54 == sensor_OUT_reqWrite_53, monitor_IN_value_54 == monitor_IN_value_53, monitor_IN_reqRead_54 == monitor_IN_reqRead_53, monitor_IN_reqWrite_54 == monitor_IN_reqWrite_53, _SafetyController_0_buffered_status_54 == _SafetyController_0_buffered_status_53, _SafetyController_0_has_data_54 == _SafetyController_0_has_data_53), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_53) == ((_SafetyController_0_has_data_53) == (0))))), Not((monitor_IN_reqWrite_53) == (And(monitor_IN_reqRead_53, (_SafetyController_0_has_data_53) == (1))))), monitor_IN_reqWrite_54 == (And(monitor_IN_reqRead_53, (_SafetyController_0_has_data_53) == (1))), sensor_current_bpm_54 == sensor_current_bpm_53, sensor_OUT_value_54 == sensor_OUT_value_53, sensor_OUT_reqRead_54 == sensor_OUT_reqRead_53, sensor_OUT_reqWrite_54 == sensor_OUT_reqWrite_53, monitor_IN_value_54 == monitor_IN_value_53, monitor_IN_reqRead_54 == monitor_IN_reqRead_53, _SafetyController_0_buffered_status_54 == _SafetyController_0_buffered_status_53, _SafetyController_0_has_data_54 == _SafetyController_0_has_data_53), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_53) == (sensor_OUT_reqWrite_53)))), sensor_OUT_reqWrite_53), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_53) == ((_SafetyController_0_has_data_53) == (0)))), Not((monitor_IN_reqWrite_53) == (And(monitor_IN_reqRead_53, (_SafetyController_0_has_data_53) == (1)))))), sensor_OUT_reqRead_53)), _SafetyController_0_buffered_status_54 == (If((sensor_current_bpm_53 > 100), 1, 0)), sensor_current_bpm_54 == (predict_next(sensor_current_bpm_53)), sensor_OUT_reqWrite_54 == (False), _SafetyController_0_has_data_54 == (1), sensor_OUT_reqRead_54 == (False), sensor_OUT_value_54 == (sensor_current_bpm_53), monitor_IN_value_54 == monitor_IN_value_53, monitor_IN_reqRead_54 == monitor_IN_reqRead_53, monitor_IN_reqWrite_54 == monitor_IN_reqWrite_53), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_53) == (False))), monitor_IN_reqWrite_53), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_53) == ((_SafetyController_0_has_data_53) == (0)))), Not((monitor_IN_reqWrite_53) == (And(monitor_IN_reqRead_53, (_SafetyController_0_has_data_53) == (1))))), sensor_OUT_reqRead_53)), monitor_IN_reqWrite_53)), monitor_IN_reqWrite_54 == (False), monitor_IN_value_54 == (_SafetyController_0_buffered_status_53), _SafetyController_0_has_data_54 == (0), monitor_IN_reqRead_54 == (False), sensor_current_bpm_54 == sensor_current_bpm_53, sensor_OUT_value_54 == sensor_OUT_value_53, sensor_OUT_reqRead_54 == sensor_OUT_reqRead_53, sensor_OUT_reqWrite_54 == sensor_OUT_reqWrite_53, _SafetyController_0_buffered_status_54 == _SafetyController_0_buffered_status_53)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_54) == (sensor_OUT_reqWrite_54))), sensor_OUT_reqWrite_55 == (sensor_OUT_reqRead_54), sensor_current_bpm_55 == sensor_current_bpm_54, sensor_OUT_value_55 == sensor_OUT_value_54, sensor_OUT_reqRead_55 == sensor_OUT_reqRead_54, monitor_IN_value_55 == monitor_IN_value_54, monitor_IN_reqRead_55 == monitor_IN_reqRead_54, monitor_IN_reqWrite_55 == monitor_IN_reqWrite_54, _SafetyController_0_buffered_status_55 == _SafetyController_0_buffered_status_54, _SafetyController_0_has_data_55 == _SafetyController_0_has_data_54), 
    And(And(Not(False), (monitor_IN_reqRead_54) == (False)), monitor_IN_reqRead_55 == (True), sensor_current_bpm_55 == sensor_current_bpm_54, sensor_OUT_value_55 == sensor_OUT_value_54, sensor_OUT_reqRead_55 == sensor_OUT_reqRead_54, sensor_OUT_reqWrite_55 == sensor_OUT_reqWrite_54, monitor_IN_value_55 == monitor_IN_value_54, monitor_IN_reqWrite_55 == monitor_IN_reqWrite_54, _SafetyController_0_buffered_status_55 == _SafetyController_0_buffered_status_54, _SafetyController_0_has_data_55 == _SafetyController_0_has_data_54), 
    And(And(Not(False), Not((sensor_OUT_reqRead_54) == ((_SafetyController_0_has_data_54) == (0)))), sensor_OUT_reqRead_55 == ((_SafetyController_0_has_data_54) == (0)), sensor_current_bpm_55 == sensor_current_bpm_54, sensor_OUT_value_55 == sensor_OUT_value_54, sensor_OUT_reqWrite_55 == sensor_OUT_reqWrite_54, monitor_IN_value_55 == monitor_IN_value_54, monitor_IN_reqRead_55 == monitor_IN_reqRead_54, monitor_IN_reqWrite_55 == monitor_IN_reqWrite_54, _SafetyController_0_buffered_status_55 == _SafetyController_0_buffered_status_54, _SafetyController_0_has_data_55 == _SafetyController_0_has_data_54), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_54) == ((_SafetyController_0_has_data_54) == (0))))), Not((monitor_IN_reqWrite_54) == (And(monitor_IN_reqRead_54, (_SafetyController_0_has_data_54) == (1))))), monitor_IN_reqWrite_55 == (And(monitor_IN_reqRead_54, (_SafetyController_0_has_data_54) == (1))), sensor_current_bpm_55 == sensor_current_bpm_54, sensor_OUT_value_55 == sensor_OUT_value_54, sensor_OUT_reqRead_55 == sensor_OUT_reqRead_54, sensor_OUT_reqWrite_55 == sensor_OUT_reqWrite_54, monitor_IN_value_55 == monitor_IN_value_54, monitor_IN_reqRead_55 == monitor_IN_reqRead_54, _SafetyController_0_buffered_status_55 == _SafetyController_0_buffered_status_54, _SafetyController_0_has_data_55 == _SafetyController_0_has_data_54), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_54) == (sensor_OUT_reqWrite_54)))), sensor_OUT_reqWrite_54), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_54) == ((_SafetyController_0_has_data_54) == (0)))), Not((monitor_IN_reqWrite_54) == (And(monitor_IN_reqRead_54, (_SafetyController_0_has_data_54) == (1)))))), sensor_OUT_reqRead_54)), _SafetyController_0_buffered_status_55 == (If((sensor_current_bpm_54 > 100), 1, 0)), sensor_current_bpm_55 == (predict_next(sensor_current_bpm_54)), sensor_OUT_reqWrite_55 == (False), _SafetyController_0_has_data_55 == (1), sensor_OUT_reqRead_55 == (False), sensor_OUT_value_55 == (sensor_current_bpm_54), monitor_IN_value_55 == monitor_IN_value_54, monitor_IN_reqRead_55 == monitor_IN_reqRead_54, monitor_IN_reqWrite_55 == monitor_IN_reqWrite_54), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_54) == (False))), monitor_IN_reqWrite_54), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_54) == ((_SafetyController_0_has_data_54) == (0)))), Not((monitor_IN_reqWrite_54) == (And(monitor_IN_reqRead_54, (_SafetyController_0_has_data_54) == (1))))), sensor_OUT_reqRead_54)), monitor_IN_reqWrite_54)), monitor_IN_reqWrite_55 == (False), monitor_IN_value_55 == (_SafetyController_0_buffered_status_54), _SafetyController_0_has_data_55 == (0), monitor_IN_reqRead_55 == (False), sensor_current_bpm_55 == sensor_current_bpm_54, sensor_OUT_value_55 == sensor_OUT_value_54, sensor_OUT_reqRead_55 == sensor_OUT_reqRead_54, sensor_OUT_reqWrite_55 == sensor_OUT_reqWrite_54, _SafetyController_0_buffered_status_55 == _SafetyController_0_buffered_status_54)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_55) == (sensor_OUT_reqWrite_55))), sensor_OUT_reqWrite_56 == (sensor_OUT_reqRead_55), sensor_current_bpm_56 == sensor_current_bpm_55, sensor_OUT_value_56 == sensor_OUT_value_55, sensor_OUT_reqRead_56 == sensor_OUT_reqRead_55, monitor_IN_value_56 == monitor_IN_value_55, monitor_IN_reqRead_56 == monitor_IN_reqRead_55, monitor_IN_reqWrite_56 == monitor_IN_reqWrite_55, _SafetyController_0_buffered_status_56 == _SafetyController_0_buffered_status_55, _SafetyController_0_has_data_56 == _SafetyController_0_has_data_55), 
    And(And(Not(False), (monitor_IN_reqRead_55) == (False)), monitor_IN_reqRead_56 == (True), sensor_current_bpm_56 == sensor_current_bpm_55, sensor_OUT_value_56 == sensor_OUT_value_55, sensor_OUT_reqRead_56 == sensor_OUT_reqRead_55, sensor_OUT_reqWrite_56 == sensor_OUT_reqWrite_55, monitor_IN_value_56 == monitor_IN_value_55, monitor_IN_reqWrite_56 == monitor_IN_reqWrite_55, _SafetyController_0_buffered_status_56 == _SafetyController_0_buffered_status_55, _SafetyController_0_has_data_56 == _SafetyController_0_has_data_55), 
    And(And(Not(False), Not((sensor_OUT_reqRead_55) == ((_SafetyController_0_has_data_55) == (0)))), sensor_OUT_reqRead_56 == ((_SafetyController_0_has_data_55) == (0)), sensor_current_bpm_56 == sensor_current_bpm_55, sensor_OUT_value_56 == sensor_OUT_value_55, sensor_OUT_reqWrite_56 == sensor_OUT_reqWrite_55, monitor_IN_value_56 == monitor_IN_value_55, monitor_IN_reqRead_56 == monitor_IN_reqRead_55, monitor_IN_reqWrite_56 == monitor_IN_reqWrite_55, _SafetyController_0_buffered_status_56 == _SafetyController_0_buffered_status_55, _SafetyController_0_has_data_56 == _SafetyController_0_has_data_55), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_55) == ((_SafetyController_0_has_data_55) == (0))))), Not((monitor_IN_reqWrite_55) == (And(monitor_IN_reqRead_55, (_SafetyController_0_has_data_55) == (1))))), monitor_IN_reqWrite_56 == (And(monitor_IN_reqRead_55, (_SafetyController_0_has_data_55) == (1))), sensor_current_bpm_56 == sensor_current_bpm_55, sensor_OUT_value_56 == sensor_OUT_value_55, sensor_OUT_reqRead_56 == sensor_OUT_reqRead_55, sensor_OUT_reqWrite_56 == sensor_OUT_reqWrite_55, monitor_IN_value_56 == monitor_IN_value_55, monitor_IN_reqRead_56 == monitor_IN_reqRead_55, _SafetyController_0_buffered_status_56 == _SafetyController_0_buffered_status_55, _SafetyController_0_has_data_56 == _SafetyController_0_has_data_55), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_55) == (sensor_OUT_reqWrite_55)))), sensor_OUT_reqWrite_55), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_55) == ((_SafetyController_0_has_data_55) == (0)))), Not((monitor_IN_reqWrite_55) == (And(monitor_IN_reqRead_55, (_SafetyController_0_has_data_55) == (1)))))), sensor_OUT_reqRead_55)), _SafetyController_0_buffered_status_56 == (If((sensor_current_bpm_55 > 100), 1, 0)), sensor_current_bpm_56 == (predict_next(sensor_current_bpm_55)), sensor_OUT_reqWrite_56 == (False), _SafetyController_0_has_data_56 == (1), sensor_OUT_reqRead_56 == (False), sensor_OUT_value_56 == (sensor_current_bpm_55), monitor_IN_value_56 == monitor_IN_value_55, monitor_IN_reqRead_56 == monitor_IN_reqRead_55, monitor_IN_reqWrite_56 == monitor_IN_reqWrite_55), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_55) == (False))), monitor_IN_reqWrite_55), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_55) == ((_SafetyController_0_has_data_55) == (0)))), Not((monitor_IN_reqWrite_55) == (And(monitor_IN_reqRead_55, (_SafetyController_0_has_data_55) == (1))))), sensor_OUT_reqRead_55)), monitor_IN_reqWrite_55)), monitor_IN_reqWrite_56 == (False), monitor_IN_value_56 == (_SafetyController_0_buffered_status_55), _SafetyController_0_has_data_56 == (0), monitor_IN_reqRead_56 == (False), sensor_current_bpm_56 == sensor_current_bpm_55, sensor_OUT_value_56 == sensor_OUT_value_55, sensor_OUT_reqRead_56 == sensor_OUT_reqRead_55, sensor_OUT_reqWrite_56 == sensor_OUT_reqWrite_55, _SafetyController_0_buffered_status_56 == _SafetyController_0_buffered_status_55)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_56) == (sensor_OUT_reqWrite_56))), sensor_OUT_reqWrite_57 == (sensor_OUT_reqRead_56), sensor_current_bpm_57 == sensor_current_bpm_56, sensor_OUT_value_57 == sensor_OUT_value_56, sensor_OUT_reqRead_57 == sensor_OUT_reqRead_56, monitor_IN_value_57 == monitor_IN_value_56, monitor_IN_reqRead_57 == monitor_IN_reqRead_56, monitor_IN_reqWrite_57 == monitor_IN_reqWrite_56, _SafetyController_0_buffered_status_57 == _SafetyController_0_buffered_status_56, _SafetyController_0_has_data_57 == _SafetyController_0_has_data_56), 
    And(And(Not(False), (monitor_IN_reqRead_56) == (False)), monitor_IN_reqRead_57 == (True), sensor_current_bpm_57 == sensor_current_bpm_56, sensor_OUT_value_57 == sensor_OUT_value_56, sensor_OUT_reqRead_57 == sensor_OUT_reqRead_56, sensor_OUT_reqWrite_57 == sensor_OUT_reqWrite_56, monitor_IN_value_57 == monitor_IN_value_56, monitor_IN_reqWrite_57 == monitor_IN_reqWrite_56, _SafetyController_0_buffered_status_57 == _SafetyController_0_buffered_status_56, _SafetyController_0_has_data_57 == _SafetyController_0_has_data_56), 
    And(And(Not(False), Not((sensor_OUT_reqRead_56) == ((_SafetyController_0_has_data_56) == (0)))), sensor_OUT_reqRead_57 == ((_SafetyController_0_has_data_56) == (0)), sensor_current_bpm_57 == sensor_current_bpm_56, sensor_OUT_value_57 == sensor_OUT_value_56, sensor_OUT_reqWrite_57 == sensor_OUT_reqWrite_56, monitor_IN_value_57 == monitor_IN_value_56, monitor_IN_reqRead_57 == monitor_IN_reqRead_56, monitor_IN_reqWrite_57 == monitor_IN_reqWrite_56, _SafetyController_0_buffered_status_57 == _SafetyController_0_buffered_status_56, _SafetyController_0_has_data_57 == _SafetyController_0_has_data_56), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_56) == ((_SafetyController_0_has_data_56) == (0))))), Not((monitor_IN_reqWrite_56) == (And(monitor_IN_reqRead_56, (_SafetyController_0_has_data_56) == (1))))), monitor_IN_reqWrite_57 == (And(monitor_IN_reqRead_56, (_SafetyController_0_has_data_56) == (1))), sensor_current_bpm_57 == sensor_current_bpm_56, sensor_OUT_value_57 == sensor_OUT_value_56, sensor_OUT_reqRead_57 == sensor_OUT_reqRead_56, sensor_OUT_reqWrite_57 == sensor_OUT_reqWrite_56, monitor_IN_value_57 == monitor_IN_value_56, monitor_IN_reqRead_57 == monitor_IN_reqRead_56, _SafetyController_0_buffered_status_57 == _SafetyController_0_buffered_status_56, _SafetyController_0_has_data_57 == _SafetyController_0_has_data_56), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_56) == (sensor_OUT_reqWrite_56)))), sensor_OUT_reqWrite_56), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_56) == ((_SafetyController_0_has_data_56) == (0)))), Not((monitor_IN_reqWrite_56) == (And(monitor_IN_reqRead_56, (_SafetyController_0_has_data_56) == (1)))))), sensor_OUT_reqRead_56)), _SafetyController_0_buffered_status_57 == (If((sensor_current_bpm_56 > 100), 1, 0)), sensor_current_bpm_57 == (predict_next(sensor_current_bpm_56)), sensor_OUT_reqWrite_57 == (False), _SafetyController_0_has_data_57 == (1), sensor_OUT_reqRead_57 == (False), sensor_OUT_value_57 == (sensor_current_bpm_56), monitor_IN_value_57 == monitor_IN_value_56, monitor_IN_reqRead_57 == monitor_IN_reqRead_56, monitor_IN_reqWrite_57 == monitor_IN_reqWrite_56), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_56) == (False))), monitor_IN_reqWrite_56), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_56) == ((_SafetyController_0_has_data_56) == (0)))), Not((monitor_IN_reqWrite_56) == (And(monitor_IN_reqRead_56, (_SafetyController_0_has_data_56) == (1))))), sensor_OUT_reqRead_56)), monitor_IN_reqWrite_56)), monitor_IN_reqWrite_57 == (False), monitor_IN_value_57 == (_SafetyController_0_buffered_status_56), _SafetyController_0_has_data_57 == (0), monitor_IN_reqRead_57 == (False), sensor_current_bpm_57 == sensor_current_bpm_56, sensor_OUT_value_57 == sensor_OUT_value_56, sensor_OUT_reqRead_57 == sensor_OUT_reqRead_56, sensor_OUT_reqWrite_57 == sensor_OUT_reqWrite_56, _SafetyController_0_buffered_status_57 == _SafetyController_0_buffered_status_56)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_57) == (sensor_OUT_reqWrite_57))), sensor_OUT_reqWrite_58 == (sensor_OUT_reqRead_57), sensor_current_bpm_58 == sensor_current_bpm_57, sensor_OUT_value_58 == sensor_OUT_value_57, sensor_OUT_reqRead_58 == sensor_OUT_reqRead_57, monitor_IN_value_58 == monitor_IN_value_57, monitor_IN_reqRead_58 == monitor_IN_reqRead_57, monitor_IN_reqWrite_58 == monitor_IN_reqWrite_57, _SafetyController_0_buffered_status_58 == _SafetyController_0_buffered_status_57, _SafetyController_0_has_data_58 == _SafetyController_0_has_data_57), 
    And(And(Not(False), (monitor_IN_reqRead_57) == (False)), monitor_IN_reqRead_58 == (True), sensor_current_bpm_58 == sensor_current_bpm_57, sensor_OUT_value_58 == sensor_OUT_value_57, sensor_OUT_reqRead_58 == sensor_OUT_reqRead_57, sensor_OUT_reqWrite_58 == sensor_OUT_reqWrite_57, monitor_IN_value_58 == monitor_IN_value_57, monitor_IN_reqWrite_58 == monitor_IN_reqWrite_57, _SafetyController_0_buffered_status_58 == _SafetyController_0_buffered_status_57, _SafetyController_0_has_data_58 == _SafetyController_0_has_data_57), 
    And(And(Not(False), Not((sensor_OUT_reqRead_57) == ((_SafetyController_0_has_data_57) == (0)))), sensor_OUT_reqRead_58 == ((_SafetyController_0_has_data_57) == (0)), sensor_current_bpm_58 == sensor_current_bpm_57, sensor_OUT_value_58 == sensor_OUT_value_57, sensor_OUT_reqWrite_58 == sensor_OUT_reqWrite_57, monitor_IN_value_58 == monitor_IN_value_57, monitor_IN_reqRead_58 == monitor_IN_reqRead_57, monitor_IN_reqWrite_58 == monitor_IN_reqWrite_57, _SafetyController_0_buffered_status_58 == _SafetyController_0_buffered_status_57, _SafetyController_0_has_data_58 == _SafetyController_0_has_data_57), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_57) == ((_SafetyController_0_has_data_57) == (0))))), Not((monitor_IN_reqWrite_57) == (And(monitor_IN_reqRead_57, (_SafetyController_0_has_data_57) == (1))))), monitor_IN_reqWrite_58 == (And(monitor_IN_reqRead_57, (_SafetyController_0_has_data_57) == (1))), sensor_current_bpm_58 == sensor_current_bpm_57, sensor_OUT_value_58 == sensor_OUT_value_57, sensor_OUT_reqRead_58 == sensor_OUT_reqRead_57, sensor_OUT_reqWrite_58 == sensor_OUT_reqWrite_57, monitor_IN_value_58 == monitor_IN_value_57, monitor_IN_reqRead_58 == monitor_IN_reqRead_57, _SafetyController_0_buffered_status_58 == _SafetyController_0_buffered_status_57, _SafetyController_0_has_data_58 == _SafetyController_0_has_data_57), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_57) == (sensor_OUT_reqWrite_57)))), sensor_OUT_reqWrite_57), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_57) == ((_SafetyController_0_has_data_57) == (0)))), Not((monitor_IN_reqWrite_57) == (And(monitor_IN_reqRead_57, (_SafetyController_0_has_data_57) == (1)))))), sensor_OUT_reqRead_57)), _SafetyController_0_buffered_status_58 == (If((sensor_current_bpm_57 > 100), 1, 0)), sensor_current_bpm_58 == (predict_next(sensor_current_bpm_57)), sensor_OUT_reqWrite_58 == (False), _SafetyController_0_has_data_58 == (1), sensor_OUT_reqRead_58 == (False), sensor_OUT_value_58 == (sensor_current_bpm_57), monitor_IN_value_58 == monitor_IN_value_57, monitor_IN_reqRead_58 == monitor_IN_reqRead_57, monitor_IN_reqWrite_58 == monitor_IN_reqWrite_57), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_57) == (False))), monitor_IN_reqWrite_57), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_57) == ((_SafetyController_0_has_data_57) == (0)))), Not((monitor_IN_reqWrite_57) == (And(monitor_IN_reqRead_57, (_SafetyController_0_has_data_57) == (1))))), sensor_OUT_reqRead_57)), monitor_IN_reqWrite_57)), monitor_IN_reqWrite_58 == (False), monitor_IN_value_58 == (_SafetyController_0_buffered_status_57), _SafetyController_0_has_data_58 == (0), monitor_IN_reqRead_58 == (False), sensor_current_bpm_58 == sensor_current_bpm_57, sensor_OUT_value_58 == sensor_OUT_value_57, sensor_OUT_reqRead_58 == sensor_OUT_reqRead_57, sensor_OUT_reqWrite_58 == sensor_OUT_reqWrite_57, _SafetyController_0_buffered_status_58 == _SafetyController_0_buffered_status_57)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_58) == (sensor_OUT_reqWrite_58))), sensor_OUT_reqWrite_59 == (sensor_OUT_reqRead_58), sensor_current_bpm_59 == sensor_current_bpm_58, sensor_OUT_value_59 == sensor_OUT_value_58, sensor_OUT_reqRead_59 == sensor_OUT_reqRead_58, monitor_IN_value_59 == monitor_IN_value_58, monitor_IN_reqRead_59 == monitor_IN_reqRead_58, monitor_IN_reqWrite_59 == monitor_IN_reqWrite_58, _SafetyController_0_buffered_status_59 == _SafetyController_0_buffered_status_58, _SafetyController_0_has_data_59 == _SafetyController_0_has_data_58), 
    And(And(Not(False), (monitor_IN_reqRead_58) == (False)), monitor_IN_reqRead_59 == (True), sensor_current_bpm_59 == sensor_current_bpm_58, sensor_OUT_value_59 == sensor_OUT_value_58, sensor_OUT_reqRead_59 == sensor_OUT_reqRead_58, sensor_OUT_reqWrite_59 == sensor_OUT_reqWrite_58, monitor_IN_value_59 == monitor_IN_value_58, monitor_IN_reqWrite_59 == monitor_IN_reqWrite_58, _SafetyController_0_buffered_status_59 == _SafetyController_0_buffered_status_58, _SafetyController_0_has_data_59 == _SafetyController_0_has_data_58), 
    And(And(Not(False), Not((sensor_OUT_reqRead_58) == ((_SafetyController_0_has_data_58) == (0)))), sensor_OUT_reqRead_59 == ((_SafetyController_0_has_data_58) == (0)), sensor_current_bpm_59 == sensor_current_bpm_58, sensor_OUT_value_59 == sensor_OUT_value_58, sensor_OUT_reqWrite_59 == sensor_OUT_reqWrite_58, monitor_IN_value_59 == monitor_IN_value_58, monitor_IN_reqRead_59 == monitor_IN_reqRead_58, monitor_IN_reqWrite_59 == monitor_IN_reqWrite_58, _SafetyController_0_buffered_status_59 == _SafetyController_0_buffered_status_58, _SafetyController_0_has_data_59 == _SafetyController_0_has_data_58), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_58) == ((_SafetyController_0_has_data_58) == (0))))), Not((monitor_IN_reqWrite_58) == (And(monitor_IN_reqRead_58, (_SafetyController_0_has_data_58) == (1))))), monitor_IN_reqWrite_59 == (And(monitor_IN_reqRead_58, (_SafetyController_0_has_data_58) == (1))), sensor_current_bpm_59 == sensor_current_bpm_58, sensor_OUT_value_59 == sensor_OUT_value_58, sensor_OUT_reqRead_59 == sensor_OUT_reqRead_58, sensor_OUT_reqWrite_59 == sensor_OUT_reqWrite_58, monitor_IN_value_59 == monitor_IN_value_58, monitor_IN_reqRead_59 == monitor_IN_reqRead_58, _SafetyController_0_buffered_status_59 == _SafetyController_0_buffered_status_58, _SafetyController_0_has_data_59 == _SafetyController_0_has_data_58), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_58) == (sensor_OUT_reqWrite_58)))), sensor_OUT_reqWrite_58), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_58) == ((_SafetyController_0_has_data_58) == (0)))), Not((monitor_IN_reqWrite_58) == (And(monitor_IN_reqRead_58, (_SafetyController_0_has_data_58) == (1)))))), sensor_OUT_reqRead_58)), _SafetyController_0_buffered_status_59 == (If((sensor_current_bpm_58 > 100), 1, 0)), sensor_current_bpm_59 == (predict_next(sensor_current_bpm_58)), sensor_OUT_reqWrite_59 == (False), _SafetyController_0_has_data_59 == (1), sensor_OUT_reqRead_59 == (False), sensor_OUT_value_59 == (sensor_current_bpm_58), monitor_IN_value_59 == monitor_IN_value_58, monitor_IN_reqRead_59 == monitor_IN_reqRead_58, monitor_IN_reqWrite_59 == monitor_IN_reqWrite_58), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_58) == (False))), monitor_IN_reqWrite_58), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_58) == ((_SafetyController_0_has_data_58) == (0)))), Not((monitor_IN_reqWrite_58) == (And(monitor_IN_reqRead_58, (_SafetyController_0_has_data_58) == (1))))), sensor_OUT_reqRead_58)), monitor_IN_reqWrite_58)), monitor_IN_reqWrite_59 == (False), monitor_IN_value_59 == (_SafetyController_0_buffered_status_58), _SafetyController_0_has_data_59 == (0), monitor_IN_reqRead_59 == (False), sensor_current_bpm_59 == sensor_current_bpm_58, sensor_OUT_value_59 == sensor_OUT_value_58, sensor_OUT_reqRead_59 == sensor_OUT_reqRead_58, sensor_OUT_reqWrite_59 == sensor_OUT_reqWrite_58, _SafetyController_0_buffered_status_59 == _SafetyController_0_buffered_status_58)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_59) == (sensor_OUT_reqWrite_59))), sensor_OUT_reqWrite_60 == (sensor_OUT_reqRead_59), sensor_current_bpm_60 == sensor_current_bpm_59, sensor_OUT_value_60 == sensor_OUT_value_59, sensor_OUT_reqRead_60 == sensor_OUT_reqRead_59, monitor_IN_value_60 == monitor_IN_value_59, monitor_IN_reqRead_60 == monitor_IN_reqRead_59, monitor_IN_reqWrite_60 == monitor_IN_reqWrite_59, _SafetyController_0_buffered_status_60 == _SafetyController_0_buffered_status_59, _SafetyController_0_has_data_60 == _SafetyController_0_has_data_59), 
    And(And(Not(False), (monitor_IN_reqRead_59) == (False)), monitor_IN_reqRead_60 == (True), sensor_current_bpm_60 == sensor_current_bpm_59, sensor_OUT_value_60 == sensor_OUT_value_59, sensor_OUT_reqRead_60 == sensor_OUT_reqRead_59, sensor_OUT_reqWrite_60 == sensor_OUT_reqWrite_59, monitor_IN_value_60 == monitor_IN_value_59, monitor_IN_reqWrite_60 == monitor_IN_reqWrite_59, _SafetyController_0_buffered_status_60 == _SafetyController_0_buffered_status_59, _SafetyController_0_has_data_60 == _SafetyController_0_has_data_59), 
    And(And(Not(False), Not((sensor_OUT_reqRead_59) == ((_SafetyController_0_has_data_59) == (0)))), sensor_OUT_reqRead_60 == ((_SafetyController_0_has_data_59) == (0)), sensor_current_bpm_60 == sensor_current_bpm_59, sensor_OUT_value_60 == sensor_OUT_value_59, sensor_OUT_reqWrite_60 == sensor_OUT_reqWrite_59, monitor_IN_value_60 == monitor_IN_value_59, monitor_IN_reqRead_60 == monitor_IN_reqRead_59, monitor_IN_reqWrite_60 == monitor_IN_reqWrite_59, _SafetyController_0_buffered_status_60 == _SafetyController_0_buffered_status_59, _SafetyController_0_has_data_60 == _SafetyController_0_has_data_59), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_59) == ((_SafetyController_0_has_data_59) == (0))))), Not((monitor_IN_reqWrite_59) == (And(monitor_IN_reqRead_59, (_SafetyController_0_has_data_59) == (1))))), monitor_IN_reqWrite_60 == (And(monitor_IN_reqRead_59, (_SafetyController_0_has_data_59) == (1))), sensor_current_bpm_60 == sensor_current_bpm_59, sensor_OUT_value_60 == sensor_OUT_value_59, sensor_OUT_reqRead_60 == sensor_OUT_reqRead_59, sensor_OUT_reqWrite_60 == sensor_OUT_reqWrite_59, monitor_IN_value_60 == monitor_IN_value_59, monitor_IN_reqRead_60 == monitor_IN_reqRead_59, _SafetyController_0_buffered_status_60 == _SafetyController_0_buffered_status_59, _SafetyController_0_has_data_60 == _SafetyController_0_has_data_59), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_59) == (sensor_OUT_reqWrite_59)))), sensor_OUT_reqWrite_59), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_59) == ((_SafetyController_0_has_data_59) == (0)))), Not((monitor_IN_reqWrite_59) == (And(monitor_IN_reqRead_59, (_SafetyController_0_has_data_59) == (1)))))), sensor_OUT_reqRead_59)), _SafetyController_0_buffered_status_60 == (If((sensor_current_bpm_59 > 100), 1, 0)), sensor_current_bpm_60 == (predict_next(sensor_current_bpm_59)), sensor_OUT_reqWrite_60 == (False), _SafetyController_0_has_data_60 == (1), sensor_OUT_reqRead_60 == (False), sensor_OUT_value_60 == (sensor_current_bpm_59), monitor_IN_value_60 == monitor_IN_value_59, monitor_IN_reqRead_60 == monitor_IN_reqRead_59, monitor_IN_reqWrite_60 == monitor_IN_reqWrite_59), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_59) == (False))), monitor_IN_reqWrite_59), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_59) == ((_SafetyController_0_has_data_59) == (0)))), Not((monitor_IN_reqWrite_59) == (And(monitor_IN_reqRead_59, (_SafetyController_0_has_data_59) == (1))))), sensor_OUT_reqRead_59)), monitor_IN_reqWrite_59)), monitor_IN_reqWrite_60 == (False), monitor_IN_value_60 == (_SafetyController_0_buffered_status_59), _SafetyController_0_has_data_60 == (0), monitor_IN_reqRead_60 == (False), sensor_current_bpm_60 == sensor_current_bpm_59, sensor_OUT_value_60 == sensor_OUT_value_59, sensor_OUT_reqRead_60 == sensor_OUT_reqRead_59, sensor_OUT_reqWrite_60 == sensor_OUT_reqWrite_59, _SafetyController_0_buffered_status_60 == _SafetyController_0_buffered_status_59)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_60) == (sensor_OUT_reqWrite_60))), sensor_OUT_reqWrite_61 == (sensor_OUT_reqRead_60), sensor_current_bpm_61 == sensor_current_bpm_60, sensor_OUT_value_61 == sensor_OUT_value_60, sensor_OUT_reqRead_61 == sensor_OUT_reqRead_60, monitor_IN_value_61 == monitor_IN_value_60, monitor_IN_reqRead_61 == monitor_IN_reqRead_60, monitor_IN_reqWrite_61 == monitor_IN_reqWrite_60, _SafetyController_0_buffered_status_61 == _SafetyController_0_buffered_status_60, _SafetyController_0_has_data_61 == _SafetyController_0_has_data_60), 
    And(And(Not(False), (monitor_IN_reqRead_60) == (False)), monitor_IN_reqRead_61 == (True), sensor_current_bpm_61 == sensor_current_bpm_60, sensor_OUT_value_61 == sensor_OUT_value_60, sensor_OUT_reqRead_61 == sensor_OUT_reqRead_60, sensor_OUT_reqWrite_61 == sensor_OUT_reqWrite_60, monitor_IN_value_61 == monitor_IN_value_60, monitor_IN_reqWrite_61 == monitor_IN_reqWrite_60, _SafetyController_0_buffered_status_61 == _SafetyController_0_buffered_status_60, _SafetyController_0_has_data_61 == _SafetyController_0_has_data_60), 
    And(And(Not(False), Not((sensor_OUT_reqRead_60) == ((_SafetyController_0_has_data_60) == (0)))), sensor_OUT_reqRead_61 == ((_SafetyController_0_has_data_60) == (0)), sensor_current_bpm_61 == sensor_current_bpm_60, sensor_OUT_value_61 == sensor_OUT_value_60, sensor_OUT_reqWrite_61 == sensor_OUT_reqWrite_60, monitor_IN_value_61 == monitor_IN_value_60, monitor_IN_reqRead_61 == monitor_IN_reqRead_60, monitor_IN_reqWrite_61 == monitor_IN_reqWrite_60, _SafetyController_0_buffered_status_61 == _SafetyController_0_buffered_status_60, _SafetyController_0_has_data_61 == _SafetyController_0_has_data_60), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_60) == ((_SafetyController_0_has_data_60) == (0))))), Not((monitor_IN_reqWrite_60) == (And(monitor_IN_reqRead_60, (_SafetyController_0_has_data_60) == (1))))), monitor_IN_reqWrite_61 == (And(monitor_IN_reqRead_60, (_SafetyController_0_has_data_60) == (1))), sensor_current_bpm_61 == sensor_current_bpm_60, sensor_OUT_value_61 == sensor_OUT_value_60, sensor_OUT_reqRead_61 == sensor_OUT_reqRead_60, sensor_OUT_reqWrite_61 == sensor_OUT_reqWrite_60, monitor_IN_value_61 == monitor_IN_value_60, monitor_IN_reqRead_61 == monitor_IN_reqRead_60, _SafetyController_0_buffered_status_61 == _SafetyController_0_buffered_status_60, _SafetyController_0_has_data_61 == _SafetyController_0_has_data_60), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_60) == (sensor_OUT_reqWrite_60)))), sensor_OUT_reqWrite_60), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_60) == ((_SafetyController_0_has_data_60) == (0)))), Not((monitor_IN_reqWrite_60) == (And(monitor_IN_reqRead_60, (_SafetyController_0_has_data_60) == (1)))))), sensor_OUT_reqRead_60)), _SafetyController_0_buffered_status_61 == (If((sensor_current_bpm_60 > 100), 1, 0)), sensor_current_bpm_61 == (predict_next(sensor_current_bpm_60)), sensor_OUT_reqWrite_61 == (False), _SafetyController_0_has_data_61 == (1), sensor_OUT_reqRead_61 == (False), sensor_OUT_value_61 == (sensor_current_bpm_60), monitor_IN_value_61 == monitor_IN_value_60, monitor_IN_reqRead_61 == monitor_IN_reqRead_60, monitor_IN_reqWrite_61 == monitor_IN_reqWrite_60), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_60) == (False))), monitor_IN_reqWrite_60), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_60) == ((_SafetyController_0_has_data_60) == (0)))), Not((monitor_IN_reqWrite_60) == (And(monitor_IN_reqRead_60, (_SafetyController_0_has_data_60) == (1))))), sensor_OUT_reqRead_60)), monitor_IN_reqWrite_60)), monitor_IN_reqWrite_61 == (False), monitor_IN_value_61 == (_SafetyController_0_buffered_status_60), _SafetyController_0_has_data_61 == (0), monitor_IN_reqRead_61 == (False), sensor_current_bpm_61 == sensor_current_bpm_60, sensor_OUT_value_61 == sensor_OUT_value_60, sensor_OUT_reqRead_61 == sensor_OUT_reqRead_60, sensor_OUT_reqWrite_61 == sensor_OUT_reqWrite_60, _SafetyController_0_buffered_status_61 == _SafetyController_0_buffered_status_60)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_61) == (sensor_OUT_reqWrite_61))), sensor_OUT_reqWrite_62 == (sensor_OUT_reqRead_61), sensor_current_bpm_62 == sensor_current_bpm_61, sensor_OUT_value_62 == sensor_OUT_value_61, sensor_OUT_reqRead_62 == sensor_OUT_reqRead_61, monitor_IN_value_62 == monitor_IN_value_61, monitor_IN_reqRead_62 == monitor_IN_reqRead_61, monitor_IN_reqWrite_62 == monitor_IN_reqWrite_61, _SafetyController_0_buffered_status_62 == _SafetyController_0_buffered_status_61, _SafetyController_0_has_data_62 == _SafetyController_0_has_data_61), 
    And(And(Not(False), (monitor_IN_reqRead_61) == (False)), monitor_IN_reqRead_62 == (True), sensor_current_bpm_62 == sensor_current_bpm_61, sensor_OUT_value_62 == sensor_OUT_value_61, sensor_OUT_reqRead_62 == sensor_OUT_reqRead_61, sensor_OUT_reqWrite_62 == sensor_OUT_reqWrite_61, monitor_IN_value_62 == monitor_IN_value_61, monitor_IN_reqWrite_62 == monitor_IN_reqWrite_61, _SafetyController_0_buffered_status_62 == _SafetyController_0_buffered_status_61, _SafetyController_0_has_data_62 == _SafetyController_0_has_data_61), 
    And(And(Not(False), Not((sensor_OUT_reqRead_61) == ((_SafetyController_0_has_data_61) == (0)))), sensor_OUT_reqRead_62 == ((_SafetyController_0_has_data_61) == (0)), sensor_current_bpm_62 == sensor_current_bpm_61, sensor_OUT_value_62 == sensor_OUT_value_61, sensor_OUT_reqWrite_62 == sensor_OUT_reqWrite_61, monitor_IN_value_62 == monitor_IN_value_61, monitor_IN_reqRead_62 == monitor_IN_reqRead_61, monitor_IN_reqWrite_62 == monitor_IN_reqWrite_61, _SafetyController_0_buffered_status_62 == _SafetyController_0_buffered_status_61, _SafetyController_0_has_data_62 == _SafetyController_0_has_data_61), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_61) == ((_SafetyController_0_has_data_61) == (0))))), Not((monitor_IN_reqWrite_61) == (And(monitor_IN_reqRead_61, (_SafetyController_0_has_data_61) == (1))))), monitor_IN_reqWrite_62 == (And(monitor_IN_reqRead_61, (_SafetyController_0_has_data_61) == (1))), sensor_current_bpm_62 == sensor_current_bpm_61, sensor_OUT_value_62 == sensor_OUT_value_61, sensor_OUT_reqRead_62 == sensor_OUT_reqRead_61, sensor_OUT_reqWrite_62 == sensor_OUT_reqWrite_61, monitor_IN_value_62 == monitor_IN_value_61, monitor_IN_reqRead_62 == monitor_IN_reqRead_61, _SafetyController_0_buffered_status_62 == _SafetyController_0_buffered_status_61, _SafetyController_0_has_data_62 == _SafetyController_0_has_data_61), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_61) == (sensor_OUT_reqWrite_61)))), sensor_OUT_reqWrite_61), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_61) == ((_SafetyController_0_has_data_61) == (0)))), Not((monitor_IN_reqWrite_61) == (And(monitor_IN_reqRead_61, (_SafetyController_0_has_data_61) == (1)))))), sensor_OUT_reqRead_61)), _SafetyController_0_buffered_status_62 == (If((sensor_current_bpm_61 > 100), 1, 0)), sensor_current_bpm_62 == (predict_next(sensor_current_bpm_61)), sensor_OUT_reqWrite_62 == (False), _SafetyController_0_has_data_62 == (1), sensor_OUT_reqRead_62 == (False), sensor_OUT_value_62 == (sensor_current_bpm_61), monitor_IN_value_62 == monitor_IN_value_61, monitor_IN_reqRead_62 == monitor_IN_reqRead_61, monitor_IN_reqWrite_62 == monitor_IN_reqWrite_61), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_61) == (False))), monitor_IN_reqWrite_61), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_61) == ((_SafetyController_0_has_data_61) == (0)))), Not((monitor_IN_reqWrite_61) == (And(monitor_IN_reqRead_61, (_SafetyController_0_has_data_61) == (1))))), sensor_OUT_reqRead_61)), monitor_IN_reqWrite_61)), monitor_IN_reqWrite_62 == (False), monitor_IN_value_62 == (_SafetyController_0_buffered_status_61), _SafetyController_0_has_data_62 == (0), monitor_IN_reqRead_62 == (False), sensor_current_bpm_62 == sensor_current_bpm_61, sensor_OUT_value_62 == sensor_OUT_value_61, sensor_OUT_reqRead_62 == sensor_OUT_reqRead_61, sensor_OUT_reqWrite_62 == sensor_OUT_reqWrite_61, _SafetyController_0_buffered_status_62 == _SafetyController_0_buffered_status_61)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_62) == (sensor_OUT_reqWrite_62))), sensor_OUT_reqWrite_63 == (sensor_OUT_reqRead_62), sensor_current_bpm_63 == sensor_current_bpm_62, sensor_OUT_value_63 == sensor_OUT_value_62, sensor_OUT_reqRead_63 == sensor_OUT_reqRead_62, monitor_IN_value_63 == monitor_IN_value_62, monitor_IN_reqRead_63 == monitor_IN_reqRead_62, monitor_IN_reqWrite_63 == monitor_IN_reqWrite_62, _SafetyController_0_buffered_status_63 == _SafetyController_0_buffered_status_62, _SafetyController_0_has_data_63 == _SafetyController_0_has_data_62), 
    And(And(Not(False), (monitor_IN_reqRead_62) == (False)), monitor_IN_reqRead_63 == (True), sensor_current_bpm_63 == sensor_current_bpm_62, sensor_OUT_value_63 == sensor_OUT_value_62, sensor_OUT_reqRead_63 == sensor_OUT_reqRead_62, sensor_OUT_reqWrite_63 == sensor_OUT_reqWrite_62, monitor_IN_value_63 == monitor_IN_value_62, monitor_IN_reqWrite_63 == monitor_IN_reqWrite_62, _SafetyController_0_buffered_status_63 == _SafetyController_0_buffered_status_62, _SafetyController_0_has_data_63 == _SafetyController_0_has_data_62), 
    And(And(Not(False), Not((sensor_OUT_reqRead_62) == ((_SafetyController_0_has_data_62) == (0)))), sensor_OUT_reqRead_63 == ((_SafetyController_0_has_data_62) == (0)), sensor_current_bpm_63 == sensor_current_bpm_62, sensor_OUT_value_63 == sensor_OUT_value_62, sensor_OUT_reqWrite_63 == sensor_OUT_reqWrite_62, monitor_IN_value_63 == monitor_IN_value_62, monitor_IN_reqRead_63 == monitor_IN_reqRead_62, monitor_IN_reqWrite_63 == monitor_IN_reqWrite_62, _SafetyController_0_buffered_status_63 == _SafetyController_0_buffered_status_62, _SafetyController_0_has_data_63 == _SafetyController_0_has_data_62), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_62) == ((_SafetyController_0_has_data_62) == (0))))), Not((monitor_IN_reqWrite_62) == (And(monitor_IN_reqRead_62, (_SafetyController_0_has_data_62) == (1))))), monitor_IN_reqWrite_63 == (And(monitor_IN_reqRead_62, (_SafetyController_0_has_data_62) == (1))), sensor_current_bpm_63 == sensor_current_bpm_62, sensor_OUT_value_63 == sensor_OUT_value_62, sensor_OUT_reqRead_63 == sensor_OUT_reqRead_62, sensor_OUT_reqWrite_63 == sensor_OUT_reqWrite_62, monitor_IN_value_63 == monitor_IN_value_62, monitor_IN_reqRead_63 == monitor_IN_reqRead_62, _SafetyController_0_buffered_status_63 == _SafetyController_0_buffered_status_62, _SafetyController_0_has_data_63 == _SafetyController_0_has_data_62), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_62) == (sensor_OUT_reqWrite_62)))), sensor_OUT_reqWrite_62), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_62) == ((_SafetyController_0_has_data_62) == (0)))), Not((monitor_IN_reqWrite_62) == (And(monitor_IN_reqRead_62, (_SafetyController_0_has_data_62) == (1)))))), sensor_OUT_reqRead_62)), _SafetyController_0_buffered_status_63 == (If((sensor_current_bpm_62 > 100), 1, 0)), sensor_current_bpm_63 == (predict_next(sensor_current_bpm_62)), sensor_OUT_reqWrite_63 == (False), _SafetyController_0_has_data_63 == (1), sensor_OUT_reqRead_63 == (False), sensor_OUT_value_63 == (sensor_current_bpm_62), monitor_IN_value_63 == monitor_IN_value_62, monitor_IN_reqRead_63 == monitor_IN_reqRead_62, monitor_IN_reqWrite_63 == monitor_IN_reqWrite_62), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_62) == (False))), monitor_IN_reqWrite_62), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_62) == ((_SafetyController_0_has_data_62) == (0)))), Not((monitor_IN_reqWrite_62) == (And(monitor_IN_reqRead_62, (_SafetyController_0_has_data_62) == (1))))), sensor_OUT_reqRead_62)), monitor_IN_reqWrite_62)), monitor_IN_reqWrite_63 == (False), monitor_IN_value_63 == (_SafetyController_0_buffered_status_62), _SafetyController_0_has_data_63 == (0), monitor_IN_reqRead_63 == (False), sensor_current_bpm_63 == sensor_current_bpm_62, sensor_OUT_value_63 == sensor_OUT_value_62, sensor_OUT_reqRead_63 == sensor_OUT_reqRead_62, sensor_OUT_reqWrite_63 == sensor_OUT_reqWrite_62, _SafetyController_0_buffered_status_63 == _SafetyController_0_buffered_status_62)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_63) == (sensor_OUT_reqWrite_63))), sensor_OUT_reqWrite_64 == (sensor_OUT_reqRead_63), sensor_current_bpm_64 == sensor_current_bpm_63, sensor_OUT_value_64 == sensor_OUT_value_63, sensor_OUT_reqRead_64 == sensor_OUT_reqRead_63, monitor_IN_value_64 == monitor_IN_value_63, monitor_IN_reqRead_64 == monitor_IN_reqRead_63, monitor_IN_reqWrite_64 == monitor_IN_reqWrite_63, _SafetyController_0_buffered_status_64 == _SafetyController_0_buffered_status_63, _SafetyController_0_has_data_64 == _SafetyController_0_has_data_63), 
    And(And(Not(False), (monitor_IN_reqRead_63) == (False)), monitor_IN_reqRead_64 == (True), sensor_current_bpm_64 == sensor_current_bpm_63, sensor_OUT_value_64 == sensor_OUT_value_63, sensor_OUT_reqRead_64 == sensor_OUT_reqRead_63, sensor_OUT_reqWrite_64 == sensor_OUT_reqWrite_63, monitor_IN_value_64 == monitor_IN_value_63, monitor_IN_reqWrite_64 == monitor_IN_reqWrite_63, _SafetyController_0_buffered_status_64 == _SafetyController_0_buffered_status_63, _SafetyController_0_has_data_64 == _SafetyController_0_has_data_63), 
    And(And(Not(False), Not((sensor_OUT_reqRead_63) == ((_SafetyController_0_has_data_63) == (0)))), sensor_OUT_reqRead_64 == ((_SafetyController_0_has_data_63) == (0)), sensor_current_bpm_64 == sensor_current_bpm_63, sensor_OUT_value_64 == sensor_OUT_value_63, sensor_OUT_reqWrite_64 == sensor_OUT_reqWrite_63, monitor_IN_value_64 == monitor_IN_value_63, monitor_IN_reqRead_64 == monitor_IN_reqRead_63, monitor_IN_reqWrite_64 == monitor_IN_reqWrite_63, _SafetyController_0_buffered_status_64 == _SafetyController_0_buffered_status_63, _SafetyController_0_has_data_64 == _SafetyController_0_has_data_63), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_63) == ((_SafetyController_0_has_data_63) == (0))))), Not((monitor_IN_reqWrite_63) == (And(monitor_IN_reqRead_63, (_SafetyController_0_has_data_63) == (1))))), monitor_IN_reqWrite_64 == (And(monitor_IN_reqRead_63, (_SafetyController_0_has_data_63) == (1))), sensor_current_bpm_64 == sensor_current_bpm_63, sensor_OUT_value_64 == sensor_OUT_value_63, sensor_OUT_reqRead_64 == sensor_OUT_reqRead_63, sensor_OUT_reqWrite_64 == sensor_OUT_reqWrite_63, monitor_IN_value_64 == monitor_IN_value_63, monitor_IN_reqRead_64 == monitor_IN_reqRead_63, _SafetyController_0_buffered_status_64 == _SafetyController_0_buffered_status_63, _SafetyController_0_has_data_64 == _SafetyController_0_has_data_63), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_63) == (sensor_OUT_reqWrite_63)))), sensor_OUT_reqWrite_63), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_63) == ((_SafetyController_0_has_data_63) == (0)))), Not((monitor_IN_reqWrite_63) == (And(monitor_IN_reqRead_63, (_SafetyController_0_has_data_63) == (1)))))), sensor_OUT_reqRead_63)), _SafetyController_0_buffered_status_64 == (If((sensor_current_bpm_63 > 100), 1, 0)), sensor_current_bpm_64 == (predict_next(sensor_current_bpm_63)), sensor_OUT_reqWrite_64 == (False), _SafetyController_0_has_data_64 == (1), sensor_OUT_reqRead_64 == (False), sensor_OUT_value_64 == (sensor_current_bpm_63), monitor_IN_value_64 == monitor_IN_value_63, monitor_IN_reqRead_64 == monitor_IN_reqRead_63, monitor_IN_reqWrite_64 == monitor_IN_reqWrite_63), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_63) == (False))), monitor_IN_reqWrite_63), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_63) == ((_SafetyController_0_has_data_63) == (0)))), Not((monitor_IN_reqWrite_63) == (And(monitor_IN_reqRead_63, (_SafetyController_0_has_data_63) == (1))))), sensor_OUT_reqRead_63)), monitor_IN_reqWrite_63)), monitor_IN_reqWrite_64 == (False), monitor_IN_value_64 == (_SafetyController_0_buffered_status_63), _SafetyController_0_has_data_64 == (0), monitor_IN_reqRead_64 == (False), sensor_current_bpm_64 == sensor_current_bpm_63, sensor_OUT_value_64 == sensor_OUT_value_63, sensor_OUT_reqRead_64 == sensor_OUT_reqRead_63, sensor_OUT_reqWrite_64 == sensor_OUT_reqWrite_63, _SafetyController_0_buffered_status_64 == _SafetyController_0_buffered_status_63)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_64) == (sensor_OUT_reqWrite_64))), sensor_OUT_reqWrite_65 == (sensor_OUT_reqRead_64), sensor_current_bpm_65 == sensor_current_bpm_64, sensor_OUT_value_65 == sensor_OUT_value_64, sensor_OUT_reqRead_65 == sensor_OUT_reqRead_64, monitor_IN_value_65 == monitor_IN_value_64, monitor_IN_reqRead_65 == monitor_IN_reqRead_64, monitor_IN_reqWrite_65 == monitor_IN_reqWrite_64, _SafetyController_0_buffered_status_65 == _SafetyController_0_buffered_status_64, _SafetyController_0_has_data_65 == _SafetyController_0_has_data_64), 
    And(And(Not(False), (monitor_IN_reqRead_64) == (False)), monitor_IN_reqRead_65 == (True), sensor_current_bpm_65 == sensor_current_bpm_64, sensor_OUT_value_65 == sensor_OUT_value_64, sensor_OUT_reqRead_65 == sensor_OUT_reqRead_64, sensor_OUT_reqWrite_65 == sensor_OUT_reqWrite_64, monitor_IN_value_65 == monitor_IN_value_64, monitor_IN_reqWrite_65 == monitor_IN_reqWrite_64, _SafetyController_0_buffered_status_65 == _SafetyController_0_buffered_status_64, _SafetyController_0_has_data_65 == _SafetyController_0_has_data_64), 
    And(And(Not(False), Not((sensor_OUT_reqRead_64) == ((_SafetyController_0_has_data_64) == (0)))), sensor_OUT_reqRead_65 == ((_SafetyController_0_has_data_64) == (0)), sensor_current_bpm_65 == sensor_current_bpm_64, sensor_OUT_value_65 == sensor_OUT_value_64, sensor_OUT_reqWrite_65 == sensor_OUT_reqWrite_64, monitor_IN_value_65 == monitor_IN_value_64, monitor_IN_reqRead_65 == monitor_IN_reqRead_64, monitor_IN_reqWrite_65 == monitor_IN_reqWrite_64, _SafetyController_0_buffered_status_65 == _SafetyController_0_buffered_status_64, _SafetyController_0_has_data_65 == _SafetyController_0_has_data_64), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_64) == ((_SafetyController_0_has_data_64) == (0))))), Not((monitor_IN_reqWrite_64) == (And(monitor_IN_reqRead_64, (_SafetyController_0_has_data_64) == (1))))), monitor_IN_reqWrite_65 == (And(monitor_IN_reqRead_64, (_SafetyController_0_has_data_64) == (1))), sensor_current_bpm_65 == sensor_current_bpm_64, sensor_OUT_value_65 == sensor_OUT_value_64, sensor_OUT_reqRead_65 == sensor_OUT_reqRead_64, sensor_OUT_reqWrite_65 == sensor_OUT_reqWrite_64, monitor_IN_value_65 == monitor_IN_value_64, monitor_IN_reqRead_65 == monitor_IN_reqRead_64, _SafetyController_0_buffered_status_65 == _SafetyController_0_buffered_status_64, _SafetyController_0_has_data_65 == _SafetyController_0_has_data_64), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_64) == (sensor_OUT_reqWrite_64)))), sensor_OUT_reqWrite_64), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_64) == ((_SafetyController_0_has_data_64) == (0)))), Not((monitor_IN_reqWrite_64) == (And(monitor_IN_reqRead_64, (_SafetyController_0_has_data_64) == (1)))))), sensor_OUT_reqRead_64)), _SafetyController_0_buffered_status_65 == (If((sensor_current_bpm_64 > 100), 1, 0)), sensor_current_bpm_65 == (predict_next(sensor_current_bpm_64)), sensor_OUT_reqWrite_65 == (False), _SafetyController_0_has_data_65 == (1), sensor_OUT_reqRead_65 == (False), sensor_OUT_value_65 == (sensor_current_bpm_64), monitor_IN_value_65 == monitor_IN_value_64, monitor_IN_reqRead_65 == monitor_IN_reqRead_64, monitor_IN_reqWrite_65 == monitor_IN_reqWrite_64), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_64) == (False))), monitor_IN_reqWrite_64), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_64) == ((_SafetyController_0_has_data_64) == (0)))), Not((monitor_IN_reqWrite_64) == (And(monitor_IN_reqRead_64, (_SafetyController_0_has_data_64) == (1))))), sensor_OUT_reqRead_64)), monitor_IN_reqWrite_64)), monitor_IN_reqWrite_65 == (False), monitor_IN_value_65 == (_SafetyController_0_buffered_status_64), _SafetyController_0_has_data_65 == (0), monitor_IN_reqRead_65 == (False), sensor_current_bpm_65 == sensor_current_bpm_64, sensor_OUT_value_65 == sensor_OUT_value_64, sensor_OUT_reqRead_65 == sensor_OUT_reqRead_64, sensor_OUT_reqWrite_65 == sensor_OUT_reqWrite_64, _SafetyController_0_buffered_status_65 == _SafetyController_0_buffered_status_64)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_65) == (sensor_OUT_reqWrite_65))), sensor_OUT_reqWrite_66 == (sensor_OUT_reqRead_65), sensor_current_bpm_66 == sensor_current_bpm_65, sensor_OUT_value_66 == sensor_OUT_value_65, sensor_OUT_reqRead_66 == sensor_OUT_reqRead_65, monitor_IN_value_66 == monitor_IN_value_65, monitor_IN_reqRead_66 == monitor_IN_reqRead_65, monitor_IN_reqWrite_66 == monitor_IN_reqWrite_65, _SafetyController_0_buffered_status_66 == _SafetyController_0_buffered_status_65, _SafetyController_0_has_data_66 == _SafetyController_0_has_data_65), 
    And(And(Not(False), (monitor_IN_reqRead_65) == (False)), monitor_IN_reqRead_66 == (True), sensor_current_bpm_66 == sensor_current_bpm_65, sensor_OUT_value_66 == sensor_OUT_value_65, sensor_OUT_reqRead_66 == sensor_OUT_reqRead_65, sensor_OUT_reqWrite_66 == sensor_OUT_reqWrite_65, monitor_IN_value_66 == monitor_IN_value_65, monitor_IN_reqWrite_66 == monitor_IN_reqWrite_65, _SafetyController_0_buffered_status_66 == _SafetyController_0_buffered_status_65, _SafetyController_0_has_data_66 == _SafetyController_0_has_data_65), 
    And(And(Not(False), Not((sensor_OUT_reqRead_65) == ((_SafetyController_0_has_data_65) == (0)))), sensor_OUT_reqRead_66 == ((_SafetyController_0_has_data_65) == (0)), sensor_current_bpm_66 == sensor_current_bpm_65, sensor_OUT_value_66 == sensor_OUT_value_65, sensor_OUT_reqWrite_66 == sensor_OUT_reqWrite_65, monitor_IN_value_66 == monitor_IN_value_65, monitor_IN_reqRead_66 == monitor_IN_reqRead_65, monitor_IN_reqWrite_66 == monitor_IN_reqWrite_65, _SafetyController_0_buffered_status_66 == _SafetyController_0_buffered_status_65, _SafetyController_0_has_data_66 == _SafetyController_0_has_data_65), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_65) == ((_SafetyController_0_has_data_65) == (0))))), Not((monitor_IN_reqWrite_65) == (And(monitor_IN_reqRead_65, (_SafetyController_0_has_data_65) == (1))))), monitor_IN_reqWrite_66 == (And(monitor_IN_reqRead_65, (_SafetyController_0_has_data_65) == (1))), sensor_current_bpm_66 == sensor_current_bpm_65, sensor_OUT_value_66 == sensor_OUT_value_65, sensor_OUT_reqRead_66 == sensor_OUT_reqRead_65, sensor_OUT_reqWrite_66 == sensor_OUT_reqWrite_65, monitor_IN_value_66 == monitor_IN_value_65, monitor_IN_reqRead_66 == monitor_IN_reqRead_65, _SafetyController_0_buffered_status_66 == _SafetyController_0_buffered_status_65, _SafetyController_0_has_data_66 == _SafetyController_0_has_data_65), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_65) == (sensor_OUT_reqWrite_65)))), sensor_OUT_reqWrite_65), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_65) == ((_SafetyController_0_has_data_65) == (0)))), Not((monitor_IN_reqWrite_65) == (And(monitor_IN_reqRead_65, (_SafetyController_0_has_data_65) == (1)))))), sensor_OUT_reqRead_65)), _SafetyController_0_buffered_status_66 == (If((sensor_current_bpm_65 > 100), 1, 0)), sensor_current_bpm_66 == (predict_next(sensor_current_bpm_65)), sensor_OUT_reqWrite_66 == (False), _SafetyController_0_has_data_66 == (1), sensor_OUT_reqRead_66 == (False), sensor_OUT_value_66 == (sensor_current_bpm_65), monitor_IN_value_66 == monitor_IN_value_65, monitor_IN_reqRead_66 == monitor_IN_reqRead_65, monitor_IN_reqWrite_66 == monitor_IN_reqWrite_65), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_65) == (False))), monitor_IN_reqWrite_65), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_65) == ((_SafetyController_0_has_data_65) == (0)))), Not((monitor_IN_reqWrite_65) == (And(monitor_IN_reqRead_65, (_SafetyController_0_has_data_65) == (1))))), sensor_OUT_reqRead_65)), monitor_IN_reqWrite_65)), monitor_IN_reqWrite_66 == (False), monitor_IN_value_66 == (_SafetyController_0_buffered_status_65), _SafetyController_0_has_data_66 == (0), monitor_IN_reqRead_66 == (False), sensor_current_bpm_66 == sensor_current_bpm_65, sensor_OUT_value_66 == sensor_OUT_value_65, sensor_OUT_reqRead_66 == sensor_OUT_reqRead_65, sensor_OUT_reqWrite_66 == sensor_OUT_reqWrite_65, _SafetyController_0_buffered_status_66 == _SafetyController_0_buffered_status_65)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_66) == (sensor_OUT_reqWrite_66))), sensor_OUT_reqWrite_67 == (sensor_OUT_reqRead_66), sensor_current_bpm_67 == sensor_current_bpm_66, sensor_OUT_value_67 == sensor_OUT_value_66, sensor_OUT_reqRead_67 == sensor_OUT_reqRead_66, monitor_IN_value_67 == monitor_IN_value_66, monitor_IN_reqRead_67 == monitor_IN_reqRead_66, monitor_IN_reqWrite_67 == monitor_IN_reqWrite_66, _SafetyController_0_buffered_status_67 == _SafetyController_0_buffered_status_66, _SafetyController_0_has_data_67 == _SafetyController_0_has_data_66), 
    And(And(Not(False), (monitor_IN_reqRead_66) == (False)), monitor_IN_reqRead_67 == (True), sensor_current_bpm_67 == sensor_current_bpm_66, sensor_OUT_value_67 == sensor_OUT_value_66, sensor_OUT_reqRead_67 == sensor_OUT_reqRead_66, sensor_OUT_reqWrite_67 == sensor_OUT_reqWrite_66, monitor_IN_value_67 == monitor_IN_value_66, monitor_IN_reqWrite_67 == monitor_IN_reqWrite_66, _SafetyController_0_buffered_status_67 == _SafetyController_0_buffered_status_66, _SafetyController_0_has_data_67 == _SafetyController_0_has_data_66), 
    And(And(Not(False), Not((sensor_OUT_reqRead_66) == ((_SafetyController_0_has_data_66) == (0)))), sensor_OUT_reqRead_67 == ((_SafetyController_0_has_data_66) == (0)), sensor_current_bpm_67 == sensor_current_bpm_66, sensor_OUT_value_67 == sensor_OUT_value_66, sensor_OUT_reqWrite_67 == sensor_OUT_reqWrite_66, monitor_IN_value_67 == monitor_IN_value_66, monitor_IN_reqRead_67 == monitor_IN_reqRead_66, monitor_IN_reqWrite_67 == monitor_IN_reqWrite_66, _SafetyController_0_buffered_status_67 == _SafetyController_0_buffered_status_66, _SafetyController_0_has_data_67 == _SafetyController_0_has_data_66), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_66) == ((_SafetyController_0_has_data_66) == (0))))), Not((monitor_IN_reqWrite_66) == (And(monitor_IN_reqRead_66, (_SafetyController_0_has_data_66) == (1))))), monitor_IN_reqWrite_67 == (And(monitor_IN_reqRead_66, (_SafetyController_0_has_data_66) == (1))), sensor_current_bpm_67 == sensor_current_bpm_66, sensor_OUT_value_67 == sensor_OUT_value_66, sensor_OUT_reqRead_67 == sensor_OUT_reqRead_66, sensor_OUT_reqWrite_67 == sensor_OUT_reqWrite_66, monitor_IN_value_67 == monitor_IN_value_66, monitor_IN_reqRead_67 == monitor_IN_reqRead_66, _SafetyController_0_buffered_status_67 == _SafetyController_0_buffered_status_66, _SafetyController_0_has_data_67 == _SafetyController_0_has_data_66), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_66) == (sensor_OUT_reqWrite_66)))), sensor_OUT_reqWrite_66), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_66) == ((_SafetyController_0_has_data_66) == (0)))), Not((monitor_IN_reqWrite_66) == (And(monitor_IN_reqRead_66, (_SafetyController_0_has_data_66) == (1)))))), sensor_OUT_reqRead_66)), _SafetyController_0_buffered_status_67 == (If((sensor_current_bpm_66 > 100), 1, 0)), sensor_current_bpm_67 == (predict_next(sensor_current_bpm_66)), sensor_OUT_reqWrite_67 == (False), _SafetyController_0_has_data_67 == (1), sensor_OUT_reqRead_67 == (False), sensor_OUT_value_67 == (sensor_current_bpm_66), monitor_IN_value_67 == monitor_IN_value_66, monitor_IN_reqRead_67 == monitor_IN_reqRead_66, monitor_IN_reqWrite_67 == monitor_IN_reqWrite_66), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_66) == (False))), monitor_IN_reqWrite_66), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_66) == ((_SafetyController_0_has_data_66) == (0)))), Not((monitor_IN_reqWrite_66) == (And(monitor_IN_reqRead_66, (_SafetyController_0_has_data_66) == (1))))), sensor_OUT_reqRead_66)), monitor_IN_reqWrite_66)), monitor_IN_reqWrite_67 == (False), monitor_IN_value_67 == (_SafetyController_0_buffered_status_66), _SafetyController_0_has_data_67 == (0), monitor_IN_reqRead_67 == (False), sensor_current_bpm_67 == sensor_current_bpm_66, sensor_OUT_value_67 == sensor_OUT_value_66, sensor_OUT_reqRead_67 == sensor_OUT_reqRead_66, sensor_OUT_reqWrite_67 == sensor_OUT_reqWrite_66, _SafetyController_0_buffered_status_67 == _SafetyController_0_buffered_status_66)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_67) == (sensor_OUT_reqWrite_67))), sensor_OUT_reqWrite_68 == (sensor_OUT_reqRead_67), sensor_current_bpm_68 == sensor_current_bpm_67, sensor_OUT_value_68 == sensor_OUT_value_67, sensor_OUT_reqRead_68 == sensor_OUT_reqRead_67, monitor_IN_value_68 == monitor_IN_value_67, monitor_IN_reqRead_68 == monitor_IN_reqRead_67, monitor_IN_reqWrite_68 == monitor_IN_reqWrite_67, _SafetyController_0_buffered_status_68 == _SafetyController_0_buffered_status_67, _SafetyController_0_has_data_68 == _SafetyController_0_has_data_67), 
    And(And(Not(False), (monitor_IN_reqRead_67) == (False)), monitor_IN_reqRead_68 == (True), sensor_current_bpm_68 == sensor_current_bpm_67, sensor_OUT_value_68 == sensor_OUT_value_67, sensor_OUT_reqRead_68 == sensor_OUT_reqRead_67, sensor_OUT_reqWrite_68 == sensor_OUT_reqWrite_67, monitor_IN_value_68 == monitor_IN_value_67, monitor_IN_reqWrite_68 == monitor_IN_reqWrite_67, _SafetyController_0_buffered_status_68 == _SafetyController_0_buffered_status_67, _SafetyController_0_has_data_68 == _SafetyController_0_has_data_67), 
    And(And(Not(False), Not((sensor_OUT_reqRead_67) == ((_SafetyController_0_has_data_67) == (0)))), sensor_OUT_reqRead_68 == ((_SafetyController_0_has_data_67) == (0)), sensor_current_bpm_68 == sensor_current_bpm_67, sensor_OUT_value_68 == sensor_OUT_value_67, sensor_OUT_reqWrite_68 == sensor_OUT_reqWrite_67, monitor_IN_value_68 == monitor_IN_value_67, monitor_IN_reqRead_68 == monitor_IN_reqRead_67, monitor_IN_reqWrite_68 == monitor_IN_reqWrite_67, _SafetyController_0_buffered_status_68 == _SafetyController_0_buffered_status_67, _SafetyController_0_has_data_68 == _SafetyController_0_has_data_67), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_67) == ((_SafetyController_0_has_data_67) == (0))))), Not((monitor_IN_reqWrite_67) == (And(monitor_IN_reqRead_67, (_SafetyController_0_has_data_67) == (1))))), monitor_IN_reqWrite_68 == (And(monitor_IN_reqRead_67, (_SafetyController_0_has_data_67) == (1))), sensor_current_bpm_68 == sensor_current_bpm_67, sensor_OUT_value_68 == sensor_OUT_value_67, sensor_OUT_reqRead_68 == sensor_OUT_reqRead_67, sensor_OUT_reqWrite_68 == sensor_OUT_reqWrite_67, monitor_IN_value_68 == monitor_IN_value_67, monitor_IN_reqRead_68 == monitor_IN_reqRead_67, _SafetyController_0_buffered_status_68 == _SafetyController_0_buffered_status_67, _SafetyController_0_has_data_68 == _SafetyController_0_has_data_67), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_67) == (sensor_OUT_reqWrite_67)))), sensor_OUT_reqWrite_67), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_67) == ((_SafetyController_0_has_data_67) == (0)))), Not((monitor_IN_reqWrite_67) == (And(monitor_IN_reqRead_67, (_SafetyController_0_has_data_67) == (1)))))), sensor_OUT_reqRead_67)), _SafetyController_0_buffered_status_68 == (If((sensor_current_bpm_67 > 100), 1, 0)), sensor_current_bpm_68 == (predict_next(sensor_current_bpm_67)), sensor_OUT_reqWrite_68 == (False), _SafetyController_0_has_data_68 == (1), sensor_OUT_reqRead_68 == (False), sensor_OUT_value_68 == (sensor_current_bpm_67), monitor_IN_value_68 == monitor_IN_value_67, monitor_IN_reqRead_68 == monitor_IN_reqRead_67, monitor_IN_reqWrite_68 == monitor_IN_reqWrite_67), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_67) == (False))), monitor_IN_reqWrite_67), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_67) == ((_SafetyController_0_has_data_67) == (0)))), Not((monitor_IN_reqWrite_67) == (And(monitor_IN_reqRead_67, (_SafetyController_0_has_data_67) == (1))))), sensor_OUT_reqRead_67)), monitor_IN_reqWrite_67)), monitor_IN_reqWrite_68 == (False), monitor_IN_value_68 == (_SafetyController_0_buffered_status_67), _SafetyController_0_has_data_68 == (0), monitor_IN_reqRead_68 == (False), sensor_current_bpm_68 == sensor_current_bpm_67, sensor_OUT_value_68 == sensor_OUT_value_67, sensor_OUT_reqRead_68 == sensor_OUT_reqRead_67, sensor_OUT_reqWrite_68 == sensor_OUT_reqWrite_67, _SafetyController_0_buffered_status_68 == _SafetyController_0_buffered_status_67)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_68) == (sensor_OUT_reqWrite_68))), sensor_OUT_reqWrite_69 == (sensor_OUT_reqRead_68), sensor_current_bpm_69 == sensor_current_bpm_68, sensor_OUT_value_69 == sensor_OUT_value_68, sensor_OUT_reqRead_69 == sensor_OUT_reqRead_68, monitor_IN_value_69 == monitor_IN_value_68, monitor_IN_reqRead_69 == monitor_IN_reqRead_68, monitor_IN_reqWrite_69 == monitor_IN_reqWrite_68, _SafetyController_0_buffered_status_69 == _SafetyController_0_buffered_status_68, _SafetyController_0_has_data_69 == _SafetyController_0_has_data_68), 
    And(And(Not(False), (monitor_IN_reqRead_68) == (False)), monitor_IN_reqRead_69 == (True), sensor_current_bpm_69 == sensor_current_bpm_68, sensor_OUT_value_69 == sensor_OUT_value_68, sensor_OUT_reqRead_69 == sensor_OUT_reqRead_68, sensor_OUT_reqWrite_69 == sensor_OUT_reqWrite_68, monitor_IN_value_69 == monitor_IN_value_68, monitor_IN_reqWrite_69 == monitor_IN_reqWrite_68, _SafetyController_0_buffered_status_69 == _SafetyController_0_buffered_status_68, _SafetyController_0_has_data_69 == _SafetyController_0_has_data_68), 
    And(And(Not(False), Not((sensor_OUT_reqRead_68) == ((_SafetyController_0_has_data_68) == (0)))), sensor_OUT_reqRead_69 == ((_SafetyController_0_has_data_68) == (0)), sensor_current_bpm_69 == sensor_current_bpm_68, sensor_OUT_value_69 == sensor_OUT_value_68, sensor_OUT_reqWrite_69 == sensor_OUT_reqWrite_68, monitor_IN_value_69 == monitor_IN_value_68, monitor_IN_reqRead_69 == monitor_IN_reqRead_68, monitor_IN_reqWrite_69 == monitor_IN_reqWrite_68, _SafetyController_0_buffered_status_69 == _SafetyController_0_buffered_status_68, _SafetyController_0_has_data_69 == _SafetyController_0_has_data_68), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_68) == ((_SafetyController_0_has_data_68) == (0))))), Not((monitor_IN_reqWrite_68) == (And(monitor_IN_reqRead_68, (_SafetyController_0_has_data_68) == (1))))), monitor_IN_reqWrite_69 == (And(monitor_IN_reqRead_68, (_SafetyController_0_has_data_68) == (1))), sensor_current_bpm_69 == sensor_current_bpm_68, sensor_OUT_value_69 == sensor_OUT_value_68, sensor_OUT_reqRead_69 == sensor_OUT_reqRead_68, sensor_OUT_reqWrite_69 == sensor_OUT_reqWrite_68, monitor_IN_value_69 == monitor_IN_value_68, monitor_IN_reqRead_69 == monitor_IN_reqRead_68, _SafetyController_0_buffered_status_69 == _SafetyController_0_buffered_status_68, _SafetyController_0_has_data_69 == _SafetyController_0_has_data_68), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_68) == (sensor_OUT_reqWrite_68)))), sensor_OUT_reqWrite_68), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_68) == ((_SafetyController_0_has_data_68) == (0)))), Not((monitor_IN_reqWrite_68) == (And(monitor_IN_reqRead_68, (_SafetyController_0_has_data_68) == (1)))))), sensor_OUT_reqRead_68)), _SafetyController_0_buffered_status_69 == (If((sensor_current_bpm_68 > 100), 1, 0)), sensor_current_bpm_69 == (predict_next(sensor_current_bpm_68)), sensor_OUT_reqWrite_69 == (False), _SafetyController_0_has_data_69 == (1), sensor_OUT_reqRead_69 == (False), sensor_OUT_value_69 == (sensor_current_bpm_68), monitor_IN_value_69 == monitor_IN_value_68, monitor_IN_reqRead_69 == monitor_IN_reqRead_68, monitor_IN_reqWrite_69 == monitor_IN_reqWrite_68), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_68) == (False))), monitor_IN_reqWrite_68), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_68) == ((_SafetyController_0_has_data_68) == (0)))), Not((monitor_IN_reqWrite_68) == (And(monitor_IN_reqRead_68, (_SafetyController_0_has_data_68) == (1))))), sensor_OUT_reqRead_68)), monitor_IN_reqWrite_68)), monitor_IN_reqWrite_69 == (False), monitor_IN_value_69 == (_SafetyController_0_buffered_status_68), _SafetyController_0_has_data_69 == (0), monitor_IN_reqRead_69 == (False), sensor_current_bpm_69 == sensor_current_bpm_68, sensor_OUT_value_69 == sensor_OUT_value_68, sensor_OUT_reqRead_69 == sensor_OUT_reqRead_68, sensor_OUT_reqWrite_69 == sensor_OUT_reqWrite_68, _SafetyController_0_buffered_status_69 == _SafetyController_0_buffered_status_68)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_69) == (sensor_OUT_reqWrite_69))), sensor_OUT_reqWrite_70 == (sensor_OUT_reqRead_69), sensor_current_bpm_70 == sensor_current_bpm_69, sensor_OUT_value_70 == sensor_OUT_value_69, sensor_OUT_reqRead_70 == sensor_OUT_reqRead_69, monitor_IN_value_70 == monitor_IN_value_69, monitor_IN_reqRead_70 == monitor_IN_reqRead_69, monitor_IN_reqWrite_70 == monitor_IN_reqWrite_69, _SafetyController_0_buffered_status_70 == _SafetyController_0_buffered_status_69, _SafetyController_0_has_data_70 == _SafetyController_0_has_data_69), 
    And(And(Not(False), (monitor_IN_reqRead_69) == (False)), monitor_IN_reqRead_70 == (True), sensor_current_bpm_70 == sensor_current_bpm_69, sensor_OUT_value_70 == sensor_OUT_value_69, sensor_OUT_reqRead_70 == sensor_OUT_reqRead_69, sensor_OUT_reqWrite_70 == sensor_OUT_reqWrite_69, monitor_IN_value_70 == monitor_IN_value_69, monitor_IN_reqWrite_70 == monitor_IN_reqWrite_69, _SafetyController_0_buffered_status_70 == _SafetyController_0_buffered_status_69, _SafetyController_0_has_data_70 == _SafetyController_0_has_data_69), 
    And(And(Not(False), Not((sensor_OUT_reqRead_69) == ((_SafetyController_0_has_data_69) == (0)))), sensor_OUT_reqRead_70 == ((_SafetyController_0_has_data_69) == (0)), sensor_current_bpm_70 == sensor_current_bpm_69, sensor_OUT_value_70 == sensor_OUT_value_69, sensor_OUT_reqWrite_70 == sensor_OUT_reqWrite_69, monitor_IN_value_70 == monitor_IN_value_69, monitor_IN_reqRead_70 == monitor_IN_reqRead_69, monitor_IN_reqWrite_70 == monitor_IN_reqWrite_69, _SafetyController_0_buffered_status_70 == _SafetyController_0_buffered_status_69, _SafetyController_0_has_data_70 == _SafetyController_0_has_data_69), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_69) == ((_SafetyController_0_has_data_69) == (0))))), Not((monitor_IN_reqWrite_69) == (And(monitor_IN_reqRead_69, (_SafetyController_0_has_data_69) == (1))))), monitor_IN_reqWrite_70 == (And(monitor_IN_reqRead_69, (_SafetyController_0_has_data_69) == (1))), sensor_current_bpm_70 == sensor_current_bpm_69, sensor_OUT_value_70 == sensor_OUT_value_69, sensor_OUT_reqRead_70 == sensor_OUT_reqRead_69, sensor_OUT_reqWrite_70 == sensor_OUT_reqWrite_69, monitor_IN_value_70 == monitor_IN_value_69, monitor_IN_reqRead_70 == monitor_IN_reqRead_69, _SafetyController_0_buffered_status_70 == _SafetyController_0_buffered_status_69, _SafetyController_0_has_data_70 == _SafetyController_0_has_data_69), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_69) == (sensor_OUT_reqWrite_69)))), sensor_OUT_reqWrite_69), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_69) == ((_SafetyController_0_has_data_69) == (0)))), Not((monitor_IN_reqWrite_69) == (And(monitor_IN_reqRead_69, (_SafetyController_0_has_data_69) == (1)))))), sensor_OUT_reqRead_69)), _SafetyController_0_buffered_status_70 == (If((sensor_current_bpm_69 > 100), 1, 0)), sensor_current_bpm_70 == (predict_next(sensor_current_bpm_69)), sensor_OUT_reqWrite_70 == (False), _SafetyController_0_has_data_70 == (1), sensor_OUT_reqRead_70 == (False), sensor_OUT_value_70 == (sensor_current_bpm_69), monitor_IN_value_70 == monitor_IN_value_69, monitor_IN_reqRead_70 == monitor_IN_reqRead_69, monitor_IN_reqWrite_70 == monitor_IN_reqWrite_69), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_69) == (False))), monitor_IN_reqWrite_69), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_69) == ((_SafetyController_0_has_data_69) == (0)))), Not((monitor_IN_reqWrite_69) == (And(monitor_IN_reqRead_69, (_SafetyController_0_has_data_69) == (1))))), sensor_OUT_reqRead_69)), monitor_IN_reqWrite_69)), monitor_IN_reqWrite_70 == (False), monitor_IN_value_70 == (_SafetyController_0_buffered_status_69), _SafetyController_0_has_data_70 == (0), monitor_IN_reqRead_70 == (False), sensor_current_bpm_70 == sensor_current_bpm_69, sensor_OUT_value_70 == sensor_OUT_value_69, sensor_OUT_reqRead_70 == sensor_OUT_reqRead_69, sensor_OUT_reqWrite_70 == sensor_OUT_reqWrite_69, _SafetyController_0_buffered_status_70 == _SafetyController_0_buffered_status_69)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_70) == (sensor_OUT_reqWrite_70))), sensor_OUT_reqWrite_71 == (sensor_OUT_reqRead_70), sensor_current_bpm_71 == sensor_current_bpm_70, sensor_OUT_value_71 == sensor_OUT_value_70, sensor_OUT_reqRead_71 == sensor_OUT_reqRead_70, monitor_IN_value_71 == monitor_IN_value_70, monitor_IN_reqRead_71 == monitor_IN_reqRead_70, monitor_IN_reqWrite_71 == monitor_IN_reqWrite_70, _SafetyController_0_buffered_status_71 == _SafetyController_0_buffered_status_70, _SafetyController_0_has_data_71 == _SafetyController_0_has_data_70), 
    And(And(Not(False), (monitor_IN_reqRead_70) == (False)), monitor_IN_reqRead_71 == (True), sensor_current_bpm_71 == sensor_current_bpm_70, sensor_OUT_value_71 == sensor_OUT_value_70, sensor_OUT_reqRead_71 == sensor_OUT_reqRead_70, sensor_OUT_reqWrite_71 == sensor_OUT_reqWrite_70, monitor_IN_value_71 == monitor_IN_value_70, monitor_IN_reqWrite_71 == monitor_IN_reqWrite_70, _SafetyController_0_buffered_status_71 == _SafetyController_0_buffered_status_70, _SafetyController_0_has_data_71 == _SafetyController_0_has_data_70), 
    And(And(Not(False), Not((sensor_OUT_reqRead_70) == ((_SafetyController_0_has_data_70) == (0)))), sensor_OUT_reqRead_71 == ((_SafetyController_0_has_data_70) == (0)), sensor_current_bpm_71 == sensor_current_bpm_70, sensor_OUT_value_71 == sensor_OUT_value_70, sensor_OUT_reqWrite_71 == sensor_OUT_reqWrite_70, monitor_IN_value_71 == monitor_IN_value_70, monitor_IN_reqRead_71 == monitor_IN_reqRead_70, monitor_IN_reqWrite_71 == monitor_IN_reqWrite_70, _SafetyController_0_buffered_status_71 == _SafetyController_0_buffered_status_70, _SafetyController_0_has_data_71 == _SafetyController_0_has_data_70), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_70) == ((_SafetyController_0_has_data_70) == (0))))), Not((monitor_IN_reqWrite_70) == (And(monitor_IN_reqRead_70, (_SafetyController_0_has_data_70) == (1))))), monitor_IN_reqWrite_71 == (And(monitor_IN_reqRead_70, (_SafetyController_0_has_data_70) == (1))), sensor_current_bpm_71 == sensor_current_bpm_70, sensor_OUT_value_71 == sensor_OUT_value_70, sensor_OUT_reqRead_71 == sensor_OUT_reqRead_70, sensor_OUT_reqWrite_71 == sensor_OUT_reqWrite_70, monitor_IN_value_71 == monitor_IN_value_70, monitor_IN_reqRead_71 == monitor_IN_reqRead_70, _SafetyController_0_buffered_status_71 == _SafetyController_0_buffered_status_70, _SafetyController_0_has_data_71 == _SafetyController_0_has_data_70), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_70) == (sensor_OUT_reqWrite_70)))), sensor_OUT_reqWrite_70), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_70) == ((_SafetyController_0_has_data_70) == (0)))), Not((monitor_IN_reqWrite_70) == (And(monitor_IN_reqRead_70, (_SafetyController_0_has_data_70) == (1)))))), sensor_OUT_reqRead_70)), _SafetyController_0_buffered_status_71 == (If((sensor_current_bpm_70 > 100), 1, 0)), sensor_current_bpm_71 == (predict_next(sensor_current_bpm_70)), sensor_OUT_reqWrite_71 == (False), _SafetyController_0_has_data_71 == (1), sensor_OUT_reqRead_71 == (False), sensor_OUT_value_71 == (sensor_current_bpm_70), monitor_IN_value_71 == monitor_IN_value_70, monitor_IN_reqRead_71 == monitor_IN_reqRead_70, monitor_IN_reqWrite_71 == monitor_IN_reqWrite_70), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_70) == (False))), monitor_IN_reqWrite_70), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_70) == ((_SafetyController_0_has_data_70) == (0)))), Not((monitor_IN_reqWrite_70) == (And(monitor_IN_reqRead_70, (_SafetyController_0_has_data_70) == (1))))), sensor_OUT_reqRead_70)), monitor_IN_reqWrite_70)), monitor_IN_reqWrite_71 == (False), monitor_IN_value_71 == (_SafetyController_0_buffered_status_70), _SafetyController_0_has_data_71 == (0), monitor_IN_reqRead_71 == (False), sensor_current_bpm_71 == sensor_current_bpm_70, sensor_OUT_value_71 == sensor_OUT_value_70, sensor_OUT_reqRead_71 == sensor_OUT_reqRead_70, sensor_OUT_reqWrite_71 == sensor_OUT_reqWrite_70, _SafetyController_0_buffered_status_71 == _SafetyController_0_buffered_status_70)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_71) == (sensor_OUT_reqWrite_71))), sensor_OUT_reqWrite_72 == (sensor_OUT_reqRead_71), sensor_current_bpm_72 == sensor_current_bpm_71, sensor_OUT_value_72 == sensor_OUT_value_71, sensor_OUT_reqRead_72 == sensor_OUT_reqRead_71, monitor_IN_value_72 == monitor_IN_value_71, monitor_IN_reqRead_72 == monitor_IN_reqRead_71, monitor_IN_reqWrite_72 == monitor_IN_reqWrite_71, _SafetyController_0_buffered_status_72 == _SafetyController_0_buffered_status_71, _SafetyController_0_has_data_72 == _SafetyController_0_has_data_71), 
    And(And(Not(False), (monitor_IN_reqRead_71) == (False)), monitor_IN_reqRead_72 == (True), sensor_current_bpm_72 == sensor_current_bpm_71, sensor_OUT_value_72 == sensor_OUT_value_71, sensor_OUT_reqRead_72 == sensor_OUT_reqRead_71, sensor_OUT_reqWrite_72 == sensor_OUT_reqWrite_71, monitor_IN_value_72 == monitor_IN_value_71, monitor_IN_reqWrite_72 == monitor_IN_reqWrite_71, _SafetyController_0_buffered_status_72 == _SafetyController_0_buffered_status_71, _SafetyController_0_has_data_72 == _SafetyController_0_has_data_71), 
    And(And(Not(False), Not((sensor_OUT_reqRead_71) == ((_SafetyController_0_has_data_71) == (0)))), sensor_OUT_reqRead_72 == ((_SafetyController_0_has_data_71) == (0)), sensor_current_bpm_72 == sensor_current_bpm_71, sensor_OUT_value_72 == sensor_OUT_value_71, sensor_OUT_reqWrite_72 == sensor_OUT_reqWrite_71, monitor_IN_value_72 == monitor_IN_value_71, monitor_IN_reqRead_72 == monitor_IN_reqRead_71, monitor_IN_reqWrite_72 == monitor_IN_reqWrite_71, _SafetyController_0_buffered_status_72 == _SafetyController_0_buffered_status_71, _SafetyController_0_has_data_72 == _SafetyController_0_has_data_71), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_71) == ((_SafetyController_0_has_data_71) == (0))))), Not((monitor_IN_reqWrite_71) == (And(monitor_IN_reqRead_71, (_SafetyController_0_has_data_71) == (1))))), monitor_IN_reqWrite_72 == (And(monitor_IN_reqRead_71, (_SafetyController_0_has_data_71) == (1))), sensor_current_bpm_72 == sensor_current_bpm_71, sensor_OUT_value_72 == sensor_OUT_value_71, sensor_OUT_reqRead_72 == sensor_OUT_reqRead_71, sensor_OUT_reqWrite_72 == sensor_OUT_reqWrite_71, monitor_IN_value_72 == monitor_IN_value_71, monitor_IN_reqRead_72 == monitor_IN_reqRead_71, _SafetyController_0_buffered_status_72 == _SafetyController_0_buffered_status_71, _SafetyController_0_has_data_72 == _SafetyController_0_has_data_71), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_71) == (sensor_OUT_reqWrite_71)))), sensor_OUT_reqWrite_71), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_71) == ((_SafetyController_0_has_data_71) == (0)))), Not((monitor_IN_reqWrite_71) == (And(monitor_IN_reqRead_71, (_SafetyController_0_has_data_71) == (1)))))), sensor_OUT_reqRead_71)), _SafetyController_0_buffered_status_72 == (If((sensor_current_bpm_71 > 100), 1, 0)), sensor_current_bpm_72 == (predict_next(sensor_current_bpm_71)), sensor_OUT_reqWrite_72 == (False), _SafetyController_0_has_data_72 == (1), sensor_OUT_reqRead_72 == (False), sensor_OUT_value_72 == (sensor_current_bpm_71), monitor_IN_value_72 == monitor_IN_value_71, monitor_IN_reqRead_72 == monitor_IN_reqRead_71, monitor_IN_reqWrite_72 == monitor_IN_reqWrite_71), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_71) == (False))), monitor_IN_reqWrite_71), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_71) == ((_SafetyController_0_has_data_71) == (0)))), Not((monitor_IN_reqWrite_71) == (And(monitor_IN_reqRead_71, (_SafetyController_0_has_data_71) == (1))))), sensor_OUT_reqRead_71)), monitor_IN_reqWrite_71)), monitor_IN_reqWrite_72 == (False), monitor_IN_value_72 == (_SafetyController_0_buffered_status_71), _SafetyController_0_has_data_72 == (0), monitor_IN_reqRead_72 == (False), sensor_current_bpm_72 == sensor_current_bpm_71, sensor_OUT_value_72 == sensor_OUT_value_71, sensor_OUT_reqRead_72 == sensor_OUT_reqRead_71, sensor_OUT_reqWrite_72 == sensor_OUT_reqWrite_71, _SafetyController_0_buffered_status_72 == _SafetyController_0_buffered_status_71)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_72) == (sensor_OUT_reqWrite_72))), sensor_OUT_reqWrite_73 == (sensor_OUT_reqRead_72), sensor_current_bpm_73 == sensor_current_bpm_72, sensor_OUT_value_73 == sensor_OUT_value_72, sensor_OUT_reqRead_73 == sensor_OUT_reqRead_72, monitor_IN_value_73 == monitor_IN_value_72, monitor_IN_reqRead_73 == monitor_IN_reqRead_72, monitor_IN_reqWrite_73 == monitor_IN_reqWrite_72, _SafetyController_0_buffered_status_73 == _SafetyController_0_buffered_status_72, _SafetyController_0_has_data_73 == _SafetyController_0_has_data_72), 
    And(And(Not(False), (monitor_IN_reqRead_72) == (False)), monitor_IN_reqRead_73 == (True), sensor_current_bpm_73 == sensor_current_bpm_72, sensor_OUT_value_73 == sensor_OUT_value_72, sensor_OUT_reqRead_73 == sensor_OUT_reqRead_72, sensor_OUT_reqWrite_73 == sensor_OUT_reqWrite_72, monitor_IN_value_73 == monitor_IN_value_72, monitor_IN_reqWrite_73 == monitor_IN_reqWrite_72, _SafetyController_0_buffered_status_73 == _SafetyController_0_buffered_status_72, _SafetyController_0_has_data_73 == _SafetyController_0_has_data_72), 
    And(And(Not(False), Not((sensor_OUT_reqRead_72) == ((_SafetyController_0_has_data_72) == (0)))), sensor_OUT_reqRead_73 == ((_SafetyController_0_has_data_72) == (0)), sensor_current_bpm_73 == sensor_current_bpm_72, sensor_OUT_value_73 == sensor_OUT_value_72, sensor_OUT_reqWrite_73 == sensor_OUT_reqWrite_72, monitor_IN_value_73 == monitor_IN_value_72, monitor_IN_reqRead_73 == monitor_IN_reqRead_72, monitor_IN_reqWrite_73 == monitor_IN_reqWrite_72, _SafetyController_0_buffered_status_73 == _SafetyController_0_buffered_status_72, _SafetyController_0_has_data_73 == _SafetyController_0_has_data_72), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_72) == ((_SafetyController_0_has_data_72) == (0))))), Not((monitor_IN_reqWrite_72) == (And(monitor_IN_reqRead_72, (_SafetyController_0_has_data_72) == (1))))), monitor_IN_reqWrite_73 == (And(monitor_IN_reqRead_72, (_SafetyController_0_has_data_72) == (1))), sensor_current_bpm_73 == sensor_current_bpm_72, sensor_OUT_value_73 == sensor_OUT_value_72, sensor_OUT_reqRead_73 == sensor_OUT_reqRead_72, sensor_OUT_reqWrite_73 == sensor_OUT_reqWrite_72, monitor_IN_value_73 == monitor_IN_value_72, monitor_IN_reqRead_73 == monitor_IN_reqRead_72, _SafetyController_0_buffered_status_73 == _SafetyController_0_buffered_status_72, _SafetyController_0_has_data_73 == _SafetyController_0_has_data_72), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_72) == (sensor_OUT_reqWrite_72)))), sensor_OUT_reqWrite_72), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_72) == ((_SafetyController_0_has_data_72) == (0)))), Not((monitor_IN_reqWrite_72) == (And(monitor_IN_reqRead_72, (_SafetyController_0_has_data_72) == (1)))))), sensor_OUT_reqRead_72)), _SafetyController_0_buffered_status_73 == (If((sensor_current_bpm_72 > 100), 1, 0)), sensor_current_bpm_73 == (predict_next(sensor_current_bpm_72)), sensor_OUT_reqWrite_73 == (False), _SafetyController_0_has_data_73 == (1), sensor_OUT_reqRead_73 == (False), sensor_OUT_value_73 == (sensor_current_bpm_72), monitor_IN_value_73 == monitor_IN_value_72, monitor_IN_reqRead_73 == monitor_IN_reqRead_72, monitor_IN_reqWrite_73 == monitor_IN_reqWrite_72), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_72) == (False))), monitor_IN_reqWrite_72), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_72) == ((_SafetyController_0_has_data_72) == (0)))), Not((monitor_IN_reqWrite_72) == (And(monitor_IN_reqRead_72, (_SafetyController_0_has_data_72) == (1))))), sensor_OUT_reqRead_72)), monitor_IN_reqWrite_72)), monitor_IN_reqWrite_73 == (False), monitor_IN_value_73 == (_SafetyController_0_buffered_status_72), _SafetyController_0_has_data_73 == (0), monitor_IN_reqRead_73 == (False), sensor_current_bpm_73 == sensor_current_bpm_72, sensor_OUT_value_73 == sensor_OUT_value_72, sensor_OUT_reqRead_73 == sensor_OUT_reqRead_72, sensor_OUT_reqWrite_73 == sensor_OUT_reqWrite_72, _SafetyController_0_buffered_status_73 == _SafetyController_0_buffered_status_72)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_73) == (sensor_OUT_reqWrite_73))), sensor_OUT_reqWrite_74 == (sensor_OUT_reqRead_73), sensor_current_bpm_74 == sensor_current_bpm_73, sensor_OUT_value_74 == sensor_OUT_value_73, sensor_OUT_reqRead_74 == sensor_OUT_reqRead_73, monitor_IN_value_74 == monitor_IN_value_73, monitor_IN_reqRead_74 == monitor_IN_reqRead_73, monitor_IN_reqWrite_74 == monitor_IN_reqWrite_73, _SafetyController_0_buffered_status_74 == _SafetyController_0_buffered_status_73, _SafetyController_0_has_data_74 == _SafetyController_0_has_data_73), 
    And(And(Not(False), (monitor_IN_reqRead_73) == (False)), monitor_IN_reqRead_74 == (True), sensor_current_bpm_74 == sensor_current_bpm_73, sensor_OUT_value_74 == sensor_OUT_value_73, sensor_OUT_reqRead_74 == sensor_OUT_reqRead_73, sensor_OUT_reqWrite_74 == sensor_OUT_reqWrite_73, monitor_IN_value_74 == monitor_IN_value_73, monitor_IN_reqWrite_74 == monitor_IN_reqWrite_73, _SafetyController_0_buffered_status_74 == _SafetyController_0_buffered_status_73, _SafetyController_0_has_data_74 == _SafetyController_0_has_data_73), 
    And(And(Not(False), Not((sensor_OUT_reqRead_73) == ((_SafetyController_0_has_data_73) == (0)))), sensor_OUT_reqRead_74 == ((_SafetyController_0_has_data_73) == (0)), sensor_current_bpm_74 == sensor_current_bpm_73, sensor_OUT_value_74 == sensor_OUT_value_73, sensor_OUT_reqWrite_74 == sensor_OUT_reqWrite_73, monitor_IN_value_74 == monitor_IN_value_73, monitor_IN_reqRead_74 == monitor_IN_reqRead_73, monitor_IN_reqWrite_74 == monitor_IN_reqWrite_73, _SafetyController_0_buffered_status_74 == _SafetyController_0_buffered_status_73, _SafetyController_0_has_data_74 == _SafetyController_0_has_data_73), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_73) == ((_SafetyController_0_has_data_73) == (0))))), Not((monitor_IN_reqWrite_73) == (And(monitor_IN_reqRead_73, (_SafetyController_0_has_data_73) == (1))))), monitor_IN_reqWrite_74 == (And(monitor_IN_reqRead_73, (_SafetyController_0_has_data_73) == (1))), sensor_current_bpm_74 == sensor_current_bpm_73, sensor_OUT_value_74 == sensor_OUT_value_73, sensor_OUT_reqRead_74 == sensor_OUT_reqRead_73, sensor_OUT_reqWrite_74 == sensor_OUT_reqWrite_73, monitor_IN_value_74 == monitor_IN_value_73, monitor_IN_reqRead_74 == monitor_IN_reqRead_73, _SafetyController_0_buffered_status_74 == _SafetyController_0_buffered_status_73, _SafetyController_0_has_data_74 == _SafetyController_0_has_data_73), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_73) == (sensor_OUT_reqWrite_73)))), sensor_OUT_reqWrite_73), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_73) == ((_SafetyController_0_has_data_73) == (0)))), Not((monitor_IN_reqWrite_73) == (And(monitor_IN_reqRead_73, (_SafetyController_0_has_data_73) == (1)))))), sensor_OUT_reqRead_73)), _SafetyController_0_buffered_status_74 == (If((sensor_current_bpm_73 > 100), 1, 0)), sensor_current_bpm_74 == (predict_next(sensor_current_bpm_73)), sensor_OUT_reqWrite_74 == (False), _SafetyController_0_has_data_74 == (1), sensor_OUT_reqRead_74 == (False), sensor_OUT_value_74 == (sensor_current_bpm_73), monitor_IN_value_74 == monitor_IN_value_73, monitor_IN_reqRead_74 == monitor_IN_reqRead_73, monitor_IN_reqWrite_74 == monitor_IN_reqWrite_73), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_73) == (False))), monitor_IN_reqWrite_73), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_73) == ((_SafetyController_0_has_data_73) == (0)))), Not((monitor_IN_reqWrite_73) == (And(monitor_IN_reqRead_73, (_SafetyController_0_has_data_73) == (1))))), sensor_OUT_reqRead_73)), monitor_IN_reqWrite_73)), monitor_IN_reqWrite_74 == (False), monitor_IN_value_74 == (_SafetyController_0_buffered_status_73), _SafetyController_0_has_data_74 == (0), monitor_IN_reqRead_74 == (False), sensor_current_bpm_74 == sensor_current_bpm_73, sensor_OUT_value_74 == sensor_OUT_value_73, sensor_OUT_reqRead_74 == sensor_OUT_reqRead_73, sensor_OUT_reqWrite_74 == sensor_OUT_reqWrite_73, _SafetyController_0_buffered_status_74 == _SafetyController_0_buffered_status_73)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_74) == (sensor_OUT_reqWrite_74))), sensor_OUT_reqWrite_75 == (sensor_OUT_reqRead_74), sensor_current_bpm_75 == sensor_current_bpm_74, sensor_OUT_value_75 == sensor_OUT_value_74, sensor_OUT_reqRead_75 == sensor_OUT_reqRead_74, monitor_IN_value_75 == monitor_IN_value_74, monitor_IN_reqRead_75 == monitor_IN_reqRead_74, monitor_IN_reqWrite_75 == monitor_IN_reqWrite_74, _SafetyController_0_buffered_status_75 == _SafetyController_0_buffered_status_74, _SafetyController_0_has_data_75 == _SafetyController_0_has_data_74), 
    And(And(Not(False), (monitor_IN_reqRead_74) == (False)), monitor_IN_reqRead_75 == (True), sensor_current_bpm_75 == sensor_current_bpm_74, sensor_OUT_value_75 == sensor_OUT_value_74, sensor_OUT_reqRead_75 == sensor_OUT_reqRead_74, sensor_OUT_reqWrite_75 == sensor_OUT_reqWrite_74, monitor_IN_value_75 == monitor_IN_value_74, monitor_IN_reqWrite_75 == monitor_IN_reqWrite_74, _SafetyController_0_buffered_status_75 == _SafetyController_0_buffered_status_74, _SafetyController_0_has_data_75 == _SafetyController_0_has_data_74), 
    And(And(Not(False), Not((sensor_OUT_reqRead_74) == ((_SafetyController_0_has_data_74) == (0)))), sensor_OUT_reqRead_75 == ((_SafetyController_0_has_data_74) == (0)), sensor_current_bpm_75 == sensor_current_bpm_74, sensor_OUT_value_75 == sensor_OUT_value_74, sensor_OUT_reqWrite_75 == sensor_OUT_reqWrite_74, monitor_IN_value_75 == monitor_IN_value_74, monitor_IN_reqRead_75 == monitor_IN_reqRead_74, monitor_IN_reqWrite_75 == monitor_IN_reqWrite_74, _SafetyController_0_buffered_status_75 == _SafetyController_0_buffered_status_74, _SafetyController_0_has_data_75 == _SafetyController_0_has_data_74), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_74) == ((_SafetyController_0_has_data_74) == (0))))), Not((monitor_IN_reqWrite_74) == (And(monitor_IN_reqRead_74, (_SafetyController_0_has_data_74) == (1))))), monitor_IN_reqWrite_75 == (And(monitor_IN_reqRead_74, (_SafetyController_0_has_data_74) == (1))), sensor_current_bpm_75 == sensor_current_bpm_74, sensor_OUT_value_75 == sensor_OUT_value_74, sensor_OUT_reqRead_75 == sensor_OUT_reqRead_74, sensor_OUT_reqWrite_75 == sensor_OUT_reqWrite_74, monitor_IN_value_75 == monitor_IN_value_74, monitor_IN_reqRead_75 == monitor_IN_reqRead_74, _SafetyController_0_buffered_status_75 == _SafetyController_0_buffered_status_74, _SafetyController_0_has_data_75 == _SafetyController_0_has_data_74), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_74) == (sensor_OUT_reqWrite_74)))), sensor_OUT_reqWrite_74), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_74) == ((_SafetyController_0_has_data_74) == (0)))), Not((monitor_IN_reqWrite_74) == (And(monitor_IN_reqRead_74, (_SafetyController_0_has_data_74) == (1)))))), sensor_OUT_reqRead_74)), _SafetyController_0_buffered_status_75 == (If((sensor_current_bpm_74 > 100), 1, 0)), sensor_current_bpm_75 == (predict_next(sensor_current_bpm_74)), sensor_OUT_reqWrite_75 == (False), _SafetyController_0_has_data_75 == (1), sensor_OUT_reqRead_75 == (False), sensor_OUT_value_75 == (sensor_current_bpm_74), monitor_IN_value_75 == monitor_IN_value_74, monitor_IN_reqRead_75 == monitor_IN_reqRead_74, monitor_IN_reqWrite_75 == monitor_IN_reqWrite_74), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_74) == (False))), monitor_IN_reqWrite_74), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_74) == ((_SafetyController_0_has_data_74) == (0)))), Not((monitor_IN_reqWrite_74) == (And(monitor_IN_reqRead_74, (_SafetyController_0_has_data_74) == (1))))), sensor_OUT_reqRead_74)), monitor_IN_reqWrite_74)), monitor_IN_reqWrite_75 == (False), monitor_IN_value_75 == (_SafetyController_0_buffered_status_74), _SafetyController_0_has_data_75 == (0), monitor_IN_reqRead_75 == (False), sensor_current_bpm_75 == sensor_current_bpm_74, sensor_OUT_value_75 == sensor_OUT_value_74, sensor_OUT_reqRead_75 == sensor_OUT_reqRead_74, sensor_OUT_reqWrite_75 == sensor_OUT_reqWrite_74, _SafetyController_0_buffered_status_75 == _SafetyController_0_buffered_status_74)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_75) == (sensor_OUT_reqWrite_75))), sensor_OUT_reqWrite_76 == (sensor_OUT_reqRead_75), sensor_current_bpm_76 == sensor_current_bpm_75, sensor_OUT_value_76 == sensor_OUT_value_75, sensor_OUT_reqRead_76 == sensor_OUT_reqRead_75, monitor_IN_value_76 == monitor_IN_value_75, monitor_IN_reqRead_76 == monitor_IN_reqRead_75, monitor_IN_reqWrite_76 == monitor_IN_reqWrite_75, _SafetyController_0_buffered_status_76 == _SafetyController_0_buffered_status_75, _SafetyController_0_has_data_76 == _SafetyController_0_has_data_75), 
    And(And(Not(False), (monitor_IN_reqRead_75) == (False)), monitor_IN_reqRead_76 == (True), sensor_current_bpm_76 == sensor_current_bpm_75, sensor_OUT_value_76 == sensor_OUT_value_75, sensor_OUT_reqRead_76 == sensor_OUT_reqRead_75, sensor_OUT_reqWrite_76 == sensor_OUT_reqWrite_75, monitor_IN_value_76 == monitor_IN_value_75, monitor_IN_reqWrite_76 == monitor_IN_reqWrite_75, _SafetyController_0_buffered_status_76 == _SafetyController_0_buffered_status_75, _SafetyController_0_has_data_76 == _SafetyController_0_has_data_75), 
    And(And(Not(False), Not((sensor_OUT_reqRead_75) == ((_SafetyController_0_has_data_75) == (0)))), sensor_OUT_reqRead_76 == ((_SafetyController_0_has_data_75) == (0)), sensor_current_bpm_76 == sensor_current_bpm_75, sensor_OUT_value_76 == sensor_OUT_value_75, sensor_OUT_reqWrite_76 == sensor_OUT_reqWrite_75, monitor_IN_value_76 == monitor_IN_value_75, monitor_IN_reqRead_76 == monitor_IN_reqRead_75, monitor_IN_reqWrite_76 == monitor_IN_reqWrite_75, _SafetyController_0_buffered_status_76 == _SafetyController_0_buffered_status_75, _SafetyController_0_has_data_76 == _SafetyController_0_has_data_75), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_75) == ((_SafetyController_0_has_data_75) == (0))))), Not((monitor_IN_reqWrite_75) == (And(monitor_IN_reqRead_75, (_SafetyController_0_has_data_75) == (1))))), monitor_IN_reqWrite_76 == (And(monitor_IN_reqRead_75, (_SafetyController_0_has_data_75) == (1))), sensor_current_bpm_76 == sensor_current_bpm_75, sensor_OUT_value_76 == sensor_OUT_value_75, sensor_OUT_reqRead_76 == sensor_OUT_reqRead_75, sensor_OUT_reqWrite_76 == sensor_OUT_reqWrite_75, monitor_IN_value_76 == monitor_IN_value_75, monitor_IN_reqRead_76 == monitor_IN_reqRead_75, _SafetyController_0_buffered_status_76 == _SafetyController_0_buffered_status_75, _SafetyController_0_has_data_76 == _SafetyController_0_has_data_75), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_75) == (sensor_OUT_reqWrite_75)))), sensor_OUT_reqWrite_75), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_75) == ((_SafetyController_0_has_data_75) == (0)))), Not((monitor_IN_reqWrite_75) == (And(monitor_IN_reqRead_75, (_SafetyController_0_has_data_75) == (1)))))), sensor_OUT_reqRead_75)), _SafetyController_0_buffered_status_76 == (If((sensor_current_bpm_75 > 100), 1, 0)), sensor_current_bpm_76 == (predict_next(sensor_current_bpm_75)), sensor_OUT_reqWrite_76 == (False), _SafetyController_0_has_data_76 == (1), sensor_OUT_reqRead_76 == (False), sensor_OUT_value_76 == (sensor_current_bpm_75), monitor_IN_value_76 == monitor_IN_value_75, monitor_IN_reqRead_76 == monitor_IN_reqRead_75, monitor_IN_reqWrite_76 == monitor_IN_reqWrite_75), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_75) == (False))), monitor_IN_reqWrite_75), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_75) == ((_SafetyController_0_has_data_75) == (0)))), Not((monitor_IN_reqWrite_75) == (And(monitor_IN_reqRead_75, (_SafetyController_0_has_data_75) == (1))))), sensor_OUT_reqRead_75)), monitor_IN_reqWrite_75)), monitor_IN_reqWrite_76 == (False), monitor_IN_value_76 == (_SafetyController_0_buffered_status_75), _SafetyController_0_has_data_76 == (0), monitor_IN_reqRead_76 == (False), sensor_current_bpm_76 == sensor_current_bpm_75, sensor_OUT_value_76 == sensor_OUT_value_75, sensor_OUT_reqRead_76 == sensor_OUT_reqRead_75, sensor_OUT_reqWrite_76 == sensor_OUT_reqWrite_75, _SafetyController_0_buffered_status_76 == _SafetyController_0_buffered_status_75)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_76) == (sensor_OUT_reqWrite_76))), sensor_OUT_reqWrite_77 == (sensor_OUT_reqRead_76), sensor_current_bpm_77 == sensor_current_bpm_76, sensor_OUT_value_77 == sensor_OUT_value_76, sensor_OUT_reqRead_77 == sensor_OUT_reqRead_76, monitor_IN_value_77 == monitor_IN_value_76, monitor_IN_reqRead_77 == monitor_IN_reqRead_76, monitor_IN_reqWrite_77 == monitor_IN_reqWrite_76, _SafetyController_0_buffered_status_77 == _SafetyController_0_buffered_status_76, _SafetyController_0_has_data_77 == _SafetyController_0_has_data_76), 
    And(And(Not(False), (monitor_IN_reqRead_76) == (False)), monitor_IN_reqRead_77 == (True), sensor_current_bpm_77 == sensor_current_bpm_76, sensor_OUT_value_77 == sensor_OUT_value_76, sensor_OUT_reqRead_77 == sensor_OUT_reqRead_76, sensor_OUT_reqWrite_77 == sensor_OUT_reqWrite_76, monitor_IN_value_77 == monitor_IN_value_76, monitor_IN_reqWrite_77 == monitor_IN_reqWrite_76, _SafetyController_0_buffered_status_77 == _SafetyController_0_buffered_status_76, _SafetyController_0_has_data_77 == _SafetyController_0_has_data_76), 
    And(And(Not(False), Not((sensor_OUT_reqRead_76) == ((_SafetyController_0_has_data_76) == (0)))), sensor_OUT_reqRead_77 == ((_SafetyController_0_has_data_76) == (0)), sensor_current_bpm_77 == sensor_current_bpm_76, sensor_OUT_value_77 == sensor_OUT_value_76, sensor_OUT_reqWrite_77 == sensor_OUT_reqWrite_76, monitor_IN_value_77 == monitor_IN_value_76, monitor_IN_reqRead_77 == monitor_IN_reqRead_76, monitor_IN_reqWrite_77 == monitor_IN_reqWrite_76, _SafetyController_0_buffered_status_77 == _SafetyController_0_buffered_status_76, _SafetyController_0_has_data_77 == _SafetyController_0_has_data_76), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_76) == ((_SafetyController_0_has_data_76) == (0))))), Not((monitor_IN_reqWrite_76) == (And(monitor_IN_reqRead_76, (_SafetyController_0_has_data_76) == (1))))), monitor_IN_reqWrite_77 == (And(monitor_IN_reqRead_76, (_SafetyController_0_has_data_76) == (1))), sensor_current_bpm_77 == sensor_current_bpm_76, sensor_OUT_value_77 == sensor_OUT_value_76, sensor_OUT_reqRead_77 == sensor_OUT_reqRead_76, sensor_OUT_reqWrite_77 == sensor_OUT_reqWrite_76, monitor_IN_value_77 == monitor_IN_value_76, monitor_IN_reqRead_77 == monitor_IN_reqRead_76, _SafetyController_0_buffered_status_77 == _SafetyController_0_buffered_status_76, _SafetyController_0_has_data_77 == _SafetyController_0_has_data_76), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_76) == (sensor_OUT_reqWrite_76)))), sensor_OUT_reqWrite_76), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_76) == ((_SafetyController_0_has_data_76) == (0)))), Not((monitor_IN_reqWrite_76) == (And(monitor_IN_reqRead_76, (_SafetyController_0_has_data_76) == (1)))))), sensor_OUT_reqRead_76)), _SafetyController_0_buffered_status_77 == (If((sensor_current_bpm_76 > 100), 1, 0)), sensor_current_bpm_77 == (predict_next(sensor_current_bpm_76)), sensor_OUT_reqWrite_77 == (False), _SafetyController_0_has_data_77 == (1), sensor_OUT_reqRead_77 == (False), sensor_OUT_value_77 == (sensor_current_bpm_76), monitor_IN_value_77 == monitor_IN_value_76, monitor_IN_reqRead_77 == monitor_IN_reqRead_76, monitor_IN_reqWrite_77 == monitor_IN_reqWrite_76), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_76) == (False))), monitor_IN_reqWrite_76), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_76) == ((_SafetyController_0_has_data_76) == (0)))), Not((monitor_IN_reqWrite_76) == (And(monitor_IN_reqRead_76, (_SafetyController_0_has_data_76) == (1))))), sensor_OUT_reqRead_76)), monitor_IN_reqWrite_76)), monitor_IN_reqWrite_77 == (False), monitor_IN_value_77 == (_SafetyController_0_buffered_status_76), _SafetyController_0_has_data_77 == (0), monitor_IN_reqRead_77 == (False), sensor_current_bpm_77 == sensor_current_bpm_76, sensor_OUT_value_77 == sensor_OUT_value_76, sensor_OUT_reqRead_77 == sensor_OUT_reqRead_76, sensor_OUT_reqWrite_77 == sensor_OUT_reqWrite_76, _SafetyController_0_buffered_status_77 == _SafetyController_0_buffered_status_76)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_77) == (sensor_OUT_reqWrite_77))), sensor_OUT_reqWrite_78 == (sensor_OUT_reqRead_77), sensor_current_bpm_78 == sensor_current_bpm_77, sensor_OUT_value_78 == sensor_OUT_value_77, sensor_OUT_reqRead_78 == sensor_OUT_reqRead_77, monitor_IN_value_78 == monitor_IN_value_77, monitor_IN_reqRead_78 == monitor_IN_reqRead_77, monitor_IN_reqWrite_78 == monitor_IN_reqWrite_77, _SafetyController_0_buffered_status_78 == _SafetyController_0_buffered_status_77, _SafetyController_0_has_data_78 == _SafetyController_0_has_data_77), 
    And(And(Not(False), (monitor_IN_reqRead_77) == (False)), monitor_IN_reqRead_78 == (True), sensor_current_bpm_78 == sensor_current_bpm_77, sensor_OUT_value_78 == sensor_OUT_value_77, sensor_OUT_reqRead_78 == sensor_OUT_reqRead_77, sensor_OUT_reqWrite_78 == sensor_OUT_reqWrite_77, monitor_IN_value_78 == monitor_IN_value_77, monitor_IN_reqWrite_78 == monitor_IN_reqWrite_77, _SafetyController_0_buffered_status_78 == _SafetyController_0_buffered_status_77, _SafetyController_0_has_data_78 == _SafetyController_0_has_data_77), 
    And(And(Not(False), Not((sensor_OUT_reqRead_77) == ((_SafetyController_0_has_data_77) == (0)))), sensor_OUT_reqRead_78 == ((_SafetyController_0_has_data_77) == (0)), sensor_current_bpm_78 == sensor_current_bpm_77, sensor_OUT_value_78 == sensor_OUT_value_77, sensor_OUT_reqWrite_78 == sensor_OUT_reqWrite_77, monitor_IN_value_78 == monitor_IN_value_77, monitor_IN_reqRead_78 == monitor_IN_reqRead_77, monitor_IN_reqWrite_78 == monitor_IN_reqWrite_77, _SafetyController_0_buffered_status_78 == _SafetyController_0_buffered_status_77, _SafetyController_0_has_data_78 == _SafetyController_0_has_data_77), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_77) == ((_SafetyController_0_has_data_77) == (0))))), Not((monitor_IN_reqWrite_77) == (And(monitor_IN_reqRead_77, (_SafetyController_0_has_data_77) == (1))))), monitor_IN_reqWrite_78 == (And(monitor_IN_reqRead_77, (_SafetyController_0_has_data_77) == (1))), sensor_current_bpm_78 == sensor_current_bpm_77, sensor_OUT_value_78 == sensor_OUT_value_77, sensor_OUT_reqRead_78 == sensor_OUT_reqRead_77, sensor_OUT_reqWrite_78 == sensor_OUT_reqWrite_77, monitor_IN_value_78 == monitor_IN_value_77, monitor_IN_reqRead_78 == monitor_IN_reqRead_77, _SafetyController_0_buffered_status_78 == _SafetyController_0_buffered_status_77, _SafetyController_0_has_data_78 == _SafetyController_0_has_data_77), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_77) == (sensor_OUT_reqWrite_77)))), sensor_OUT_reqWrite_77), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_77) == ((_SafetyController_0_has_data_77) == (0)))), Not((monitor_IN_reqWrite_77) == (And(monitor_IN_reqRead_77, (_SafetyController_0_has_data_77) == (1)))))), sensor_OUT_reqRead_77)), _SafetyController_0_buffered_status_78 == (If((sensor_current_bpm_77 > 100), 1, 0)), sensor_current_bpm_78 == (predict_next(sensor_current_bpm_77)), sensor_OUT_reqWrite_78 == (False), _SafetyController_0_has_data_78 == (1), sensor_OUT_reqRead_78 == (False), sensor_OUT_value_78 == (sensor_current_bpm_77), monitor_IN_value_78 == monitor_IN_value_77, monitor_IN_reqRead_78 == monitor_IN_reqRead_77, monitor_IN_reqWrite_78 == monitor_IN_reqWrite_77), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_77) == (False))), monitor_IN_reqWrite_77), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_77) == ((_SafetyController_0_has_data_77) == (0)))), Not((monitor_IN_reqWrite_77) == (And(monitor_IN_reqRead_77, (_SafetyController_0_has_data_77) == (1))))), sensor_OUT_reqRead_77)), monitor_IN_reqWrite_77)), monitor_IN_reqWrite_78 == (False), monitor_IN_value_78 == (_SafetyController_0_buffered_status_77), _SafetyController_0_has_data_78 == (0), monitor_IN_reqRead_78 == (False), sensor_current_bpm_78 == sensor_current_bpm_77, sensor_OUT_value_78 == sensor_OUT_value_77, sensor_OUT_reqRead_78 == sensor_OUT_reqRead_77, sensor_OUT_reqWrite_78 == sensor_OUT_reqWrite_77, _SafetyController_0_buffered_status_78 == _SafetyController_0_buffered_status_77)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_78) == (sensor_OUT_reqWrite_78))), sensor_OUT_reqWrite_79 == (sensor_OUT_reqRead_78), sensor_current_bpm_79 == sensor_current_bpm_78, sensor_OUT_value_79 == sensor_OUT_value_78, sensor_OUT_reqRead_79 == sensor_OUT_reqRead_78, monitor_IN_value_79 == monitor_IN_value_78, monitor_IN_reqRead_79 == monitor_IN_reqRead_78, monitor_IN_reqWrite_79 == monitor_IN_reqWrite_78, _SafetyController_0_buffered_status_79 == _SafetyController_0_buffered_status_78, _SafetyController_0_has_data_79 == _SafetyController_0_has_data_78), 
    And(And(Not(False), (monitor_IN_reqRead_78) == (False)), monitor_IN_reqRead_79 == (True), sensor_current_bpm_79 == sensor_current_bpm_78, sensor_OUT_value_79 == sensor_OUT_value_78, sensor_OUT_reqRead_79 == sensor_OUT_reqRead_78, sensor_OUT_reqWrite_79 == sensor_OUT_reqWrite_78, monitor_IN_value_79 == monitor_IN_value_78, monitor_IN_reqWrite_79 == monitor_IN_reqWrite_78, _SafetyController_0_buffered_status_79 == _SafetyController_0_buffered_status_78, _SafetyController_0_has_data_79 == _SafetyController_0_has_data_78), 
    And(And(Not(False), Not((sensor_OUT_reqRead_78) == ((_SafetyController_0_has_data_78) == (0)))), sensor_OUT_reqRead_79 == ((_SafetyController_0_has_data_78) == (0)), sensor_current_bpm_79 == sensor_current_bpm_78, sensor_OUT_value_79 == sensor_OUT_value_78, sensor_OUT_reqWrite_79 == sensor_OUT_reqWrite_78, monitor_IN_value_79 == monitor_IN_value_78, monitor_IN_reqRead_79 == monitor_IN_reqRead_78, monitor_IN_reqWrite_79 == monitor_IN_reqWrite_78, _SafetyController_0_buffered_status_79 == _SafetyController_0_buffered_status_78, _SafetyController_0_has_data_79 == _SafetyController_0_has_data_78), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_78) == ((_SafetyController_0_has_data_78) == (0))))), Not((monitor_IN_reqWrite_78) == (And(monitor_IN_reqRead_78, (_SafetyController_0_has_data_78) == (1))))), monitor_IN_reqWrite_79 == (And(monitor_IN_reqRead_78, (_SafetyController_0_has_data_78) == (1))), sensor_current_bpm_79 == sensor_current_bpm_78, sensor_OUT_value_79 == sensor_OUT_value_78, sensor_OUT_reqRead_79 == sensor_OUT_reqRead_78, sensor_OUT_reqWrite_79 == sensor_OUT_reqWrite_78, monitor_IN_value_79 == monitor_IN_value_78, monitor_IN_reqRead_79 == monitor_IN_reqRead_78, _SafetyController_0_buffered_status_79 == _SafetyController_0_buffered_status_78, _SafetyController_0_has_data_79 == _SafetyController_0_has_data_78), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_78) == (sensor_OUT_reqWrite_78)))), sensor_OUT_reqWrite_78), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_78) == ((_SafetyController_0_has_data_78) == (0)))), Not((monitor_IN_reqWrite_78) == (And(monitor_IN_reqRead_78, (_SafetyController_0_has_data_78) == (1)))))), sensor_OUT_reqRead_78)), _SafetyController_0_buffered_status_79 == (If((sensor_current_bpm_78 > 100), 1, 0)), sensor_current_bpm_79 == (predict_next(sensor_current_bpm_78)), sensor_OUT_reqWrite_79 == (False), _SafetyController_0_has_data_79 == (1), sensor_OUT_reqRead_79 == (False), sensor_OUT_value_79 == (sensor_current_bpm_78), monitor_IN_value_79 == monitor_IN_value_78, monitor_IN_reqRead_79 == monitor_IN_reqRead_78, monitor_IN_reqWrite_79 == monitor_IN_reqWrite_78), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_78) == (False))), monitor_IN_reqWrite_78), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_78) == ((_SafetyController_0_has_data_78) == (0)))), Not((monitor_IN_reqWrite_78) == (And(monitor_IN_reqRead_78, (_SafetyController_0_has_data_78) == (1))))), sensor_OUT_reqRead_78)), monitor_IN_reqWrite_78)), monitor_IN_reqWrite_79 == (False), monitor_IN_value_79 == (_SafetyController_0_buffered_status_78), _SafetyController_0_has_data_79 == (0), monitor_IN_reqRead_79 == (False), sensor_current_bpm_79 == sensor_current_bpm_78, sensor_OUT_value_79 == sensor_OUT_value_78, sensor_OUT_reqRead_79 == sensor_OUT_reqRead_78, sensor_OUT_reqWrite_79 == sensor_OUT_reqWrite_78, _SafetyController_0_buffered_status_79 == _SafetyController_0_buffered_status_78)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_79) == (sensor_OUT_reqWrite_79))), sensor_OUT_reqWrite_80 == (sensor_OUT_reqRead_79), sensor_current_bpm_80 == sensor_current_bpm_79, sensor_OUT_value_80 == sensor_OUT_value_79, sensor_OUT_reqRead_80 == sensor_OUT_reqRead_79, monitor_IN_value_80 == monitor_IN_value_79, monitor_IN_reqRead_80 == monitor_IN_reqRead_79, monitor_IN_reqWrite_80 == monitor_IN_reqWrite_79, _SafetyController_0_buffered_status_80 == _SafetyController_0_buffered_status_79, _SafetyController_0_has_data_80 == _SafetyController_0_has_data_79), 
    And(And(Not(False), (monitor_IN_reqRead_79) == (False)), monitor_IN_reqRead_80 == (True), sensor_current_bpm_80 == sensor_current_bpm_79, sensor_OUT_value_80 == sensor_OUT_value_79, sensor_OUT_reqRead_80 == sensor_OUT_reqRead_79, sensor_OUT_reqWrite_80 == sensor_OUT_reqWrite_79, monitor_IN_value_80 == monitor_IN_value_79, monitor_IN_reqWrite_80 == monitor_IN_reqWrite_79, _SafetyController_0_buffered_status_80 == _SafetyController_0_buffered_status_79, _SafetyController_0_has_data_80 == _SafetyController_0_has_data_79), 
    And(And(Not(False), Not((sensor_OUT_reqRead_79) == ((_SafetyController_0_has_data_79) == (0)))), sensor_OUT_reqRead_80 == ((_SafetyController_0_has_data_79) == (0)), sensor_current_bpm_80 == sensor_current_bpm_79, sensor_OUT_value_80 == sensor_OUT_value_79, sensor_OUT_reqWrite_80 == sensor_OUT_reqWrite_79, monitor_IN_value_80 == monitor_IN_value_79, monitor_IN_reqRead_80 == monitor_IN_reqRead_79, monitor_IN_reqWrite_80 == monitor_IN_reqWrite_79, _SafetyController_0_buffered_status_80 == _SafetyController_0_buffered_status_79, _SafetyController_0_has_data_80 == _SafetyController_0_has_data_79), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_79) == ((_SafetyController_0_has_data_79) == (0))))), Not((monitor_IN_reqWrite_79) == (And(monitor_IN_reqRead_79, (_SafetyController_0_has_data_79) == (1))))), monitor_IN_reqWrite_80 == (And(monitor_IN_reqRead_79, (_SafetyController_0_has_data_79) == (1))), sensor_current_bpm_80 == sensor_current_bpm_79, sensor_OUT_value_80 == sensor_OUT_value_79, sensor_OUT_reqRead_80 == sensor_OUT_reqRead_79, sensor_OUT_reqWrite_80 == sensor_OUT_reqWrite_79, monitor_IN_value_80 == monitor_IN_value_79, monitor_IN_reqRead_80 == monitor_IN_reqRead_79, _SafetyController_0_buffered_status_80 == _SafetyController_0_buffered_status_79, _SafetyController_0_has_data_80 == _SafetyController_0_has_data_79), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_79) == (sensor_OUT_reqWrite_79)))), sensor_OUT_reqWrite_79), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_79) == ((_SafetyController_0_has_data_79) == (0)))), Not((monitor_IN_reqWrite_79) == (And(monitor_IN_reqRead_79, (_SafetyController_0_has_data_79) == (1)))))), sensor_OUT_reqRead_79)), _SafetyController_0_buffered_status_80 == (If((sensor_current_bpm_79 > 100), 1, 0)), sensor_current_bpm_80 == (predict_next(sensor_current_bpm_79)), sensor_OUT_reqWrite_80 == (False), _SafetyController_0_has_data_80 == (1), sensor_OUT_reqRead_80 == (False), sensor_OUT_value_80 == (sensor_current_bpm_79), monitor_IN_value_80 == monitor_IN_value_79, monitor_IN_reqRead_80 == monitor_IN_reqRead_79, monitor_IN_reqWrite_80 == monitor_IN_reqWrite_79), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_79) == (False))), monitor_IN_reqWrite_79), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_79) == ((_SafetyController_0_has_data_79) == (0)))), Not((monitor_IN_reqWrite_79) == (And(monitor_IN_reqRead_79, (_SafetyController_0_has_data_79) == (1))))), sensor_OUT_reqRead_79)), monitor_IN_reqWrite_79)), monitor_IN_reqWrite_80 == (False), monitor_IN_value_80 == (_SafetyController_0_buffered_status_79), _SafetyController_0_has_data_80 == (0), monitor_IN_reqRead_80 == (False), sensor_current_bpm_80 == sensor_current_bpm_79, sensor_OUT_value_80 == sensor_OUT_value_79, sensor_OUT_reqRead_80 == sensor_OUT_reqRead_79, sensor_OUT_reqWrite_80 == sensor_OUT_reqWrite_79, _SafetyController_0_buffered_status_80 == _SafetyController_0_buffered_status_79)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_80) == (sensor_OUT_reqWrite_80))), sensor_OUT_reqWrite_81 == (sensor_OUT_reqRead_80), sensor_current_bpm_81 == sensor_current_bpm_80, sensor_OUT_value_81 == sensor_OUT_value_80, sensor_OUT_reqRead_81 == sensor_OUT_reqRead_80, monitor_IN_value_81 == monitor_IN_value_80, monitor_IN_reqRead_81 == monitor_IN_reqRead_80, monitor_IN_reqWrite_81 == monitor_IN_reqWrite_80, _SafetyController_0_buffered_status_81 == _SafetyController_0_buffered_status_80, _SafetyController_0_has_data_81 == _SafetyController_0_has_data_80), 
    And(And(Not(False), (monitor_IN_reqRead_80) == (False)), monitor_IN_reqRead_81 == (True), sensor_current_bpm_81 == sensor_current_bpm_80, sensor_OUT_value_81 == sensor_OUT_value_80, sensor_OUT_reqRead_81 == sensor_OUT_reqRead_80, sensor_OUT_reqWrite_81 == sensor_OUT_reqWrite_80, monitor_IN_value_81 == monitor_IN_value_80, monitor_IN_reqWrite_81 == monitor_IN_reqWrite_80, _SafetyController_0_buffered_status_81 == _SafetyController_0_buffered_status_80, _SafetyController_0_has_data_81 == _SafetyController_0_has_data_80), 
    And(And(Not(False), Not((sensor_OUT_reqRead_80) == ((_SafetyController_0_has_data_80) == (0)))), sensor_OUT_reqRead_81 == ((_SafetyController_0_has_data_80) == (0)), sensor_current_bpm_81 == sensor_current_bpm_80, sensor_OUT_value_81 == sensor_OUT_value_80, sensor_OUT_reqWrite_81 == sensor_OUT_reqWrite_80, monitor_IN_value_81 == monitor_IN_value_80, monitor_IN_reqRead_81 == monitor_IN_reqRead_80, monitor_IN_reqWrite_81 == monitor_IN_reqWrite_80, _SafetyController_0_buffered_status_81 == _SafetyController_0_buffered_status_80, _SafetyController_0_has_data_81 == _SafetyController_0_has_data_80), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_80) == ((_SafetyController_0_has_data_80) == (0))))), Not((monitor_IN_reqWrite_80) == (And(monitor_IN_reqRead_80, (_SafetyController_0_has_data_80) == (1))))), monitor_IN_reqWrite_81 == (And(monitor_IN_reqRead_80, (_SafetyController_0_has_data_80) == (1))), sensor_current_bpm_81 == sensor_current_bpm_80, sensor_OUT_value_81 == sensor_OUT_value_80, sensor_OUT_reqRead_81 == sensor_OUT_reqRead_80, sensor_OUT_reqWrite_81 == sensor_OUT_reqWrite_80, monitor_IN_value_81 == monitor_IN_value_80, monitor_IN_reqRead_81 == monitor_IN_reqRead_80, _SafetyController_0_buffered_status_81 == _SafetyController_0_buffered_status_80, _SafetyController_0_has_data_81 == _SafetyController_0_has_data_80), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_80) == (sensor_OUT_reqWrite_80)))), sensor_OUT_reqWrite_80), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_80) == ((_SafetyController_0_has_data_80) == (0)))), Not((monitor_IN_reqWrite_80) == (And(monitor_IN_reqRead_80, (_SafetyController_0_has_data_80) == (1)))))), sensor_OUT_reqRead_80)), _SafetyController_0_buffered_status_81 == (If((sensor_current_bpm_80 > 100), 1, 0)), sensor_current_bpm_81 == (predict_next(sensor_current_bpm_80)), sensor_OUT_reqWrite_81 == (False), _SafetyController_0_has_data_81 == (1), sensor_OUT_reqRead_81 == (False), sensor_OUT_value_81 == (sensor_current_bpm_80), monitor_IN_value_81 == monitor_IN_value_80, monitor_IN_reqRead_81 == monitor_IN_reqRead_80, monitor_IN_reqWrite_81 == monitor_IN_reqWrite_80), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_80) == (False))), monitor_IN_reqWrite_80), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_80) == ((_SafetyController_0_has_data_80) == (0)))), Not((monitor_IN_reqWrite_80) == (And(monitor_IN_reqRead_80, (_SafetyController_0_has_data_80) == (1))))), sensor_OUT_reqRead_80)), monitor_IN_reqWrite_80)), monitor_IN_reqWrite_81 == (False), monitor_IN_value_81 == (_SafetyController_0_buffered_status_80), _SafetyController_0_has_data_81 == (0), monitor_IN_reqRead_81 == (False), sensor_current_bpm_81 == sensor_current_bpm_80, sensor_OUT_value_81 == sensor_OUT_value_80, sensor_OUT_reqRead_81 == sensor_OUT_reqRead_80, sensor_OUT_reqWrite_81 == sensor_OUT_reqWrite_80, _SafetyController_0_buffered_status_81 == _SafetyController_0_buffered_status_80)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_81) == (sensor_OUT_reqWrite_81))), sensor_OUT_reqWrite_82 == (sensor_OUT_reqRead_81), sensor_current_bpm_82 == sensor_current_bpm_81, sensor_OUT_value_82 == sensor_OUT_value_81, sensor_OUT_reqRead_82 == sensor_OUT_reqRead_81, monitor_IN_value_82 == monitor_IN_value_81, monitor_IN_reqRead_82 == monitor_IN_reqRead_81, monitor_IN_reqWrite_82 == monitor_IN_reqWrite_81, _SafetyController_0_buffered_status_82 == _SafetyController_0_buffered_status_81, _SafetyController_0_has_data_82 == _SafetyController_0_has_data_81), 
    And(And(Not(False), (monitor_IN_reqRead_81) == (False)), monitor_IN_reqRead_82 == (True), sensor_current_bpm_82 == sensor_current_bpm_81, sensor_OUT_value_82 == sensor_OUT_value_81, sensor_OUT_reqRead_82 == sensor_OUT_reqRead_81, sensor_OUT_reqWrite_82 == sensor_OUT_reqWrite_81, monitor_IN_value_82 == monitor_IN_value_81, monitor_IN_reqWrite_82 == monitor_IN_reqWrite_81, _SafetyController_0_buffered_status_82 == _SafetyController_0_buffered_status_81, _SafetyController_0_has_data_82 == _SafetyController_0_has_data_81), 
    And(And(Not(False), Not((sensor_OUT_reqRead_81) == ((_SafetyController_0_has_data_81) == (0)))), sensor_OUT_reqRead_82 == ((_SafetyController_0_has_data_81) == (0)), sensor_current_bpm_82 == sensor_current_bpm_81, sensor_OUT_value_82 == sensor_OUT_value_81, sensor_OUT_reqWrite_82 == sensor_OUT_reqWrite_81, monitor_IN_value_82 == monitor_IN_value_81, monitor_IN_reqRead_82 == monitor_IN_reqRead_81, monitor_IN_reqWrite_82 == monitor_IN_reqWrite_81, _SafetyController_0_buffered_status_82 == _SafetyController_0_buffered_status_81, _SafetyController_0_has_data_82 == _SafetyController_0_has_data_81), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_81) == ((_SafetyController_0_has_data_81) == (0))))), Not((monitor_IN_reqWrite_81) == (And(monitor_IN_reqRead_81, (_SafetyController_0_has_data_81) == (1))))), monitor_IN_reqWrite_82 == (And(monitor_IN_reqRead_81, (_SafetyController_0_has_data_81) == (1))), sensor_current_bpm_82 == sensor_current_bpm_81, sensor_OUT_value_82 == sensor_OUT_value_81, sensor_OUT_reqRead_82 == sensor_OUT_reqRead_81, sensor_OUT_reqWrite_82 == sensor_OUT_reqWrite_81, monitor_IN_value_82 == monitor_IN_value_81, monitor_IN_reqRead_82 == monitor_IN_reqRead_81, _SafetyController_0_buffered_status_82 == _SafetyController_0_buffered_status_81, _SafetyController_0_has_data_82 == _SafetyController_0_has_data_81), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_81) == (sensor_OUT_reqWrite_81)))), sensor_OUT_reqWrite_81), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_81) == ((_SafetyController_0_has_data_81) == (0)))), Not((monitor_IN_reqWrite_81) == (And(monitor_IN_reqRead_81, (_SafetyController_0_has_data_81) == (1)))))), sensor_OUT_reqRead_81)), _SafetyController_0_buffered_status_82 == (If((sensor_current_bpm_81 > 100), 1, 0)), sensor_current_bpm_82 == (predict_next(sensor_current_bpm_81)), sensor_OUT_reqWrite_82 == (False), _SafetyController_0_has_data_82 == (1), sensor_OUT_reqRead_82 == (False), sensor_OUT_value_82 == (sensor_current_bpm_81), monitor_IN_value_82 == monitor_IN_value_81, monitor_IN_reqRead_82 == monitor_IN_reqRead_81, monitor_IN_reqWrite_82 == monitor_IN_reqWrite_81), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_81) == (False))), monitor_IN_reqWrite_81), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_81) == ((_SafetyController_0_has_data_81) == (0)))), Not((monitor_IN_reqWrite_81) == (And(monitor_IN_reqRead_81, (_SafetyController_0_has_data_81) == (1))))), sensor_OUT_reqRead_81)), monitor_IN_reqWrite_81)), monitor_IN_reqWrite_82 == (False), monitor_IN_value_82 == (_SafetyController_0_buffered_status_81), _SafetyController_0_has_data_82 == (0), monitor_IN_reqRead_82 == (False), sensor_current_bpm_82 == sensor_current_bpm_81, sensor_OUT_value_82 == sensor_OUT_value_81, sensor_OUT_reqRead_82 == sensor_OUT_reqRead_81, sensor_OUT_reqWrite_82 == sensor_OUT_reqWrite_81, _SafetyController_0_buffered_status_82 == _SafetyController_0_buffered_status_81)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_82) == (sensor_OUT_reqWrite_82))), sensor_OUT_reqWrite_83 == (sensor_OUT_reqRead_82), sensor_current_bpm_83 == sensor_current_bpm_82, sensor_OUT_value_83 == sensor_OUT_value_82, sensor_OUT_reqRead_83 == sensor_OUT_reqRead_82, monitor_IN_value_83 == monitor_IN_value_82, monitor_IN_reqRead_83 == monitor_IN_reqRead_82, monitor_IN_reqWrite_83 == monitor_IN_reqWrite_82, _SafetyController_0_buffered_status_83 == _SafetyController_0_buffered_status_82, _SafetyController_0_has_data_83 == _SafetyController_0_has_data_82), 
    And(And(Not(False), (monitor_IN_reqRead_82) == (False)), monitor_IN_reqRead_83 == (True), sensor_current_bpm_83 == sensor_current_bpm_82, sensor_OUT_value_83 == sensor_OUT_value_82, sensor_OUT_reqRead_83 == sensor_OUT_reqRead_82, sensor_OUT_reqWrite_83 == sensor_OUT_reqWrite_82, monitor_IN_value_83 == monitor_IN_value_82, monitor_IN_reqWrite_83 == monitor_IN_reqWrite_82, _SafetyController_0_buffered_status_83 == _SafetyController_0_buffered_status_82, _SafetyController_0_has_data_83 == _SafetyController_0_has_data_82), 
    And(And(Not(False), Not((sensor_OUT_reqRead_82) == ((_SafetyController_0_has_data_82) == (0)))), sensor_OUT_reqRead_83 == ((_SafetyController_0_has_data_82) == (0)), sensor_current_bpm_83 == sensor_current_bpm_82, sensor_OUT_value_83 == sensor_OUT_value_82, sensor_OUT_reqWrite_83 == sensor_OUT_reqWrite_82, monitor_IN_value_83 == monitor_IN_value_82, monitor_IN_reqRead_83 == monitor_IN_reqRead_82, monitor_IN_reqWrite_83 == monitor_IN_reqWrite_82, _SafetyController_0_buffered_status_83 == _SafetyController_0_buffered_status_82, _SafetyController_0_has_data_83 == _SafetyController_0_has_data_82), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_82) == ((_SafetyController_0_has_data_82) == (0))))), Not((monitor_IN_reqWrite_82) == (And(monitor_IN_reqRead_82, (_SafetyController_0_has_data_82) == (1))))), monitor_IN_reqWrite_83 == (And(monitor_IN_reqRead_82, (_SafetyController_0_has_data_82) == (1))), sensor_current_bpm_83 == sensor_current_bpm_82, sensor_OUT_value_83 == sensor_OUT_value_82, sensor_OUT_reqRead_83 == sensor_OUT_reqRead_82, sensor_OUT_reqWrite_83 == sensor_OUT_reqWrite_82, monitor_IN_value_83 == monitor_IN_value_82, monitor_IN_reqRead_83 == monitor_IN_reqRead_82, _SafetyController_0_buffered_status_83 == _SafetyController_0_buffered_status_82, _SafetyController_0_has_data_83 == _SafetyController_0_has_data_82), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_82) == (sensor_OUT_reqWrite_82)))), sensor_OUT_reqWrite_82), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_82) == ((_SafetyController_0_has_data_82) == (0)))), Not((monitor_IN_reqWrite_82) == (And(monitor_IN_reqRead_82, (_SafetyController_0_has_data_82) == (1)))))), sensor_OUT_reqRead_82)), _SafetyController_0_buffered_status_83 == (If((sensor_current_bpm_82 > 100), 1, 0)), sensor_current_bpm_83 == (predict_next(sensor_current_bpm_82)), sensor_OUT_reqWrite_83 == (False), _SafetyController_0_has_data_83 == (1), sensor_OUT_reqRead_83 == (False), sensor_OUT_value_83 == (sensor_current_bpm_82), monitor_IN_value_83 == monitor_IN_value_82, monitor_IN_reqRead_83 == monitor_IN_reqRead_82, monitor_IN_reqWrite_83 == monitor_IN_reqWrite_82), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_82) == (False))), monitor_IN_reqWrite_82), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_82) == ((_SafetyController_0_has_data_82) == (0)))), Not((monitor_IN_reqWrite_82) == (And(monitor_IN_reqRead_82, (_SafetyController_0_has_data_82) == (1))))), sensor_OUT_reqRead_82)), monitor_IN_reqWrite_82)), monitor_IN_reqWrite_83 == (False), monitor_IN_value_83 == (_SafetyController_0_buffered_status_82), _SafetyController_0_has_data_83 == (0), monitor_IN_reqRead_83 == (False), sensor_current_bpm_83 == sensor_current_bpm_82, sensor_OUT_value_83 == sensor_OUT_value_82, sensor_OUT_reqRead_83 == sensor_OUT_reqRead_82, sensor_OUT_reqWrite_83 == sensor_OUT_reqWrite_82, _SafetyController_0_buffered_status_83 == _SafetyController_0_buffered_status_82)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_83) == (sensor_OUT_reqWrite_83))), sensor_OUT_reqWrite_84 == (sensor_OUT_reqRead_83), sensor_current_bpm_84 == sensor_current_bpm_83, sensor_OUT_value_84 == sensor_OUT_value_83, sensor_OUT_reqRead_84 == sensor_OUT_reqRead_83, monitor_IN_value_84 == monitor_IN_value_83, monitor_IN_reqRead_84 == monitor_IN_reqRead_83, monitor_IN_reqWrite_84 == monitor_IN_reqWrite_83, _SafetyController_0_buffered_status_84 == _SafetyController_0_buffered_status_83, _SafetyController_0_has_data_84 == _SafetyController_0_has_data_83), 
    And(And(Not(False), (monitor_IN_reqRead_83) == (False)), monitor_IN_reqRead_84 == (True), sensor_current_bpm_84 == sensor_current_bpm_83, sensor_OUT_value_84 == sensor_OUT_value_83, sensor_OUT_reqRead_84 == sensor_OUT_reqRead_83, sensor_OUT_reqWrite_84 == sensor_OUT_reqWrite_83, monitor_IN_value_84 == monitor_IN_value_83, monitor_IN_reqWrite_84 == monitor_IN_reqWrite_83, _SafetyController_0_buffered_status_84 == _SafetyController_0_buffered_status_83, _SafetyController_0_has_data_84 == _SafetyController_0_has_data_83), 
    And(And(Not(False), Not((sensor_OUT_reqRead_83) == ((_SafetyController_0_has_data_83) == (0)))), sensor_OUT_reqRead_84 == ((_SafetyController_0_has_data_83) == (0)), sensor_current_bpm_84 == sensor_current_bpm_83, sensor_OUT_value_84 == sensor_OUT_value_83, sensor_OUT_reqWrite_84 == sensor_OUT_reqWrite_83, monitor_IN_value_84 == monitor_IN_value_83, monitor_IN_reqRead_84 == monitor_IN_reqRead_83, monitor_IN_reqWrite_84 == monitor_IN_reqWrite_83, _SafetyController_0_buffered_status_84 == _SafetyController_0_buffered_status_83, _SafetyController_0_has_data_84 == _SafetyController_0_has_data_83), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_83) == ((_SafetyController_0_has_data_83) == (0))))), Not((monitor_IN_reqWrite_83) == (And(monitor_IN_reqRead_83, (_SafetyController_0_has_data_83) == (1))))), monitor_IN_reqWrite_84 == (And(monitor_IN_reqRead_83, (_SafetyController_0_has_data_83) == (1))), sensor_current_bpm_84 == sensor_current_bpm_83, sensor_OUT_value_84 == sensor_OUT_value_83, sensor_OUT_reqRead_84 == sensor_OUT_reqRead_83, sensor_OUT_reqWrite_84 == sensor_OUT_reqWrite_83, monitor_IN_value_84 == monitor_IN_value_83, monitor_IN_reqRead_84 == monitor_IN_reqRead_83, _SafetyController_0_buffered_status_84 == _SafetyController_0_buffered_status_83, _SafetyController_0_has_data_84 == _SafetyController_0_has_data_83), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_83) == (sensor_OUT_reqWrite_83)))), sensor_OUT_reqWrite_83), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_83) == ((_SafetyController_0_has_data_83) == (0)))), Not((monitor_IN_reqWrite_83) == (And(monitor_IN_reqRead_83, (_SafetyController_0_has_data_83) == (1)))))), sensor_OUT_reqRead_83)), _SafetyController_0_buffered_status_84 == (If((sensor_current_bpm_83 > 100), 1, 0)), sensor_current_bpm_84 == (predict_next(sensor_current_bpm_83)), sensor_OUT_reqWrite_84 == (False), _SafetyController_0_has_data_84 == (1), sensor_OUT_reqRead_84 == (False), sensor_OUT_value_84 == (sensor_current_bpm_83), monitor_IN_value_84 == monitor_IN_value_83, monitor_IN_reqRead_84 == monitor_IN_reqRead_83, monitor_IN_reqWrite_84 == monitor_IN_reqWrite_83), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_83) == (False))), monitor_IN_reqWrite_83), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_83) == ((_SafetyController_0_has_data_83) == (0)))), Not((monitor_IN_reqWrite_83) == (And(monitor_IN_reqRead_83, (_SafetyController_0_has_data_83) == (1))))), sensor_OUT_reqRead_83)), monitor_IN_reqWrite_83)), monitor_IN_reqWrite_84 == (False), monitor_IN_value_84 == (_SafetyController_0_buffered_status_83), _SafetyController_0_has_data_84 == (0), monitor_IN_reqRead_84 == (False), sensor_current_bpm_84 == sensor_current_bpm_83, sensor_OUT_value_84 == sensor_OUT_value_83, sensor_OUT_reqRead_84 == sensor_OUT_reqRead_83, sensor_OUT_reqWrite_84 == sensor_OUT_reqWrite_83, _SafetyController_0_buffered_status_84 == _SafetyController_0_buffered_status_83)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_84) == (sensor_OUT_reqWrite_84))), sensor_OUT_reqWrite_85 == (sensor_OUT_reqRead_84), sensor_current_bpm_85 == sensor_current_bpm_84, sensor_OUT_value_85 == sensor_OUT_value_84, sensor_OUT_reqRead_85 == sensor_OUT_reqRead_84, monitor_IN_value_85 == monitor_IN_value_84, monitor_IN_reqRead_85 == monitor_IN_reqRead_84, monitor_IN_reqWrite_85 == monitor_IN_reqWrite_84, _SafetyController_0_buffered_status_85 == _SafetyController_0_buffered_status_84, _SafetyController_0_has_data_85 == _SafetyController_0_has_data_84), 
    And(And(Not(False), (monitor_IN_reqRead_84) == (False)), monitor_IN_reqRead_85 == (True), sensor_current_bpm_85 == sensor_current_bpm_84, sensor_OUT_value_85 == sensor_OUT_value_84, sensor_OUT_reqRead_85 == sensor_OUT_reqRead_84, sensor_OUT_reqWrite_85 == sensor_OUT_reqWrite_84, monitor_IN_value_85 == monitor_IN_value_84, monitor_IN_reqWrite_85 == monitor_IN_reqWrite_84, _SafetyController_0_buffered_status_85 == _SafetyController_0_buffered_status_84, _SafetyController_0_has_data_85 == _SafetyController_0_has_data_84), 
    And(And(Not(False), Not((sensor_OUT_reqRead_84) == ((_SafetyController_0_has_data_84) == (0)))), sensor_OUT_reqRead_85 == ((_SafetyController_0_has_data_84) == (0)), sensor_current_bpm_85 == sensor_current_bpm_84, sensor_OUT_value_85 == sensor_OUT_value_84, sensor_OUT_reqWrite_85 == sensor_OUT_reqWrite_84, monitor_IN_value_85 == monitor_IN_value_84, monitor_IN_reqRead_85 == monitor_IN_reqRead_84, monitor_IN_reqWrite_85 == monitor_IN_reqWrite_84, _SafetyController_0_buffered_status_85 == _SafetyController_0_buffered_status_84, _SafetyController_0_has_data_85 == _SafetyController_0_has_data_84), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_84) == ((_SafetyController_0_has_data_84) == (0))))), Not((monitor_IN_reqWrite_84) == (And(monitor_IN_reqRead_84, (_SafetyController_0_has_data_84) == (1))))), monitor_IN_reqWrite_85 == (And(monitor_IN_reqRead_84, (_SafetyController_0_has_data_84) == (1))), sensor_current_bpm_85 == sensor_current_bpm_84, sensor_OUT_value_85 == sensor_OUT_value_84, sensor_OUT_reqRead_85 == sensor_OUT_reqRead_84, sensor_OUT_reqWrite_85 == sensor_OUT_reqWrite_84, monitor_IN_value_85 == monitor_IN_value_84, monitor_IN_reqRead_85 == monitor_IN_reqRead_84, _SafetyController_0_buffered_status_85 == _SafetyController_0_buffered_status_84, _SafetyController_0_has_data_85 == _SafetyController_0_has_data_84), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_84) == (sensor_OUT_reqWrite_84)))), sensor_OUT_reqWrite_84), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_84) == ((_SafetyController_0_has_data_84) == (0)))), Not((monitor_IN_reqWrite_84) == (And(monitor_IN_reqRead_84, (_SafetyController_0_has_data_84) == (1)))))), sensor_OUT_reqRead_84)), _SafetyController_0_buffered_status_85 == (If((sensor_current_bpm_84 > 100), 1, 0)), sensor_current_bpm_85 == (predict_next(sensor_current_bpm_84)), sensor_OUT_reqWrite_85 == (False), _SafetyController_0_has_data_85 == (1), sensor_OUT_reqRead_85 == (False), sensor_OUT_value_85 == (sensor_current_bpm_84), monitor_IN_value_85 == monitor_IN_value_84, monitor_IN_reqRead_85 == monitor_IN_reqRead_84, monitor_IN_reqWrite_85 == monitor_IN_reqWrite_84), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_84) == (False))), monitor_IN_reqWrite_84), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_84) == ((_SafetyController_0_has_data_84) == (0)))), Not((monitor_IN_reqWrite_84) == (And(monitor_IN_reqRead_84, (_SafetyController_0_has_data_84) == (1))))), sensor_OUT_reqRead_84)), monitor_IN_reqWrite_84)), monitor_IN_reqWrite_85 == (False), monitor_IN_value_85 == (_SafetyController_0_buffered_status_84), _SafetyController_0_has_data_85 == (0), monitor_IN_reqRead_85 == (False), sensor_current_bpm_85 == sensor_current_bpm_84, sensor_OUT_value_85 == sensor_OUT_value_84, sensor_OUT_reqRead_85 == sensor_OUT_reqRead_84, sensor_OUT_reqWrite_85 == sensor_OUT_reqWrite_84, _SafetyController_0_buffered_status_85 == _SafetyController_0_buffered_status_84)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_85) == (sensor_OUT_reqWrite_85))), sensor_OUT_reqWrite_86 == (sensor_OUT_reqRead_85), sensor_current_bpm_86 == sensor_current_bpm_85, sensor_OUT_value_86 == sensor_OUT_value_85, sensor_OUT_reqRead_86 == sensor_OUT_reqRead_85, monitor_IN_value_86 == monitor_IN_value_85, monitor_IN_reqRead_86 == monitor_IN_reqRead_85, monitor_IN_reqWrite_86 == monitor_IN_reqWrite_85, _SafetyController_0_buffered_status_86 == _SafetyController_0_buffered_status_85, _SafetyController_0_has_data_86 == _SafetyController_0_has_data_85), 
    And(And(Not(False), (monitor_IN_reqRead_85) == (False)), monitor_IN_reqRead_86 == (True), sensor_current_bpm_86 == sensor_current_bpm_85, sensor_OUT_value_86 == sensor_OUT_value_85, sensor_OUT_reqRead_86 == sensor_OUT_reqRead_85, sensor_OUT_reqWrite_86 == sensor_OUT_reqWrite_85, monitor_IN_value_86 == monitor_IN_value_85, monitor_IN_reqWrite_86 == monitor_IN_reqWrite_85, _SafetyController_0_buffered_status_86 == _SafetyController_0_buffered_status_85, _SafetyController_0_has_data_86 == _SafetyController_0_has_data_85), 
    And(And(Not(False), Not((sensor_OUT_reqRead_85) == ((_SafetyController_0_has_data_85) == (0)))), sensor_OUT_reqRead_86 == ((_SafetyController_0_has_data_85) == (0)), sensor_current_bpm_86 == sensor_current_bpm_85, sensor_OUT_value_86 == sensor_OUT_value_85, sensor_OUT_reqWrite_86 == sensor_OUT_reqWrite_85, monitor_IN_value_86 == monitor_IN_value_85, monitor_IN_reqRead_86 == monitor_IN_reqRead_85, monitor_IN_reqWrite_86 == monitor_IN_reqWrite_85, _SafetyController_0_buffered_status_86 == _SafetyController_0_buffered_status_85, _SafetyController_0_has_data_86 == _SafetyController_0_has_data_85), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_85) == ((_SafetyController_0_has_data_85) == (0))))), Not((monitor_IN_reqWrite_85) == (And(monitor_IN_reqRead_85, (_SafetyController_0_has_data_85) == (1))))), monitor_IN_reqWrite_86 == (And(monitor_IN_reqRead_85, (_SafetyController_0_has_data_85) == (1))), sensor_current_bpm_86 == sensor_current_bpm_85, sensor_OUT_value_86 == sensor_OUT_value_85, sensor_OUT_reqRead_86 == sensor_OUT_reqRead_85, sensor_OUT_reqWrite_86 == sensor_OUT_reqWrite_85, monitor_IN_value_86 == monitor_IN_value_85, monitor_IN_reqRead_86 == monitor_IN_reqRead_85, _SafetyController_0_buffered_status_86 == _SafetyController_0_buffered_status_85, _SafetyController_0_has_data_86 == _SafetyController_0_has_data_85), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_85) == (sensor_OUT_reqWrite_85)))), sensor_OUT_reqWrite_85), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_85) == ((_SafetyController_0_has_data_85) == (0)))), Not((monitor_IN_reqWrite_85) == (And(monitor_IN_reqRead_85, (_SafetyController_0_has_data_85) == (1)))))), sensor_OUT_reqRead_85)), _SafetyController_0_buffered_status_86 == (If((sensor_current_bpm_85 > 100), 1, 0)), sensor_current_bpm_86 == (predict_next(sensor_current_bpm_85)), sensor_OUT_reqWrite_86 == (False), _SafetyController_0_has_data_86 == (1), sensor_OUT_reqRead_86 == (False), sensor_OUT_value_86 == (sensor_current_bpm_85), monitor_IN_value_86 == monitor_IN_value_85, monitor_IN_reqRead_86 == monitor_IN_reqRead_85, monitor_IN_reqWrite_86 == monitor_IN_reqWrite_85), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_85) == (False))), monitor_IN_reqWrite_85), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_85) == ((_SafetyController_0_has_data_85) == (0)))), Not((monitor_IN_reqWrite_85) == (And(monitor_IN_reqRead_85, (_SafetyController_0_has_data_85) == (1))))), sensor_OUT_reqRead_85)), monitor_IN_reqWrite_85)), monitor_IN_reqWrite_86 == (False), monitor_IN_value_86 == (_SafetyController_0_buffered_status_85), _SafetyController_0_has_data_86 == (0), monitor_IN_reqRead_86 == (False), sensor_current_bpm_86 == sensor_current_bpm_85, sensor_OUT_value_86 == sensor_OUT_value_85, sensor_OUT_reqRead_86 == sensor_OUT_reqRead_85, sensor_OUT_reqWrite_86 == sensor_OUT_reqWrite_85, _SafetyController_0_buffered_status_86 == _SafetyController_0_buffered_status_85)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_86) == (sensor_OUT_reqWrite_86))), sensor_OUT_reqWrite_87 == (sensor_OUT_reqRead_86), sensor_current_bpm_87 == sensor_current_bpm_86, sensor_OUT_value_87 == sensor_OUT_value_86, sensor_OUT_reqRead_87 == sensor_OUT_reqRead_86, monitor_IN_value_87 == monitor_IN_value_86, monitor_IN_reqRead_87 == monitor_IN_reqRead_86, monitor_IN_reqWrite_87 == monitor_IN_reqWrite_86, _SafetyController_0_buffered_status_87 == _SafetyController_0_buffered_status_86, _SafetyController_0_has_data_87 == _SafetyController_0_has_data_86), 
    And(And(Not(False), (monitor_IN_reqRead_86) == (False)), monitor_IN_reqRead_87 == (True), sensor_current_bpm_87 == sensor_current_bpm_86, sensor_OUT_value_87 == sensor_OUT_value_86, sensor_OUT_reqRead_87 == sensor_OUT_reqRead_86, sensor_OUT_reqWrite_87 == sensor_OUT_reqWrite_86, monitor_IN_value_87 == monitor_IN_value_86, monitor_IN_reqWrite_87 == monitor_IN_reqWrite_86, _SafetyController_0_buffered_status_87 == _SafetyController_0_buffered_status_86, _SafetyController_0_has_data_87 == _SafetyController_0_has_data_86), 
    And(And(Not(False), Not((sensor_OUT_reqRead_86) == ((_SafetyController_0_has_data_86) == (0)))), sensor_OUT_reqRead_87 == ((_SafetyController_0_has_data_86) == (0)), sensor_current_bpm_87 == sensor_current_bpm_86, sensor_OUT_value_87 == sensor_OUT_value_86, sensor_OUT_reqWrite_87 == sensor_OUT_reqWrite_86, monitor_IN_value_87 == monitor_IN_value_86, monitor_IN_reqRead_87 == monitor_IN_reqRead_86, monitor_IN_reqWrite_87 == monitor_IN_reqWrite_86, _SafetyController_0_buffered_status_87 == _SafetyController_0_buffered_status_86, _SafetyController_0_has_data_87 == _SafetyController_0_has_data_86), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_86) == ((_SafetyController_0_has_data_86) == (0))))), Not((monitor_IN_reqWrite_86) == (And(monitor_IN_reqRead_86, (_SafetyController_0_has_data_86) == (1))))), monitor_IN_reqWrite_87 == (And(monitor_IN_reqRead_86, (_SafetyController_0_has_data_86) == (1))), sensor_current_bpm_87 == sensor_current_bpm_86, sensor_OUT_value_87 == sensor_OUT_value_86, sensor_OUT_reqRead_87 == sensor_OUT_reqRead_86, sensor_OUT_reqWrite_87 == sensor_OUT_reqWrite_86, monitor_IN_value_87 == monitor_IN_value_86, monitor_IN_reqRead_87 == monitor_IN_reqRead_86, _SafetyController_0_buffered_status_87 == _SafetyController_0_buffered_status_86, _SafetyController_0_has_data_87 == _SafetyController_0_has_data_86), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_86) == (sensor_OUT_reqWrite_86)))), sensor_OUT_reqWrite_86), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_86) == ((_SafetyController_0_has_data_86) == (0)))), Not((monitor_IN_reqWrite_86) == (And(monitor_IN_reqRead_86, (_SafetyController_0_has_data_86) == (1)))))), sensor_OUT_reqRead_86)), _SafetyController_0_buffered_status_87 == (If((sensor_current_bpm_86 > 100), 1, 0)), sensor_current_bpm_87 == (predict_next(sensor_current_bpm_86)), sensor_OUT_reqWrite_87 == (False), _SafetyController_0_has_data_87 == (1), sensor_OUT_reqRead_87 == (False), sensor_OUT_value_87 == (sensor_current_bpm_86), monitor_IN_value_87 == monitor_IN_value_86, monitor_IN_reqRead_87 == monitor_IN_reqRead_86, monitor_IN_reqWrite_87 == monitor_IN_reqWrite_86), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_86) == (False))), monitor_IN_reqWrite_86), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_86) == ((_SafetyController_0_has_data_86) == (0)))), Not((monitor_IN_reqWrite_86) == (And(monitor_IN_reqRead_86, (_SafetyController_0_has_data_86) == (1))))), sensor_OUT_reqRead_86)), monitor_IN_reqWrite_86)), monitor_IN_reqWrite_87 == (False), monitor_IN_value_87 == (_SafetyController_0_buffered_status_86), _SafetyController_0_has_data_87 == (0), monitor_IN_reqRead_87 == (False), sensor_current_bpm_87 == sensor_current_bpm_86, sensor_OUT_value_87 == sensor_OUT_value_86, sensor_OUT_reqRead_87 == sensor_OUT_reqRead_86, sensor_OUT_reqWrite_87 == sensor_OUT_reqWrite_86, _SafetyController_0_buffered_status_87 == _SafetyController_0_buffered_status_86)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_87) == (sensor_OUT_reqWrite_87))), sensor_OUT_reqWrite_88 == (sensor_OUT_reqRead_87), sensor_current_bpm_88 == sensor_current_bpm_87, sensor_OUT_value_88 == sensor_OUT_value_87, sensor_OUT_reqRead_88 == sensor_OUT_reqRead_87, monitor_IN_value_88 == monitor_IN_value_87, monitor_IN_reqRead_88 == monitor_IN_reqRead_87, monitor_IN_reqWrite_88 == monitor_IN_reqWrite_87, _SafetyController_0_buffered_status_88 == _SafetyController_0_buffered_status_87, _SafetyController_0_has_data_88 == _SafetyController_0_has_data_87), 
    And(And(Not(False), (monitor_IN_reqRead_87) == (False)), monitor_IN_reqRead_88 == (True), sensor_current_bpm_88 == sensor_current_bpm_87, sensor_OUT_value_88 == sensor_OUT_value_87, sensor_OUT_reqRead_88 == sensor_OUT_reqRead_87, sensor_OUT_reqWrite_88 == sensor_OUT_reqWrite_87, monitor_IN_value_88 == monitor_IN_value_87, monitor_IN_reqWrite_88 == monitor_IN_reqWrite_87, _SafetyController_0_buffered_status_88 == _SafetyController_0_buffered_status_87, _SafetyController_0_has_data_88 == _SafetyController_0_has_data_87), 
    And(And(Not(False), Not((sensor_OUT_reqRead_87) == ((_SafetyController_0_has_data_87) == (0)))), sensor_OUT_reqRead_88 == ((_SafetyController_0_has_data_87) == (0)), sensor_current_bpm_88 == sensor_current_bpm_87, sensor_OUT_value_88 == sensor_OUT_value_87, sensor_OUT_reqWrite_88 == sensor_OUT_reqWrite_87, monitor_IN_value_88 == monitor_IN_value_87, monitor_IN_reqRead_88 == monitor_IN_reqRead_87, monitor_IN_reqWrite_88 == monitor_IN_reqWrite_87, _SafetyController_0_buffered_status_88 == _SafetyController_0_buffered_status_87, _SafetyController_0_has_data_88 == _SafetyController_0_has_data_87), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_87) == ((_SafetyController_0_has_data_87) == (0))))), Not((monitor_IN_reqWrite_87) == (And(monitor_IN_reqRead_87, (_SafetyController_0_has_data_87) == (1))))), monitor_IN_reqWrite_88 == (And(monitor_IN_reqRead_87, (_SafetyController_0_has_data_87) == (1))), sensor_current_bpm_88 == sensor_current_bpm_87, sensor_OUT_value_88 == sensor_OUT_value_87, sensor_OUT_reqRead_88 == sensor_OUT_reqRead_87, sensor_OUT_reqWrite_88 == sensor_OUT_reqWrite_87, monitor_IN_value_88 == monitor_IN_value_87, monitor_IN_reqRead_88 == monitor_IN_reqRead_87, _SafetyController_0_buffered_status_88 == _SafetyController_0_buffered_status_87, _SafetyController_0_has_data_88 == _SafetyController_0_has_data_87), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_87) == (sensor_OUT_reqWrite_87)))), sensor_OUT_reqWrite_87), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_87) == ((_SafetyController_0_has_data_87) == (0)))), Not((monitor_IN_reqWrite_87) == (And(monitor_IN_reqRead_87, (_SafetyController_0_has_data_87) == (1)))))), sensor_OUT_reqRead_87)), _SafetyController_0_buffered_status_88 == (If((sensor_current_bpm_87 > 100), 1, 0)), sensor_current_bpm_88 == (predict_next(sensor_current_bpm_87)), sensor_OUT_reqWrite_88 == (False), _SafetyController_0_has_data_88 == (1), sensor_OUT_reqRead_88 == (False), sensor_OUT_value_88 == (sensor_current_bpm_87), monitor_IN_value_88 == monitor_IN_value_87, monitor_IN_reqRead_88 == monitor_IN_reqRead_87, monitor_IN_reqWrite_88 == monitor_IN_reqWrite_87), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_87) == (False))), monitor_IN_reqWrite_87), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_87) == ((_SafetyController_0_has_data_87) == (0)))), Not((monitor_IN_reqWrite_87) == (And(monitor_IN_reqRead_87, (_SafetyController_0_has_data_87) == (1))))), sensor_OUT_reqRead_87)), monitor_IN_reqWrite_87)), monitor_IN_reqWrite_88 == (False), monitor_IN_value_88 == (_SafetyController_0_buffered_status_87), _SafetyController_0_has_data_88 == (0), monitor_IN_reqRead_88 == (False), sensor_current_bpm_88 == sensor_current_bpm_87, sensor_OUT_value_88 == sensor_OUT_value_87, sensor_OUT_reqRead_88 == sensor_OUT_reqRead_87, sensor_OUT_reqWrite_88 == sensor_OUT_reqWrite_87, _SafetyController_0_buffered_status_88 == _SafetyController_0_buffered_status_87)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_88) == (sensor_OUT_reqWrite_88))), sensor_OUT_reqWrite_89 == (sensor_OUT_reqRead_88), sensor_current_bpm_89 == sensor_current_bpm_88, sensor_OUT_value_89 == sensor_OUT_value_88, sensor_OUT_reqRead_89 == sensor_OUT_reqRead_88, monitor_IN_value_89 == monitor_IN_value_88, monitor_IN_reqRead_89 == monitor_IN_reqRead_88, monitor_IN_reqWrite_89 == monitor_IN_reqWrite_88, _SafetyController_0_buffered_status_89 == _SafetyController_0_buffered_status_88, _SafetyController_0_has_data_89 == _SafetyController_0_has_data_88), 
    And(And(Not(False), (monitor_IN_reqRead_88) == (False)), monitor_IN_reqRead_89 == (True), sensor_current_bpm_89 == sensor_current_bpm_88, sensor_OUT_value_89 == sensor_OUT_value_88, sensor_OUT_reqRead_89 == sensor_OUT_reqRead_88, sensor_OUT_reqWrite_89 == sensor_OUT_reqWrite_88, monitor_IN_value_89 == monitor_IN_value_88, monitor_IN_reqWrite_89 == monitor_IN_reqWrite_88, _SafetyController_0_buffered_status_89 == _SafetyController_0_buffered_status_88, _SafetyController_0_has_data_89 == _SafetyController_0_has_data_88), 
    And(And(Not(False), Not((sensor_OUT_reqRead_88) == ((_SafetyController_0_has_data_88) == (0)))), sensor_OUT_reqRead_89 == ((_SafetyController_0_has_data_88) == (0)), sensor_current_bpm_89 == sensor_current_bpm_88, sensor_OUT_value_89 == sensor_OUT_value_88, sensor_OUT_reqWrite_89 == sensor_OUT_reqWrite_88, monitor_IN_value_89 == monitor_IN_value_88, monitor_IN_reqRead_89 == monitor_IN_reqRead_88, monitor_IN_reqWrite_89 == monitor_IN_reqWrite_88, _SafetyController_0_buffered_status_89 == _SafetyController_0_buffered_status_88, _SafetyController_0_has_data_89 == _SafetyController_0_has_data_88), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_88) == ((_SafetyController_0_has_data_88) == (0))))), Not((monitor_IN_reqWrite_88) == (And(monitor_IN_reqRead_88, (_SafetyController_0_has_data_88) == (1))))), monitor_IN_reqWrite_89 == (And(monitor_IN_reqRead_88, (_SafetyController_0_has_data_88) == (1))), sensor_current_bpm_89 == sensor_current_bpm_88, sensor_OUT_value_89 == sensor_OUT_value_88, sensor_OUT_reqRead_89 == sensor_OUT_reqRead_88, sensor_OUT_reqWrite_89 == sensor_OUT_reqWrite_88, monitor_IN_value_89 == monitor_IN_value_88, monitor_IN_reqRead_89 == monitor_IN_reqRead_88, _SafetyController_0_buffered_status_89 == _SafetyController_0_buffered_status_88, _SafetyController_0_has_data_89 == _SafetyController_0_has_data_88), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_88) == (sensor_OUT_reqWrite_88)))), sensor_OUT_reqWrite_88), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_88) == ((_SafetyController_0_has_data_88) == (0)))), Not((monitor_IN_reqWrite_88) == (And(monitor_IN_reqRead_88, (_SafetyController_0_has_data_88) == (1)))))), sensor_OUT_reqRead_88)), _SafetyController_0_buffered_status_89 == (If((sensor_current_bpm_88 > 100), 1, 0)), sensor_current_bpm_89 == (predict_next(sensor_current_bpm_88)), sensor_OUT_reqWrite_89 == (False), _SafetyController_0_has_data_89 == (1), sensor_OUT_reqRead_89 == (False), sensor_OUT_value_89 == (sensor_current_bpm_88), monitor_IN_value_89 == monitor_IN_value_88, monitor_IN_reqRead_89 == monitor_IN_reqRead_88, monitor_IN_reqWrite_89 == monitor_IN_reqWrite_88), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_88) == (False))), monitor_IN_reqWrite_88), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_88) == ((_SafetyController_0_has_data_88) == (0)))), Not((monitor_IN_reqWrite_88) == (And(monitor_IN_reqRead_88, (_SafetyController_0_has_data_88) == (1))))), sensor_OUT_reqRead_88)), monitor_IN_reqWrite_88)), monitor_IN_reqWrite_89 == (False), monitor_IN_value_89 == (_SafetyController_0_buffered_status_88), _SafetyController_0_has_data_89 == (0), monitor_IN_reqRead_89 == (False), sensor_current_bpm_89 == sensor_current_bpm_88, sensor_OUT_value_89 == sensor_OUT_value_88, sensor_OUT_reqRead_89 == sensor_OUT_reqRead_88, sensor_OUT_reqWrite_89 == sensor_OUT_reqWrite_88, _SafetyController_0_buffered_status_89 == _SafetyController_0_buffered_status_88)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_89) == (sensor_OUT_reqWrite_89))), sensor_OUT_reqWrite_90 == (sensor_OUT_reqRead_89), sensor_current_bpm_90 == sensor_current_bpm_89, sensor_OUT_value_90 == sensor_OUT_value_89, sensor_OUT_reqRead_90 == sensor_OUT_reqRead_89, monitor_IN_value_90 == monitor_IN_value_89, monitor_IN_reqRead_90 == monitor_IN_reqRead_89, monitor_IN_reqWrite_90 == monitor_IN_reqWrite_89, _SafetyController_0_buffered_status_90 == _SafetyController_0_buffered_status_89, _SafetyController_0_has_data_90 == _SafetyController_0_has_data_89), 
    And(And(Not(False), (monitor_IN_reqRead_89) == (False)), monitor_IN_reqRead_90 == (True), sensor_current_bpm_90 == sensor_current_bpm_89, sensor_OUT_value_90 == sensor_OUT_value_89, sensor_OUT_reqRead_90 == sensor_OUT_reqRead_89, sensor_OUT_reqWrite_90 == sensor_OUT_reqWrite_89, monitor_IN_value_90 == monitor_IN_value_89, monitor_IN_reqWrite_90 == monitor_IN_reqWrite_89, _SafetyController_0_buffered_status_90 == _SafetyController_0_buffered_status_89, _SafetyController_0_has_data_90 == _SafetyController_0_has_data_89), 
    And(And(Not(False), Not((sensor_OUT_reqRead_89) == ((_SafetyController_0_has_data_89) == (0)))), sensor_OUT_reqRead_90 == ((_SafetyController_0_has_data_89) == (0)), sensor_current_bpm_90 == sensor_current_bpm_89, sensor_OUT_value_90 == sensor_OUT_value_89, sensor_OUT_reqWrite_90 == sensor_OUT_reqWrite_89, monitor_IN_value_90 == monitor_IN_value_89, monitor_IN_reqRead_90 == monitor_IN_reqRead_89, monitor_IN_reqWrite_90 == monitor_IN_reqWrite_89, _SafetyController_0_buffered_status_90 == _SafetyController_0_buffered_status_89, _SafetyController_0_has_data_90 == _SafetyController_0_has_data_89), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_89) == ((_SafetyController_0_has_data_89) == (0))))), Not((monitor_IN_reqWrite_89) == (And(monitor_IN_reqRead_89, (_SafetyController_0_has_data_89) == (1))))), monitor_IN_reqWrite_90 == (And(monitor_IN_reqRead_89, (_SafetyController_0_has_data_89) == (1))), sensor_current_bpm_90 == sensor_current_bpm_89, sensor_OUT_value_90 == sensor_OUT_value_89, sensor_OUT_reqRead_90 == sensor_OUT_reqRead_89, sensor_OUT_reqWrite_90 == sensor_OUT_reqWrite_89, monitor_IN_value_90 == monitor_IN_value_89, monitor_IN_reqRead_90 == monitor_IN_reqRead_89, _SafetyController_0_buffered_status_90 == _SafetyController_0_buffered_status_89, _SafetyController_0_has_data_90 == _SafetyController_0_has_data_89), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_89) == (sensor_OUT_reqWrite_89)))), sensor_OUT_reqWrite_89), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_89) == ((_SafetyController_0_has_data_89) == (0)))), Not((monitor_IN_reqWrite_89) == (And(monitor_IN_reqRead_89, (_SafetyController_0_has_data_89) == (1)))))), sensor_OUT_reqRead_89)), _SafetyController_0_buffered_status_90 == (If((sensor_current_bpm_89 > 100), 1, 0)), sensor_current_bpm_90 == (predict_next(sensor_current_bpm_89)), sensor_OUT_reqWrite_90 == (False), _SafetyController_0_has_data_90 == (1), sensor_OUT_reqRead_90 == (False), sensor_OUT_value_90 == (sensor_current_bpm_89), monitor_IN_value_90 == monitor_IN_value_89, monitor_IN_reqRead_90 == monitor_IN_reqRead_89, monitor_IN_reqWrite_90 == monitor_IN_reqWrite_89), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_89) == (False))), monitor_IN_reqWrite_89), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_89) == ((_SafetyController_0_has_data_89) == (0)))), Not((monitor_IN_reqWrite_89) == (And(monitor_IN_reqRead_89, (_SafetyController_0_has_data_89) == (1))))), sensor_OUT_reqRead_89)), monitor_IN_reqWrite_89)), monitor_IN_reqWrite_90 == (False), monitor_IN_value_90 == (_SafetyController_0_buffered_status_89), _SafetyController_0_has_data_90 == (0), monitor_IN_reqRead_90 == (False), sensor_current_bpm_90 == sensor_current_bpm_89, sensor_OUT_value_90 == sensor_OUT_value_89, sensor_OUT_reqRead_90 == sensor_OUT_reqRead_89, sensor_OUT_reqWrite_90 == sensor_OUT_reqWrite_89, _SafetyController_0_buffered_status_90 == _SafetyController_0_buffered_status_89)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_90) == (sensor_OUT_reqWrite_90))), sensor_OUT_reqWrite_91 == (sensor_OUT_reqRead_90), sensor_current_bpm_91 == sensor_current_bpm_90, sensor_OUT_value_91 == sensor_OUT_value_90, sensor_OUT_reqRead_91 == sensor_OUT_reqRead_90, monitor_IN_value_91 == monitor_IN_value_90, monitor_IN_reqRead_91 == monitor_IN_reqRead_90, monitor_IN_reqWrite_91 == monitor_IN_reqWrite_90, _SafetyController_0_buffered_status_91 == _SafetyController_0_buffered_status_90, _SafetyController_0_has_data_91 == _SafetyController_0_has_data_90), 
    And(And(Not(False), (monitor_IN_reqRead_90) == (False)), monitor_IN_reqRead_91 == (True), sensor_current_bpm_91 == sensor_current_bpm_90, sensor_OUT_value_91 == sensor_OUT_value_90, sensor_OUT_reqRead_91 == sensor_OUT_reqRead_90, sensor_OUT_reqWrite_91 == sensor_OUT_reqWrite_90, monitor_IN_value_91 == monitor_IN_value_90, monitor_IN_reqWrite_91 == monitor_IN_reqWrite_90, _SafetyController_0_buffered_status_91 == _SafetyController_0_buffered_status_90, _SafetyController_0_has_data_91 == _SafetyController_0_has_data_90), 
    And(And(Not(False), Not((sensor_OUT_reqRead_90) == ((_SafetyController_0_has_data_90) == (0)))), sensor_OUT_reqRead_91 == ((_SafetyController_0_has_data_90) == (0)), sensor_current_bpm_91 == sensor_current_bpm_90, sensor_OUT_value_91 == sensor_OUT_value_90, sensor_OUT_reqWrite_91 == sensor_OUT_reqWrite_90, monitor_IN_value_91 == monitor_IN_value_90, monitor_IN_reqRead_91 == monitor_IN_reqRead_90, monitor_IN_reqWrite_91 == monitor_IN_reqWrite_90, _SafetyController_0_buffered_status_91 == _SafetyController_0_buffered_status_90, _SafetyController_0_has_data_91 == _SafetyController_0_has_data_90), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_90) == ((_SafetyController_0_has_data_90) == (0))))), Not((monitor_IN_reqWrite_90) == (And(monitor_IN_reqRead_90, (_SafetyController_0_has_data_90) == (1))))), monitor_IN_reqWrite_91 == (And(monitor_IN_reqRead_90, (_SafetyController_0_has_data_90) == (1))), sensor_current_bpm_91 == sensor_current_bpm_90, sensor_OUT_value_91 == sensor_OUT_value_90, sensor_OUT_reqRead_91 == sensor_OUT_reqRead_90, sensor_OUT_reqWrite_91 == sensor_OUT_reqWrite_90, monitor_IN_value_91 == monitor_IN_value_90, monitor_IN_reqRead_91 == monitor_IN_reqRead_90, _SafetyController_0_buffered_status_91 == _SafetyController_0_buffered_status_90, _SafetyController_0_has_data_91 == _SafetyController_0_has_data_90), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_90) == (sensor_OUT_reqWrite_90)))), sensor_OUT_reqWrite_90), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_90) == ((_SafetyController_0_has_data_90) == (0)))), Not((monitor_IN_reqWrite_90) == (And(monitor_IN_reqRead_90, (_SafetyController_0_has_data_90) == (1)))))), sensor_OUT_reqRead_90)), _SafetyController_0_buffered_status_91 == (If((sensor_current_bpm_90 > 100), 1, 0)), sensor_current_bpm_91 == (predict_next(sensor_current_bpm_90)), sensor_OUT_reqWrite_91 == (False), _SafetyController_0_has_data_91 == (1), sensor_OUT_reqRead_91 == (False), sensor_OUT_value_91 == (sensor_current_bpm_90), monitor_IN_value_91 == monitor_IN_value_90, monitor_IN_reqRead_91 == monitor_IN_reqRead_90, monitor_IN_reqWrite_91 == monitor_IN_reqWrite_90), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_90) == (False))), monitor_IN_reqWrite_90), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_90) == ((_SafetyController_0_has_data_90) == (0)))), Not((monitor_IN_reqWrite_90) == (And(monitor_IN_reqRead_90, (_SafetyController_0_has_data_90) == (1))))), sensor_OUT_reqRead_90)), monitor_IN_reqWrite_90)), monitor_IN_reqWrite_91 == (False), monitor_IN_value_91 == (_SafetyController_0_buffered_status_90), _SafetyController_0_has_data_91 == (0), monitor_IN_reqRead_91 == (False), sensor_current_bpm_91 == sensor_current_bpm_90, sensor_OUT_value_91 == sensor_OUT_value_90, sensor_OUT_reqRead_91 == sensor_OUT_reqRead_90, sensor_OUT_reqWrite_91 == sensor_OUT_reqWrite_90, _SafetyController_0_buffered_status_91 == _SafetyController_0_buffered_status_90)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_91) == (sensor_OUT_reqWrite_91))), sensor_OUT_reqWrite_92 == (sensor_OUT_reqRead_91), sensor_current_bpm_92 == sensor_current_bpm_91, sensor_OUT_value_92 == sensor_OUT_value_91, sensor_OUT_reqRead_92 == sensor_OUT_reqRead_91, monitor_IN_value_92 == monitor_IN_value_91, monitor_IN_reqRead_92 == monitor_IN_reqRead_91, monitor_IN_reqWrite_92 == monitor_IN_reqWrite_91, _SafetyController_0_buffered_status_92 == _SafetyController_0_buffered_status_91, _SafetyController_0_has_data_92 == _SafetyController_0_has_data_91), 
    And(And(Not(False), (monitor_IN_reqRead_91) == (False)), monitor_IN_reqRead_92 == (True), sensor_current_bpm_92 == sensor_current_bpm_91, sensor_OUT_value_92 == sensor_OUT_value_91, sensor_OUT_reqRead_92 == sensor_OUT_reqRead_91, sensor_OUT_reqWrite_92 == sensor_OUT_reqWrite_91, monitor_IN_value_92 == monitor_IN_value_91, monitor_IN_reqWrite_92 == monitor_IN_reqWrite_91, _SafetyController_0_buffered_status_92 == _SafetyController_0_buffered_status_91, _SafetyController_0_has_data_92 == _SafetyController_0_has_data_91), 
    And(And(Not(False), Not((sensor_OUT_reqRead_91) == ((_SafetyController_0_has_data_91) == (0)))), sensor_OUT_reqRead_92 == ((_SafetyController_0_has_data_91) == (0)), sensor_current_bpm_92 == sensor_current_bpm_91, sensor_OUT_value_92 == sensor_OUT_value_91, sensor_OUT_reqWrite_92 == sensor_OUT_reqWrite_91, monitor_IN_value_92 == monitor_IN_value_91, monitor_IN_reqRead_92 == monitor_IN_reqRead_91, monitor_IN_reqWrite_92 == monitor_IN_reqWrite_91, _SafetyController_0_buffered_status_92 == _SafetyController_0_buffered_status_91, _SafetyController_0_has_data_92 == _SafetyController_0_has_data_91), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_91) == ((_SafetyController_0_has_data_91) == (0))))), Not((monitor_IN_reqWrite_91) == (And(monitor_IN_reqRead_91, (_SafetyController_0_has_data_91) == (1))))), monitor_IN_reqWrite_92 == (And(monitor_IN_reqRead_91, (_SafetyController_0_has_data_91) == (1))), sensor_current_bpm_92 == sensor_current_bpm_91, sensor_OUT_value_92 == sensor_OUT_value_91, sensor_OUT_reqRead_92 == sensor_OUT_reqRead_91, sensor_OUT_reqWrite_92 == sensor_OUT_reqWrite_91, monitor_IN_value_92 == monitor_IN_value_91, monitor_IN_reqRead_92 == monitor_IN_reqRead_91, _SafetyController_0_buffered_status_92 == _SafetyController_0_buffered_status_91, _SafetyController_0_has_data_92 == _SafetyController_0_has_data_91), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_91) == (sensor_OUT_reqWrite_91)))), sensor_OUT_reqWrite_91), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_91) == ((_SafetyController_0_has_data_91) == (0)))), Not((monitor_IN_reqWrite_91) == (And(monitor_IN_reqRead_91, (_SafetyController_0_has_data_91) == (1)))))), sensor_OUT_reqRead_91)), _SafetyController_0_buffered_status_92 == (If((sensor_current_bpm_91 > 100), 1, 0)), sensor_current_bpm_92 == (predict_next(sensor_current_bpm_91)), sensor_OUT_reqWrite_92 == (False), _SafetyController_0_has_data_92 == (1), sensor_OUT_reqRead_92 == (False), sensor_OUT_value_92 == (sensor_current_bpm_91), monitor_IN_value_92 == monitor_IN_value_91, monitor_IN_reqRead_92 == monitor_IN_reqRead_91, monitor_IN_reqWrite_92 == monitor_IN_reqWrite_91), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_91) == (False))), monitor_IN_reqWrite_91), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_91) == ((_SafetyController_0_has_data_91) == (0)))), Not((monitor_IN_reqWrite_91) == (And(monitor_IN_reqRead_91, (_SafetyController_0_has_data_91) == (1))))), sensor_OUT_reqRead_91)), monitor_IN_reqWrite_91)), monitor_IN_reqWrite_92 == (False), monitor_IN_value_92 == (_SafetyController_0_buffered_status_91), _SafetyController_0_has_data_92 == (0), monitor_IN_reqRead_92 == (False), sensor_current_bpm_92 == sensor_current_bpm_91, sensor_OUT_value_92 == sensor_OUT_value_91, sensor_OUT_reqRead_92 == sensor_OUT_reqRead_91, sensor_OUT_reqWrite_92 == sensor_OUT_reqWrite_91, _SafetyController_0_buffered_status_92 == _SafetyController_0_buffered_status_91)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_92) == (sensor_OUT_reqWrite_92))), sensor_OUT_reqWrite_93 == (sensor_OUT_reqRead_92), sensor_current_bpm_93 == sensor_current_bpm_92, sensor_OUT_value_93 == sensor_OUT_value_92, sensor_OUT_reqRead_93 == sensor_OUT_reqRead_92, monitor_IN_value_93 == monitor_IN_value_92, monitor_IN_reqRead_93 == monitor_IN_reqRead_92, monitor_IN_reqWrite_93 == monitor_IN_reqWrite_92, _SafetyController_0_buffered_status_93 == _SafetyController_0_buffered_status_92, _SafetyController_0_has_data_93 == _SafetyController_0_has_data_92), 
    And(And(Not(False), (monitor_IN_reqRead_92) == (False)), monitor_IN_reqRead_93 == (True), sensor_current_bpm_93 == sensor_current_bpm_92, sensor_OUT_value_93 == sensor_OUT_value_92, sensor_OUT_reqRead_93 == sensor_OUT_reqRead_92, sensor_OUT_reqWrite_93 == sensor_OUT_reqWrite_92, monitor_IN_value_93 == monitor_IN_value_92, monitor_IN_reqWrite_93 == monitor_IN_reqWrite_92, _SafetyController_0_buffered_status_93 == _SafetyController_0_buffered_status_92, _SafetyController_0_has_data_93 == _SafetyController_0_has_data_92), 
    And(And(Not(False), Not((sensor_OUT_reqRead_92) == ((_SafetyController_0_has_data_92) == (0)))), sensor_OUT_reqRead_93 == ((_SafetyController_0_has_data_92) == (0)), sensor_current_bpm_93 == sensor_current_bpm_92, sensor_OUT_value_93 == sensor_OUT_value_92, sensor_OUT_reqWrite_93 == sensor_OUT_reqWrite_92, monitor_IN_value_93 == monitor_IN_value_92, monitor_IN_reqRead_93 == monitor_IN_reqRead_92, monitor_IN_reqWrite_93 == monitor_IN_reqWrite_92, _SafetyController_0_buffered_status_93 == _SafetyController_0_buffered_status_92, _SafetyController_0_has_data_93 == _SafetyController_0_has_data_92), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_92) == ((_SafetyController_0_has_data_92) == (0))))), Not((monitor_IN_reqWrite_92) == (And(monitor_IN_reqRead_92, (_SafetyController_0_has_data_92) == (1))))), monitor_IN_reqWrite_93 == (And(monitor_IN_reqRead_92, (_SafetyController_0_has_data_92) == (1))), sensor_current_bpm_93 == sensor_current_bpm_92, sensor_OUT_value_93 == sensor_OUT_value_92, sensor_OUT_reqRead_93 == sensor_OUT_reqRead_92, sensor_OUT_reqWrite_93 == sensor_OUT_reqWrite_92, monitor_IN_value_93 == monitor_IN_value_92, monitor_IN_reqRead_93 == monitor_IN_reqRead_92, _SafetyController_0_buffered_status_93 == _SafetyController_0_buffered_status_92, _SafetyController_0_has_data_93 == _SafetyController_0_has_data_92), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_92) == (sensor_OUT_reqWrite_92)))), sensor_OUT_reqWrite_92), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_92) == ((_SafetyController_0_has_data_92) == (0)))), Not((monitor_IN_reqWrite_92) == (And(monitor_IN_reqRead_92, (_SafetyController_0_has_data_92) == (1)))))), sensor_OUT_reqRead_92)), _SafetyController_0_buffered_status_93 == (If((sensor_current_bpm_92 > 100), 1, 0)), sensor_current_bpm_93 == (predict_next(sensor_current_bpm_92)), sensor_OUT_reqWrite_93 == (False), _SafetyController_0_has_data_93 == (1), sensor_OUT_reqRead_93 == (False), sensor_OUT_value_93 == (sensor_current_bpm_92), monitor_IN_value_93 == monitor_IN_value_92, monitor_IN_reqRead_93 == monitor_IN_reqRead_92, monitor_IN_reqWrite_93 == monitor_IN_reqWrite_92), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_92) == (False))), monitor_IN_reqWrite_92), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_92) == ((_SafetyController_0_has_data_92) == (0)))), Not((monitor_IN_reqWrite_92) == (And(monitor_IN_reqRead_92, (_SafetyController_0_has_data_92) == (1))))), sensor_OUT_reqRead_92)), monitor_IN_reqWrite_92)), monitor_IN_reqWrite_93 == (False), monitor_IN_value_93 == (_SafetyController_0_buffered_status_92), _SafetyController_0_has_data_93 == (0), monitor_IN_reqRead_93 == (False), sensor_current_bpm_93 == sensor_current_bpm_92, sensor_OUT_value_93 == sensor_OUT_value_92, sensor_OUT_reqRead_93 == sensor_OUT_reqRead_92, sensor_OUT_reqWrite_93 == sensor_OUT_reqWrite_92, _SafetyController_0_buffered_status_93 == _SafetyController_0_buffered_status_92)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_93) == (sensor_OUT_reqWrite_93))), sensor_OUT_reqWrite_94 == (sensor_OUT_reqRead_93), sensor_current_bpm_94 == sensor_current_bpm_93, sensor_OUT_value_94 == sensor_OUT_value_93, sensor_OUT_reqRead_94 == sensor_OUT_reqRead_93, monitor_IN_value_94 == monitor_IN_value_93, monitor_IN_reqRead_94 == monitor_IN_reqRead_93, monitor_IN_reqWrite_94 == monitor_IN_reqWrite_93, _SafetyController_0_buffered_status_94 == _SafetyController_0_buffered_status_93, _SafetyController_0_has_data_94 == _SafetyController_0_has_data_93), 
    And(And(Not(False), (monitor_IN_reqRead_93) == (False)), monitor_IN_reqRead_94 == (True), sensor_current_bpm_94 == sensor_current_bpm_93, sensor_OUT_value_94 == sensor_OUT_value_93, sensor_OUT_reqRead_94 == sensor_OUT_reqRead_93, sensor_OUT_reqWrite_94 == sensor_OUT_reqWrite_93, monitor_IN_value_94 == monitor_IN_value_93, monitor_IN_reqWrite_94 == monitor_IN_reqWrite_93, _SafetyController_0_buffered_status_94 == _SafetyController_0_buffered_status_93, _SafetyController_0_has_data_94 == _SafetyController_0_has_data_93), 
    And(And(Not(False), Not((sensor_OUT_reqRead_93) == ((_SafetyController_0_has_data_93) == (0)))), sensor_OUT_reqRead_94 == ((_SafetyController_0_has_data_93) == (0)), sensor_current_bpm_94 == sensor_current_bpm_93, sensor_OUT_value_94 == sensor_OUT_value_93, sensor_OUT_reqWrite_94 == sensor_OUT_reqWrite_93, monitor_IN_value_94 == monitor_IN_value_93, monitor_IN_reqRead_94 == monitor_IN_reqRead_93, monitor_IN_reqWrite_94 == monitor_IN_reqWrite_93, _SafetyController_0_buffered_status_94 == _SafetyController_0_buffered_status_93, _SafetyController_0_has_data_94 == _SafetyController_0_has_data_93), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_93) == ((_SafetyController_0_has_data_93) == (0))))), Not((monitor_IN_reqWrite_93) == (And(monitor_IN_reqRead_93, (_SafetyController_0_has_data_93) == (1))))), monitor_IN_reqWrite_94 == (And(monitor_IN_reqRead_93, (_SafetyController_0_has_data_93) == (1))), sensor_current_bpm_94 == sensor_current_bpm_93, sensor_OUT_value_94 == sensor_OUT_value_93, sensor_OUT_reqRead_94 == sensor_OUT_reqRead_93, sensor_OUT_reqWrite_94 == sensor_OUT_reqWrite_93, monitor_IN_value_94 == monitor_IN_value_93, monitor_IN_reqRead_94 == monitor_IN_reqRead_93, _SafetyController_0_buffered_status_94 == _SafetyController_0_buffered_status_93, _SafetyController_0_has_data_94 == _SafetyController_0_has_data_93), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_93) == (sensor_OUT_reqWrite_93)))), sensor_OUT_reqWrite_93), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_93) == ((_SafetyController_0_has_data_93) == (0)))), Not((monitor_IN_reqWrite_93) == (And(monitor_IN_reqRead_93, (_SafetyController_0_has_data_93) == (1)))))), sensor_OUT_reqRead_93)), _SafetyController_0_buffered_status_94 == (If((sensor_current_bpm_93 > 100), 1, 0)), sensor_current_bpm_94 == (predict_next(sensor_current_bpm_93)), sensor_OUT_reqWrite_94 == (False), _SafetyController_0_has_data_94 == (1), sensor_OUT_reqRead_94 == (False), sensor_OUT_value_94 == (sensor_current_bpm_93), monitor_IN_value_94 == monitor_IN_value_93, monitor_IN_reqRead_94 == monitor_IN_reqRead_93, monitor_IN_reqWrite_94 == monitor_IN_reqWrite_93), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_93) == (False))), monitor_IN_reqWrite_93), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_93) == ((_SafetyController_0_has_data_93) == (0)))), Not((monitor_IN_reqWrite_93) == (And(monitor_IN_reqRead_93, (_SafetyController_0_has_data_93) == (1))))), sensor_OUT_reqRead_93)), monitor_IN_reqWrite_93)), monitor_IN_reqWrite_94 == (False), monitor_IN_value_94 == (_SafetyController_0_buffered_status_93), _SafetyController_0_has_data_94 == (0), monitor_IN_reqRead_94 == (False), sensor_current_bpm_94 == sensor_current_bpm_93, sensor_OUT_value_94 == sensor_OUT_value_93, sensor_OUT_reqRead_94 == sensor_OUT_reqRead_93, sensor_OUT_reqWrite_94 == sensor_OUT_reqWrite_93, _SafetyController_0_buffered_status_94 == _SafetyController_0_buffered_status_93)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_94) == (sensor_OUT_reqWrite_94))), sensor_OUT_reqWrite_95 == (sensor_OUT_reqRead_94), sensor_current_bpm_95 == sensor_current_bpm_94, sensor_OUT_value_95 == sensor_OUT_value_94, sensor_OUT_reqRead_95 == sensor_OUT_reqRead_94, monitor_IN_value_95 == monitor_IN_value_94, monitor_IN_reqRead_95 == monitor_IN_reqRead_94, monitor_IN_reqWrite_95 == monitor_IN_reqWrite_94, _SafetyController_0_buffered_status_95 == _SafetyController_0_buffered_status_94, _SafetyController_0_has_data_95 == _SafetyController_0_has_data_94), 
    And(And(Not(False), (monitor_IN_reqRead_94) == (False)), monitor_IN_reqRead_95 == (True), sensor_current_bpm_95 == sensor_current_bpm_94, sensor_OUT_value_95 == sensor_OUT_value_94, sensor_OUT_reqRead_95 == sensor_OUT_reqRead_94, sensor_OUT_reqWrite_95 == sensor_OUT_reqWrite_94, monitor_IN_value_95 == monitor_IN_value_94, monitor_IN_reqWrite_95 == monitor_IN_reqWrite_94, _SafetyController_0_buffered_status_95 == _SafetyController_0_buffered_status_94, _SafetyController_0_has_data_95 == _SafetyController_0_has_data_94), 
    And(And(Not(False), Not((sensor_OUT_reqRead_94) == ((_SafetyController_0_has_data_94) == (0)))), sensor_OUT_reqRead_95 == ((_SafetyController_0_has_data_94) == (0)), sensor_current_bpm_95 == sensor_current_bpm_94, sensor_OUT_value_95 == sensor_OUT_value_94, sensor_OUT_reqWrite_95 == sensor_OUT_reqWrite_94, monitor_IN_value_95 == monitor_IN_value_94, monitor_IN_reqRead_95 == monitor_IN_reqRead_94, monitor_IN_reqWrite_95 == monitor_IN_reqWrite_94, _SafetyController_0_buffered_status_95 == _SafetyController_0_buffered_status_94, _SafetyController_0_has_data_95 == _SafetyController_0_has_data_94), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_94) == ((_SafetyController_0_has_data_94) == (0))))), Not((monitor_IN_reqWrite_94) == (And(monitor_IN_reqRead_94, (_SafetyController_0_has_data_94) == (1))))), monitor_IN_reqWrite_95 == (And(monitor_IN_reqRead_94, (_SafetyController_0_has_data_94) == (1))), sensor_current_bpm_95 == sensor_current_bpm_94, sensor_OUT_value_95 == sensor_OUT_value_94, sensor_OUT_reqRead_95 == sensor_OUT_reqRead_94, sensor_OUT_reqWrite_95 == sensor_OUT_reqWrite_94, monitor_IN_value_95 == monitor_IN_value_94, monitor_IN_reqRead_95 == monitor_IN_reqRead_94, _SafetyController_0_buffered_status_95 == _SafetyController_0_buffered_status_94, _SafetyController_0_has_data_95 == _SafetyController_0_has_data_94), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_94) == (sensor_OUT_reqWrite_94)))), sensor_OUT_reqWrite_94), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_94) == ((_SafetyController_0_has_data_94) == (0)))), Not((monitor_IN_reqWrite_94) == (And(monitor_IN_reqRead_94, (_SafetyController_0_has_data_94) == (1)))))), sensor_OUT_reqRead_94)), _SafetyController_0_buffered_status_95 == (If((sensor_current_bpm_94 > 100), 1, 0)), sensor_current_bpm_95 == (predict_next(sensor_current_bpm_94)), sensor_OUT_reqWrite_95 == (False), _SafetyController_0_has_data_95 == (1), sensor_OUT_reqRead_95 == (False), sensor_OUT_value_95 == (sensor_current_bpm_94), monitor_IN_value_95 == monitor_IN_value_94, monitor_IN_reqRead_95 == monitor_IN_reqRead_94, monitor_IN_reqWrite_95 == monitor_IN_reqWrite_94), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_94) == (False))), monitor_IN_reqWrite_94), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_94) == ((_SafetyController_0_has_data_94) == (0)))), Not((monitor_IN_reqWrite_94) == (And(monitor_IN_reqRead_94, (_SafetyController_0_has_data_94) == (1))))), sensor_OUT_reqRead_94)), monitor_IN_reqWrite_94)), monitor_IN_reqWrite_95 == (False), monitor_IN_value_95 == (_SafetyController_0_buffered_status_94), _SafetyController_0_has_data_95 == (0), monitor_IN_reqRead_95 == (False), sensor_current_bpm_95 == sensor_current_bpm_94, sensor_OUT_value_95 == sensor_OUT_value_94, sensor_OUT_reqRead_95 == sensor_OUT_reqRead_94, sensor_OUT_reqWrite_95 == sensor_OUT_reqWrite_94, _SafetyController_0_buffered_status_95 == _SafetyController_0_buffered_status_94)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_95) == (sensor_OUT_reqWrite_95))), sensor_OUT_reqWrite_96 == (sensor_OUT_reqRead_95), sensor_current_bpm_96 == sensor_current_bpm_95, sensor_OUT_value_96 == sensor_OUT_value_95, sensor_OUT_reqRead_96 == sensor_OUT_reqRead_95, monitor_IN_value_96 == monitor_IN_value_95, monitor_IN_reqRead_96 == monitor_IN_reqRead_95, monitor_IN_reqWrite_96 == monitor_IN_reqWrite_95, _SafetyController_0_buffered_status_96 == _SafetyController_0_buffered_status_95, _SafetyController_0_has_data_96 == _SafetyController_0_has_data_95), 
    And(And(Not(False), (monitor_IN_reqRead_95) == (False)), monitor_IN_reqRead_96 == (True), sensor_current_bpm_96 == sensor_current_bpm_95, sensor_OUT_value_96 == sensor_OUT_value_95, sensor_OUT_reqRead_96 == sensor_OUT_reqRead_95, sensor_OUT_reqWrite_96 == sensor_OUT_reqWrite_95, monitor_IN_value_96 == monitor_IN_value_95, monitor_IN_reqWrite_96 == monitor_IN_reqWrite_95, _SafetyController_0_buffered_status_96 == _SafetyController_0_buffered_status_95, _SafetyController_0_has_data_96 == _SafetyController_0_has_data_95), 
    And(And(Not(False), Not((sensor_OUT_reqRead_95) == ((_SafetyController_0_has_data_95) == (0)))), sensor_OUT_reqRead_96 == ((_SafetyController_0_has_data_95) == (0)), sensor_current_bpm_96 == sensor_current_bpm_95, sensor_OUT_value_96 == sensor_OUT_value_95, sensor_OUT_reqWrite_96 == sensor_OUT_reqWrite_95, monitor_IN_value_96 == monitor_IN_value_95, monitor_IN_reqRead_96 == monitor_IN_reqRead_95, monitor_IN_reqWrite_96 == monitor_IN_reqWrite_95, _SafetyController_0_buffered_status_96 == _SafetyController_0_buffered_status_95, _SafetyController_0_has_data_96 == _SafetyController_0_has_data_95), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_95) == ((_SafetyController_0_has_data_95) == (0))))), Not((monitor_IN_reqWrite_95) == (And(monitor_IN_reqRead_95, (_SafetyController_0_has_data_95) == (1))))), monitor_IN_reqWrite_96 == (And(monitor_IN_reqRead_95, (_SafetyController_0_has_data_95) == (1))), sensor_current_bpm_96 == sensor_current_bpm_95, sensor_OUT_value_96 == sensor_OUT_value_95, sensor_OUT_reqRead_96 == sensor_OUT_reqRead_95, sensor_OUT_reqWrite_96 == sensor_OUT_reqWrite_95, monitor_IN_value_96 == monitor_IN_value_95, monitor_IN_reqRead_96 == monitor_IN_reqRead_95, _SafetyController_0_buffered_status_96 == _SafetyController_0_buffered_status_95, _SafetyController_0_has_data_96 == _SafetyController_0_has_data_95), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_95) == (sensor_OUT_reqWrite_95)))), sensor_OUT_reqWrite_95), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_95) == ((_SafetyController_0_has_data_95) == (0)))), Not((monitor_IN_reqWrite_95) == (And(monitor_IN_reqRead_95, (_SafetyController_0_has_data_95) == (1)))))), sensor_OUT_reqRead_95)), _SafetyController_0_buffered_status_96 == (If((sensor_current_bpm_95 > 100), 1, 0)), sensor_current_bpm_96 == (predict_next(sensor_current_bpm_95)), sensor_OUT_reqWrite_96 == (False), _SafetyController_0_has_data_96 == (1), sensor_OUT_reqRead_96 == (False), sensor_OUT_value_96 == (sensor_current_bpm_95), monitor_IN_value_96 == monitor_IN_value_95, monitor_IN_reqRead_96 == monitor_IN_reqRead_95, monitor_IN_reqWrite_96 == monitor_IN_reqWrite_95), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_95) == (False))), monitor_IN_reqWrite_95), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_95) == ((_SafetyController_0_has_data_95) == (0)))), Not((monitor_IN_reqWrite_95) == (And(monitor_IN_reqRead_95, (_SafetyController_0_has_data_95) == (1))))), sensor_OUT_reqRead_95)), monitor_IN_reqWrite_95)), monitor_IN_reqWrite_96 == (False), monitor_IN_value_96 == (_SafetyController_0_buffered_status_95), _SafetyController_0_has_data_96 == (0), monitor_IN_reqRead_96 == (False), sensor_current_bpm_96 == sensor_current_bpm_95, sensor_OUT_value_96 == sensor_OUT_value_95, sensor_OUT_reqRead_96 == sensor_OUT_reqRead_95, sensor_OUT_reqWrite_96 == sensor_OUT_reqWrite_95, _SafetyController_0_buffered_status_96 == _SafetyController_0_buffered_status_95)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_96) == (sensor_OUT_reqWrite_96))), sensor_OUT_reqWrite_97 == (sensor_OUT_reqRead_96), sensor_current_bpm_97 == sensor_current_bpm_96, sensor_OUT_value_97 == sensor_OUT_value_96, sensor_OUT_reqRead_97 == sensor_OUT_reqRead_96, monitor_IN_value_97 == monitor_IN_value_96, monitor_IN_reqRead_97 == monitor_IN_reqRead_96, monitor_IN_reqWrite_97 == monitor_IN_reqWrite_96, _SafetyController_0_buffered_status_97 == _SafetyController_0_buffered_status_96, _SafetyController_0_has_data_97 == _SafetyController_0_has_data_96), 
    And(And(Not(False), (monitor_IN_reqRead_96) == (False)), monitor_IN_reqRead_97 == (True), sensor_current_bpm_97 == sensor_current_bpm_96, sensor_OUT_value_97 == sensor_OUT_value_96, sensor_OUT_reqRead_97 == sensor_OUT_reqRead_96, sensor_OUT_reqWrite_97 == sensor_OUT_reqWrite_96, monitor_IN_value_97 == monitor_IN_value_96, monitor_IN_reqWrite_97 == monitor_IN_reqWrite_96, _SafetyController_0_buffered_status_97 == _SafetyController_0_buffered_status_96, _SafetyController_0_has_data_97 == _SafetyController_0_has_data_96), 
    And(And(Not(False), Not((sensor_OUT_reqRead_96) == ((_SafetyController_0_has_data_96) == (0)))), sensor_OUT_reqRead_97 == ((_SafetyController_0_has_data_96) == (0)), sensor_current_bpm_97 == sensor_current_bpm_96, sensor_OUT_value_97 == sensor_OUT_value_96, sensor_OUT_reqWrite_97 == sensor_OUT_reqWrite_96, monitor_IN_value_97 == monitor_IN_value_96, monitor_IN_reqRead_97 == monitor_IN_reqRead_96, monitor_IN_reqWrite_97 == monitor_IN_reqWrite_96, _SafetyController_0_buffered_status_97 == _SafetyController_0_buffered_status_96, _SafetyController_0_has_data_97 == _SafetyController_0_has_data_96), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_96) == ((_SafetyController_0_has_data_96) == (0))))), Not((monitor_IN_reqWrite_96) == (And(monitor_IN_reqRead_96, (_SafetyController_0_has_data_96) == (1))))), monitor_IN_reqWrite_97 == (And(monitor_IN_reqRead_96, (_SafetyController_0_has_data_96) == (1))), sensor_current_bpm_97 == sensor_current_bpm_96, sensor_OUT_value_97 == sensor_OUT_value_96, sensor_OUT_reqRead_97 == sensor_OUT_reqRead_96, sensor_OUT_reqWrite_97 == sensor_OUT_reqWrite_96, monitor_IN_value_97 == monitor_IN_value_96, monitor_IN_reqRead_97 == monitor_IN_reqRead_96, _SafetyController_0_buffered_status_97 == _SafetyController_0_buffered_status_96, _SafetyController_0_has_data_97 == _SafetyController_0_has_data_96), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_96) == (sensor_OUT_reqWrite_96)))), sensor_OUT_reqWrite_96), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_96) == ((_SafetyController_0_has_data_96) == (0)))), Not((monitor_IN_reqWrite_96) == (And(monitor_IN_reqRead_96, (_SafetyController_0_has_data_96) == (1)))))), sensor_OUT_reqRead_96)), _SafetyController_0_buffered_status_97 == (If((sensor_current_bpm_96 > 100), 1, 0)), sensor_current_bpm_97 == (predict_next(sensor_current_bpm_96)), sensor_OUT_reqWrite_97 == (False), _SafetyController_0_has_data_97 == (1), sensor_OUT_reqRead_97 == (False), sensor_OUT_value_97 == (sensor_current_bpm_96), monitor_IN_value_97 == monitor_IN_value_96, monitor_IN_reqRead_97 == monitor_IN_reqRead_96, monitor_IN_reqWrite_97 == monitor_IN_reqWrite_96), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_96) == (False))), monitor_IN_reqWrite_96), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_96) == ((_SafetyController_0_has_data_96) == (0)))), Not((monitor_IN_reqWrite_96) == (And(monitor_IN_reqRead_96, (_SafetyController_0_has_data_96) == (1))))), sensor_OUT_reqRead_96)), monitor_IN_reqWrite_96)), monitor_IN_reqWrite_97 == (False), monitor_IN_value_97 == (_SafetyController_0_buffered_status_96), _SafetyController_0_has_data_97 == (0), monitor_IN_reqRead_97 == (False), sensor_current_bpm_97 == sensor_current_bpm_96, sensor_OUT_value_97 == sensor_OUT_value_96, sensor_OUT_reqRead_97 == sensor_OUT_reqRead_96, sensor_OUT_reqWrite_97 == sensor_OUT_reqWrite_96, _SafetyController_0_buffered_status_97 == _SafetyController_0_buffered_status_96)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_97) == (sensor_OUT_reqWrite_97))), sensor_OUT_reqWrite_98 == (sensor_OUT_reqRead_97), sensor_current_bpm_98 == sensor_current_bpm_97, sensor_OUT_value_98 == sensor_OUT_value_97, sensor_OUT_reqRead_98 == sensor_OUT_reqRead_97, monitor_IN_value_98 == monitor_IN_value_97, monitor_IN_reqRead_98 == monitor_IN_reqRead_97, monitor_IN_reqWrite_98 == monitor_IN_reqWrite_97, _SafetyController_0_buffered_status_98 == _SafetyController_0_buffered_status_97, _SafetyController_0_has_data_98 == _SafetyController_0_has_data_97), 
    And(And(Not(False), (monitor_IN_reqRead_97) == (False)), monitor_IN_reqRead_98 == (True), sensor_current_bpm_98 == sensor_current_bpm_97, sensor_OUT_value_98 == sensor_OUT_value_97, sensor_OUT_reqRead_98 == sensor_OUT_reqRead_97, sensor_OUT_reqWrite_98 == sensor_OUT_reqWrite_97, monitor_IN_value_98 == monitor_IN_value_97, monitor_IN_reqWrite_98 == monitor_IN_reqWrite_97, _SafetyController_0_buffered_status_98 == _SafetyController_0_buffered_status_97, _SafetyController_0_has_data_98 == _SafetyController_0_has_data_97), 
    And(And(Not(False), Not((sensor_OUT_reqRead_97) == ((_SafetyController_0_has_data_97) == (0)))), sensor_OUT_reqRead_98 == ((_SafetyController_0_has_data_97) == (0)), sensor_current_bpm_98 == sensor_current_bpm_97, sensor_OUT_value_98 == sensor_OUT_value_97, sensor_OUT_reqWrite_98 == sensor_OUT_reqWrite_97, monitor_IN_value_98 == monitor_IN_value_97, monitor_IN_reqRead_98 == monitor_IN_reqRead_97, monitor_IN_reqWrite_98 == monitor_IN_reqWrite_97, _SafetyController_0_buffered_status_98 == _SafetyController_0_buffered_status_97, _SafetyController_0_has_data_98 == _SafetyController_0_has_data_97), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_97) == ((_SafetyController_0_has_data_97) == (0))))), Not((monitor_IN_reqWrite_97) == (And(monitor_IN_reqRead_97, (_SafetyController_0_has_data_97) == (1))))), monitor_IN_reqWrite_98 == (And(monitor_IN_reqRead_97, (_SafetyController_0_has_data_97) == (1))), sensor_current_bpm_98 == sensor_current_bpm_97, sensor_OUT_value_98 == sensor_OUT_value_97, sensor_OUT_reqRead_98 == sensor_OUT_reqRead_97, sensor_OUT_reqWrite_98 == sensor_OUT_reqWrite_97, monitor_IN_value_98 == monitor_IN_value_97, monitor_IN_reqRead_98 == monitor_IN_reqRead_97, _SafetyController_0_buffered_status_98 == _SafetyController_0_buffered_status_97, _SafetyController_0_has_data_98 == _SafetyController_0_has_data_97), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_97) == (sensor_OUT_reqWrite_97)))), sensor_OUT_reqWrite_97), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_97) == ((_SafetyController_0_has_data_97) == (0)))), Not((monitor_IN_reqWrite_97) == (And(monitor_IN_reqRead_97, (_SafetyController_0_has_data_97) == (1)))))), sensor_OUT_reqRead_97)), _SafetyController_0_buffered_status_98 == (If((sensor_current_bpm_97 > 100), 1, 0)), sensor_current_bpm_98 == (predict_next(sensor_current_bpm_97)), sensor_OUT_reqWrite_98 == (False), _SafetyController_0_has_data_98 == (1), sensor_OUT_reqRead_98 == (False), sensor_OUT_value_98 == (sensor_current_bpm_97), monitor_IN_value_98 == monitor_IN_value_97, monitor_IN_reqRead_98 == monitor_IN_reqRead_97, monitor_IN_reqWrite_98 == monitor_IN_reqWrite_97), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_97) == (False))), monitor_IN_reqWrite_97), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_97) == ((_SafetyController_0_has_data_97) == (0)))), Not((monitor_IN_reqWrite_97) == (And(monitor_IN_reqRead_97, (_SafetyController_0_has_data_97) == (1))))), sensor_OUT_reqRead_97)), monitor_IN_reqWrite_97)), monitor_IN_reqWrite_98 == (False), monitor_IN_value_98 == (_SafetyController_0_buffered_status_97), _SafetyController_0_has_data_98 == (0), monitor_IN_reqRead_98 == (False), sensor_current_bpm_98 == sensor_current_bpm_97, sensor_OUT_value_98 == sensor_OUT_value_97, sensor_OUT_reqRead_98 == sensor_OUT_reqRead_97, sensor_OUT_reqWrite_98 == sensor_OUT_reqWrite_97, _SafetyController_0_buffered_status_98 == _SafetyController_0_buffered_status_97)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_98) == (sensor_OUT_reqWrite_98))), sensor_OUT_reqWrite_99 == (sensor_OUT_reqRead_98), sensor_current_bpm_99 == sensor_current_bpm_98, sensor_OUT_value_99 == sensor_OUT_value_98, sensor_OUT_reqRead_99 == sensor_OUT_reqRead_98, monitor_IN_value_99 == monitor_IN_value_98, monitor_IN_reqRead_99 == monitor_IN_reqRead_98, monitor_IN_reqWrite_99 == monitor_IN_reqWrite_98, _SafetyController_0_buffered_status_99 == _SafetyController_0_buffered_status_98, _SafetyController_0_has_data_99 == _SafetyController_0_has_data_98), 
    And(And(Not(False), (monitor_IN_reqRead_98) == (False)), monitor_IN_reqRead_99 == (True), sensor_current_bpm_99 == sensor_current_bpm_98, sensor_OUT_value_99 == sensor_OUT_value_98, sensor_OUT_reqRead_99 == sensor_OUT_reqRead_98, sensor_OUT_reqWrite_99 == sensor_OUT_reqWrite_98, monitor_IN_value_99 == monitor_IN_value_98, monitor_IN_reqWrite_99 == monitor_IN_reqWrite_98, _SafetyController_0_buffered_status_99 == _SafetyController_0_buffered_status_98, _SafetyController_0_has_data_99 == _SafetyController_0_has_data_98), 
    And(And(Not(False), Not((sensor_OUT_reqRead_98) == ((_SafetyController_0_has_data_98) == (0)))), sensor_OUT_reqRead_99 == ((_SafetyController_0_has_data_98) == (0)), sensor_current_bpm_99 == sensor_current_bpm_98, sensor_OUT_value_99 == sensor_OUT_value_98, sensor_OUT_reqWrite_99 == sensor_OUT_reqWrite_98, monitor_IN_value_99 == monitor_IN_value_98, monitor_IN_reqRead_99 == monitor_IN_reqRead_98, monitor_IN_reqWrite_99 == monitor_IN_reqWrite_98, _SafetyController_0_buffered_status_99 == _SafetyController_0_buffered_status_98, _SafetyController_0_has_data_99 == _SafetyController_0_has_data_98), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_98) == ((_SafetyController_0_has_data_98) == (0))))), Not((monitor_IN_reqWrite_98) == (And(monitor_IN_reqRead_98, (_SafetyController_0_has_data_98) == (1))))), monitor_IN_reqWrite_99 == (And(monitor_IN_reqRead_98, (_SafetyController_0_has_data_98) == (1))), sensor_current_bpm_99 == sensor_current_bpm_98, sensor_OUT_value_99 == sensor_OUT_value_98, sensor_OUT_reqRead_99 == sensor_OUT_reqRead_98, sensor_OUT_reqWrite_99 == sensor_OUT_reqWrite_98, monitor_IN_value_99 == monitor_IN_value_98, monitor_IN_reqRead_99 == monitor_IN_reqRead_98, _SafetyController_0_buffered_status_99 == _SafetyController_0_buffered_status_98, _SafetyController_0_has_data_99 == _SafetyController_0_has_data_98), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_98) == (sensor_OUT_reqWrite_98)))), sensor_OUT_reqWrite_98), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_98) == ((_SafetyController_0_has_data_98) == (0)))), Not((monitor_IN_reqWrite_98) == (And(monitor_IN_reqRead_98, (_SafetyController_0_has_data_98) == (1)))))), sensor_OUT_reqRead_98)), _SafetyController_0_buffered_status_99 == (If((sensor_current_bpm_98 > 100), 1, 0)), sensor_current_bpm_99 == (predict_next(sensor_current_bpm_98)), sensor_OUT_reqWrite_99 == (False), _SafetyController_0_has_data_99 == (1), sensor_OUT_reqRead_99 == (False), sensor_OUT_value_99 == (sensor_current_bpm_98), monitor_IN_value_99 == monitor_IN_value_98, monitor_IN_reqRead_99 == monitor_IN_reqRead_98, monitor_IN_reqWrite_99 == monitor_IN_reqWrite_98), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_98) == (False))), monitor_IN_reqWrite_98), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_98) == ((_SafetyController_0_has_data_98) == (0)))), Not((monitor_IN_reqWrite_98) == (And(monitor_IN_reqRead_98, (_SafetyController_0_has_data_98) == (1))))), sensor_OUT_reqRead_98)), monitor_IN_reqWrite_98)), monitor_IN_reqWrite_99 == (False), monitor_IN_value_99 == (_SafetyController_0_buffered_status_98), _SafetyController_0_has_data_99 == (0), monitor_IN_reqRead_99 == (False), sensor_current_bpm_99 == sensor_current_bpm_98, sensor_OUT_value_99 == sensor_OUT_value_98, sensor_OUT_reqRead_99 == sensor_OUT_reqRead_98, sensor_OUT_reqWrite_99 == sensor_OUT_reqWrite_98, _SafetyController_0_buffered_status_99 == _SafetyController_0_buffered_status_98)
)
)

s.add(Or(
    And(And(Not(False), Not((sensor_OUT_reqRead_99) == (sensor_OUT_reqWrite_99))), sensor_OUT_reqWrite_100 == (sensor_OUT_reqRead_99), sensor_current_bpm_100 == sensor_current_bpm_99, sensor_OUT_value_100 == sensor_OUT_value_99, sensor_OUT_reqRead_100 == sensor_OUT_reqRead_99, monitor_IN_value_100 == monitor_IN_value_99, monitor_IN_reqRead_100 == monitor_IN_reqRead_99, monitor_IN_reqWrite_100 == monitor_IN_reqWrite_99, _SafetyController_0_buffered_status_100 == _SafetyController_0_buffered_status_99, _SafetyController_0_has_data_100 == _SafetyController_0_has_data_99), 
    And(And(Not(False), (monitor_IN_reqRead_99) == (False)), monitor_IN_reqRead_100 == (True), sensor_current_bpm_100 == sensor_current_bpm_99, sensor_OUT_value_100 == sensor_OUT_value_99, sensor_OUT_reqRead_100 == sensor_OUT_reqRead_99, sensor_OUT_reqWrite_100 == sensor_OUT_reqWrite_99, monitor_IN_value_100 == monitor_IN_value_99, monitor_IN_reqWrite_100 == monitor_IN_reqWrite_99, _SafetyController_0_buffered_status_100 == _SafetyController_0_buffered_status_99, _SafetyController_0_has_data_100 == _SafetyController_0_has_data_99), 
    And(And(Not(False), Not((sensor_OUT_reqRead_99) == ((_SafetyController_0_has_data_99) == (0)))), sensor_OUT_reqRead_100 == ((_SafetyController_0_has_data_99) == (0)), sensor_current_bpm_100 == sensor_current_bpm_99, sensor_OUT_value_100 == sensor_OUT_value_99, sensor_OUT_reqWrite_100 == sensor_OUT_reqWrite_99, monitor_IN_value_100 == monitor_IN_value_99, monitor_IN_reqRead_100 == monitor_IN_reqRead_99, monitor_IN_reqWrite_100 == monitor_IN_reqWrite_99, _SafetyController_0_buffered_status_100 == _SafetyController_0_buffered_status_99, _SafetyController_0_has_data_100 == _SafetyController_0_has_data_99), 
    And(And(Not(Or(False, Not((sensor_OUT_reqRead_99) == ((_SafetyController_0_has_data_99) == (0))))), Not((monitor_IN_reqWrite_99) == (And(monitor_IN_reqRead_99, (_SafetyController_0_has_data_99) == (1))))), monitor_IN_reqWrite_100 == (And(monitor_IN_reqRead_99, (_SafetyController_0_has_data_99) == (1))), sensor_current_bpm_100 == sensor_current_bpm_99, sensor_OUT_value_100 == sensor_OUT_value_99, sensor_OUT_reqRead_100 == sensor_OUT_reqRead_99, sensor_OUT_reqWrite_100 == sensor_OUT_reqWrite_99, monitor_IN_value_100 == monitor_IN_value_99, monitor_IN_reqRead_100 == monitor_IN_reqRead_99, _SafetyController_0_buffered_status_100 == _SafetyController_0_buffered_status_99, _SafetyController_0_has_data_100 == _SafetyController_0_has_data_99), 
    And(And(And(Not(Or(False, Not((sensor_OUT_reqRead_99) == (sensor_OUT_reqWrite_99)))), sensor_OUT_reqWrite_99), And(Not(Or(Or(False, Not((sensor_OUT_reqRead_99) == ((_SafetyController_0_has_data_99) == (0)))), Not((monitor_IN_reqWrite_99) == (And(monitor_IN_reqRead_99, (_SafetyController_0_has_data_99) == (1)))))), sensor_OUT_reqRead_99)), _SafetyController_0_buffered_status_100 == (If((sensor_current_bpm_99 > 100), 1, 0)), sensor_current_bpm_100 == (predict_next(sensor_current_bpm_99)), sensor_OUT_reqWrite_100 == (False), _SafetyController_0_has_data_100 == (1), sensor_OUT_reqRead_100 == (False), sensor_OUT_value_100 == (sensor_current_bpm_99), monitor_IN_value_100 == monitor_IN_value_99, monitor_IN_reqRead_100 == monitor_IN_reqRead_99, monitor_IN_reqWrite_100 == monitor_IN_reqWrite_99), 
    And(And(And(Not(Or(False, (monitor_IN_reqRead_99) == (False))), monitor_IN_reqWrite_99), And(Not(Or(Or(Or(False, Not((sensor_OUT_reqRead_99) == ((_SafetyController_0_has_data_99) == (0)))), Not((monitor_IN_reqWrite_99) == (And(monitor_IN_reqRead_99, (_SafetyController_0_has_data_99) == (1))))), sensor_OUT_reqRead_99)), monitor_IN_reqWrite_99)), monitor_IN_reqWrite_100 == (False), monitor_IN_value_100 == (_SafetyController_0_buffered_status_99), _SafetyController_0_has_data_100 == (0), monitor_IN_reqRead_100 == (False), sensor_current_bpm_100 == sensor_current_bpm_99, sensor_OUT_value_100 == sensor_OUT_value_99, sensor_OUT_reqRead_100 == sensor_OUT_reqRead_99, sensor_OUT_reqWrite_100 == sensor_OUT_reqWrite_99, _SafetyController_0_buffered_status_100 == _SafetyController_0_buffered_status_99)
)
)

# Properties verification
# Property monitor_safe violation condition:
s.add(Or(
  Not(And((monitor_IN_value_0) == (0), (monitor_IN_value_1) == (0), (monitor_IN_value_2) == (0), (monitor_IN_value_3) == (0), (monitor_IN_value_4) == (0), (monitor_IN_value_5) == (0), (monitor_IN_value_6) == (0), (monitor_IN_value_7) == (0), (monitor_IN_value_8) == (0), (monitor_IN_value_9) == (0), (monitor_IN_value_10) == (0), (monitor_IN_value_11) == (0), (monitor_IN_value_12) == (0), (monitor_IN_value_13) == (0), (monitor_IN_value_14) == (0), (monitor_IN_value_15) == (0), (monitor_IN_value_16) == (0), (monitor_IN_value_17) == (0), (monitor_IN_value_18) == (0), (monitor_IN_value_19) == (0), (monitor_IN_value_20) == (0), (monitor_IN_value_21) == (0), (monitor_IN_value_22) == (0), (monitor_IN_value_23) == (0), (monitor_IN_value_24) == (0), (monitor_IN_value_25) == (0), (monitor_IN_value_26) == (0), (monitor_IN_value_27) == (0), (monitor_IN_value_28) == (0), (monitor_IN_value_29) == (0), (monitor_IN_value_30) == (0), (monitor_IN_value_31) == (0), (monitor_IN_value_32) == (0), (monitor_IN_value_33) == (0), (monitor_IN_value_34) == (0), (monitor_IN_value_35) == (0), (monitor_IN_value_36) == (0), (monitor_IN_value_37) == (0), (monitor_IN_value_38) == (0), (monitor_IN_value_39) == (0), (monitor_IN_value_40) == (0), (monitor_IN_value_41) == (0), (monitor_IN_value_42) == (0), (monitor_IN_value_43) == (0), (monitor_IN_value_44) == (0), (monitor_IN_value_45) == (0), (monitor_IN_value_46) == (0), (monitor_IN_value_47) == (0), (monitor_IN_value_48) == (0), (monitor_IN_value_49) == (0), (monitor_IN_value_50) == (0), (monitor_IN_value_51) == (0), (monitor_IN_value_52) == (0), (monitor_IN_value_53) == (0), (monitor_IN_value_54) == (0), (monitor_IN_value_55) == (0), (monitor_IN_value_56) == (0), (monitor_IN_value_57) == (0), (monitor_IN_value_58) == (0), (monitor_IN_value_59) == (0), (monitor_IN_value_60) == (0), (monitor_IN_value_61) == (0), (monitor_IN_value_62) == (0), (monitor_IN_value_63) == (0), (monitor_IN_value_64) == (0), (monitor_IN_value_65) == (0), (monitor_IN_value_66) == (0), (monitor_IN_value_67) == (0), (monitor_IN_value_68) == (0), (monitor_IN_value_69) == (0), (monitor_IN_value_70) == (0), (monitor_IN_value_71) == (0), (monitor_IN_value_72) == (0), (monitor_IN_value_73) == (0), (monitor_IN_value_74) == (0), (monitor_IN_value_75) == (0), (monitor_IN_value_76) == (0), (monitor_IN_value_77) == (0), (monitor_IN_value_78) == (0), (monitor_IN_value_79) == (0), (monitor_IN_value_80) == (0), (monitor_IN_value_81) == (0), (monitor_IN_value_82) == (0), (monitor_IN_value_83) == (0), (monitor_IN_value_84) == (0), (monitor_IN_value_85) == (0), (monitor_IN_value_86) == (0), (monitor_IN_value_87) == (0), (monitor_IN_value_88) == (0), (monitor_IN_value_89) == (0), (monitor_IN_value_90) == (0), (monitor_IN_value_91) == (0), (monitor_IN_value_92) == (0), (monitor_IN_value_93) == (0), (monitor_IN_value_94) == (0), (monitor_IN_value_95) == (0), (monitor_IN_value_96) == (0), (monitor_IN_value_97) == (0), (monitor_IN_value_98) == (0), (monitor_IN_value_99) == (0), (monitor_IN_value_100) == (0)))
))

# ===============================================================================
# Implicit type safety verification (bounded integers)
# To check for integer overflows/underflows, uncomment the following block.
# NOTE: This checks if ANY variable violates its bounds. If 'sat', a violation exists.
# You may want to comment out other property checks to isolate this verification.
# ===============================================================================
# s.add(Or(
#   Or(sensor_current_bpm_0 < 0, sensor_current_bpm_0 > 200),
#   Or(sensor_OUT_value_0 < 0, sensor_OUT_value_0 > 200),
#   Or(monitor_IN_value_0 < 0, monitor_IN_value_0 > 1),
#   Or(_SafetyController_0_buffered_status_0 < 0, _SafetyController_0_buffered_status_0 > 1),
#   Or(_SafetyController_0_has_data_0 < 0, _SafetyController_0_has_data_0 > 1),
#   Or(sensor_current_bpm_1 < 0, sensor_current_bpm_1 > 200),
#   Or(sensor_OUT_value_1 < 0, sensor_OUT_value_1 > 200),
#   Or(monitor_IN_value_1 < 0, monitor_IN_value_1 > 1),
#   Or(_SafetyController_0_buffered_status_1 < 0, _SafetyController_0_buffered_status_1 > 1),
#   Or(_SafetyController_0_has_data_1 < 0, _SafetyController_0_has_data_1 > 1),
#   Or(sensor_current_bpm_2 < 0, sensor_current_bpm_2 > 200),
#   Or(sensor_OUT_value_2 < 0, sensor_OUT_value_2 > 200),
#   Or(monitor_IN_value_2 < 0, monitor_IN_value_2 > 1),
#   Or(_SafetyController_0_buffered_status_2 < 0, _SafetyController_0_buffered_status_2 > 1),
#   Or(_SafetyController_0_has_data_2 < 0, _SafetyController_0_has_data_2 > 1),
#   Or(sensor_current_bpm_3 < 0, sensor_current_bpm_3 > 200),
#   Or(sensor_OUT_value_3 < 0, sensor_OUT_value_3 > 200),
#   Or(monitor_IN_value_3 < 0, monitor_IN_value_3 > 1),
#   Or(_SafetyController_0_buffered_status_3 < 0, _SafetyController_0_buffered_status_3 > 1),
#   Or(_SafetyController_0_has_data_3 < 0, _SafetyController_0_has_data_3 > 1),
#   Or(sensor_current_bpm_4 < 0, sensor_current_bpm_4 > 200),
#   Or(sensor_OUT_value_4 < 0, sensor_OUT_value_4 > 200),
#   Or(monitor_IN_value_4 < 0, monitor_IN_value_4 > 1),
#   Or(_SafetyController_0_buffered_status_4 < 0, _SafetyController_0_buffered_status_4 > 1),
#   Or(_SafetyController_0_has_data_4 < 0, _SafetyController_0_has_data_4 > 1),
#   Or(sensor_current_bpm_5 < 0, sensor_current_bpm_5 > 200),
#   Or(sensor_OUT_value_5 < 0, sensor_OUT_value_5 > 200),
#   Or(monitor_IN_value_5 < 0, monitor_IN_value_5 > 1),
#   Or(_SafetyController_0_buffered_status_5 < 0, _SafetyController_0_buffered_status_5 > 1),
#   Or(_SafetyController_0_has_data_5 < 0, _SafetyController_0_has_data_5 > 1),
#   Or(sensor_current_bpm_6 < 0, sensor_current_bpm_6 > 200),
#   Or(sensor_OUT_value_6 < 0, sensor_OUT_value_6 > 200),
#   Or(monitor_IN_value_6 < 0, monitor_IN_value_6 > 1),
#   Or(_SafetyController_0_buffered_status_6 < 0, _SafetyController_0_buffered_status_6 > 1),
#   Or(_SafetyController_0_has_data_6 < 0, _SafetyController_0_has_data_6 > 1),
#   Or(sensor_current_bpm_7 < 0, sensor_current_bpm_7 > 200),
#   Or(sensor_OUT_value_7 < 0, sensor_OUT_value_7 > 200),
#   Or(monitor_IN_value_7 < 0, monitor_IN_value_7 > 1),
#   Or(_SafetyController_0_buffered_status_7 < 0, _SafetyController_0_buffered_status_7 > 1),
#   Or(_SafetyController_0_has_data_7 < 0, _SafetyController_0_has_data_7 > 1),
#   Or(sensor_current_bpm_8 < 0, sensor_current_bpm_8 > 200),
#   Or(sensor_OUT_value_8 < 0, sensor_OUT_value_8 > 200),
#   Or(monitor_IN_value_8 < 0, monitor_IN_value_8 > 1),
#   Or(_SafetyController_0_buffered_status_8 < 0, _SafetyController_0_buffered_status_8 > 1),
#   Or(_SafetyController_0_has_data_8 < 0, _SafetyController_0_has_data_8 > 1),
#   Or(sensor_current_bpm_9 < 0, sensor_current_bpm_9 > 200),
#   Or(sensor_OUT_value_9 < 0, sensor_OUT_value_9 > 200),
#   Or(monitor_IN_value_9 < 0, monitor_IN_value_9 > 1),
#   Or(_SafetyController_0_buffered_status_9 < 0, _SafetyController_0_buffered_status_9 > 1),
#   Or(_SafetyController_0_has_data_9 < 0, _SafetyController_0_has_data_9 > 1),
#   Or(sensor_current_bpm_10 < 0, sensor_current_bpm_10 > 200),
#   Or(sensor_OUT_value_10 < 0, sensor_OUT_value_10 > 200),
#   Or(monitor_IN_value_10 < 0, monitor_IN_value_10 > 1),
#   Or(_SafetyController_0_buffered_status_10 < 0, _SafetyController_0_buffered_status_10 > 1),
#   Or(_SafetyController_0_has_data_10 < 0, _SafetyController_0_has_data_10 > 1),
#   Or(sensor_current_bpm_11 < 0, sensor_current_bpm_11 > 200),
#   Or(sensor_OUT_value_11 < 0, sensor_OUT_value_11 > 200),
#   Or(monitor_IN_value_11 < 0, monitor_IN_value_11 > 1),
#   Or(_SafetyController_0_buffered_status_11 < 0, _SafetyController_0_buffered_status_11 > 1),
#   Or(_SafetyController_0_has_data_11 < 0, _SafetyController_0_has_data_11 > 1),
#   Or(sensor_current_bpm_12 < 0, sensor_current_bpm_12 > 200),
#   Or(sensor_OUT_value_12 < 0, sensor_OUT_value_12 > 200),
#   Or(monitor_IN_value_12 < 0, monitor_IN_value_12 > 1),
#   Or(_SafetyController_0_buffered_status_12 < 0, _SafetyController_0_buffered_status_12 > 1),
#   Or(_SafetyController_0_has_data_12 < 0, _SafetyController_0_has_data_12 > 1),
#   Or(sensor_current_bpm_13 < 0, sensor_current_bpm_13 > 200),
#   Or(sensor_OUT_value_13 < 0, sensor_OUT_value_13 > 200),
#   Or(monitor_IN_value_13 < 0, monitor_IN_value_13 > 1),
#   Or(_SafetyController_0_buffered_status_13 < 0, _SafetyController_0_buffered_status_13 > 1),
#   Or(_SafetyController_0_has_data_13 < 0, _SafetyController_0_has_data_13 > 1),
#   Or(sensor_current_bpm_14 < 0, sensor_current_bpm_14 > 200),
#   Or(sensor_OUT_value_14 < 0, sensor_OUT_value_14 > 200),
#   Or(monitor_IN_value_14 < 0, monitor_IN_value_14 > 1),
#   Or(_SafetyController_0_buffered_status_14 < 0, _SafetyController_0_buffered_status_14 > 1),
#   Or(_SafetyController_0_has_data_14 < 0, _SafetyController_0_has_data_14 > 1),
#   Or(sensor_current_bpm_15 < 0, sensor_current_bpm_15 > 200),
#   Or(sensor_OUT_value_15 < 0, sensor_OUT_value_15 > 200),
#   Or(monitor_IN_value_15 < 0, monitor_IN_value_15 > 1),
#   Or(_SafetyController_0_buffered_status_15 < 0, _SafetyController_0_buffered_status_15 > 1),
#   Or(_SafetyController_0_has_data_15 < 0, _SafetyController_0_has_data_15 > 1),
#   Or(sensor_current_bpm_16 < 0, sensor_current_bpm_16 > 200),
#   Or(sensor_OUT_value_16 < 0, sensor_OUT_value_16 > 200),
#   Or(monitor_IN_value_16 < 0, monitor_IN_value_16 > 1),
#   Or(_SafetyController_0_buffered_status_16 < 0, _SafetyController_0_buffered_status_16 > 1),
#   Or(_SafetyController_0_has_data_16 < 0, _SafetyController_0_has_data_16 > 1),
#   Or(sensor_current_bpm_17 < 0, sensor_current_bpm_17 > 200),
#   Or(sensor_OUT_value_17 < 0, sensor_OUT_value_17 > 200),
#   Or(monitor_IN_value_17 < 0, monitor_IN_value_17 > 1),
#   Or(_SafetyController_0_buffered_status_17 < 0, _SafetyController_0_buffered_status_17 > 1),
#   Or(_SafetyController_0_has_data_17 < 0, _SafetyController_0_has_data_17 > 1),
#   Or(sensor_current_bpm_18 < 0, sensor_current_bpm_18 > 200),
#   Or(sensor_OUT_value_18 < 0, sensor_OUT_value_18 > 200),
#   Or(monitor_IN_value_18 < 0, monitor_IN_value_18 > 1),
#   Or(_SafetyController_0_buffered_status_18 < 0, _SafetyController_0_buffered_status_18 > 1),
#   Or(_SafetyController_0_has_data_18 < 0, _SafetyController_0_has_data_18 > 1),
#   Or(sensor_current_bpm_19 < 0, sensor_current_bpm_19 > 200),
#   Or(sensor_OUT_value_19 < 0, sensor_OUT_value_19 > 200),
#   Or(monitor_IN_value_19 < 0, monitor_IN_value_19 > 1),
#   Or(_SafetyController_0_buffered_status_19 < 0, _SafetyController_0_buffered_status_19 > 1),
#   Or(_SafetyController_0_has_data_19 < 0, _SafetyController_0_has_data_19 > 1),
#   Or(sensor_current_bpm_20 < 0, sensor_current_bpm_20 > 200),
#   Or(sensor_OUT_value_20 < 0, sensor_OUT_value_20 > 200),
#   Or(monitor_IN_value_20 < 0, monitor_IN_value_20 > 1),
#   Or(_SafetyController_0_buffered_status_20 < 0, _SafetyController_0_buffered_status_20 > 1),
#   Or(_SafetyController_0_has_data_20 < 0, _SafetyController_0_has_data_20 > 1),
#   Or(sensor_current_bpm_21 < 0, sensor_current_bpm_21 > 200),
#   Or(sensor_OUT_value_21 < 0, sensor_OUT_value_21 > 200),
#   Or(monitor_IN_value_21 < 0, monitor_IN_value_21 > 1),
#   Or(_SafetyController_0_buffered_status_21 < 0, _SafetyController_0_buffered_status_21 > 1),
#   Or(_SafetyController_0_has_data_21 < 0, _SafetyController_0_has_data_21 > 1),
#   Or(sensor_current_bpm_22 < 0, sensor_current_bpm_22 > 200),
#   Or(sensor_OUT_value_22 < 0, sensor_OUT_value_22 > 200),
#   Or(monitor_IN_value_22 < 0, monitor_IN_value_22 > 1),
#   Or(_SafetyController_0_buffered_status_22 < 0, _SafetyController_0_buffered_status_22 > 1),
#   Or(_SafetyController_0_has_data_22 < 0, _SafetyController_0_has_data_22 > 1),
#   Or(sensor_current_bpm_23 < 0, sensor_current_bpm_23 > 200),
#   Or(sensor_OUT_value_23 < 0, sensor_OUT_value_23 > 200),
#   Or(monitor_IN_value_23 < 0, monitor_IN_value_23 > 1),
#   Or(_SafetyController_0_buffered_status_23 < 0, _SafetyController_0_buffered_status_23 > 1),
#   Or(_SafetyController_0_has_data_23 < 0, _SafetyController_0_has_data_23 > 1),
#   Or(sensor_current_bpm_24 < 0, sensor_current_bpm_24 > 200),
#   Or(sensor_OUT_value_24 < 0, sensor_OUT_value_24 > 200),
#   Or(monitor_IN_value_24 < 0, monitor_IN_value_24 > 1),
#   Or(_SafetyController_0_buffered_status_24 < 0, _SafetyController_0_buffered_status_24 > 1),
#   Or(_SafetyController_0_has_data_24 < 0, _SafetyController_0_has_data_24 > 1),
#   Or(sensor_current_bpm_25 < 0, sensor_current_bpm_25 > 200),
#   Or(sensor_OUT_value_25 < 0, sensor_OUT_value_25 > 200),
#   Or(monitor_IN_value_25 < 0, monitor_IN_value_25 > 1),
#   Or(_SafetyController_0_buffered_status_25 < 0, _SafetyController_0_buffered_status_25 > 1),
#   Or(_SafetyController_0_has_data_25 < 0, _SafetyController_0_has_data_25 > 1),
#   Or(sensor_current_bpm_26 < 0, sensor_current_bpm_26 > 200),
#   Or(sensor_OUT_value_26 < 0, sensor_OUT_value_26 > 200),
#   Or(monitor_IN_value_26 < 0, monitor_IN_value_26 > 1),
#   Or(_SafetyController_0_buffered_status_26 < 0, _SafetyController_0_buffered_status_26 > 1),
#   Or(_SafetyController_0_has_data_26 < 0, _SafetyController_0_has_data_26 > 1),
#   Or(sensor_current_bpm_27 < 0, sensor_current_bpm_27 > 200),
#   Or(sensor_OUT_value_27 < 0, sensor_OUT_value_27 > 200),
#   Or(monitor_IN_value_27 < 0, monitor_IN_value_27 > 1),
#   Or(_SafetyController_0_buffered_status_27 < 0, _SafetyController_0_buffered_status_27 > 1),
#   Or(_SafetyController_0_has_data_27 < 0, _SafetyController_0_has_data_27 > 1),
#   Or(sensor_current_bpm_28 < 0, sensor_current_bpm_28 > 200),
#   Or(sensor_OUT_value_28 < 0, sensor_OUT_value_28 > 200),
#   Or(monitor_IN_value_28 < 0, monitor_IN_value_28 > 1),
#   Or(_SafetyController_0_buffered_status_28 < 0, _SafetyController_0_buffered_status_28 > 1),
#   Or(_SafetyController_0_has_data_28 < 0, _SafetyController_0_has_data_28 > 1),
#   Or(sensor_current_bpm_29 < 0, sensor_current_bpm_29 > 200),
#   Or(sensor_OUT_value_29 < 0, sensor_OUT_value_29 > 200),
#   Or(monitor_IN_value_29 < 0, monitor_IN_value_29 > 1),
#   Or(_SafetyController_0_buffered_status_29 < 0, _SafetyController_0_buffered_status_29 > 1),
#   Or(_SafetyController_0_has_data_29 < 0, _SafetyController_0_has_data_29 > 1),
#   Or(sensor_current_bpm_30 < 0, sensor_current_bpm_30 > 200),
#   Or(sensor_OUT_value_30 < 0, sensor_OUT_value_30 > 200),
#   Or(monitor_IN_value_30 < 0, monitor_IN_value_30 > 1),
#   Or(_SafetyController_0_buffered_status_30 < 0, _SafetyController_0_buffered_status_30 > 1),
#   Or(_SafetyController_0_has_data_30 < 0, _SafetyController_0_has_data_30 > 1),
#   Or(sensor_current_bpm_31 < 0, sensor_current_bpm_31 > 200),
#   Or(sensor_OUT_value_31 < 0, sensor_OUT_value_31 > 200),
#   Or(monitor_IN_value_31 < 0, monitor_IN_value_31 > 1),
#   Or(_SafetyController_0_buffered_status_31 < 0, _SafetyController_0_buffered_status_31 > 1),
#   Or(_SafetyController_0_has_data_31 < 0, _SafetyController_0_has_data_31 > 1),
#   Or(sensor_current_bpm_32 < 0, sensor_current_bpm_32 > 200),
#   Or(sensor_OUT_value_32 < 0, sensor_OUT_value_32 > 200),
#   Or(monitor_IN_value_32 < 0, monitor_IN_value_32 > 1),
#   Or(_SafetyController_0_buffered_status_32 < 0, _SafetyController_0_buffered_status_32 > 1),
#   Or(_SafetyController_0_has_data_32 < 0, _SafetyController_0_has_data_32 > 1),
#   Or(sensor_current_bpm_33 < 0, sensor_current_bpm_33 > 200),
#   Or(sensor_OUT_value_33 < 0, sensor_OUT_value_33 > 200),
#   Or(monitor_IN_value_33 < 0, monitor_IN_value_33 > 1),
#   Or(_SafetyController_0_buffered_status_33 < 0, _SafetyController_0_buffered_status_33 > 1),
#   Or(_SafetyController_0_has_data_33 < 0, _SafetyController_0_has_data_33 > 1),
#   Or(sensor_current_bpm_34 < 0, sensor_current_bpm_34 > 200),
#   Or(sensor_OUT_value_34 < 0, sensor_OUT_value_34 > 200),
#   Or(monitor_IN_value_34 < 0, monitor_IN_value_34 > 1),
#   Or(_SafetyController_0_buffered_status_34 < 0, _SafetyController_0_buffered_status_34 > 1),
#   Or(_SafetyController_0_has_data_34 < 0, _SafetyController_0_has_data_34 > 1),
#   Or(sensor_current_bpm_35 < 0, sensor_current_bpm_35 > 200),
#   Or(sensor_OUT_value_35 < 0, sensor_OUT_value_35 > 200),
#   Or(monitor_IN_value_35 < 0, monitor_IN_value_35 > 1),
#   Or(_SafetyController_0_buffered_status_35 < 0, _SafetyController_0_buffered_status_35 > 1),
#   Or(_SafetyController_0_has_data_35 < 0, _SafetyController_0_has_data_35 > 1),
#   Or(sensor_current_bpm_36 < 0, sensor_current_bpm_36 > 200),
#   Or(sensor_OUT_value_36 < 0, sensor_OUT_value_36 > 200),
#   Or(monitor_IN_value_36 < 0, monitor_IN_value_36 > 1),
#   Or(_SafetyController_0_buffered_status_36 < 0, _SafetyController_0_buffered_status_36 > 1),
#   Or(_SafetyController_0_has_data_36 < 0, _SafetyController_0_has_data_36 > 1),
#   Or(sensor_current_bpm_37 < 0, sensor_current_bpm_37 > 200),
#   Or(sensor_OUT_value_37 < 0, sensor_OUT_value_37 > 200),
#   Or(monitor_IN_value_37 < 0, monitor_IN_value_37 > 1),
#   Or(_SafetyController_0_buffered_status_37 < 0, _SafetyController_0_buffered_status_37 > 1),
#   Or(_SafetyController_0_has_data_37 < 0, _SafetyController_0_has_data_37 > 1),
#   Or(sensor_current_bpm_38 < 0, sensor_current_bpm_38 > 200),
#   Or(sensor_OUT_value_38 < 0, sensor_OUT_value_38 > 200),
#   Or(monitor_IN_value_38 < 0, monitor_IN_value_38 > 1),
#   Or(_SafetyController_0_buffered_status_38 < 0, _SafetyController_0_buffered_status_38 > 1),
#   Or(_SafetyController_0_has_data_38 < 0, _SafetyController_0_has_data_38 > 1),
#   Or(sensor_current_bpm_39 < 0, sensor_current_bpm_39 > 200),
#   Or(sensor_OUT_value_39 < 0, sensor_OUT_value_39 > 200),
#   Or(monitor_IN_value_39 < 0, monitor_IN_value_39 > 1),
#   Or(_SafetyController_0_buffered_status_39 < 0, _SafetyController_0_buffered_status_39 > 1),
#   Or(_SafetyController_0_has_data_39 < 0, _SafetyController_0_has_data_39 > 1),
#   Or(sensor_current_bpm_40 < 0, sensor_current_bpm_40 > 200),
#   Or(sensor_OUT_value_40 < 0, sensor_OUT_value_40 > 200),
#   Or(monitor_IN_value_40 < 0, monitor_IN_value_40 > 1),
#   Or(_SafetyController_0_buffered_status_40 < 0, _SafetyController_0_buffered_status_40 > 1),
#   Or(_SafetyController_0_has_data_40 < 0, _SafetyController_0_has_data_40 > 1),
#   Or(sensor_current_bpm_41 < 0, sensor_current_bpm_41 > 200),
#   Or(sensor_OUT_value_41 < 0, sensor_OUT_value_41 > 200),
#   Or(monitor_IN_value_41 < 0, monitor_IN_value_41 > 1),
#   Or(_SafetyController_0_buffered_status_41 < 0, _SafetyController_0_buffered_status_41 > 1),
#   Or(_SafetyController_0_has_data_41 < 0, _SafetyController_0_has_data_41 > 1),
#   Or(sensor_current_bpm_42 < 0, sensor_current_bpm_42 > 200),
#   Or(sensor_OUT_value_42 < 0, sensor_OUT_value_42 > 200),
#   Or(monitor_IN_value_42 < 0, monitor_IN_value_42 > 1),
#   Or(_SafetyController_0_buffered_status_42 < 0, _SafetyController_0_buffered_status_42 > 1),
#   Or(_SafetyController_0_has_data_42 < 0, _SafetyController_0_has_data_42 > 1),
#   Or(sensor_current_bpm_43 < 0, sensor_current_bpm_43 > 200),
#   Or(sensor_OUT_value_43 < 0, sensor_OUT_value_43 > 200),
#   Or(monitor_IN_value_43 < 0, monitor_IN_value_43 > 1),
#   Or(_SafetyController_0_buffered_status_43 < 0, _SafetyController_0_buffered_status_43 > 1),
#   Or(_SafetyController_0_has_data_43 < 0, _SafetyController_0_has_data_43 > 1),
#   Or(sensor_current_bpm_44 < 0, sensor_current_bpm_44 > 200),
#   Or(sensor_OUT_value_44 < 0, sensor_OUT_value_44 > 200),
#   Or(monitor_IN_value_44 < 0, monitor_IN_value_44 > 1),
#   Or(_SafetyController_0_buffered_status_44 < 0, _SafetyController_0_buffered_status_44 > 1),
#   Or(_SafetyController_0_has_data_44 < 0, _SafetyController_0_has_data_44 > 1),
#   Or(sensor_current_bpm_45 < 0, sensor_current_bpm_45 > 200),
#   Or(sensor_OUT_value_45 < 0, sensor_OUT_value_45 > 200),
#   Or(monitor_IN_value_45 < 0, monitor_IN_value_45 > 1),
#   Or(_SafetyController_0_buffered_status_45 < 0, _SafetyController_0_buffered_status_45 > 1),
#   Or(_SafetyController_0_has_data_45 < 0, _SafetyController_0_has_data_45 > 1),
#   Or(sensor_current_bpm_46 < 0, sensor_current_bpm_46 > 200),
#   Or(sensor_OUT_value_46 < 0, sensor_OUT_value_46 > 200),
#   Or(monitor_IN_value_46 < 0, monitor_IN_value_46 > 1),
#   Or(_SafetyController_0_buffered_status_46 < 0, _SafetyController_0_buffered_status_46 > 1),
#   Or(_SafetyController_0_has_data_46 < 0, _SafetyController_0_has_data_46 > 1),
#   Or(sensor_current_bpm_47 < 0, sensor_current_bpm_47 > 200),
#   Or(sensor_OUT_value_47 < 0, sensor_OUT_value_47 > 200),
#   Or(monitor_IN_value_47 < 0, monitor_IN_value_47 > 1),
#   Or(_SafetyController_0_buffered_status_47 < 0, _SafetyController_0_buffered_status_47 > 1),
#   Or(_SafetyController_0_has_data_47 < 0, _SafetyController_0_has_data_47 > 1),
#   Or(sensor_current_bpm_48 < 0, sensor_current_bpm_48 > 200),
#   Or(sensor_OUT_value_48 < 0, sensor_OUT_value_48 > 200),
#   Or(monitor_IN_value_48 < 0, monitor_IN_value_48 > 1),
#   Or(_SafetyController_0_buffered_status_48 < 0, _SafetyController_0_buffered_status_48 > 1),
#   Or(_SafetyController_0_has_data_48 < 0, _SafetyController_0_has_data_48 > 1),
#   Or(sensor_current_bpm_49 < 0, sensor_current_bpm_49 > 200),
#   Or(sensor_OUT_value_49 < 0, sensor_OUT_value_49 > 200),
#   Or(monitor_IN_value_49 < 0, monitor_IN_value_49 > 1),
#   Or(_SafetyController_0_buffered_status_49 < 0, _SafetyController_0_buffered_status_49 > 1),
#   Or(_SafetyController_0_has_data_49 < 0, _SafetyController_0_has_data_49 > 1),
#   Or(sensor_current_bpm_50 < 0, sensor_current_bpm_50 > 200),
#   Or(sensor_OUT_value_50 < 0, sensor_OUT_value_50 > 200),
#   Or(monitor_IN_value_50 < 0, monitor_IN_value_50 > 1),
#   Or(_SafetyController_0_buffered_status_50 < 0, _SafetyController_0_buffered_status_50 > 1),
#   Or(_SafetyController_0_has_data_50 < 0, _SafetyController_0_has_data_50 > 1),
#   Or(sensor_current_bpm_51 < 0, sensor_current_bpm_51 > 200),
#   Or(sensor_OUT_value_51 < 0, sensor_OUT_value_51 > 200),
#   Or(monitor_IN_value_51 < 0, monitor_IN_value_51 > 1),
#   Or(_SafetyController_0_buffered_status_51 < 0, _SafetyController_0_buffered_status_51 > 1),
#   Or(_SafetyController_0_has_data_51 < 0, _SafetyController_0_has_data_51 > 1),
#   Or(sensor_current_bpm_52 < 0, sensor_current_bpm_52 > 200),
#   Or(sensor_OUT_value_52 < 0, sensor_OUT_value_52 > 200),
#   Or(monitor_IN_value_52 < 0, monitor_IN_value_52 > 1),
#   Or(_SafetyController_0_buffered_status_52 < 0, _SafetyController_0_buffered_status_52 > 1),
#   Or(_SafetyController_0_has_data_52 < 0, _SafetyController_0_has_data_52 > 1),
#   Or(sensor_current_bpm_53 < 0, sensor_current_bpm_53 > 200),
#   Or(sensor_OUT_value_53 < 0, sensor_OUT_value_53 > 200),
#   Or(monitor_IN_value_53 < 0, monitor_IN_value_53 > 1),
#   Or(_SafetyController_0_buffered_status_53 < 0, _SafetyController_0_buffered_status_53 > 1),
#   Or(_SafetyController_0_has_data_53 < 0, _SafetyController_0_has_data_53 > 1),
#   Or(sensor_current_bpm_54 < 0, sensor_current_bpm_54 > 200),
#   Or(sensor_OUT_value_54 < 0, sensor_OUT_value_54 > 200),
#   Or(monitor_IN_value_54 < 0, monitor_IN_value_54 > 1),
#   Or(_SafetyController_0_buffered_status_54 < 0, _SafetyController_0_buffered_status_54 > 1),
#   Or(_SafetyController_0_has_data_54 < 0, _SafetyController_0_has_data_54 > 1),
#   Or(sensor_current_bpm_55 < 0, sensor_current_bpm_55 > 200),
#   Or(sensor_OUT_value_55 < 0, sensor_OUT_value_55 > 200),
#   Or(monitor_IN_value_55 < 0, monitor_IN_value_55 > 1),
#   Or(_SafetyController_0_buffered_status_55 < 0, _SafetyController_0_buffered_status_55 > 1),
#   Or(_SafetyController_0_has_data_55 < 0, _SafetyController_0_has_data_55 > 1),
#   Or(sensor_current_bpm_56 < 0, sensor_current_bpm_56 > 200),
#   Or(sensor_OUT_value_56 < 0, sensor_OUT_value_56 > 200),
#   Or(monitor_IN_value_56 < 0, monitor_IN_value_56 > 1),
#   Or(_SafetyController_0_buffered_status_56 < 0, _SafetyController_0_buffered_status_56 > 1),
#   Or(_SafetyController_0_has_data_56 < 0, _SafetyController_0_has_data_56 > 1),
#   Or(sensor_current_bpm_57 < 0, sensor_current_bpm_57 > 200),
#   Or(sensor_OUT_value_57 < 0, sensor_OUT_value_57 > 200),
#   Or(monitor_IN_value_57 < 0, monitor_IN_value_57 > 1),
#   Or(_SafetyController_0_buffered_status_57 < 0, _SafetyController_0_buffered_status_57 > 1),
#   Or(_SafetyController_0_has_data_57 < 0, _SafetyController_0_has_data_57 > 1),
#   Or(sensor_current_bpm_58 < 0, sensor_current_bpm_58 > 200),
#   Or(sensor_OUT_value_58 < 0, sensor_OUT_value_58 > 200),
#   Or(monitor_IN_value_58 < 0, monitor_IN_value_58 > 1),
#   Or(_SafetyController_0_buffered_status_58 < 0, _SafetyController_0_buffered_status_58 > 1),
#   Or(_SafetyController_0_has_data_58 < 0, _SafetyController_0_has_data_58 > 1),
#   Or(sensor_current_bpm_59 < 0, sensor_current_bpm_59 > 200),
#   Or(sensor_OUT_value_59 < 0, sensor_OUT_value_59 > 200),
#   Or(monitor_IN_value_59 < 0, monitor_IN_value_59 > 1),
#   Or(_SafetyController_0_buffered_status_59 < 0, _SafetyController_0_buffered_status_59 > 1),
#   Or(_SafetyController_0_has_data_59 < 0, _SafetyController_0_has_data_59 > 1),
#   Or(sensor_current_bpm_60 < 0, sensor_current_bpm_60 > 200),
#   Or(sensor_OUT_value_60 < 0, sensor_OUT_value_60 > 200),
#   Or(monitor_IN_value_60 < 0, monitor_IN_value_60 > 1),
#   Or(_SafetyController_0_buffered_status_60 < 0, _SafetyController_0_buffered_status_60 > 1),
#   Or(_SafetyController_0_has_data_60 < 0, _SafetyController_0_has_data_60 > 1),
#   Or(sensor_current_bpm_61 < 0, sensor_current_bpm_61 > 200),
#   Or(sensor_OUT_value_61 < 0, sensor_OUT_value_61 > 200),
#   Or(monitor_IN_value_61 < 0, monitor_IN_value_61 > 1),
#   Or(_SafetyController_0_buffered_status_61 < 0, _SafetyController_0_buffered_status_61 > 1),
#   Or(_SafetyController_0_has_data_61 < 0, _SafetyController_0_has_data_61 > 1),
#   Or(sensor_current_bpm_62 < 0, sensor_current_bpm_62 > 200),
#   Or(sensor_OUT_value_62 < 0, sensor_OUT_value_62 > 200),
#   Or(monitor_IN_value_62 < 0, monitor_IN_value_62 > 1),
#   Or(_SafetyController_0_buffered_status_62 < 0, _SafetyController_0_buffered_status_62 > 1),
#   Or(_SafetyController_0_has_data_62 < 0, _SafetyController_0_has_data_62 > 1),
#   Or(sensor_current_bpm_63 < 0, sensor_current_bpm_63 > 200),
#   Or(sensor_OUT_value_63 < 0, sensor_OUT_value_63 > 200),
#   Or(monitor_IN_value_63 < 0, monitor_IN_value_63 > 1),
#   Or(_SafetyController_0_buffered_status_63 < 0, _SafetyController_0_buffered_status_63 > 1),
#   Or(_SafetyController_0_has_data_63 < 0, _SafetyController_0_has_data_63 > 1),
#   Or(sensor_current_bpm_64 < 0, sensor_current_bpm_64 > 200),
#   Or(sensor_OUT_value_64 < 0, sensor_OUT_value_64 > 200),
#   Or(monitor_IN_value_64 < 0, monitor_IN_value_64 > 1),
#   Or(_SafetyController_0_buffered_status_64 < 0, _SafetyController_0_buffered_status_64 > 1),
#   Or(_SafetyController_0_has_data_64 < 0, _SafetyController_0_has_data_64 > 1),
#   Or(sensor_current_bpm_65 < 0, sensor_current_bpm_65 > 200),
#   Or(sensor_OUT_value_65 < 0, sensor_OUT_value_65 > 200),
#   Or(monitor_IN_value_65 < 0, monitor_IN_value_65 > 1),
#   Or(_SafetyController_0_buffered_status_65 < 0, _SafetyController_0_buffered_status_65 > 1),
#   Or(_SafetyController_0_has_data_65 < 0, _SafetyController_0_has_data_65 > 1),
#   Or(sensor_current_bpm_66 < 0, sensor_current_bpm_66 > 200),
#   Or(sensor_OUT_value_66 < 0, sensor_OUT_value_66 > 200),
#   Or(monitor_IN_value_66 < 0, monitor_IN_value_66 > 1),
#   Or(_SafetyController_0_buffered_status_66 < 0, _SafetyController_0_buffered_status_66 > 1),
#   Or(_SafetyController_0_has_data_66 < 0, _SafetyController_0_has_data_66 > 1),
#   Or(sensor_current_bpm_67 < 0, sensor_current_bpm_67 > 200),
#   Or(sensor_OUT_value_67 < 0, sensor_OUT_value_67 > 200),
#   Or(monitor_IN_value_67 < 0, monitor_IN_value_67 > 1),
#   Or(_SafetyController_0_buffered_status_67 < 0, _SafetyController_0_buffered_status_67 > 1),
#   Or(_SafetyController_0_has_data_67 < 0, _SafetyController_0_has_data_67 > 1),
#   Or(sensor_current_bpm_68 < 0, sensor_current_bpm_68 > 200),
#   Or(sensor_OUT_value_68 < 0, sensor_OUT_value_68 > 200),
#   Or(monitor_IN_value_68 < 0, monitor_IN_value_68 > 1),
#   Or(_SafetyController_0_buffered_status_68 < 0, _SafetyController_0_buffered_status_68 > 1),
#   Or(_SafetyController_0_has_data_68 < 0, _SafetyController_0_has_data_68 > 1),
#   Or(sensor_current_bpm_69 < 0, sensor_current_bpm_69 > 200),
#   Or(sensor_OUT_value_69 < 0, sensor_OUT_value_69 > 200),
#   Or(monitor_IN_value_69 < 0, monitor_IN_value_69 > 1),
#   Or(_SafetyController_0_buffered_status_69 < 0, _SafetyController_0_buffered_status_69 > 1),
#   Or(_SafetyController_0_has_data_69 < 0, _SafetyController_0_has_data_69 > 1),
#   Or(sensor_current_bpm_70 < 0, sensor_current_bpm_70 > 200),
#   Or(sensor_OUT_value_70 < 0, sensor_OUT_value_70 > 200),
#   Or(monitor_IN_value_70 < 0, monitor_IN_value_70 > 1),
#   Or(_SafetyController_0_buffered_status_70 < 0, _SafetyController_0_buffered_status_70 > 1),
#   Or(_SafetyController_0_has_data_70 < 0, _SafetyController_0_has_data_70 > 1),
#   Or(sensor_current_bpm_71 < 0, sensor_current_bpm_71 > 200),
#   Or(sensor_OUT_value_71 < 0, sensor_OUT_value_71 > 200),
#   Or(monitor_IN_value_71 < 0, monitor_IN_value_71 > 1),
#   Or(_SafetyController_0_buffered_status_71 < 0, _SafetyController_0_buffered_status_71 > 1),
#   Or(_SafetyController_0_has_data_71 < 0, _SafetyController_0_has_data_71 > 1),
#   Or(sensor_current_bpm_72 < 0, sensor_current_bpm_72 > 200),
#   Or(sensor_OUT_value_72 < 0, sensor_OUT_value_72 > 200),
#   Or(monitor_IN_value_72 < 0, monitor_IN_value_72 > 1),
#   Or(_SafetyController_0_buffered_status_72 < 0, _SafetyController_0_buffered_status_72 > 1),
#   Or(_SafetyController_0_has_data_72 < 0, _SafetyController_0_has_data_72 > 1),
#   Or(sensor_current_bpm_73 < 0, sensor_current_bpm_73 > 200),
#   Or(sensor_OUT_value_73 < 0, sensor_OUT_value_73 > 200),
#   Or(monitor_IN_value_73 < 0, monitor_IN_value_73 > 1),
#   Or(_SafetyController_0_buffered_status_73 < 0, _SafetyController_0_buffered_status_73 > 1),
#   Or(_SafetyController_0_has_data_73 < 0, _SafetyController_0_has_data_73 > 1),
#   Or(sensor_current_bpm_74 < 0, sensor_current_bpm_74 > 200),
#   Or(sensor_OUT_value_74 < 0, sensor_OUT_value_74 > 200),
#   Or(monitor_IN_value_74 < 0, monitor_IN_value_74 > 1),
#   Or(_SafetyController_0_buffered_status_74 < 0, _SafetyController_0_buffered_status_74 > 1),
#   Or(_SafetyController_0_has_data_74 < 0, _SafetyController_0_has_data_74 > 1),
#   Or(sensor_current_bpm_75 < 0, sensor_current_bpm_75 > 200),
#   Or(sensor_OUT_value_75 < 0, sensor_OUT_value_75 > 200),
#   Or(monitor_IN_value_75 < 0, monitor_IN_value_75 > 1),
#   Or(_SafetyController_0_buffered_status_75 < 0, _SafetyController_0_buffered_status_75 > 1),
#   Or(_SafetyController_0_has_data_75 < 0, _SafetyController_0_has_data_75 > 1),
#   Or(sensor_current_bpm_76 < 0, sensor_current_bpm_76 > 200),
#   Or(sensor_OUT_value_76 < 0, sensor_OUT_value_76 > 200),
#   Or(monitor_IN_value_76 < 0, monitor_IN_value_76 > 1),
#   Or(_SafetyController_0_buffered_status_76 < 0, _SafetyController_0_buffered_status_76 > 1),
#   Or(_SafetyController_0_has_data_76 < 0, _SafetyController_0_has_data_76 > 1),
#   Or(sensor_current_bpm_77 < 0, sensor_current_bpm_77 > 200),
#   Or(sensor_OUT_value_77 < 0, sensor_OUT_value_77 > 200),
#   Or(monitor_IN_value_77 < 0, monitor_IN_value_77 > 1),
#   Or(_SafetyController_0_buffered_status_77 < 0, _SafetyController_0_buffered_status_77 > 1),
#   Or(_SafetyController_0_has_data_77 < 0, _SafetyController_0_has_data_77 > 1),
#   Or(sensor_current_bpm_78 < 0, sensor_current_bpm_78 > 200),
#   Or(sensor_OUT_value_78 < 0, sensor_OUT_value_78 > 200),
#   Or(monitor_IN_value_78 < 0, monitor_IN_value_78 > 1),
#   Or(_SafetyController_0_buffered_status_78 < 0, _SafetyController_0_buffered_status_78 > 1),
#   Or(_SafetyController_0_has_data_78 < 0, _SafetyController_0_has_data_78 > 1),
#   Or(sensor_current_bpm_79 < 0, sensor_current_bpm_79 > 200),
#   Or(sensor_OUT_value_79 < 0, sensor_OUT_value_79 > 200),
#   Or(monitor_IN_value_79 < 0, monitor_IN_value_79 > 1),
#   Or(_SafetyController_0_buffered_status_79 < 0, _SafetyController_0_buffered_status_79 > 1),
#   Or(_SafetyController_0_has_data_79 < 0, _SafetyController_0_has_data_79 > 1),
#   Or(sensor_current_bpm_80 < 0, sensor_current_bpm_80 > 200),
#   Or(sensor_OUT_value_80 < 0, sensor_OUT_value_80 > 200),
#   Or(monitor_IN_value_80 < 0, monitor_IN_value_80 > 1),
#   Or(_SafetyController_0_buffered_status_80 < 0, _SafetyController_0_buffered_status_80 > 1),
#   Or(_SafetyController_0_has_data_80 < 0, _SafetyController_0_has_data_80 > 1),
#   Or(sensor_current_bpm_81 < 0, sensor_current_bpm_81 > 200),
#   Or(sensor_OUT_value_81 < 0, sensor_OUT_value_81 > 200),
#   Or(monitor_IN_value_81 < 0, monitor_IN_value_81 > 1),
#   Or(_SafetyController_0_buffered_status_81 < 0, _SafetyController_0_buffered_status_81 > 1),
#   Or(_SafetyController_0_has_data_81 < 0, _SafetyController_0_has_data_81 > 1),
#   Or(sensor_current_bpm_82 < 0, sensor_current_bpm_82 > 200),
#   Or(sensor_OUT_value_82 < 0, sensor_OUT_value_82 > 200),
#   Or(monitor_IN_value_82 < 0, monitor_IN_value_82 > 1),
#   Or(_SafetyController_0_buffered_status_82 < 0, _SafetyController_0_buffered_status_82 > 1),
#   Or(_SafetyController_0_has_data_82 < 0, _SafetyController_0_has_data_82 > 1),
#   Or(sensor_current_bpm_83 < 0, sensor_current_bpm_83 > 200),
#   Or(sensor_OUT_value_83 < 0, sensor_OUT_value_83 > 200),
#   Or(monitor_IN_value_83 < 0, monitor_IN_value_83 > 1),
#   Or(_SafetyController_0_buffered_status_83 < 0, _SafetyController_0_buffered_status_83 > 1),
#   Or(_SafetyController_0_has_data_83 < 0, _SafetyController_0_has_data_83 > 1),
#   Or(sensor_current_bpm_84 < 0, sensor_current_bpm_84 > 200),
#   Or(sensor_OUT_value_84 < 0, sensor_OUT_value_84 > 200),
#   Or(monitor_IN_value_84 < 0, monitor_IN_value_84 > 1),
#   Or(_SafetyController_0_buffered_status_84 < 0, _SafetyController_0_buffered_status_84 > 1),
#   Or(_SafetyController_0_has_data_84 < 0, _SafetyController_0_has_data_84 > 1),
#   Or(sensor_current_bpm_85 < 0, sensor_current_bpm_85 > 200),
#   Or(sensor_OUT_value_85 < 0, sensor_OUT_value_85 > 200),
#   Or(monitor_IN_value_85 < 0, monitor_IN_value_85 > 1),
#   Or(_SafetyController_0_buffered_status_85 < 0, _SafetyController_0_buffered_status_85 > 1),
#   Or(_SafetyController_0_has_data_85 < 0, _SafetyController_0_has_data_85 > 1),
#   Or(sensor_current_bpm_86 < 0, sensor_current_bpm_86 > 200),
#   Or(sensor_OUT_value_86 < 0, sensor_OUT_value_86 > 200),
#   Or(monitor_IN_value_86 < 0, monitor_IN_value_86 > 1),
#   Or(_SafetyController_0_buffered_status_86 < 0, _SafetyController_0_buffered_status_86 > 1),
#   Or(_SafetyController_0_has_data_86 < 0, _SafetyController_0_has_data_86 > 1),
#   Or(sensor_current_bpm_87 < 0, sensor_current_bpm_87 > 200),
#   Or(sensor_OUT_value_87 < 0, sensor_OUT_value_87 > 200),
#   Or(monitor_IN_value_87 < 0, monitor_IN_value_87 > 1),
#   Or(_SafetyController_0_buffered_status_87 < 0, _SafetyController_0_buffered_status_87 > 1),
#   Or(_SafetyController_0_has_data_87 < 0, _SafetyController_0_has_data_87 > 1),
#   Or(sensor_current_bpm_88 < 0, sensor_current_bpm_88 > 200),
#   Or(sensor_OUT_value_88 < 0, sensor_OUT_value_88 > 200),
#   Or(monitor_IN_value_88 < 0, monitor_IN_value_88 > 1),
#   Or(_SafetyController_0_buffered_status_88 < 0, _SafetyController_0_buffered_status_88 > 1),
#   Or(_SafetyController_0_has_data_88 < 0, _SafetyController_0_has_data_88 > 1),
#   Or(sensor_current_bpm_89 < 0, sensor_current_bpm_89 > 200),
#   Or(sensor_OUT_value_89 < 0, sensor_OUT_value_89 > 200),
#   Or(monitor_IN_value_89 < 0, monitor_IN_value_89 > 1),
#   Or(_SafetyController_0_buffered_status_89 < 0, _SafetyController_0_buffered_status_89 > 1),
#   Or(_SafetyController_0_has_data_89 < 0, _SafetyController_0_has_data_89 > 1),
#   Or(sensor_current_bpm_90 < 0, sensor_current_bpm_90 > 200),
#   Or(sensor_OUT_value_90 < 0, sensor_OUT_value_90 > 200),
#   Or(monitor_IN_value_90 < 0, monitor_IN_value_90 > 1),
#   Or(_SafetyController_0_buffered_status_90 < 0, _SafetyController_0_buffered_status_90 > 1),
#   Or(_SafetyController_0_has_data_90 < 0, _SafetyController_0_has_data_90 > 1),
#   Or(sensor_current_bpm_91 < 0, sensor_current_bpm_91 > 200),
#   Or(sensor_OUT_value_91 < 0, sensor_OUT_value_91 > 200),
#   Or(monitor_IN_value_91 < 0, monitor_IN_value_91 > 1),
#   Or(_SafetyController_0_buffered_status_91 < 0, _SafetyController_0_buffered_status_91 > 1),
#   Or(_SafetyController_0_has_data_91 < 0, _SafetyController_0_has_data_91 > 1),
#   Or(sensor_current_bpm_92 < 0, sensor_current_bpm_92 > 200),
#   Or(sensor_OUT_value_92 < 0, sensor_OUT_value_92 > 200),
#   Or(monitor_IN_value_92 < 0, monitor_IN_value_92 > 1),
#   Or(_SafetyController_0_buffered_status_92 < 0, _SafetyController_0_buffered_status_92 > 1),
#   Or(_SafetyController_0_has_data_92 < 0, _SafetyController_0_has_data_92 > 1),
#   Or(sensor_current_bpm_93 < 0, sensor_current_bpm_93 > 200),
#   Or(sensor_OUT_value_93 < 0, sensor_OUT_value_93 > 200),
#   Or(monitor_IN_value_93 < 0, monitor_IN_value_93 > 1),
#   Or(_SafetyController_0_buffered_status_93 < 0, _SafetyController_0_buffered_status_93 > 1),
#   Or(_SafetyController_0_has_data_93 < 0, _SafetyController_0_has_data_93 > 1),
#   Or(sensor_current_bpm_94 < 0, sensor_current_bpm_94 > 200),
#   Or(sensor_OUT_value_94 < 0, sensor_OUT_value_94 > 200),
#   Or(monitor_IN_value_94 < 0, monitor_IN_value_94 > 1),
#   Or(_SafetyController_0_buffered_status_94 < 0, _SafetyController_0_buffered_status_94 > 1),
#   Or(_SafetyController_0_has_data_94 < 0, _SafetyController_0_has_data_94 > 1),
#   Or(sensor_current_bpm_95 < 0, sensor_current_bpm_95 > 200),
#   Or(sensor_OUT_value_95 < 0, sensor_OUT_value_95 > 200),
#   Or(monitor_IN_value_95 < 0, monitor_IN_value_95 > 1),
#   Or(_SafetyController_0_buffered_status_95 < 0, _SafetyController_0_buffered_status_95 > 1),
#   Or(_SafetyController_0_has_data_95 < 0, _SafetyController_0_has_data_95 > 1),
#   Or(sensor_current_bpm_96 < 0, sensor_current_bpm_96 > 200),
#   Or(sensor_OUT_value_96 < 0, sensor_OUT_value_96 > 200),
#   Or(monitor_IN_value_96 < 0, monitor_IN_value_96 > 1),
#   Or(_SafetyController_0_buffered_status_96 < 0, _SafetyController_0_buffered_status_96 > 1),
#   Or(_SafetyController_0_has_data_96 < 0, _SafetyController_0_has_data_96 > 1),
#   Or(sensor_current_bpm_97 < 0, sensor_current_bpm_97 > 200),
#   Or(sensor_OUT_value_97 < 0, sensor_OUT_value_97 > 200),
#   Or(monitor_IN_value_97 < 0, monitor_IN_value_97 > 1),
#   Or(_SafetyController_0_buffered_status_97 < 0, _SafetyController_0_buffered_status_97 > 1),
#   Or(_SafetyController_0_has_data_97 < 0, _SafetyController_0_has_data_97 > 1),
#   Or(sensor_current_bpm_98 < 0, sensor_current_bpm_98 > 200),
#   Or(sensor_OUT_value_98 < 0, sensor_OUT_value_98 > 200),
#   Or(monitor_IN_value_98 < 0, monitor_IN_value_98 > 1),
#   Or(_SafetyController_0_buffered_status_98 < 0, _SafetyController_0_buffered_status_98 > 1),
#   Or(_SafetyController_0_has_data_98 < 0, _SafetyController_0_has_data_98 > 1),
#   Or(sensor_current_bpm_99 < 0, sensor_current_bpm_99 > 200),
#   Or(sensor_OUT_value_99 < 0, sensor_OUT_value_99 > 200),
#   Or(monitor_IN_value_99 < 0, monitor_IN_value_99 > 1),
#   Or(_SafetyController_0_buffered_status_99 < 0, _SafetyController_0_buffered_status_99 > 1),
#   Or(_SafetyController_0_has_data_99 < 0, _SafetyController_0_has_data_99 > 1),
#   Or(sensor_current_bpm_100 < 0, sensor_current_bpm_100 > 200),
#   Or(sensor_OUT_value_100 < 0, sensor_OUT_value_100 > 200),
#   Or(monitor_IN_value_100 < 0, monitor_IN_value_100 > 1),
#   Or(_SafetyController_0_buffered_status_100 < 0, _SafetyController_0_buffered_status_100 > 1),
#   Or(_SafetyController_0_has_data_100 < 0, _SafetyController_0_has_data_100 > 1)
# ))
print(s.check())
if s.check() == sat:
    m = s.model()
    print("counterexample model:")
    vars_to_print = [
        'sensor_current_bpm',
        'sensor_OUT_value',
        'sensor_OUT_reqRead',
        'sensor_OUT_reqWrite',
        'monitor_IN_value',
        'monitor_IN_reqRead',
        'monitor_IN_reqWrite',
        '_SafetyController_0_buffered_status',
        '_SafetyController_0_has_data',
    ]

    for i in range(101):
        print(f"Step {i}:")
        for base_name in vars_to_print:
            var_name = f"{base_name}_{i}"
            if var_name in globals():
                val = m.evaluate(globals()[var_name])
                print(f"  {base_name} : {val}")
        print("-" * 20)
