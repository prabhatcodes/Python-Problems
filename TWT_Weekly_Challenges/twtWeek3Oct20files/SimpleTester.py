def test_sol():
    cases= # copy the dictionary from https://hastebin.com/uyekakular.yaml here
    correct=0
    incorrect=0
    for i in cases:
        if solution(i)==cases[i]:
            correct=correct+1
            # print("Case=",i,"Expected=",cases[i], "Returned", solution(i))
        else:
            incorrect=incorrect+1
            # print("Case=",i,"Expected=",cases[i], "Returned", solution(i))
    print
    print("Correct percentage:", (correct/len(cases))*100)
