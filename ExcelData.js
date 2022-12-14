function ExcelData(){
    const readXlsxFile = require('read-excel-file/node');
    const fs = require('fs');

    readXlsxFile("./productNumbers.xlsx").then((rows) => {
    console.log(rows);
    let jsonData = [];
    for (let i = 0; i < rows.length; i++) {
        if (i !== 0) {
        const inputData = {
            itemCode: rows[i][0],
        };
        jsonData.push(inputData);
        }
    }
    return jsonData
    });
}