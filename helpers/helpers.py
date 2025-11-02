def convert_post_code_in_name(post_code):
    name = ''
    for i in range(0, 10, 2):
        two_digit = int(str(post_code)[i:i + 2])
        latin_symbol = chr(97 + (int(two_digit) % 26))
        name += latin_symbol
    return name

def find_customer_avg_name(customers_name):
    names_lengths = [len(name) for name in customers_name]
    average_name_length = sum(names_lengths) / len(names_lengths)
    name_for_delete = min(customers_name, key=lambda name: abs(len(name) - average_name_length))
    return name_for_delete

def sorting_data(data):
    sorted_data = sorted(data, reverse=True)
    return sorted_data