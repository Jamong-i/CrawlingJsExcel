// Excel 데이터 불러오기
const readXlsxFile = require('read-excel-file/node');
const fs = require('fs');

global.itemData = itemData;
var itemData = [];

readXlsxFile("./productNumbers.xlsx").then((rows) => {
  let jsonData = [];
  for (let i = 0; i < rows.length; i++) {
    if (i !== 0) {
      const inputData = {
        id: i,
        itemCode: rows[i][0]
      };
      jsonData.push(inputData);
    }
  }
  const jsonDataToString = JSON.stringify(jsonData);
  fs.writeFileSync("./dataToJSon.json", jsonDataToString);
});

const readJsFile = require('read-json-file/node')
fs.readFile('dataToJSon.json').then((rows) => {

  console.log(rows)

  // // Crawling
  // const axios = require("axios");
  // const cheerio = require("cheerio");
  // const log = console.log;

  // for (let i = 0; i< data.length; i++) {
  // const getHtml = async () => {
  //   try {
  //     return await axios.get("https://www.domecall.net/goods/goods_view.php?goodsNo="+data.itemCode);
  //   } catch (error) {
  //     console.error(error);
  //   }
  // };

  // getHtml()
  //   .then(html => {
  //     let ulList = 0;
  //     const $ = cheerio.load(html.data);
  //     const $bodyList = $("#frmView > div > div.item").children("div.item > ul");

  //     $bodyList.each(function(elem) {
  //       ulList = {
  //           price: $(this).find('li.price > div > strong').text(),
  //           bacode: $(this).find('ul > li:nth-child(2) > div').text(),
  //           productCode: $(this).find('ul > li:nth-child(3) > div').text(),
  //           origin: $(this).find('ul > li:nth-child(4) > div').text(),
  //           bigBoxCount: $(this).find('ul > li:nth-child(5) > div > span').text(),
  //           smallBoxCount: $(this).find('ul > li:nth-child(6) > div > span').text()
  //       };
  //     });

  //     const data = ulList;
  //     return data;
  //   })
  //   .then(res => log(res));
  // };
})