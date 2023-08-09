def print_operation_table(operation, num_rows=6, num_columns=6):
    for row in range(1, num_rows + 1):
        row_values = [operation(row, col) for col in range(1, num_columns + 1)]
        row_str = ' '.join(str(value) for value in row_values)
        print(row_str)

def main():
    print_operation_table(lambda x, y: x * y)

if __name__ == "__main__":
    main()
