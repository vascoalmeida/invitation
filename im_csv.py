import sys
import os
import csv
import pymysql
from Crypto.Hash import SHA512
from random import randint

def import_from_csv():
    if(len(sys.argv) < 2):
        print("Please use the file like this: 'python3 <CSV file> [more CSV files]'")
        return
    
    salt_limit = 10**1000
        
    for filename in sys.argv[1:]:
        if not os.path.isfile(filename):
            print("[ERROR] '%s' file not found.")
            continue

        reader = csv.DictReader(open(filename))
        writer = csv.DictWriter(open("%s_with_hash.csv" % filename, "w"), fieldnames=['name', 'email', 'hash', 'response'])
        writer.writeheader()

        conn = pymysql.connect("localhost", "guest", "password", "invite")
        cursor = conn.cursor()

        for row in reader:
            name = row["name"]
            email = row["email"]
            response = row["response"]

            sha512 = SHA512.new()
            sha512.update(row["email"].encode())
            sha512.update(str(randint(0, salt_limit)).encode())
            h = sha512.hexdigest()

            writer.writerow({"name": name, "email": email, "hash": h, "response": response})
            
            try:
                cursor.execute("INSERT INTO invited_people (name, email, hash, response) VALUES ('%s', '%s', '%s', '%s')" % (name, email, h, response))
            except pymysql.err.IntegrityError:
                cursor.execute("UPDATE invited_people SET response = '%s' WHERE hash='%s';" % (response, h))
            
            conn.commit()


if __name__ == "__main__":
    import_from_csv()