from tkinter import messagebox

def coin_increase(coins_earned):
        
    f1 = open ("coins.txt", "r+")
    
    coins_read=(f1.read())

    if coins_read == '':
        f1.write(str(coins_earned))
        messagebox.showinfo("Coins:","Coins:"+str(coins_earned))
        return coins_earned
    else:
        coins_read = int(coins_read)
        f1.seek(0)
        f1.truncate()
    

        new_coins = coins_read+coins_earned
        f1.write(str(new_coins))

        messagebox.showinfo("Coins:","Coins:"+str(new_coins))

        f1.close()

        return new_coins    

def coin_decrease(coins_spent):
    f1 = open ("coins.txt", "r+")
    coins_read = f1.read()
    if coins_read!='':
        coins_read=int(coins_read)
    else:
        coins_read = 0
    
    f1.seek(0)
    f1.truncate()
    
    if coins_read>=100:
        new_coins = coins_read-coins_spent
        f1.write(str(new_coins))

        f1.close()
        return True
    else:
        messagebox.showinfo("Insufficient coins","You do not have enough coins! :( \nComplete some tasks to play again!")
        return False 
    



