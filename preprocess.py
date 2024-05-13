import pandas as pd
import msoffcrypto
import io

def read_encrypted_data(passwd = 'Capstone_2024', path_to_data = "data/CONFIDENTIAL_SampleData_Shared-2024-05-08.xlsx"):
    decrypted_workbook = io.BytesIO()
    with open(path_to_data, 'rb') as file:
        office_file = msoffcrypto.OfficeFile(file)
        office_file.load_key(password=passwd)
        office_file.decrypt(decrypted_workbook)
    
    return pd.read_excel(decrypted_workbook)

def reformat_data(data):
    df = data.copy()
    df["Event_Remarks_Text"] = df["Event_Remarks_Text"].astype(str)
    df = df.sort_values(by=["Event_Anonymizer", "Event_Remarks_Created_Timestamp", "Remarks_Line_Order"], ascending=True)
    event_group = df.groupby(["Event_Anonymizer"], as_index=False, sort=False)

    agg_funcs = {
        col: 'first' for col in ["Grouped_Event_Type_Code_Desc", "Grouped_Event_Subtype_Code_Desc", 
                                 "Priority", "Public_Generated_Event_Flag", "Event_Attended_Flag"]
    }
    agg_funcs["Event_Remarks_Text"] = lambda x: "\n".join(x)
    
    return event_group.agg(agg_funcs)


if __name__ == "__main__":
    data = read_encrypted_data()
    df = reformat_data(data)
