import csv

def list_to_csv(film_rows, list_name):
    
    with open(f'{list_name}.csv', 'w') as f:
        write = csv.writer(f)

        write.writerows(film_rows)
        
    return