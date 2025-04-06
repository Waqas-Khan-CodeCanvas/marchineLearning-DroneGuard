import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib

class DroneAttackDetector:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.scaler = StandardScaler()
        self.label_encoders = {}
        
    def preprocess_data(self, data):
        """
        Preprocess the drone network traffic data
        """
        df = data.copy()
        
        # Handle missing values
        df = df.fillna(0)
        
        # Convert timestamp to numerical features
        if 'timestamp' in df.columns:
            df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
            df['minute'] = pd.to_datetime(df['timestamp']).dt.minute
            df = df.drop('timestamp', axis=1)
        
        # Encode categorical variables
        categorical_columns = df.select_dtypes(include=['object']).columns
        for column in categorical_columns:
            if column not in self.label_encoders:
                self.label_encoders[column] = LabelEncoder()
                df[column] = self.label_encoders[column].fit_transform(df[column])
            else:
                df[column] = self.label_encoders[column].transform(df[column])
        
        return df
    
    def train(self, X, y):
        """
        Train the attack detection model
        """
        # Preprocess features
        X_processed = self.preprocess_data(X)
        
        # Split the data
        X_train, X_test, y_train, y_test = train_test_split(
            X_processed, y, test_size=0.2, random_state=42
        )
        
        # Scale features
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        # Train model
        self.model.fit(X_train_scaled, y_train)
        
        # Make predictions
        y_pred = self.model.predict(X_test_scaled)
        
        # Calculate metrics
        metrics = {
            'accuracy': accuracy_score(y_test, y_pred),
            'precision': precision_score(y_test, y_pred, average='weighted'),
            'recall': recall_score(y_test, y_pred, average='weighted'),
            'f1': f1_score(y_test, y_pred, average='weighted')
        }
        
        return metrics
    
    def predict(self, X):
        """
        Make predictions on new data
        """
        X_processed = self.preprocess_data(X)
        X_scaled = self.scaler.transform(X_processed)
        return self.model.predict(X_scaled)
    
    def save_model(self, path):
        """
        Save the trained model
        """
        joblib.dump({
            'model': self.model,
            'scaler': self.scaler,
            'label_encoders': self.label_encoders
        }, path)
    
    @classmethod
    def load_model(cls, path):
        """
        Load a trained model
        """
        detector = cls()
        saved_model = joblib.load(path)
        detector.model = saved_model['model']
        detector.scaler = saved_model['scaler']
        detector.label_encoders = saved_model['label_encoders']
        return detector

def main():
    # Load data
    try:
        print("Loading dataset...")
        data = pd.read_csv("drone_data.csv")
        
        # Prepare features and target
        X = data.drop(['attack_label'], axis=1)
        y = data['attack_label']
        
        # Create and train the model
        print("\nTraining model...")
        detector = DroneAttackDetector()
        metrics = detector.train(X, y)
        
        print("\nTraining Results:")
        for metric, value in metrics.items():
            print(f"{metric.capitalize()}: {value:.4f}")
        
        # Save the model
        detector.save_model('drone_attack_model.joblib')
        print("\nModel saved successfully!")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 