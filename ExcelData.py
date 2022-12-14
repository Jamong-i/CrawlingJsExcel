from openpyxl import load_workbook

def getItemList(startColumn, endColumn):
    '''
    Get excel product number

    :param startColumn: Excel Start Column
    :param endColumn: Excel End Column
    :return: List - ItemNum
    '''

    # productNumbers.xlsx 데이터 가져오기 (data_only=Ture / 수식이 아닌 값으로 받가.)
    load_wb = load_workbook("../Crawlling/productNumbers.xlsx", data_only=True)

    # 시트 이름으로 불러오기
    load_ws = load_wb['Sheet1']

    # 상품 번호 리스트
    itemCode = []

    # 엑셀 상품번호 추출 후 리스트화
    get_cells = load_ws[startColumn:endColumn]
    for row in get_cells:
        for cell in row:
            itemCode.append(cell.value)

    return itemCode
