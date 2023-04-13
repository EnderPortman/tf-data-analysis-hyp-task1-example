import pandas as pd
import numpy as np
from scipy.stats import norm 


chat_id = 192196854 
def solution(x_success: int, # usually
             x_cnt: int, #usually
             y_success: int, #test
             y_cnt: int) -> bool: #test
    p1 = x_success/x_cnt
    p2 = y_success/y_cnt
    p = (x_success + y_success)/(x_cnt + y_cnt)
    z = (p2 - p1)/((p * (1-p) * (1/x_cnt + 1/y_cnt))**0.5)
    p_val = norm.cdf(-abs(z)) * 2
    if p_val < 0.08:
      r = True
    else:
      r = False
    return r
