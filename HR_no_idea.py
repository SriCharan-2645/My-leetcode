"""
There is an array of  integers. There are also  disjoint sets,  and , each containing  integers. You like all the integers in set  and dislike all the integers in set . Your initial happiness is . For each  integer in the array, if , you add  to your happiness. If , you add  to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since  and  are sets, they have no repeated elements. However, the array might contain duplicate elements.

Constraints



Input Format

The first line contains integers  and  separated by a space.
The second line contains  integers, the elements of the array.
The third and fourth lines contain  integers,  and , respectively.

Output Format

Output a single integer, your total happiness.

Sample Input

3 2
1 5 3
3 1
5 7
Sample Output

1
Explanation

You gain  unit of happiness for elements  and  in set . You lose  unit for  in set . The element  in set  does not exist in the array so it is not included in the calculation.

Hence, the total happiness is 2-1=1.
"""


# use input().split() as many times and in as order as given in the question.
n, m= input().split()
arr= list(input().split())
a= input().split()
b= input().split()
# print(n,m,arr,a,b)
# code was failing timeout error, bcoz of linear time taken to initialize the dictionary. In question it is mentioned as sets. so we just take in sets. their look up time is O(1)
a = set(a)
b = set(b)
# list takes more time to read large data, lets convert to dict.  so it will take O(n) time initiallly , but for look ups it will just take O(1)
# dicA, dicB = {}, {}
# for i in a:
#     dicA[i] = dicA.get(i, 0)+1
# for i in b:
#     dicB[i] = dicB.get(i, 0)+1
# print(dicA,dicB)

res = 0
for i in arr:
    if i in a:
        res += 1
    elif i in b:
        res -= 1
print(res)