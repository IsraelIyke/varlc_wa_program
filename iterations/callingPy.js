const { spawn } = require("child_process");

const childpython = spawn("python", ["theScript.py"]);

let resultString = "";

childpython.stdout.on("data", function (stdData) {
  resultString += stdData.toString();
});

childpython.stdout.on("end", function () {
  // Parse the string as JSON when stdout
  let resultData = JSON.parse(resultString);
  console.log(resultData);
});
