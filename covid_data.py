import pandas as pd
import matplotlib.pyplot as plt
import requests

# This script is to fetch covid data from WHO website and aggregate data by Date
# Present it in a chart

url = "https://covid19.who.int/WHO-COVID-19-global-data.csv"
response = requests.get(url)

with open("WHO-COVID-19-global-data.csv", "wb") as f:
    f.write(response.content)


# Load the data from the CSV file
df = pd.read_csv("WHO-COVID-19-global-data.csv", parse_dates=["Date_reported"])

# Compute the total confirmed cases by date
total_cases = df.groupby("Date_reported")["New_cases"].sum().cumsum()

# Create a line plot of the total confirmed cases over time
fig = plt.figure(figsize=(19.20, 10.80))

plt.plot(total_cases)
plt.xlabel("Confirmation Date")
plt.ylabel("Total confirmed cases")
plt.title("WHO - COVID-19 Global Cases")
mng = plt.get_current_fig_manager()
mng.window.state('zoomed')

plt.show()
