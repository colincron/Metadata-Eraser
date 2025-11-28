import pypdf, click, mimetypes
from PIL import Image

def is_pdf(file_path):
    mime_type, _ = mimetypes.guess_type(file_path)
    return mime_type == 'application/pdf'

def is_jpg(file_path):
    mime_type, _ = mimetypes.guess_type(file_path)
    return mime_type == 'image/jpeg'

def pdf_eraser(file):
    src_pdf = pypdf.PdfReader(file)
    dst_pdf = pypdf.PdfWriter(clone_from=src_pdf)
    dst_pdf.metadata = None
    dst_pdf.write(file)
    print("[+] Metadata removed successfully.")

def jpg_eraser(file):
    img = Image.open(file)
    data = list(img.getdata())
    img_without_metadata = Image.new(img.mode, img.size)
    img_without_metadata.putdata(data)
    img_without_metadata.save(file)
    print("[+] Metadata removed successfully.")

@click.command()
@click.option('--file', prompt='File name', help='Filename')
def metadata_eraser(file):
    if is_pdf(file):
        pdf_eraser(file)
    elif is_jpg(file):
        jpg_eraser(file)

if __name__ == "__main__":
    metadata_eraser()