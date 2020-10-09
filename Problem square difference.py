sum_sqr=0
sqr_sum=0
i=1
while(i!=101):
    sum_sqr=sum_sqr+i*i
    sqr_sum=sqr_sum+i
    i=i+1
sqr_sum=sqr_sum*sqr_sum
print(sqr_sum-sum_sqr)

