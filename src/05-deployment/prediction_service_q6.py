import pickle


def predict(record_to_score):
    input_file_name = "pipeline_v2.bin"
    with open(input_file_name, "rb") as file_in:
        dv, model = pickle.load(file_in)

    X_record = dv.transform(record_to_score.dict())
    y_pred = model.predict_proba(X_record)[0, 1]

    return y_pred
