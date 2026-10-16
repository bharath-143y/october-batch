cpu_hours=int(input("enter number of cpu hours:"))
storage=int(input("enter storage in gb:))
data_transfer=int(input("enter data transfer in gb;"))
cpu_cost=storage*2  


uptime = 97.5
bill = 50000 if uptime >= 99.9: refund = 0
elif uptime >= 98: refund = bill * 0.10
else:
refund = bill * 0.25
print("Refund Amount:", refund)