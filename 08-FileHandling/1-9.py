###
# Prints employees employed in a specified position.
#

# Employee List
file_name = 'it_company.txt'

# Position
job_title = 'Software Engineer'


with open(file_name, 'r') as file:
   count = 1
   for line in file:
      if job_title in line:
        print(f"{count}. {line}")
        count +=1