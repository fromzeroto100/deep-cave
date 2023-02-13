import random, sys, time

width = 70
pause_amount = 0.05
print('Deep cave')
print('Press Ctrl-C')

leftWidth = 20
gapWidth = 10

while True:
    rightWidth = width - gapWidth - leftWidth
    print(('#' * leftWidth) + ('' * gapWidth) + ('#' * rightWidth))
    try:
        time.sleep(pause_amount)
        except KeyboardInterrupt:
            sys.exit()
    diceRoll = random.randint(1,6)
    if diceRoll == 1 and leftWidth > 1:
                
