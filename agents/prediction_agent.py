import random

def predict_resolution_time(priority):

    if priority.lower() == "critical":
        return "Estimated Resolution: 1 Hour"

    elif priority.lower() == "high":
        return "Estimated Resolution: 3 Hours"

    elif priority.lower() == "medium":
        return "Estimated Resolution: 1 Day"

    else:
        return "Estimated Resolution: 2 Days"


if __name__ == "__main__":

    priority = input("Enter priority:\n")

    print(predict_resolution_time(priority))