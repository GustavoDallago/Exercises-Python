glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]
glicose = []


for i in range(len(glicemia)):
    if glicemia[i] <= 70:
        glicose.append(( 'Hipoglicemia: ', glicemia[i]))
    elif 70 < glicemia[i] <= 99:
        glicose.append(( 'Normal: ', glicemia[i]))
    elif 100 <= glicemia[i] <= 125:
        glicose.append(( 'Alterada: ', glicemia[i]))
    else:
        glicose.append(( 'Diabetes: ', glicemia[i]))
        
print(glicose)