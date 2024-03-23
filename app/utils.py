""""
generates sample data for api
"""

import os
import random

def generate_city_data():
    directory = "data/cities"
    files = os.listdir(directory)
    random_file = random.choice(files)
    country_name = random_file.split('-')[0]

    with open(os.path.join(directory, random_file), 'r') as file:
        # this needs to be imporved wrt memeory effciency
        num_lines = sum(1 for line in file)
        random_line_num = random.randint(1, num_lines)
        file.seek(0)
        
        for _ in range(random_line_num - 1):
            file.readline()

        city_name = file.readline().strip()

    country_city_data = {"country_name": country_name, "city_name" : city_name}
    
    return country_city_data