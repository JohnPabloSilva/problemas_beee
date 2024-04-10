tot_seg = int(input())
hours = tot_seg //  3600
minutes = (tot_seg % 3600) // 60
segs = (tot_seg % 60)

print('{}:{}:{}'.format(hours, minutes, segs))