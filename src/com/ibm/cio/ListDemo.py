'''
Created on Jul 28, 2017

@author: zgsun
'''

if __name__ == '__main__':
    student=["Owen", "Nick","Jerry","Chinh","Rita"];
    print(student);
    
    print(student[1:3]);
    
    print(student[2]);
    
    for i in range(len(student)):
        print(student[i]);
        if student[i] == "Rita":
            student[i]="Jeff";
    
    print(student[-1]);
    
    print(student.index("Jerry"));
    
    print("Rita" in student);
    
    student.append("Bhavana");
    
    student.insert(1, "Deverre");
    
    student.remove("Chinh");
    
    #print(student);
    
    student.sort();
    
    print(student);

    student.reverse();
    
    print(student);
    
    
    