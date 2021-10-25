# with open('D:\Projects\CourseProjects\Automata\Scripts\smaple_.txt', 'r') as f:
#     res = f.readline()
#     print(res)

# f = open("Scripts\smaple_.txt", "r")
# print(f.readline())
# f.close()
import pandas as pd
res = pd.read_csv('Scripts\smaple.csv', delim_whitespace=True)
print(res)