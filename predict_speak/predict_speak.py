import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd

def predict_speak(text):
    # Carregar o dataset
    df = pd.read_excel('predict.xlsx')
    df = df[['speak', 'action']]
    df.dropna(axis=0, subset=['action'], inplace=True)
    # Misturar o dataset para entregar sempre uma parte diferente para treinar o modelo
    df = df.sample(frac=1, random_state=42)

    nltk.download('stopwords')
    stop_words = set(stopwords.words('portuguese'))

    def preprocess_text(text):
        # Convert to lowercase
        text = str(text)
        text = text.lower()
        # Remove punctuations and special characters
        text = ''.join([char for char in text if char.isalnum() or char.isspace()])
        # Remove stopwords
        text = ' '.join([word for word in text.split() if word not in stop_words])
        return text

    df['processed_text'] = df['speak'].apply(preprocess_text)

    # Use o conjunto de dados completo para treinamento
    X_train = df['processed_text']
    y_train = df['action']

    # Vetoriza os dados de treinamento
    vectorizer = TfidfVectorizer()
    X_train_vectorized = vectorizer.fit_transform(X_train)

    # Inicializa e treina o modelo
    model = MultinomialNB()
    model.fit(X_train_vectorized, y_train)

    # Novos dados para prever
    novos_dados = [
        text
    ]
    
    # Aplicar o pré-processamento aos novos dados
    novos_dados_preprocessados = [preprocess_text(text) for text in novos_dados]

    # Vetorizar os novos dados
    novos_dados_vectorized = vectorizer.transform(novos_dados_preprocessados)

    # Fazer previsões nos novos dados
    novas_previsoes = model.predict(novos_dados_vectorized)

    # Imprimir as previsões
    return novas_previsoes[0]

