
def text_validation(propmt):
    while True:
        user_input=input(propmt).strip().title()
        if not user_input:
            print("Can not return empty input")
            continue
        return user_input

def total_copies_validation(propmt):
    while True:
        try: 
            total_copies=int(input(propmt))
            if total_copies>0:
                return total_copies
            else:
                print("Invalid input. Please enter a positive number.")
                continue
        except (ValueError, TypeError):
            print("Please enter valid number")
            continue
