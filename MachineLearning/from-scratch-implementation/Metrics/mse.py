# Mean Squared Error

def mean_squared_error(y_test:list , y_pred:list):

    if len(y_pred) != len( y_test):
        print("Two arrays don't have same length")
        return None
    n = len(y_test)
    mse = 0
    for i in range(len(y_test)):
        mse += 1/n*(y_test[i] - y_pred[i])**2

    return mse


if __name__ == '__main__':
    y_test = [10 , 14 , 33 , 45 , 11]
    y_pred = [11 , 12 , 30 , 40 , 9]

    mae = mean_squared_error(y_test , y_pred)
    print(f"MAE : {mae}")

