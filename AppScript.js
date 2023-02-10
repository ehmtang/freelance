
/**
 * Google AppScript 
 * 
 * Function reads active sheet, column A2:A.
 * Cleans hyperlink and retrieves image from link
 * To be activated upon trigger 'upon opening spreadsheet'
 */
function getImageFromHyperlink() {

    var sheet = SpreadsheetApp.getActiveSheet();
    var numRows = sheet.getLastRow();
    var urls = sheet.getRange("A2:A").getValues();
  
    for (var i = 2; i <= numRows; i++) {
      var cell = sheet.getRange("A" + i);
      var formula = cell.getFormula();
      
      if (!formula) {
        var url = urls[i-2][0];
        if (url && url.startsWith("https://")) {
          var cleanedLink = url.trim().replace(/ /g, "%20");
          cell.setFormula('=IMAGE("' + cleanedLink + '")');
        } else {
          console.log("skip: not start with https")
        }
      } else {
        console.log("skip: is formula")
      }
    }
  }
  
  