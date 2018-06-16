import smtplib
import os
import sys
import pymysql
from getpass import getpass

menu_options = """
Please enter one of the following options:
1: Use template file for email, where $$$ will be replaced with link
2: Use personalised text inserted in command line, where $$$ will be replaced with link
3: Just send the link
0: Exit

Desired option: """

def send_mail():
    if(len(sys.argv) < 2):
        print("Please insert the link to the invitation like this: 'python3 send_emails.py <link>'")
        return

    while True:
        option = input(menu_options)

        if option not in "0123":
            print("Option incorrect.\n")
            continue

        if option == "0":
            return

        if option == "1":
            while True:
                template_file = input("Please insert template file's path (or .exit' to exit program): ")
                if template_file == ".exit":
                    return

                if os.path.isfile(template_file): 
                    message = open(template_file).read()

                    if "$$$" not in message:
                        print("Error: The template message needs to have at least once '$$$' to specify where the link must appear.\n")
                        continue

                    break

                print("Error: That file doesn't exist.\n")
            
            break
        
        if option == "2":
            while True:
                message = input("Please insert the template message (write '$$$' where you want the link to appear): ")
                
                if "$$$" not in message:
                    print("Error: The template message needs to have at least once '$$$' to specify where the link must appear.\n")
                    continue
                
                break
            break

        if option == "3":
            message = "$$$"
            break

    connection = pymysql.connect("localhost", "guest", "password", "invite")
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT email, hash, name FROM invited_people WHERE response=''")
        people = cursor.fetchall()
    except:
        print("Error fetching info from database")
        return

    gmail_add = input("Email: ")
    gmail_passw = getpass("Password: ")

    subject = "Teste"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_add, gmail_passw)
    
    for person in people:
        to = person[0]

        if(sys.argv[1][-1] == "/"):
            link = "%s%s" % (sys.argv[1], person[1])
        else:
            link = "%s/%s" % (sys.argv[1], person[1])

        message = message.replace("$$$", link)
        
        body = "\r\n".join(["To: %s" % to,
                            "From: %s" % gmail_add,
                            "Subject: %s" % subject,
                            "", message])

        try:
            server.sendmail(gmail_add, [to], body)
            print("Email sent successfully to %s" % person[0])
        except Exception as exc:
            print(exc)
            #print("Error sending email to %s" % person[0])

    server.quit()

if __name__ == "__main__":
    send_mail()