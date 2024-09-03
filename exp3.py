#Req1:Create Ductionary
emp={'ename':['anu','pavan','satya','lakshmi','pathu'],'age':[21,22,23,24,25],'salary':[15000,18000,26000,30000,10000]}
print("The employee dataset is:",emp)
print("The employee salaries are:")
for i in emp['salary']:
    print(i)
L1=emp['salary']
print("The listed salaries:",L1)
print("The sorted salaries:",sorted(L1))
print("The reversed salaries:",L1[::-1])
print("The minimum salary is:",min(L1))
print("The maximum salary is:",max(L1))
print("The sum salary is:",sum(L1))

#req2:we will work in this file
