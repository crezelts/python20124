with open("score.txt", 'r', encoding='utf-8') as f:
    while True:
        line = f.readline()
        """ 수행평가 """
        s = line.split("/")
        """ -------- """
        if len(s) == 3:
            count = len(s[1].split(","))
            total = 0
            """ 수행평가 """
            for score in s[2].split(","):
                total = total + int(score)
            """ -------- """
            avg = total / count
            print(f"{s[0]}: {count}과목 수강 평균 {avg}점")
        else:
            break