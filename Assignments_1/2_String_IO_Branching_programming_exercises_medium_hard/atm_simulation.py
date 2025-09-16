'''
7. ATM Simulation
Description: Simulate ATM cash withdrawal with available denominations (2000, 500, 100).
Example Input:
Enter withdrawal amount: 3700
Balance: 5000
Expected Output:
Dispensed: 1x2000, 3x500, 2x100
'''

def amt_simulation(amt,balance):
    if amt>balance:
        print("You dont have sufficient balance")
    else:
        two_thousand_note=amt//2000
        amt=amt-(two_thousand_note*2000)
        five_hundard_note= amt//500
        amt=amt-(five_hundard_note*500)
        hundard_note=amt//100
        print(f"Dispensed: {two_thousand_note}x2000, {five_hundard_note}x500, {hundard_note}x100")

def main():
    amt=int(input("Enter withdrawal amount:"))
    balance=int(input("Balance:"))
    amt_simulation(amt,balance)

if __name__ == '__main__':
    main()