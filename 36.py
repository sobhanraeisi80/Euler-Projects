sum=0
for n in range(1,10**6):
    n_str=str(n)
    n_str_r=n_str[::-1]
    bin_n=bin(n)
    bin_n_str=str(bin_n)
    bin_n_str=bin_n_str[2::]
    bin_n_str_r=bin_n_str[::-1]
    if n_str==n_str_r and bin_n_str==bin_n_str_r:
        print(n)
        sum+=n
print(sum)
