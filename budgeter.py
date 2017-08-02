# -*- coding: utf-8 -*-
"""
Created on Wed Aug 02 13:47:18 2017

@author: dahoang
"""

import pandas as pd

initial_balance = 6500


income1 = pd.DataFrame()
income1['date'] = pd.date_range("2017-08-09", "2018-09-03", freq="14D")
income1['val'] = 2300
income1.ix[0, 'val'] += initial_balance

expense = pd.DataFrame()
expense['date'] = pd.date_range("2017-07-29", "2018-09-03", freq="MS")
expense['val'] = -2300/2.
expense.ix[expense['date'] == '2017-08-01', 'val'] = -1300.

#expense_amex = pd.DataFrame()
#expense['date'] = pd.date_range("2017-07-29", "2018-09-03", freq="MS")
expense['val'] = -3000
expense.ix[expense['date'] == '2017-08-01', 'val'] = -7450.
expense.ix[expense['date'] == '2017-01-01', 'val'] = -3350.

# access row of specific date
income1 = income1.append(expense, ignore_index=True)
income1 = income1.sort_values(by='date',axis=0)

import matplotlib.pyplot as plt
plt.figure()
plt.plot(income1['date'], income1['val'].cumsum(skipna=True))
plt.show()

