# this file will contains function to convert data in a csv file
# function will accept data and search terms as arguments
# we will create a csv file with search terms as file name and save the data in the csv file
# if file already exists we will append the data to the existing file
# header variable stores headers for csv file all relevent data goest to perticular header in the csv file.
import csv
from .constants import header
import datetime


def generateCSV(data, search_term):
    try:
        if not search_term or not data:
            return False
        # date = datetime.datetime.now()
        filename = search_term.replace(" ", "_").replace(",", "").lower()
        # we will create a csv file with search terms as file name and save the data in the csv file
        # if file already exists we will append the data to the existing file
        # first insert the header if not exists
        # file must be editable even if it is opened in another application
        with open(f"{filename}.csv", "a", newline="", encoding="utf-8") as file:
            # check if the file is empty
            # if the file is empty write the header
            # else append the data
            if file.tell() == 0:
                writer = csv.DictWriter(file, fieldnames=header)
                writer.writeheader()
                for row in data:
                    writer.writerow(row)
            else:
                writer = csv.DictWriter(file, fieldnames=header)
                for row in data:
                    writer.writerow(row)
        return True
    except Exception as e:
        print(f"An error occurred in generateCSV : {str(e)}")
        return False
