const { spawn } = require("child_process");

const childpython = spawn("python", ["theScript.py"]);

py.stdout.on("data", function (stdData) {
  resultString += stdData.toString();
});

py.stdout.on("end", function () {
  // Parse the string as JSON when stdout
  // data stream ends
  let resultData = JSON.parse(resultString);

  let sum = resultData["sum"];
  console.log("Sum of array from Python process =", sum);
});

childpython.stdout.on("data", (data) => {
  console.log(`stdout: ${data}`);
});

childpython.stderr.on("data", (data) => {
  console.log(`stdout2: ${data}`);
});

childpython.on("close", (code) => {
  console.log(`stdout3: ${code}`);
});
console.log(process.argv[0]);
