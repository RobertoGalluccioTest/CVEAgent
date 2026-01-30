from fastapi import FastAPI, UploadFile, File
import agent
import tempfile, os

app = FastAPI()

@app.post("/process")
async def process(pdf: UploadFile = File(...), mapping_csv: UploadFile = File(...)):
    """Process input files

    Args:
        pdf (UploadFile, optional): The pdf file to be read. Defaults to File(...).
        mapping_csv (UploadFile, optional): the CSV asset/squad mapping file in CSV format. Defaults to File(...).

    Returns:
        _type_: _description_
    """
    with tempfile.TemporaryDirectory() as tmp:
        pdf_path = os.path.join(tmp, pdf.filename)
        csv_path = os.path.join(tmp, mapping_csv.filename)
        out_path = os.path.join(tmp, "output.csv")

        with open(pdf_path, "wb") as f:
            f.write(await pdf.read())
        with open(csv_path, "wb") as f:
            f.write(await mapping_csv.read())

        await agent.run({
            "pdf_path": pdf_path,
            "mapping_csv": csv_path,
            "output_path": out_path
        })

        return {"output": out_path}
