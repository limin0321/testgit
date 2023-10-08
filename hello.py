import datetime

class DailyExpense:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, description, amount):
        today = datetime.date.today()
        if today not in self.expenses:
            self.expenses[today] = []
        
        self.expenses[today].append((description, amount))

    def view_expenses(self, date=None):
        if date:
            expenses_for_date = self.expenses.get(date, [])
        else:
            date = datetime.date.today()
            expenses_for_date = self.expenses.get(date, [])

        total = 0
        print(f"ค่าใช้จ่ายวันที่ {date.strftime('%d/%m/%Y')}:")
        for desc, amount in expenses_for_date:
            print(f"{desc}: {amount} บาท")
            total += amount

        print(f"รวม: {total} บาท")

def main():
    daily_expense = DailyExpense()

    while True:
        print("\nเมนู:")
        print("1. เพิ่มค่าใช้จ่าย")
        print("2. ดูค่าใช้จ่ายวันนี้")
        print("3. ดูค่าใช้จ่ายวันที่ต้องการ")
        print("4. ออกจากระบบ")
        
        choice = input("เลือกเมนู: ")

        if choice == '1':
            desc = input("รายละเอียดค่าใช้จ่าย: ")
            amount = float(input("จำนวนเงิน: "))
            daily_expense.add_expense(desc, amount)
        elif choice == '2':
            daily_expense.view_expenses()
        elif choice == '3':
            date_str = input("ใส่วันที่ (รูปแบบ DD/MM/YYYY): ")
            day, month, year = map(int, date_str.split('/'))
            date = datetime.date(year, month, day)
            daily_expense.view_expenses(date)
        elif choice == '4':
            break

if __name__ == "__main__":
    main()
