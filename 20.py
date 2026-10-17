nums=[int(x) for x in input("Numbers separated by spaces: ").split()]
print("Ascending:",sorted(nums,key=lambda x:x))
print("Descending:",sorted(nums,key=lambda x:x,reverse=True))
