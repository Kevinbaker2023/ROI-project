class ROI():
    def __init__(self):
        self.income = 0
        self.expenses = 0
        self.cash_flow = 0
        self.income_dict = {}
        self.expenses_dict = {}
        self.total_investment_dict = {}

    def monthly_income(self):
        print('Please enter 0 or a number greater than 0')
        rental_income = float(input('Please enter the monthly rent: '))
        misc_income = float(input('Please enter any miscellaneous income: '))
        monthly_income = rental_income + misc_income
        self.income = monthly_income
        self.income_dict['Rental Income'] = rental_income
        self.income_dict['Miscellaneous Income'] = misc_income
        if self.income > 0:
            print(f'Your total monthly income is {self.income}')
            print(self.income_dict)
    
    def monthly_expenses(self):
        print('Please enter 0 or a number greater than 0')
        monthly_tax= float(input('Please enter monthly tax cost: '))
        monthly_insurance= float(input('Please enter monthly insurance cost: '))
        monthly_utilities= float(input('Please enter monthly utilities cost, if applicable: '))
        monthly_hoa= float(input('Please enter monthly HOA cost, if applicable: '))
        monthly_lawn_snow= float(input('Please enter monthly lawn and/or snow cost, if applicable: '))
        monthly_vacancy= float(input('Please enter how much you would like to save monthly in case of vacancy: '))
        monthly_small_repair= float(input('Please enter how much you would like to save monthly for minor repairs: '))
        monthly_large_repair= float(input('Please enter how much you would like to save monthly for major repairs: '))
        monthly_management= float(input('Please enter monthly property management cost: '))
        monthly_mortage= float(input('Please enter monthly mortgage cost: '))
        total_monthly_expenses = monthly_tax + monthly_insurance + monthly_utilities + monthly_hoa + monthly_lawn_snow + monthly_vacancy + monthly_small_repair + monthly_large_repair + monthly_management + monthly_mortage
        self.expenses = total_monthly_expenses
        self.expenses_dict['Monthly Tax'] = monthly_tax
        self.expenses_dict['Monthly Insurance'] = monthly_insurance
        self.expenses_dict['Monthly Utilities'] = monthly_utilities
        self.expenses_dict['Monthly HOA'] = monthly_hoa
        self.expenses_dict['Monthly Lawn or Snow Care'] = monthly_lawn_snow
        self.expenses_dict['Monthly Vacancy'] = monthly_vacancy
        self.expenses_dict['Monthly Small Repair'] = monthly_small_repair
        self.expenses_dict['Monthly Large Repair'] = monthly_large_repair
        self.expenses_dict['Monthly Manangement'] = monthly_management
        self.expenses_dict['Monthly Mortgage'] = monthly_mortage
        if self.expenses > 0:
            print(f'Your total monthly expenses are {self.expenses}')
            print(self.expenses_dict)
    
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
        self.total_investment_dict['Down Payment'] = down_payment
        self.total_investment_dict['Closing Costs'] = closing_costs
        self.total_investment_dict['Repair Budget'] = repair_budget
        self.total_investment_dict['Miscellaneous Budget'] = misc_budget
        total_investment = down_payment + closing_costs + repair_budget + misc_budget
        annual_cash_flow = self.cash_flow * 12
        cash_on_cash = (annual_cash_flow / total_investment) * 100
        print(f'Your cash on cash return on investment on this rental property is {cash_on_cash}%')
        print(self.total_investment_dict)
    
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
                if self.income == 0 or self.expenses == 0:
                    print('Need to complete income and expenses first')
                else:
                    self.monthly_cash_flow()
            elif response == 'return on investment':
                if self.cash_flow == 0:
                    print('Need to complete cash flow first')
                else:
                    self.return_on_investment()
            else:
                print('Response not recognized, please try again')
    
roi = ROI()
roi.runner()
# print(roi.Income())
# print(roi.Expenses())
# print(roi.Cash_flow())
# print(roi.Return_on_investment())