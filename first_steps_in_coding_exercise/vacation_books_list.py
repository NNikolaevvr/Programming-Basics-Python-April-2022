number_of_pages = int(input())
pages_read_for_1_hour = int(input())
needed_days = int(input())

total_time_to_read_book = number_of_pages / pages_read_for_1_hour
needed_hours_per_day = total_time_to_read_book / needed_days

print(int(needed_hours_per_day))