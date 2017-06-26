#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import csv
plt.rcParams['figure.figsize'] = (14,6)
plt.rcParams['font.size'] = 18\

def main():
    data = np.zeros([14,14])
    data_combined = np.zeros([14,14])
    # reading in data
    with open('../data/probs.csv', mode='r') as csv_file:
        reader = csv.reader(csv_file)
        line_count = 0
        for line in reader:
            cell_count = 0
            for cell in line:
                data[line_count, cell_count] = float(cell)
                cell_count += 1
            line_count += 1
    csv_file.close()
    with open('../data/probs_combined.csv', mode='r') as csv_file:
        reader = csv.reader(csv_file)
        line_count = 0
        for line in reader:
            cell_count = 0
            for cell in line:
                data_combined[line_count, cell_count] = float(cell)
                cell_count += 1
            line_count += 1
    csv_file.close()

    plot_dict = {
        1: 'o--',
        2: 's--',
        3: 'v--',
        4: '^--',
        5: '<--',
        6: '>--',
        7: 'p--',
        8: '+--',
        9: '*--',
        10: 'h--',
        11: 'd--',
        12: 'D--',
        13: '|--',
        14: '_--',
    }

    # plotting data
    x_plot = np.arange(1,15)
    for i in range(data.shape[0]):
        plt.plot(x_plot, data[i], plot_dict[i+1], label=(i+1))
    plt.xlabel('pick number')
    plt.ylabel('probability')
    plt.xlim(1,14)
    plt.xticks(x_plot)
    plt.title('probability of obtaining a pick for each lottery team')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize = 15)
    plt.show()

    for i in range(data_combined.shape[0]):
        plt.plot(x_plot, data_combined[i], plot_dict[i+1] ,label=(i+1))
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5),fontsize = 15)
    plt.xlim(1,14)
    plt.ylim(0,1.1)
    plt.xticks(x_plot)
    plt.xlabel('pick number')
    plt.ylabel('probability')
    plt.title('probability of having picked by the nth pick for each lottery team')
    plt.show()




if __name__ == '__main__':
    main()
