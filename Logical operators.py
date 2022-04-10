# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 11:48:23 2020

@author: Sah Meey
"""
#AND: both conditions should be true
#OR: Any condition should be true

has_high_income = True
has_good_credit = False
has_good_relationship = True
has_criminal_record = False

if has_high_income and has_good_credit:
    print("Eligible")
elif has_good_relationship or has_good_credit:
    print("Qualified")
if has_high_income and not has_criminal_record:
    print("Certified")
    
    