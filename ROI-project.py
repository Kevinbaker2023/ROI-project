class ROI():
    def __init__(self):
        self.income = 0
        self.expenses = 0
        self.cash_flow = 0

    def monthly_income(self):
        print('Please enter 0 or a number greater than 0')
        rental_income = float(input('Please enter the monthly rent: '))
        misc_income = float(input('Please enter any miscellaneous income: '))
        monthly_income = rental_income + misc_income
        self.income = monthly_income
        if self.income > 0:
            print(f'Your total monthly income is {self.income}')
    
    def monthly_expenses(self):
        print('Please enter 0 or a number greater than 0')
        total_monthly_expenses = 0
        total_monthly_expenses += float(input('Please enter monthly tax cost: '))
        total_monthly_expenses += float(input('Please enter monthly insurance cost: '))
        total_monthly_expenses += float(input('Please enter monthly utilities cost, if applicable: '))
        total_monthly_expenses += float(input('Please enter monthly HOA cost, if applicable: '))
        total_monthly_expenses += float(input('Please enter monthly lawn and/or snow cost, if applicable: '))
        total_monthly_expenses += float(input('Please enter how much you would like to save monthly in case of vacancy: '))
        total_monthly_expenses += float(input('Please enter how much you would like to save monthly for minor repairs: '))
        total_monthly_expenses += float(input('Please enter how much you would like to save monthly for major repairs: '))
        total_monthly_expenses += float(input('Please enter monthly property management cost: '))
        total_monthly_expenses += float(input('Please enter monthly mortgage cost: '))
        self.expenses = total_monthly_expenses
        if self.expenses > 0:
            print(f'Your total monthly expenses are {self.expenses}')
    
    def monthly_cash_flow(self):
        total_cash_flow = self.income - self.expenses
        self.cash_flow = total_cash_flow
        print(f'Your total monthly cash flow is {self.cash_flow}')
    
    def return_on_investment(self):
        print('Please enter 0 or a number greater than 0')
        down_payment = float(input('Please enter your down payment: '))
        closing_costs = float(input('Please enter your closing costs: '))
        repair_budget = float(input('Please enter your repair budget: '))
        misc_budget = float(input('Please enter your miscellaneous budget, if applicable: '))
        total_investment = down_payment + closing_costs + repair_budget + misc_budget
        annual_cash_flow = self.cash_flow * 12
        cash_on_cash = (annual_cash_flow / total_investment) * 100
        print(f'Your cash on cash return on investment on this rental property is {cash_on_cash}%')
    
    def runner(self):
        print('Enter quit to exit')
        
        while True:
            response = input('Would you like to enter income, expenses, cash flow or return on investment?: ').lower()

            if response == 'quit':
                break
            elif response == 'income':
                self.monthly_income()
            elif response == 'expenses':
                self.monthly_expenses()
            elif response == 'cash flow':
                self.monthly_cash_flow()
            elif response == 'return on investment':
                self.return_on_investment()
            else:
                print('Response not recognized, please try again')
    
roi = ROI()
# print(roi.Income())
# print(roi.Expenses())
# print(roi.Cash_flow())
# print(roi.Return_on_investment())
roi.runner()