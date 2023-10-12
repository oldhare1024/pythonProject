class Server:
    def __init__(self, cpu_num, memory_size, disk_space, system_type):
        self.cpu_num = cpu_num
        self.memory_size = memory_size
        self.disk_space = disk_space
        self.__system_type = system_type

    def get_server_info(self):
        print(f"{self.cpu_num}核cpu，{self.memory_size}G内存，{self.disk_space}G磁盘空间，{self.__system_type}。")


server = Server(8, 40, 150, "Linux")
server.get_server_info()
