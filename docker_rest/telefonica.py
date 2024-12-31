import joblib
from joblib import load
import pandas as pd
import sklearn

class TelefonicaAI:
    def __init__(self, model_path: str, scaler_path:str, significant_columns_path: str):

        self.model = load(model_path)
        self.scaler = load(scaler_path)
        self.significant_columns = load(significant_columns_path).drop(['Churn'])
    def convert_one_hot(self, data, options):
        output = []
        for o in options:
            if data == o:
                output.append(1)
            else:
                output.append(0)

        return output

    def extract_features(self, data):
        internet_service = data['internet_service']
        number_dependents = data['number_dependents']
        number_referrals = data['number_referrals']
        satisfaction_score = data['satisfaction_score']
        tenure_in_months = data['tenure_in_months']
        total_long_distance_charges = data['total_long_distance_charges']
        total_revenue = data['total_revenue']
        contract = data['contract']
        payment_method = data['payment_method']

        x = [internet_service, number_dependents, number_referrals, satisfaction_score, tenure_in_months, total_long_distance_charges, total_revenue]
        contract = self.convert_one_hot(contract, ['Month-to-Month','One Year', 'Two Year'])
        payment_method = self.convert_one_hot(payment_method, ['Bank Withdrawal','Credit Card','Mailed Check'])

        x += contract + payment_method
        df_x = pd.DataFrame([x], columns=self.significant_columns)
        return df_x

    def predict(self, data):
        x = self.extract_features(data)
        x_scaled = self.scaler.transform(x)

        prediction = self.model.predict(x_scaled)

        pred = prediction[0]

        if pred == 1:
            response = 'Cancelará'
        else:
            response = 'No cancelará'

        return response