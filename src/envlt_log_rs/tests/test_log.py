from envlt_log import *

a = EnvLog(r"C:\dev\maya\Envlt\src\ns_Envlt\envlt_log\logs", "log")
# for i in range(100000):
#     a.write_log("error", "data")

r = EnvLog.list_log(r"C:\dev\maya\Envlt\src\ns_Envlt\envlt_log\logs")
print(r)
