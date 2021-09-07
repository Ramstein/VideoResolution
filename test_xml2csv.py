

string_to_search = '<drug type="'

def check_if_string_in_file():
    found = 1
    i, j = 1, 1
    temp_str = b""
    f = open("temp1" + ".xml", "wb")

    filepath = r"C:\Users\user\Downloads\drugbank\full database.xml"
    with open(filepath, 'rb') as read_obj:

        lines = read_obj.readlines()
        for line in lines:
            if line.find(b'<drug type="') == -1:
                pass
            else:
                # if found >= 1500:
                if found%80==0 :
                    f.write(b'</drugbank>')
                    f.close()
                    f = open("temp"+str(found) + ".xml", "wb")
                    f.write(b'<?xml version="1.0" encoding="UTF-8"?>'+b'\n'+b'<drugbank xmlns="http://www.drugbank.ca" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.drugbank.ca http://www.drugbank.ca/docs/drugbank.xsd" version="5.1" exported-on="2020-04-23">'+b'\n')
                found+=1
                print(found)
            f.write(line)


            # if i>j:
            #     f = open("temp" + str(i) + ".txt", "w"); j+=1
            # if line.find(b'<drug type="') == -1:
            #     pass
            # else:
            #     print(str(found)+" found"); found+=1
            #     if found == 1356*i:
            #         print(line)
            #         temp_str+=line+b"\n"+b"</drugbank>"
            #         f.write(temp_str.decode("utf-8"))
            #         f.close()
            #         temp_str = b""
            #         print("temp"+str(i)+".txt")
            #         i+=1
            #         continue
            # f.write(line.decode("utf-8"))


check_if_string_in_file()

