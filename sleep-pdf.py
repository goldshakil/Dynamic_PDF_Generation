import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def create_summary_graph(night1, night2, night3):
    fig = plt.figure(figsize=(7, 4))

    x_axis = [1, 2, 3]
    y_axis = [night1, night2, night3]
    positions = [0, 1, 2]

    plt.bar(positions, y_axis, width=0.8, color="#daeffb")

    plt.xticks(positions, x_axis, fontsize=16)
    plt.yticks(np.arange(0, 31, 15), fontsize=16, color="#d1d3d4")
    plt.tick_params(axis=u"both", which=u"both", length=8, color="white")

    plt.xlabel("Night", color="#939598", fontsize=16, fontweight="medium")
    plt.ylabel("AHI", color="#939598", fontsize=16, fontweight="medium")

    plt.axhline(y=15, color="#d1d3d4", linestyle="--")
    plt.axhline(y=30, color="#d1d3d4", linestyle="--")
    plt.axhline(y=31, color="white", linestyle="--")

    plt.margins(0)
    fig.subplots_adjust(bottom=0.2)

    i = 0
    for spine in plt.gca().spines.values():
        if i != 2:
            spine.set_visible(False)
        i += 1

    for index, data in enumerate(y_axis):
        plt.text(x=index, y=data+2, s=f"{data}",
                 fontsize=15, color="#34b2ea", ha="center")
    plt.show()


def create_daily_report_graph(am1, am2, am3, am4, am5, am6, y_label):
    fig = plt.figure(figsize=(7, 3))

    x_axis = ["1 am", "2 am", "3 am", "4 am", "5 am", "6 am"]
    y_axis = [am1, am2, am3, am4, am5, am6]
    positions = [0, 1, 2, 3, 4, 5]

    plt.bar(positions, y_axis, width=0.8, color="#daeffb")

    plt.xticks(positions, x_axis, fontsize=12)
    plt.yticks(np.arange(0, 31, 15), fontsize=12, color="#d1d3d4")
    plt.tick_params(axis=u"both", which=u"both", length=8, color="white")

    plt.xlabel("Hours", color="#939598", fontsize=14, fontweight="medium")
    plt.ylabel(y_label, color="#939598", fontsize=14, fontweight="medium")

    plt.axhline(y=15, color="#d1d3d4", linestyle="--")
    plt.axhline(y=30, color="#d1d3d4", linestyle="--")
    plt.axhline(y=31, color="white", linestyle="--")

    plt.margins(0)
    fig.subplots_adjust(bottom=0.2)

    i = 0
    for spine in plt.gca().spines.values():
        if i != 2:
            spine.set_visible(False)
        i += 1

    for index, data in enumerate(y_axis):
        plt.text(x=index, y=data+2, s=f"{data}",
                 fontsize=12, color="#34b2ea", ha="center")
    plt.show()


def create_heartrate_graph(csv_path):
    df = pd.read_csv(csv_path)

    # Draw Plot
    fig = plt.figure(figsize=(16, 3))
    plt.plot(df['date'], df['value'], color="#cccccc")

    # Decoration
    plt.ylim(50, 750)

    plt.xticks(np.arange(0, 750, 20), fontsize=12, color="#cccccc")
    plt.yticks(np.arange(0, 750, 100), fontsize=12, color="#cccccc")
    plt.tick_params(axis=u"both", which=u"both", length=8, color="white")

    plt.xlabel("Time")

    plt.margins(0)
    fig.subplots_adjust(bottom=0.2)

    for spine in plt.gca().spines.values():
        spine.set_edgecolor("#3595d2")

    plt.show()

# def create_pdf():
# This will be completed once FIGMA design is provided


# create_summary_graph(14, 10, 6)
# create_daily_report_graph(14, 10, 8, 14, 9, 5, "ODI")
create_heartrate_graph(
    "https://github.com/selva86/datasets/raw/master/AirPassengers.csv")
