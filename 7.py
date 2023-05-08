def fibo(ix, nums):
    if(ix == 1 or ix == 2):
        nums.append(1)
        print(1)
        return fibo(ix+1, nums)

    if(ix > 10):
        return
    
    print(nums[ix-2] + nums[ix-3])
    nums.append(nums[ix-2] + nums[ix-3])
    fibo(ix+1, nums)


nums = []

fibo(1, nums)

l, r = input("Enter two numbers: (1-10)").split(" ")
l = int(l)
r = int(r)

if(l<1 or l>10 or r<1 or r>10 or l>r):
    print("Invalid Range!")
    exit

sum = 0
for i in range(l-1,r):
    sum += nums[i]

print("The sum is: " + str(sum))


