def confusion_matrix(y_test:list , y_pred:list):
    if len(y_test) != len(y_pred):
        print("Array Size Mismatch")
        return None

    cf = [[0 , 0] , [0 , 0]]
    n = len(y_pred)
    for i in range(n):

        if y_test[i] == y_pred[i]:
            if y_test[i] == 0 :
                cf[1][1] += 1
            else:
                cf[0][0] += 1
        else:
            if y_test[i] == 0:
                cf[1][0] += 1
            else :
                cf[0][1] += 1

    return cf


def recall(y_pred,y_test):
    cf = confusion_matrix(y_pred,y_test)
    recall = (cf[0][0])/(cf[0][0]+cf[1][0])
    return recall

if __name__ == '__main__':
    print("Example : ")
    y_test = [0 , 0, 0 ,1 , 1 , 1]
    y_pred = [1 , 0, 1 , 1 , 1 ,1 ]
    print(f"y_test : {y_test} \ny_pref : {y_pred}")
    recall = recall(y_test,y_pred)
    print(f"Recall : {recall :.4f}")



