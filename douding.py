import sqlite3

class ElectricityManagementSystem:
    def __init__(self):
        self.conn = sqlite3.connect('electricity.db')
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS enterprises
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            address TEXT NOT NULL,
                            phone TEXT NOT NULL,
                            contact TEXT NOT NULL)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS electricity_prices
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            peak_price REAL NOT NULL,
                            valley_price REAL NOT NULL)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS electricity_usage
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            enterprise_id INTEGER NOT NULL,
                            peak_usage REAL NOT NULL,
                            valley_usage REAL NOT NULL,
                            month INTEGER NOT NULL,
                            year INTEGER NOT NULL,
                            total_usage REAL NOT NULL,
                            total_cost REAL NOT NULL,
                            FOREIGN KEY (enterprise_id) REFERENCES enterprises(id),
                            FOREIGN KEY (month) REFERENCES months(id),
                            FOREIGN KEY (year) REFERENCES years(id))''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS months
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS years
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            year INTEGER NOT NULL)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT NOT NULL,
                            password TEXT NOT NULL,
                            level INTEGER NOT NULL)''')
        self.cursor.execute('''INSERT INTO months (name) VALUES ('January')''')
        self.cursor.execute('''INSERT INTO months (name) VALUES ('February')''')
        self.cursor.execute('''INSERT INTO months (name) VALUES ('March')''')
        self.cursor.execute('''INSERT INTO months (name) VALUES ('April')''')
        self.cursor.execute('''INSERT INTO months (name) VALUES ('May')''')
        self.cursor.execute('''INSERT INTO months (name) VALUES ('June')''')
        self.cursor.execute('''INSERT INTO months (name) VALUES ('July')''')
        self.cursor.execute('''INSERT INTO months (name) VALUES ('August')''')
        self.cursor.execute('''INSERT INTO months (name) VALUES ('September')''')
        self.cursor.execute('''INSERT INTO months (name) VALUES ('October
        self.cursor.execute('''INSERT INTO months (name) VALUES ('November')''')
        self.cursor.execute('''INSERT INTO months (name) VALUES ('December')''')
        self.cursor.execute('''INSERT INTO years (year) VALUES (2020)''')
        self.cursor.execute('''INSERT INTO years (year) VALUES (2021)''')
        self.cursor.execute('''INSERT INTO electricity_prices (peak_price, valley_price) VALUES (0.5, 0.3)''')
    def add_enterprise(self, name, address, phone, contact):
        self.cursor.execute('''INSERT INTO enterprises (name, address, phone, contact) VALUES (?, ?, ?, ?)''', (name, address, phone, contact))
        self.conn.commit()
        print("Enterprise added successfully!")
    def add_electricity_usage(self, enterprise_id, peak_usage, valley_usage, month, year):
        total_usage = peak_usage + valley_usage
        self.cursor.execute('''SELECT peak_price, valley_price FROM electricity_prices WHERE id = 1''')
        prices = self.cursor.fetchone()
        total_cost = peak_usage * prices[0] + valley_usage * prices[1]
        self.cursor.execute('''INSERT INTO electricity_usage (enterprise_id, peak_usage, valley_usage, month, year, total_usage, total_cost) VALUES (?, ?, ?, ?, ?, ?, ?)''', (enterprise_id, peak_usage, valley_usage, month, year, total_usage, total_cost))
        self.conn.commit()
        print("Electricity usage added successfully!")
    def add_user(self, username, password, level):
        """
        添加用户
        :param username: 用户名
        :param password: 密码
        :param level: 用户等级
        """
        self.cursor.execute('''INSERT INTO users (username, password, level) VALUES (?, ?, ?)''', (username, password, level))
        self.conn.commit()
        print("User added successfully!")
def main():
    ems = ElectricityManagementSystem()
    while True:
        print("Welcome to Electricity Management System!")
        print("1. Add enterprise")
        print("2. Add electricity usage")
        print("3. Add user")
        print("4. Exit")
        choice = input("Please enter your choice: ")
        if choice == '1':
            name = input("Please enter enterprise name: ")
            address = input("Please enter enterprise address: ")
            phone = input("Please enter enterprise phone: ")
            contact = input("Please enter enterprise contact: ")
            ems.add_enterprise(name, address, phone, contact)
        elif choice == '2':
            enterprise_id = input("Please enter enterprise id: ")
            peak_usage = float(input("Please enter peak usage: "))
            valley_usage = float(input("Please enter valley usage: "))
            month = input("Please enter month (e.g. January): ")
            year = input("Please enter year (e.g. 2020): ")
            ems.add_electricity_usage(enterprise_id, peak_usage, valley_usage, month, year)
        elif choice == '3':
            username = input("Please enter username: ")
            password = input("Please enter password: ")
            level = input("Please enter level (1 for admin, 2 for user): ")
            ems.add_user(username, password, level)
        elif choice == '4':
            print("Thank you for using Electricity Management System!")
            break
        else:
            print("Invalid choice, please try again.")
# 创建一个ElectricityManagementSystem对象
ems = ElectricityManagementSystem()

# 进入主循环
while True:
    # 打印菜单
    print("Welcome to Electricity Management System!")
    print("1. Add enterprise")
    print("2. Add electricity usage")
    print("3. Add user")
    print("4. Exit")
    # 获取用户输入
    choice = input("Please enter your choice: ")
    # 根据用户输入执行相应的操作
    if choice == '1':
        # 获取企业信息
        name = input("Please enter enterprise name: ")
        address = input("Please enter enterprise address: ")
        phone = input("Please enter enterprise phone: ")
        contact = input("Please enter enterprise contact: ")
        # 添加企业
        ems.add_enterprise(name, address, phone, contact)
    elif choice == '2':
        # 获取用电信息
        enterprise_id = input("Please enter enterprise id: ")
        peak_usage = float(input("Please enter peak usage: "))
        valley_usage = float(input("Please enter valley usage: "))
        month = input("Please enter month (e.g. January): ")
        year = input("Please enter year (e.g. 2020): ")
        # 添加用电信息
        ems.add_electricity_usage(enterprise_id, peak_usage, valley_usage, month, year)
    elif choice == '3':
        # 获取用户信息
        username = input("Please enter username: ")
        password = input("Please enter password: ")
        level = input("Please enter level (1 for admin, 2 for user): ")
        # 添加用户
        ems.add_user(username, password, level)
    elif choice == '4':
        # 退出程序
        print("Thank you for using Electricity Management System!")
        break
    else:
        # 处理无效输入
        print("Invalid choice, please try again.")
    elif choice == '5':
        # 查询用电信息
        enterprise_id = input("Please enter enterprise id: ")
        month = input("Please enter month (e.g. January): ")
        year = input("Please enter year (e.g. 2020): ")
        self.cursor.execute('''SELECT enterprises.name, electricity_usage.month, electricity_usage.year, electricity_usage.peak_usage, electricity_usage.valley_usage, electricity_usage.total_usage, electricity_usage.total_cost FROM electricity_usage JOIN enterprises ON electricity_usage.enterprise_id = enterprises.id WHERE electricity_usage.enterprise_id = ? AND electricity_usage.month = ? AND electricity_usage.year = ?''', (enterprise_id, month, year))
        rows = self.cursor.fetchall()
        if len(rows) == 0:
            print("No data found.")
        else:
            print("Enterprise name: {}".format(rows[0][0]))
            print("Month: {}".format(rows[0][1]))
            print("Year: {}".format(rows[0][2]))
            print("Peak usage: {} kWh".format(rows[0][3]))
            print("Valley usage: {} kWh".format(rows[0][4]))
            print("Total usage: {} kWh".format(rows[0][5]))
            print("Total cost: {} RMB".format(rows[0][6]))


