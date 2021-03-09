import math
import argparse


parser = argparse.ArgumentParser(description="")
parser.add_argument("--type", choices=["annuity", "diff"], help="")
parser.add_argument("--payment", type=float,  help="")
parser.add_argument("--principal", type=float,  help="")
parser.add_argument("--periods", type=int, help="")
parser.add_argument("--interest", type=float, help="")
args = parser.parse_args()
i = args.interest
p = args.principal
n = args.periods
pay = args.payment
if args.type == "diff":
    if args.payment is not None:
        print("Incorrect parameters")
        exit()
    else:
        total = 0
        i = args.interest / (12 * 100)
        for m in range(1, n+1):
            d = math.ceil(p/n + i *(p - (p * (m -1))/n))
            print("Month" + str(m) + ": payment is " + str(d))
            total += d
        over_payment = int(abs(p - total))
        print("Overpayment = " + str(over_payment))
elif args.type == "annuity":
    if args.__sizeof__() == 6:
        print("Incorrect parameters")
        exit()
    elif i is None:
        print("These parameters are incorrect because --interest is missing")
        exit()
    elif p is None:
        i = args.interest / (12 * 100)
        loan_principal = pay / ((i * math.pow((1 + i), n)) / (math.pow((1 + i), n) -1))
        print("Your loan principal = " + str(loan_principal))
    elif pay is None:
        i = args.interest / (12 * 100)
        annuity_payment = math.ceil(p * ((i * math.pow((1 + i), n)) / (math.pow((1 + i), n) -1)))
        print("Your annuity payment = " + str(annuity_payment))
        over = int(abs(p - (annuity_payment * n)))
        print("Overpayment = " + str(over))
    elif n is None:
        i = args.interest / (12 * 100)
        num_periods = math.ceil(math.log((pay / (pay - i * p)), (1 + i)))
        if num_periods < 12:
            print("It will take " + str(int(num_periods)) + " months to repay this loan!")
            over = int(abs(p - (pay * num_periods)))
            print("Overpayment = " + str(over))
        if num_periods > 12:
            if num_periods % 12 != 0:
                years = int(num_periods / 12)
                months = math.ceil(num_periods) % 12
                print("It will take " + str(years) + " years " + str(months) + " months to repay this loan!")
                over = int(abs(p - (pay * num_periods)))
                print("Overpayment = " + str(over))
            else:
                years = int(num_periods / 12)
                print("It will take " + str(years) + " years to repay this loan!")
                over = int(abs(p - (pay * num_periods)))
                print("Overpayment = " + str(over))
        else:
            print("It will take 1 year to repay this loan!")
            over = int(abs(p - (pay * num_periods)))
            print("Overpayment = " + str(over))

