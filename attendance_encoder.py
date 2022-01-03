import os, tkinter
from tkinter import filedialog
from datetime import datetime
import pandas as pd
from openpyxl.reader.excel import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows

def ConvertAttFile(filepath) -> dict[str, dict[str, str]]:
    att = pd.read_excel(filepath, sheet_name='ATTENDEES', index_col='ID', usecols=[0, 1])
    att_list = att.to_dict()
    return att_list

def ConvertMasterlist(masterlist_file) -> dict[str, dict[str, str]]:
    id = pd.read_excel(masterlist_file, sheet_name='MASTERLIST', index_col='ID')
    id_list = id.to_dict()
    return id_list

def CheckMasterlist(qr_code: str, id_list: dict[str, dict[str, str]]) -> int:
    if qr_code in id_list['FIRST_NAME']:
        return 0          
    else:
        return 1

def AddPerson(qr_code: str, id_list: dict[str, dict[str, str]], att_list: dict[str, dict[str, str]], filepath: str) -> str:
    attendees = dict({'ID':[], 'FIRST_NAME':[], 'LAST_NAME':[], 'AGE':[], 'GENDER':[], 'CIVIL_STATUS':[],
                    'CONTACT_NO':[], 'ADDRESS':[], 'EMAIL_ADDRESS':[], 'PART_OF_DG':[]})

    # check first if already in attendee list, else check against masterlist
    if qr_code in att_list['FIRST_NAME']:
        return att_list['FIRST_NAME'][qr_code]

    else:
        if CheckMasterlist(qr_code, id_list) == 0:
            attendees['ID'].append(qr_code)
            attendees['FIRST_NAME'].append(id_list['FIRST_NAME'][qr_code])
            attendees['LAST_NAME'].append(id_list['LAST_NAME'][qr_code])
            attendees['AGE'].append(id_list['AGE'][qr_code])
            attendees['GENDER'].append(id_list['GENDER'][qr_code])
            attendees['CIVIL_STATUS'].append(id_list['CIVIL_STATUS'][qr_code])
            attendees['CONTACT_NO'].append(id_list['CONTACT_NO'][qr_code])
            attendees['ADDRESS'].append(id_list['ADDRESS'][qr_code])
            attendees['EMAIL_ADDRESS'].append(id_list['EMAIL_ADDRESS'][qr_code])
            attendees['PART_OF_DG'].append(id_list['PART_OF_DG'][qr_code])

            # append to excel file
            add_person = pd.DataFrame(attendees)
            att_file = load_workbook(filepath, read_only=False, keep_vba=False)
            att_file_sheet = att_file["ATTENDEES"]

            for r in dataframe_to_rows(add_person, index=False, header=False):
                att_file_sheet.append(r)
            
            att_file.save(filepath)
            att_file.close()

            return id_list['FIRST_NAME'][qr_code]

        else:
            return "QR code is not recognized." 

def AddFirstTimer():
    pass

def CreateNewFile(file_location: str) -> str:
    # file template
    attendees = pd.DataFrame({'ID':[], 'FIRST_NAME':[], 'LAST_NAME':[], 'AGE':[], 'GENDER':[], 'CIVIL_STATUS':[],
                            'CONTACT_NO':[], 'ADDRESS':[], 'EMAIL_ADDRESS':[], 'PART_OF_DG':[]})
    first_timers = pd.DataFrame({'FT_FIRST_NAME':[], 'FT_LAST_NAME':[], 'FT_AGE':[], 'FT_GENDER':[], 'FT_CIVIL_STATUS':[],
                                'FT_CONTACT_NO':[], 'FT_ADDRESS':[], 'FT_EMAIL_ADDRESS':[], 'FT_PART_OF_DG':[]})
    new_attendance = {'ATTENDEES': attendees, 'FIRST_TIMERS': first_timers}

    # set destination path + file name
    now = datetime.now()
    date_time = now.strftime("%b-%d-%Y-%H-%M")
    savefile_loc = file_location + '/CCFTANAY_ATTENDANCE_' + str(date_time) + '.xlsx'

    # save sheets into excel file
    save_file = pd.ExcelWriter(savefile_loc, engine='xlsxwriter')
    for sheet_name in new_attendance.keys():
        new_attendance[sheet_name].to_excel(save_file, sheet_name=sheet_name, index=False)
    save_file.save()

    return savefile_loc

##### TESTINGGGGG #####
"""if __name__ == '__main__':
    # files needed for encoding
    masterlist_file = ''
    file_location = ''
    existing_file = ''

    # data to append to existing file

    # choose masterlist file
    root = tkinter.Tk()
    root.withdraw()
    masterlist_file = filedialog.askopenfilename(initialdir=os.path.expanduser("~/Desktop"), 
                                                filetypes=[("Excel file", "*.xlsx")])
    root.destroy()
    print("Masterlist: ", masterlist_file)

    # convert masterlist to dict
    id_list = ConvertMasterlist(masterlist_file)

    # test qrcode
    testing = 'CCFTNY0004'

    # choose file location or existing file
    print("type 0 or 1: ")
    select = int(input())
    print("Select: ", select)
    if select == 0:
        # file location - create NEW FILE
        root = tkinter.Tk()
        root.withdraw()
        file_location = filedialog.askdirectory(initialdir=os.path.expanduser("~/Desktop"))
        root.destroy()
        print("File location: ", file_location)

        # ENCODING PART
        ## create new file
        created_file = CreateNewFile(file_location)
        print(created_file)

        ## convert attendance file to dict
        att_list = ConvertAttFile(created_file)
        print(att_list)

        ## test qr code
        message = AddPerson(testing, id_list, att_list, created_file)
        print(message)

    elif select == 1:
        # EXISTING FILE
        root = tkinter.Tk()
        root.withdraw()
        while (1):
            existing_file = filedialog.askopenfilename(initialdir=os.path.expanduser("~/Desktop"), 
                                                        filetypes=[("Excel file", "*.xlsx")])
            if existing_file == masterlist_file:
                print("Please choose a different file.")
            else:
                break
        root.destroy()
        print("Existing file: ", existing_file)

        # ENCODING PART
        ## convert attendance file to dict
        att_list = ConvertAttFile(existing_file)

        ## test qr code
        message = AddPerson(testing, id_list, att_list, existing_file)
        print(message)"""
