grade={'dohee':{'수학':76,'과학':89,'영어':93},
'juwon':{'수학':88,'과학':87,'영어':100},
'seohee':{'수학':86,'과학':93,'영어':82}       
       }
avg=[]
for i in grade.keys():
    man_avg=sum(grade[i].values())/len(grade[i].keys())
    print('{}평균은{}'.format(i,man_avg))
    avg.append(man_avg)
total_avg=sum(avg)/len(avg)
print('전체의 평균은 {}'.format(total_avg))    
