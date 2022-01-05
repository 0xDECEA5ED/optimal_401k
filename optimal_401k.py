# Imports
import functools

# Globals
salary = 78750 #Dummy numbers from spreadsheet
current_balance = 20500
max_yearly_contribution = 20500
match_percent = 0.25
match_first = 0.06
test_rate = 0.06

@functools.cache
def do_month(principal, contribution, rate):
    interest = principal*(rate/12)
    match = match_percent*contribution if contribution <= (salary/12*match_first) else salary/12*match_first*match_percent
    bal = principal + interest + contribution + match
    return bal

@functools.cache
def do_year(principal, rate, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12):
    jan = do_month(principal, a1, rate)
    feb = do_month(jan, a2, rate)
    mar = do_month(feb, a3, rate)
    apr = do_month(mar, a4, rate)
    may = do_month(apr, a5, rate)
    jun = do_month(may, a6, rate)
    jul = do_month(jun, a7, rate)
    aug = do_month(jul, a8, rate)
    sep = do_month(aug, a9, rate)
    oct = do_month(sep, a10, rate)
    nov = do_month(oct, a11, rate)
    dec = do_month(nov, a12, rate)
    return dec

def maximize(principal, rate):

    best_jan = 0
    best_feb = 0
    best_mar = 0
    best_apr = 0
    best_may = 0
    best_jun = 0
    best_jul = 0
    best_aug = 0
    best_sep = 0
    best_oct = 0
    best_nov = 0
    best_dec = 0

    max_val = 0

    for a1 in range(0,int(salary/12),11):
        if (a1) > max_yearly_contribution:
            break
        jan = do_month(principal, a1, rate)
        for a2 in range(0,int(salary/12)),11:
            if (a1+a2) > max_yearly_contribution:
                break
            feb = do_month(jan, a2, rate)
            for a3 in range(0,int(salary/12),11):
                if (a1+a2+a3) > max_yearly_contribution:
                    break
                mar = do_month(feb, a3, rate)
                for a4 in range(0,int(salary/12),11):
                    if (a1+a2+a3+a4) > max_yearly_contribution:
                        break
                    apr = do_month(mar, a4, rate)
                    for a5 in range(0,int(salary/12),101):
                        if (a1+a2+a3+a4+a5) > max_yearly_contribution:
                            break
                        may = do_month(apr, a5, rate)
                        for a6 in range(0,int(salary/12),11):
                            if (a1+a2+a3+a4+a5+a6) > max_yearly_contribution:
                                break
                            jun = do_month(may, a6, rate)
                            for a7 in range(0,int(salary/12),11):
                                if (a1+a2+a3+a4+a5+a6+a7) > max_yearly_contribution:
                                    break
                                jul = do_month(jun, a7, rate)
                                for a8 in range(0,int(salary/12),11):
                                    if (a1+a2+a3+a4+a5+a6+a7+a8) > max_yearly_contribution:
                                        break
                                    aug = do_month(jul, a8, rate)
                                    for a9 in range(0,int(salary/12),11):
                                        if (a1+a2+a3+a4+a5+a6+a7+a8+a9) > max_yearly_contribution:
                                            break
                                        sep = do_month(aug, a9, rate)
                                        for a10 in range(0,int(salary/12),11):
                                            if (a1+a2+a3+a4+a5+a6+a7+a8+a9+a10) > max_yearly_contribution:
                                                break
                                            oct = do_month(sep, a10, rate)
                                            for a11 in range(0,int(salary/12),11):
                                                if (a1+a2+a3+a4+a5+a6+a7+a8+a9+a10+a11) > max_yearly_contribution:
                                                    break
                                                nov = do_month(oct, a11, rate)
                                                for a12 in range(0,int(salary/12),11):
                                                    if (a1+a2+a3+a4+a5+a6+a7+a8+a9+a10+a11+a12) > max_yearly_contribution:
                                                        break
                                                    dec = do_month(nov, a12, rate)
                                                    if dec > max_val:
                                                        max_val = dec
                                                        best_jan = a1
                                                        best_feb = a2
                                                        best_mar = a3
                                                        best_apr = a4
                                                        best_may = a5
                                                        best_jun = a6
                                                        best_jul = a7
                                                        best_aug = a8
                                                        best_sep = a9
                                                        best_oct = a10
                                                        best_nov = a11
                                                        best_dec = a12
                                                        print("New max found:",max_val,"Bests:",best_jan,best_feb,best_mar,best_apr,best_may,best_jun,best_jul,best_aug,best_sep,best_oct,best_nov,best_dec)

    print("Best jan:",best_jan) #expected ~4337.5
    print("Best feb:",best_feb) #expected ~4337.5
    print("Best mar:",best_mar) #expected ~4337.5
    print("Best apr:",best_apr) #expected ~4337.5
    print("Best may:",best_may) #expected ~393.75
    print("Best jun:",best_jun) #expected ~393.75
    print("Best jul:",best_jul) #expected ~393.75
    print("Best aug:",best_aug) #expected ~393.75
    print("Best sep:",best_sep) #expected ~393.75
    print("Best oct:",best_oct) #expected ~393.75
    print("Best nov:",best_nov) #expected ~393.75
    print("Best dec:",best_dec) #expected ~393.75
    print("Max total:",max_val) #expected ~44376.5

maximize(current_balance,test_rate)
