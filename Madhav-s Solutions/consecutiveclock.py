print('?')
start_time = input().split(':')
start_time = ''.join(start_time)
start_time.zfill(4)

end_time = input().split(':')
end_time = ''.join(end_time)

if end_time == '0000':
    end_time = '2400'
end_time.zfill(4)

start_minutes = 60*int(start_time[:2]) + int(start_time[2:])
start_time.zfill(4)
end_minutes = 60*int(end_time[:2]) + int(end_time[2:])
end_time.zfill(4)

consecutive = 0

for i in range((end_minutes - start_minutes) + 1):
    num = int(start_time) + i
    num = str(num).zfill(4)
    for i in range(len(start_time) - 1):
        if int(num[i+1]) == (int(num[i]) + 1):
            consecutive += 1

print(consecutive)
