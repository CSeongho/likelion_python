# 1. 체중 관리 프로그램

weight, tall = input("몸무게(kg)와 키(cm) 입력: ").split()
weight = int(weight)
tall = float(tall) 

tall = tall / 100
BMI = weight / tall**2

if(20.0<=BMI<25.0):
    print("표준입니다")
else:
    print("체중관리가 필요합니다")