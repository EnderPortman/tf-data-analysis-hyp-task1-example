import pandas as pd
import numpy as np
import statsmodels.api as sm


chat_id = 192196854 
def solution(x_success: int, # usually
             x_cnt: int, #usually
             y_success: int, #test
             y_cnt: int) -> bool: #test
    z, p = sm.stats.proportions_ztest([x_success, y_success], [x_cnt, y_cnt])
    return p <= 0.08
