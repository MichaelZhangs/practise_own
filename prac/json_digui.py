str_json = {
    "name":"peter",
    "sex":"boy",
    "jobs":{
        "title":"supervisor",
        "position":"it"
    },
     "id" :{
         "birthdate":"20121011",
         "palce":"sz",
         "info":{
             "country":"china",
             "province":{
                    "province_name":"guangdong",
                    "city":{
                        "city_name":"shenzehen",
                        "county":{
                            "county_name":"longgang",
                            "hometown":"xp"
                        }
                    }
                }
         }
     },
    "age":"25"
 }

def dic_parse(dic):
    if isinstance(dic, dict):
        for key in dic:
            value = dic.get(key)
            if isinstance(value, dict):
                dic_parse(dic_parse(value))
                # for k in value.keys():
                #     if  not isinstance(value[k], dict):
                #         print(key + "." + k + "=" + value[k])
            else:
                print(key+"="+dic[key])

dic_parse(str_json)
