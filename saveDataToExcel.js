const fs = require("fs");
const pdf = require("pdf-parse");
const ObjectsToCsv = require("objects-to-csv");

const { spawn } = require("child_process");

const childpython = spawn("python", ["theScript.py"]);

let resultString = "";

childpython.stdout.on("data", function (stdData) {
  resultString += stdData.toString();
});

childpython.stdout.on("end", function () {
  // Parse the string as JSON when stdout
  let resultData = JSON.parse(resultString);

  // Function to extract data from a PDF file and return an object
  async function extractDataFromPDF(pdfPath) {
    let dataBuffer = fs.readFileSync(pdfPath);
    let data = await pdf(dataBuffer);

    let originalString = data.text;
    let nameU = originalString.split("Fullname")[1];
    let nameL = nameU.split("Gender")[0].trim();
    let departmentU = originalString.split("Department")[1];
    let departmentL = departmentU.split("JAMB")[0].trim();
    let phoneU = originalString.split("phone")[1];
    let phoneL = phoneU.split("Country")[0].trim();
    let emailU = originalString.split("address")[1];
    let emailL = emailU.split("Mobile")[0].trim();

    return {
      Name: nameL,
      Department: departmentL,
      Phone: `'${phoneL}`,
      Email: emailL,
    };
  }

  // Function to save data array of objects to a CSV file
  async function saveDataToCSV(data, csvPath) {
    const csv = new ObjectsToCsv(data);
    await csv.toDisk(csvPath);
    console.log(`Data saved to ${csvPath}`);
  }

  // Main function to extract data from multiple PDF files
  async function processPDFs(csvPath) {
    let dataArray = [];

    for (let i = 0; i < resultData.length; i++) {
      const pdfPath = `./saved/${resultData[i]}.pdf`;
      let extractedData = await extractDataFromPDF(pdfPath);
      dataArray.push(extractedData);
    }

    await saveDataToCSV(dataArray, csvPath);
  }

  // Path to the CSV file
  const csvPath = "./excel/combined_data.csv";

  // Call the main function to process the PDFs
  processPDFs(csvPath).catch((error) => console.error(error));
});
