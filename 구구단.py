for i in range(2,10):  # 2~9까지 범위
    print(str(i)+'단:',end='') #i를 강제로 str형태로 바꿈  
    for j in range(1,10):
        print('%3d'%(i*j),end='')
    print()