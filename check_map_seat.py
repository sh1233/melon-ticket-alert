import requests
import json

def get_map_seats() -> None:
    url = "https://ticket.melon.com/tktapi/product/seat/seatMapList.json?v=1&callback=getSeatListCallBack" 
   
    body = {
        'prodId': '210629',
        'pocCode': 'SC0002',
        'scheduleNo': '100001',
        'blockId': '1807,1702', #getAreaMap.json > seatData > st > sbid
        'corpCodeNo': ''
    }

    header = {
        'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
        'Content-Length': '71',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': '_fwb=157FfrvzGd8P9TaeVuTlmji.1732505114404; PCID=17325051145380684711937; PC_PCID=17325051145380684711937; _T_ANO=LdxO3meWcccuTMykzynf5Ou3ih7+bBk+LXsOne5hgFM1pfyGdzvZ7ycQLYM3424quILz2LMOUnAqIv3x/PXtIuLxXK8Is7h6jK693iG73AhtvjQXL2t9fiVDN6ZoA0A2A/tZco9e8ugZ4pdRMdtAu9Vz00SxNbNFTWpZ5+p96NbuuyqBa5bWkL6ENUToJPsFqOlqeZ8KhjTTG7Zy3l3pZJFnYmRnOFEukF4TZowAgUou4/SQU6a4LNxPfM9/L3yvuWSUMsQVRTMRkAjjchL7fVeM3GGRXX4Z4/PRXerslQxb7ZJTTQeWzSbnUjXlbOPFRV32ZqXmVkNvs7ShjNw/sQ==; MAC=QsRJhbHtBNWlff+Q4A/g20N0tIlJm7Jyprm3ylwPDBwRs+sLDWSMFJO20AOO1Kug; MLCP=MTIzODM4MTAlM0Jyb3poZWtla2VrJTNCJTNCMCUzQmV5SmhiR2NpT2lKSVV6STFOaUo5LmV5SnBjM01pT2lKdFpXMWlaWEl1YldWc2IyNHVZMjl0SWl3aWMzVmlJam9pYldWc2IyNHRhbmQwSWl3aWFXRjBJam94TnpNMU1UazVNVFEyTENKdFpXMWlaWEpMWlhraU9pSXhNak00TXpneE1DSXNJbUYxZEc5TWIyZHBibGxPSWpvaVRpSjkuaU9zR2s4NmwzR29SbDZoUTBZVHZWN0oyYWJsamg0X01URENqWWNjYXBjRSUzQiUzQjIwMjQxMjI2MTY0NTQ2JTNCRW1hRGFtJTNCMSUzQmxkeTkwMzclNDBuYXZlci5jb20lM0IyJTNC; MUS=727344124; keyCookie=12383810; NetFunnel_ID=WP15; store_melon_cupn_check=12383810; TKT_POC_ID=MP15; hide_banner=true; wcs_bt=s_585b06516861:1735528568; JSESSIONID=8302B0282F9A3CB315CC51A94A9516E9',
        'Host': 'ticket.melon.com',
        'Referer': 'https://ticket.melon.com/reservation/popup/stepBlock.htm',
        'User-Agent': 'X'
    }

    response = requests.post(url,headers=header,data=body)
    map_datas = json.loads(response.text.replace("/**/getSeatListCallBack(","").replace(");", ""))
    
    return response

get_map_seats()