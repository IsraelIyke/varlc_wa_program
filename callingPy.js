const { spawn } = require("child_process");

const childpython = spawn("python", ["theScript.py"]);

let resultString = "";

childpython.stdout.on("data", function (stdData) {
  resultString += stdData.toString();
});

childpython.stdout.on("end", function () {
  // Parse the string as JSON when stdout
  // data stream ends
  let resultData = JSON.parse(resultString);

  let sum = resultData["sum"];
  console.log("Sum of array from childpythonthon process =", sum);
});
