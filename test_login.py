import tkinter as tk

# import pyodbc
#
# # 连接到SQL Server数据库
# conn = pyodbc.connect('Driver={SQL Server};Server=LAPTOP-C3FR4UAR;Database=PhoneCount;Trusted_Connection=yes;')
#
# # 创建游标
# cursor = conn.cursor()
#
# # 创建用户信息表
# cursor.execute(
#     """
#     IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Users]') AND type in (N'U'))
#     CREATE TABLE Users (
#         UserID INT PRIMARY KEY,
#         Username VARCHAR(50)
#     )
#     """
# )
#
# # 创建收费信息表
# cursor.execute(
#     """
#     IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Charges]') AND type in (N'U'))
#     CREATE TABLE Charges (
#         ChargeID INT IDENTITY(1,1) PRIMARY KEY,
#         UserID INT,
#         Amount FLOAT,
#         FOREIGN KEY (UserID) REFERENCES Users(UserID)
#     )
#     """
# )

# 创建主窗口
root = tk.Tk()
root.title("电话计费管理系统")


# 登录界面
def login():
    username = entry_username.get()
    password = entry_password.get()
    print(username, type(username))
    print(password, type(password))
    if username == "123" and password == "123":
        login_label.config(text="登录 成功!")
        frame_main.pack()
    else:
        login_label.config(text="Invalid username or password")
    # 验证用户名和密码
    # 登录成功，显示后面的功能界面
    frame_login.pack_forget()  # 隐藏登录界面
    frame_main.pack()  # 显示主界面


# 创建登录界面
frame_login = tk.Frame(root)
frame_login.pack(padx=50, pady=100)

label_username = tk.Label(frame_login, text="用户名：")
label_username.pack()

entry_username = tk.Entry(frame_login)
entry_username.pack(pady=5)

label_password = tk.Label(frame_login, text="密码：")
label_password.pack()

entry_password = tk.Entry(frame_login, show="*")
entry_password.pack(pady=5)

btn_login = tk.Button(frame_login, text="登录", command=login)
btn_login.pack(pady=10)

login_label = tk.Label(root, text="")
login_label.pack()

# 创建主界面
frame_main = tk.Frame(root)

# 隐藏主界面
frame_main.pack_forget()

# 运行主循环
root.mainloop()

# # 提交事务
# conn.commit()
#
# # 关闭连接
# conn.close()
