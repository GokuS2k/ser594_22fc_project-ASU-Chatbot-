import numpy as np
import matplotlib.pyplot as plt


def survey():
    save_plots = r"C:/Users/rkanna14/PycharmProjects/pythonProject1/visuals"  #My laptop doesnt support PyCharm, so did in my friend's
    list_sur = []
    list_rub = ["Satisfaction", "Efficiency", "Accuracy", "Response Time", "Answered all?"]
    print("Please do rate SPARKY's customer service (from 1-5)")
    list_sur.append(int(input("How satisfied are you with our response today?")))
    list_sur.append(int(input("How efficient was this chatbot service?")))
    list_sur.append(int(input("Was the response accurate enough?")))
    list_sur.append(int(input("How good was the response time?")))
    list_sur.append(int(input("Did we answer all your questions?")))
    sug = input("Additional feedback (optional)*")
    print(list_sur)
    fig = plt.figure(figsize=(10, 5))
    plt.bar(list_rub, list_sur, color='maroon', width=0.4)
    plt.xlabel("Customer Review")
    plt.ylabel("Ratings")
    plt.title("Rating of the present customer")
    plt.show()
    fig.savefig(save_plots + '/Customer_Response')
    plt.close()

# survey()
