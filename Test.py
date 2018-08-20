import os
import matplotlib.pyplot as plt
import numpy as np


def main():
    A = input()
    B = input()

    A = list(A)
    B = list(B)
    numModifications = 0

    if len(A) < len(B):
        # Add to A
        for index, value in enumerate(B):
            if A[index] != B[index]:
                A.insert(index, value)
                numModifications += 1
            else:
                continue
    elif len(B) < len(A):
        for index, value in enumerate(B):
            if A[index] != B[index]:
                del A[index]
                numModifications += 1
            else:
                continue
    else:
        for index, value in enumerate(B):
            if A[index] == B[index+1] and :
                A[index] = B[index]
                numModifications += 1
            else:
                continue

    print(numModifications)

main()
# sss = TestMethod()

da = ["2018-06-28 11:22:40.321435",
"2018-06-28 11:22:40.322435",
"2018-06-28 09:55:16.214626",
"2018-07-03 14:29:54.195836",
"2018-07-03 15:44:34.610836",
"2018-07-04 10:43:23.818683",
"2018-07-05 10:23:07.336495",
"2018-07-06 14:56:34.123351",
"2018-07-11 13:38:52.024196",
"2018-07-13 13:14:47.038425",
"2018-07-13 13:30:00.909425",
"2018-07-13 13:43:23.513425",
"2018-07-13 13:56:12.396117",
"2018-07-16 08:47:20.126499",
"2018-07-10 08:35:43.701291"]

vol=[0.15,
0.15,
0.15,
0.15,
0.15,
0.15,
0.15,
0.15,
0.15,
0.15,
0.15,
0.15,
0.15,
0.15,
0.15
]

plt.plot(da,vol,'g*')
plt.show()

N = 5
menMeans = (20, 35, 30, 35, 27)
womenMeans = (25, 32, 34, 20, 25)
menStd = (2, 3, 4, 1, 2)
womenStd = (3, 5, 2, 3, 3)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, menMeans, width, yerr=menStd)
p2 = plt.bar(ind, womenMeans, width,
             bottom=menMeans, yerr=womenStd)

# plt.ylabel('Scores')
# plt.title('Scores by group and gender')
# plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
# plt.yticks(np.arange(0, 81, 10))
# plt.legend((p1[0], p2[0]), ('Men', 'Women'))

plt.show()

plt.plot([1,2,3,4], [2,4,6,8])
plt.show()

print("Hello world")

folderPath = R"F:"
print(folderPath)

if folderPath:
    print(F"folderPath has some value")

test_list = ["bala", "test", "sample"]

print(test_list[2])

lisDirec = os.listdir(folderPath)

print(lisDirec)

for f in lisDirec:
    if f == "Downloads":
        print(F"Found {f}")
        break

name_dict = \
    {
        "name" : "test",
        "ID" : 12345,
        "sex" : "M"
    }

try:
    some_thing = name_dict["ID"]
    print(F"ID is {0}", name_dict["ID"])
    print(name_dict["some"])
except KeyError as error:
    print("Specified key is not present")


