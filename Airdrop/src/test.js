const fs = require('fs');
var res = []
fs.readFile('./airdop_list.csv', 'utf8' , (err, data) => {
    if (err) {
      console.error(err)
      return
    }
    var lines = data.split(',,,\r\n')
    
    for (var i=0,len=lines.length; i<len; i++)
{ 
    var a = lines[i].split(',')  
    var jsonObj = {"address": a[0],  "amount": Number(a[1]) };
    res.push(jsonObj)
}
console.log('module const rawData = '+JSON.stringify(res, null ,2))
var data = new Buffer( 'export const rawData = ' +JSON.stringify(res, null ,2))
fs.writeFile('./rawData.ts',  data, 'utf8', (err, data) => {
  if (err) {
    console.error(err)
    return
  
}
})


  })

 