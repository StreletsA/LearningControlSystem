from server.DataHelper import DataHelper
from datetime import datetime

if __name__ == "__main__":
    dh = DataHelper.get_instance()
    print(dh.get_person_history("РА-138337"))
