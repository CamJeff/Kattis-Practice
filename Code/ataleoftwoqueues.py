n, m = input().split()
time_left = sum(map(int, input().split()))
time_right = sum(map(int, input().split()))

if time_left < time_right: 
    print("left") 
elif time_left > time_right:
    print("right")
else:
    print("either")