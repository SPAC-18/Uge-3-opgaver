import pandas as pd
import numpy as np
import email_validator
import argparse

try:
    file_name = "source_data (Datamigrering hjælpeværktøj)"
    f = open(file_name + ".csv", "r")
    entry_list = f.read().split("\n")
    entry_list_corrected = ""
    entry_list_errors = ""
    for i in range(len(entry_list)):
        if not all(np.unique(entry_list[i].split(",")) == ['']):
            skip = False
            entry = entry_list[i].split(",")
            indeces_to_remove = []
            for j in range(len(entry)):
                if entry[j] == "":
                    indeces_to_remove.append(j)
            for k in reversed(range(len(indeces_to_remove))):
                entry.pop(indeces_to_remove[k])
            if entry[0] == "" and len(entry) != 4:
                entry.pop(0)
            try:
                valid_purchase = entry[2].split(".")[0]+entry[2].split(".")[1]
            except:
                valid_purchase = "H"
            missing_info_check = (not entry[0].isdigit()) and "@" in entry[1] and valid_purchase.isdigit()
            if len(entry) < 4 and (missing_info_check):
                customer_id = str(i)
                name = entry[0]
                if type(name) == type("a"):
                    while name[0] == " ":
                        name = name[1:]
                    while name[-1] == " ":
                        name = name[:-2]
                email = entry[1]
                purchase_amount = str(entry[2])
                if "" == purchase_amount:
                    purchase_amount = str(entry[4])              
            elif len(entry) < 4:
                entry = [1,2,3,4]
                skip = True
            else:
                skip = False
            if len(entry) != 3:
                customer_id = str(i)
                name = entry[1]
                if type(name) == type("a"):
                    while name[0] == " ":
                        name = name[1:]
                    while name[-1] == " ":
                        name = name[:-2]
                email = entry[2]
                purchase_amount = str(entry[3])
                if "" == purchase_amount:
                    purchase_amount = str(entry[4])
            if purchase_amount == "ABC123":
                skip = True
            try:
                (email_validator.validate_email(email, check_deliverability=False, test_environment=True))
                valid_email = True
            except:
                valid_email = False
            if valid_email:
                skip == True
            if i != 0:
                try:
                    if float(purchase_amount) < 0:
                        skip = True
                except:
                    1
            if i != 0 and not skip:
                entry_list_corrected = entry_list_corrected + (customer_id + "," + name + "," + email + "," + purchase_amount + "\n")
            else:
                if not skip:
                    entry_list_corrected = entry_list_corrected + ("customer_id," + name + "," + email + "," + purchase_amount + "\n")
            if skip:
                entry_list_errors = entry_list_errors + str(entry_list[i]) + "\n"
    entry_list_corrected = entry_list_corrected[:-2]

    parser = argparse.ArgumentParser()
    parser.add_argument("-xlsx", action="store_true",
                        help="save .xlsx files")
    parser.add_argument("-csv",  action="store_true",
                        help="save .csv files")
    args = parser.parse_args()
    if args.csv:
        with open(file_name + "_new.csv", "w") as f:
            f.write(entry_list_corrected)
            f.close()
        with open(file_name + "_errors.csv", "w") as f:
            f.write(entry_list_errors)
            f.close()
    elif args.xlsx:
        with open(file_name + "_new.csv", "w") as f:
            f.write(entry_list_corrected)
            f.close()
        with open(file_name + "_errors.csv", "w") as f:
            f.write(entry_list_errors)
            f.close()
        data_new = pd.read_csv(file_name + "_new.csv")
        excel_new = data_new.to_excel(file_name + "_new.xlsx")

        data_errors = pd.read_csv(file_name + "_errors.csv")
        excel_errors = data_errors.to_excel(file_name + "_errors.xlsx")
    else:
        with open(file_name + "_new.csv", "w") as f:
            f.write(entry_list_corrected)
            f.close()
        with open(file_name + "_errors.csv", "w") as f:
            f.write(entry_list_errors)
            f.close()

except FileNotFoundError:
    print("File not found")
except ValueError:
    print("Error reading .csv file")
except PermissionError:
    print("Cannot write to file " + file_name + "_new.csv")