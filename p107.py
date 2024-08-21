import random
def rolling_dice(pip,repeat):
    for r in range(1,repeat+1):
        n=random.randint(1,pip)
        print("결과",n)

rolling_dice(6,5)