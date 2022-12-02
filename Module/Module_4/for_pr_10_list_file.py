li=['1','2','3','4','Hello','world']
f=open('file.txt','w')
# with open('file.txt') as f:
for i in li:
    f.write(str([i]))
print('Done')        
f.close()


# mobile=['samsung','redmi','oneplus']

# file=open('f1.txt','w')
# for items in mobile:
#     file.writelines([items])

# file.close()


