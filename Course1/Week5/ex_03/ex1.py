xh = int(input ("Enter Hours:"))
xr = float(input ("Enter Rate:"))
if(xh <= 40):
   xp = xh * xr
else:
   xp =( 40 * xr )+ (xh - 40) * (xr * 1.5) 

print("Pay:", xp)