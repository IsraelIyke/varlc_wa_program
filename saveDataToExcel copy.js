const fs = require("fs");
const pdf = require("pdf-parse");
const ObjectsToCsv = require("objects-to-csv");

function parsePdf(filePath) {
  return new Promise((resolve, reject) => {
    const dataBuffer = fs.readFileSync(filePath);
    pdf(dataBuffer)
      .then((data) => {
        resolve(data.text);
      })
      .catch((err) => {
        reject(err);
      });
  });
}

const pdfPath = "admission_list.pdf";

// Call the parsePdf function
parsePdf(pdfPath)
  .then((text) => {
    fs.readdir("saved/1", (err, files) => {
      if (err) {
        console.error("Error reading folder:", err);
        return;
      }

      // Print the file names

      // Function to extract data from a PDF file and return an object
      async function extractDataFromPDF(pdfPath) {
        let dataBuffer = fs.readFileSync(pdfPath);
        let data = await pdf(dataBuffer);

        let originalString = data.text;
        let phoneU = originalString.split("phone")[1];
        let phoneL = phoneU.split("Country")[0].trim();
        let emailU = originalString.split("address")[1];
        let emailL = emailU.split("Mobile")[0].trim();

        const fileNameWithoutExtension2 = pdfPath.replace(".pdf", "");
        const fileNameWithoutExtension = fileNameWithoutExtension2.replace(
          "./saved/1/",
          ""
        );
        let targetIdentifier = fileNameWithoutExtension;
        let index = text.indexOf(targetIdentifier);

        let substring = text.substring(index);
        let words = substring.split(" ");
        let extractedWords = words.slice(1, 10).join(" ").split("2023")[0];
        let splitWords = extractedWords.split(" ");

        splitWords.splice(-1);

        let Department = undefined;
        const Name = splitWords.slice(0, 3);

        const num = Number(splitWords[splitWords.length - 1]);
        if (!isNaN(num)) {
          Department = splitWords.slice(3, -1);
        } else {
          Department = splitWords.slice(3);
        }

        let nameStr = Name.join(" ");
        let departmentStr = Department.join(" ");

        return {
          Name: nameStr,
          Department: departmentStr,
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

        for (let i = 0; i < files.length; i++) {
          const fileNameWithoutExtension = files[i].replace(".pdf", "");

          const pdfPath = `./saved/1/${fileNameWithoutExtension}.pdf`;
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
  })
  .catch((err) => {
    console.error("Error parsing PDF:", err);
  });
