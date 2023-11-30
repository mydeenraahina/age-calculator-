from datetime import  date
import sys
class AgeCalculator:
    @classmethod
    def Calculate_current_age(cls):
        try:
            getting_dt=input(f"Enter your DOB ro calculate your age[YYYY-MM-DD]: ")
            dt=date.fromisoformat(getting_dt)
            current_date=date.today()
            resultant_age=current_date.year-dt.year
            print(f"your current age is :{resultant_age}")
        except (ValueError,TypeError) as e1:
            print(e1)
            
    @classmethod
    def Calculate_age_difference(cls):
        try:
            getting_person1_name=input("Enter first person name:")
            getting_person1_DOB=input("Enter first person DOB[YYYY-MM-DD]:")
            DOB_1=date.fromisoformat(getting_person1_DOB)
            getting_person2_name=input("Enter second person name:")
            DOB_2=date.fromisoformat(getting_person2_DOB)
            age_difference=abs(DOB_1.year-DOB_2.year)
            print(f"Age difference between {getting_person1_name} and { getting_person2_name} is {age_difference} years")     
        except (ValueError,TypeError) as e1:
            print(e1)
class Main(AgeCalculator):
    @staticmethod
    def continue_or_exit_block():
        while True:
            getting_input_tocontinue=input(f"Do you want to continue in this Age Calculator..[yes\no]!").casefold()
            if getting_input_tocontinue=="yes":
                Main.menu_block()
                break
            elif getting_input_tocontinue=="no":
                print("Age Calculator going to exit!")
                sys.exit()
            else:
                print("Enter a avalid input..")
    @staticmethod
    def menu_block():
        print(f"Age Calculator!...")
        print("Option available for you are..")
        print(f"1.Calculate your current_age")
        print(f"2.Calculate age difference between two persons")
        while True:
            getting_input=input("Enter your choice from the above option")
            if getting_input=="1":
                Main.Calculate_current_age()
                break

            elif getting_input=="2":
                Main.Calculate_age_difference()
                break
            else:
                print("enter a valid input")
        Main.continue_or_exit_block()
                
                
Main.menu_block()
        
