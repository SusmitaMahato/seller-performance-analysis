import seaborn as sns
import matplotlib.pyplot as plt

def show_charts(df):
    sns.boxplot(y=df["ratings"])
    plt.title("Ratings Distribution")
    plt.show()

    sns.boxplot(x="category", y="ratings", data=df)
    plt.title("Category-wise Ratings")
    plt.show()

    sns.barplot(x="seller_name", y="ratings", data=df)
    plt.title("Seller Ratings")
    plt.show()

    sns.barplot(x="seller_name", y="revenue", data=df)
    plt.title("Seller Revenue")
    plt.show()
