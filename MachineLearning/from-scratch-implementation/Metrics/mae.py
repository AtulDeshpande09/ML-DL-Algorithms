# Mean Absolute Error

def mean_absolute_error(y_test:list , y_pred:list):

    if len(y_pred) != len( y_test):
        print("Two arrays don't have same length")
        return None
    mae = 0
    n = len(y_pred)
    for i in range(len(y_test)):
        mae += 1/n*(abs(y_test[i]-y_pred[i]))

    return mae


if __name__ == '__main__':
    y_test = [10 , 14 , 33 , 45 , 11]
    y_pred = [11 , 12 , 30 , 40 , 9]

    mae = mean_absolute_error(y_test , y_pred)
    print(f"MAE : {mae}")

