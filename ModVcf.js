const fs = require("fs-extra");
const path = require("path");
const pdfParse = require("pdf-parse");
const VCard = require("vcard-creator");
const glob = require("glob"); // Import glob for matching files

// Function to extract text from a PDF file
async function extractTextFromPdf(pdfPath) {
  const dataBuffer = await fs.readFile(pdfPath);
  const pdfData = await pdfParse(dataBuffer);
  return pdfData.text.split(/\s+/); // Split text into words
}

// Function to extract data between specific words
function joinDataBetweenWords(dataArrays, startWord, endWord) {
  try {
    const startIndex = dataArrays.indexOf(startWord) + 1;
    const endIndex = dataArrays.indexOf(endWord);
    return dataArrays.slice(startIndex, endIndex).join(" ");
  } catch (error) {
    return `Error extracting data between '${startWord}' and '${endWord}'`;
  }
}

// Function to create a VCard and save it as a .vcf file
function createVCardAndSave(contactData, outputDir, filename) {
  const vcard = new VCard();
  vcard.add("fn", contactData.Fullname);
  vcard.add("email", contactData.Email);
  vcard.add("tel", contactData.Mobile);
  vcard.add("org", contactData.Faculty);
  vcard.add(
    "note",
    `Gender: ${contactData.Gender}, DOB: ${contactData.DOB}, Department: ${contactData.Department}`
  );

  const vcfContent = vcard.serialize();
  const vcfPath = path.join(outputDir, filename);

  fs.ensureDirSync(outputDir); // Ensure the output directory exists
  fs.writeFileSync(vcfPath, vcfContent, "utf8");
  console.log(`Saved VCF for ${contactData.Fullname} to ${vcfPath}`);
}

async function processPdfFilesInDirectory(directory) {
  const vcfDir = path.join(directory, "vcf_files");
  const subDirectories = await fs.readdir(directory);

  for (const subDir of subDirectories) {
    const subDirPath = path.join(directory, subDir);

    if (fs.lstatSync(subDirPath).isDirectory()) {
      console.log(`Processing directory: ${subDir}`);

      // Use glob to find all PDF files in the subdirectory
      glob(path.join(subDirPath, "*.pdf"), (err, pdfFiles) => {
        if (err) {
          console.error("Error finding PDF files:", err);
          return;
        }

        // Process each PDF file
        pdfFiles.forEach(async (pdfFile) => {
          console.log(`Processing file: ${pdfFile}`);

          // Extract data from the current PDF
          const dataArrays = await extractTextFromPdf(pdfFile);

          // Extract specific information
          const Fullname = joinDataBetweenWords(
            dataArrays,
            "Fullname",
            "Gender"
          );
          const Gender = joinDataBetweenWords(dataArrays, "Gender", "Date");
          const DOB = joinDataBetweenWords(dataArrays, "birth", "State");
          const Email = joinDataBetweenWords(dataArrays, "address", "Mobile");
          const Mobile = joinDataBetweenWords(dataArrays, "phone", "Country");
          const Faculty = joinDataBetweenWords(
            dataArrays,
            "Faculty",
            "Department"
          );
          const Department = joinDataBetweenWords(
            dataArrays,
            "Department",
            "Score"
          );
          const DepartmentTrimmed = Department.slice(0, -5); // Trim last 5 characters if necessary

          // Prepare contact data
          const contactData = {
            Fullname,
            Gender,
            DOB,
            Email,
            Mobile,
            Faculty,
            Department: DepartmentTrimmed,
          };

          // Generate the VCF file
          const filename = `${subDir}_${Fullname.replace(/\s+/g, "_")}.vcf`;
          createVCardAndSave(contactData, vcfDir, filename);
        });
      });
    }
  }
}

const mainDir = "./saved";

processPdfFilesInDirectory(mainDir)
  .then(() => {
    console.log("Processing completed for all subdirectories.");
  })
  .catch((err) => {
    console.error("Error during processing:", err);
  });
