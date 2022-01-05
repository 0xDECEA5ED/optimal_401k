# Imports

# Globals
salary = 75000 #Dummy numbers from spreadsheet
current_balance = 20500
max_yearly_contribution = 20500
match_percent = 0.25
match_first = 0.06
test_rate = 0.06

def do_month(principal, contribution, rate):
    interest = principal*(1+rate/12)
    match = match_percent*contribution if contribution <= (salary/12*match_first) else salary/12*match_first*match_percent
    bal = principal + interest + contribution + match
    return bal

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

    for a1 in range(0,int(salary/12)):
        for a2 in range(0,int(salary/12)):
            for a3 in range(0,int(salary/12)):
                for a4 in range(0,int(salary/12)):
                    for a5 in range(0,int(salary/12)):
                        for a6 in range(0,int(salary/12)):
                            for a7 in range(0,int(salary/12)):
                                for a8 in range(0,int(salary/12)):
                                    for a9 in range(0,int(salary/12)):
                                        for a10 in range(0,int(salary/12)):
                                            for a11 in range(0,int(salary/12)):
                                                #print("status: ",a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11)
                                                for a12 in range(0,int(salary/12)):
                                                    
                                                    
                                                    c_sum = a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12
                                                    
                                                    if c_sum > max_yearly_contribution:
                                                        break

                                                    total = do_year(principal, rate, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12)

                                                    if total > max_val:
                                                        max_val = total
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
                                                        print("New max found:",total)
                                                
                                                else:
                                                    continue
                                                break
                                            else:
                                                continue
                                            break
                                        else:
                                            continue
                                        break
                                    else:
                                        continue
                                    break
                                else:
                                    continue
                                break
                            else:
                                continue
                            break
                        else:
                            continue
                        break
                    else:
                        continue
                    break
                else:
                    continue
                break
            else:
                continue
            break
        else:
            continue
        break

    print("Best jan:",best_jan)
    print("Best feb:",best_feb)
    print("Best mar:",best_mar)
    print("Best apr:",best_apr)
    print("Best may:",best_may)
    print("Best jun:",best_jun)
    print("Best jul:",best_jul)
    print("Best aug:",best_aug)
    print("Best sep:",best_sep)
    print("Best oct:",best_oct)
    print("Best nov:",best_nov)
    print("Best dec:",best_dec)
    print("Max total:",max_val)
