fin_E = open('english_list.csv',"r",encoding='UTF-8')
fin_M = open('math_list.csv',"r",encoding='UTF-8')
lisE=[]
lisM=[]
name=[]
for line in fin_E.readlines():
    line = line.strip().split(",")
    lisE.append(line[1])
    name.append(line[0])
    
for line in fin_M.readlines():
    line = line.strip().split(",")
    lisM.append(line[1])
    
score=[]
fout = open("Score.csv","w")
line=''
for i in range(1,len(lisE)):
    score.append(int(lisE[i])+int(lisM[i]))
    list1 = [name[i],str(score[i-1]),"\n"]
    print(name[i],str(score[i-1]))
    
    line = ",".join(list1)
    fout.write(line)
fin_E.close()
fin_M.close()
fout.close()

line=''
fout = open("Score.csv","r")
for i in (len(name)):
    print()   
