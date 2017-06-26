#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import csv

def main():
    with open('probs.csv', mode='r') as csv_file:
        with open('probs_combined.csv', mode='w') as write_file:
            reader = csv.reader(csv_file)
            line_count = 0
            for line in reader:
                cell_count = 0
                accumulator = 0
                for cell in line:
                    accumulator += float(cell)
                    write_file.write(str(accumulator) + ',')
                    cell_count += 1
                write_file.write('\n')
                line_count += 1
        write_file.close()
    csv_file.close()


if __name__ == '__main__':
    main()
