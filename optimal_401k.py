# Globals
SALARY = 78750       # Your yearly gross salary
CUR_BAL = 20500      # Approximate current value of your 401k, if any
YEARLY_MAX = 20500   # Maximum amount in dollars to contribute to 401k, before tax
MATCH_PERCENT = 0.25 # Percentage of each paycheck matched. By default this is configured for "Employer matches 25% of the first 6% contributed"
MATCH_FIRST = 0.06   # Maximum percentage of check to match
INTEREST_RATE = 0.06 # APY rate in decimal form
STEP = 0.25          # Accuracy of optimization in dollars. Lower values significantly decrease performance

def do_year(principal, rate, vals):
    for v in vals:
        interest = principal*(rate/12)
        match = MATCH_PERCENT*v if v <= (SALARY/12*MATCH_FIRST) else SALARY/12*MATCH_FIRST*MATCH_PERCENT
        principal = principal + interest + v + match
    return principal

l = list()
remaining = YEARLY_MAX
for month in range(0,12):
    val = int(SALARY/12) if remaining > int(SALARY/12) else remaining if remaining < int(SALARY/12) and remaining > 0 else 0
    remaining -= val
    l.insert(0,val)

max = do_year(CUR_BAL, INTEREST_RATE, l)
cont = True
while cont:
    for i in range(len(l)-1,0,-1):
        if l[i] > 0 and l[i-1] <= int(SALARY/12):
            cont = False
            l[i] = l[i] - STEP
            l[i-1] = l[i-1] + STEP
            x = do_year(CUR_BAL, INTEREST_RATE, l)
            if x > max:
                max = x
                cont = True
                break
            else:
                l[i] = l[i] + STEP
                l[i-1] = l[i-1] - STEP

print("Found best set:",max,l)
