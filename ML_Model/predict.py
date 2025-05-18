import sys
import json
import joblib
import numpy as np

def main():
    # Load input data from command line argument
    input_json = sys.argv[1]
    data = json.loads(input_json)
    features = np.array([[data["n"], data["p"], data["k"], data["temperature"], data["humidity"], data["ph"], data["rainfall"]]])
    # Load model
    model = joblib.load("ML_Model/trained_model.pkl")
    # Predict
    pred = model.predict(features)
    print(json.dumps({"recommended_crop": pred[0]}))


if __name__ == "__main__":
    main()
