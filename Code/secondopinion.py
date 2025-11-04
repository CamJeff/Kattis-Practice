n = int(input())
hour = n // 3600
minutes = (n % 3600) // 60
seconds = (n % 3600) % 60
print(f"{hour} : {minutes} : {seconds}")