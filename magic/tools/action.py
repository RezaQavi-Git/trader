from datetime import datetime

def calculate_change(close, pred):
    return round((1 - (pred / close)) * 100, 5)

def wrote_to_file(pred, close):
    with open('prediction.txt', 'a') as out:
        out.write(str(datetime.now()) + ',' + str(pred) + ',' + str(close) + '\n')

        out.close()


def make_action(last_record, prediction):
    print('Writing to file ...')
    last_record_close = float(last_record['close'])
    prediction_close = float(prediction[0])
    if (last_record_close) > (prediction_close):
        print("Increasing")
    else:
        print("Decreasing")
    print(calculate_change(close=last_record_close, pred=prediction_close))

    wrote_to_file(pred=prediction_close, close=last_record_close)
