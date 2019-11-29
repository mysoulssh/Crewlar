from crewlar_data import area_info

if __name__ == '__main__':
    areaInfo = area_info.AreaInfo()
    areaDic = areaInfo.area_detail
    localDic = areaInfo.area

    # for k, v in areaDic.items():
    #     print("市/洲："+localDic[k])
    #     area_nums = str(v).split(",")
    #     areas = []
    #     for num in area_nums:
    #         areas.append(localDic[num])
    #     print(areas)

    resultLocal = {}
    for k, v in localDic.items():
        resultLocal[v] = k
    # print(resultLocal)

    input_local = input("请输入地区名：")
    ret = resultLocal[input_local]
    print("编号:"+ret)
