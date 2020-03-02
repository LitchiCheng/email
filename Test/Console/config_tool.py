import configparser
cf = configparser.ConfigParser()
ini_path = "D:\\code\\email\\Test\\Console\\fund.ini"
cf.read(ini_path)

def addFund(fund_code):
    curr_code = cf.get("fund","code")
    cf.set("fund","code",curr_code +","+ str(fund_code))
    with open(ini_path,"w+") as f:
        cf.write(f)

def delFund(fund_code):
    curr_code_list = cf.get("fund","code").split(",")
    curr_code_list.remove(str(fund_code))
    tmp_str=""
    for i in curr_code_list:
        tmp_str = tmp_str+","+str(i)
    cf.set("fund","code",tmp_str.lstrip(","))
    with open(ini_path,"w+") as f:
        cf.write(f)

if __name__ == "__main__":
    addFund(260108)
    print(cf.get("fund","code"))

    