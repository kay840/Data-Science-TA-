from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

app = Flask(__name__)

@app.route('/')
def dashboard():
    df = pd.read_csv('heart.csv')

    os.makedirs('static', exist_ok=True)

    # Plot 1: Jumlah Pasien Sehat vs Berisiko
    plt.figure(figsize=(5,3))
    sns.countplot(x='target', data=df)
    plt.title('Jumlah Pasien Sehat vs Berisiko')
    plt.savefig('static/plot1.png')
    plt.close()

    # Plot 2: Distribusi Usia
    plt.figure(figsize=(5,3))
    sns.histplot(df['age'], kde=True)
    plt.title('Distribusi Usia Pasien')
    plt.savefig('static/plot2.png')
    plt.close()

    # Plot 3: Heatmap Korelasi Antar Fitur
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    plt.title("Heatmap Korelasi Antar Fitur")
    plt.tight_layout()
    plt.savefig('static/plot_heatmap.png')
    plt.close()

    return render_template('grafik.html')

if __name__ == '__main__':
    app.run(debug=True)
