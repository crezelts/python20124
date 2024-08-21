nums=list(range(0,20,2))
nums[7]=60
# del nums[2]
nums.remove(10)
greeting=list("hellopython")
# for i in greeting:
#     print(greeting)
#     val=greeting.pop()
for i in range(5) :
    greeting.append("!")
    greeting.pop(0)
    print(greeting)