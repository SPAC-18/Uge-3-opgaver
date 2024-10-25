try:
    f = open("app_log (logfil analyse) 1.txt", "r")

    def error_finder(log_string):
        result = ""
        log_lines = log_string.split("\n")
        for entry in log_lines:
            if "ERROR" in entry or "WARNING" in entry:
                #result.append(entry)
                result = result + entry + "\n"
        return result
    
    s = open("app_log_warnings_and_errors.txt","w")
    s.write(error_finder(f.read()))
except ValueError:
    print("Error reading file")