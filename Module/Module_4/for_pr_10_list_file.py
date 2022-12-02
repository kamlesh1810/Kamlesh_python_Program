li=['1','2','3','4','Hello','world']
f=open('listInFile.txt','w')
for i in li:
    f.write(str([i]))
print('Done')        
f.close()




