#^ Tip Calculator

def calculate_tip(bill_amount, num_people, tip_percent):
    total_per_person = bill_amount / num_people
    total_with_tip = total_per_person * (1 + tip_percent / 100)
    return total_with_tip

print("TIP CALCULATOR")

while True:
    try:
        bill_amount = float(input("How much was the bill?"))
        num_people = int(input("How many people are splitting the bill?"))
        tip_percent = int(input("Do you want to tip 10, 15, or 20%?"))
        
        if tip_percent not in [10, 15, 20]:
            print("Invalid tip percentage. Please choose from 10, 15, or 20")
            continue
        
        total_with_tip = calculate_tip(bill_amount, num_people, tip_percent)
        print(f"Each person will need to pay: ${total_with_tip:.2f}")
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")