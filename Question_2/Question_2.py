total_lines=''
while True:
    line=input()
    line_list=line.split('//')
    for i in range(len(line_list[0])):
        if (line_list[0])[i-1]=='-' and (line_list[0])[i]=='>':
            (line_list[0])[i-1]='.'
            del (line_list[0])[i]
        print(line_list[0],'//',line_list[1])
#print(total_lines)
#for i in range(len(total_lines)):
 #   if