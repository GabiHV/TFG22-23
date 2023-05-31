# Variables globales
INPUT_COLS_PROCESSING = ["t_ext", "h_ext", "t_C_cal","h_C_cal","t_L_cal","h_L_cal"]
INPUT_COLS = ["t_ext", "h_ext", "t_C_cal","h_C_cal","t_L_cal","h_L_cal", 'sensor']

MIN_MAX_COLS_VALUES = {"t_ext": (-50, 50), "h_ext": (0, 100), "t_C_cal": (-50, 50), 
                       "t_L_cal": (-50, 50), "h_C_cal": (0, 100), "h_L_cal": (0, 100),
                       'sensor': (0, 7)}