# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 11:43:49 2020

@author: Sah Meey
"""

price = 1000000
has_good_credit = True
if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")