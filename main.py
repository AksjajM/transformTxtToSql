# FileName input
input_file = "go_training.txt"

# FileName output
output_file = "insert_queries.sql"

with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    # Save header
    next(infile)

    # Iterate over the lines
    for line in infile:
        # Remove whitespaces and ~
        line = line.strip()
        parts = line.split("~")

        # Retrieve the values of every part
        year_month = parts[0].split()
        year = year_month[0]
        month = year_month[1]
        sales_staff = parts[1]
        course = parts[2]

        # Create the SQL Insert-query
        query = f"INSERT INTO go_training (year, month, sales_staff, course) VALUES ({year}, {month}, '{sales_staff}', '{course}');"

        # Write the query to the output file
        outfile.write(query + "\n")

print("De SQL INSERT-query's zijn succesvol gegenereerd en opgeslagen in insert_queries.sql.")
