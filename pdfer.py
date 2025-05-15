import PyPDF2
import os

def read_pdf(file_path):
    """
    Read and parse a PDF file
    Args:
        file_path (str): Path to the PDF file
    Returns:
        str: Extracted text from the PDF
    """
    try:
        # Check if file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"PDF file not found at {file_path}")
            
        # Open the PDF file
        with open(file_path, 'rb') as file:
            # Create PDF reader object
            pdf_reader = PyPDF2.PdfReader(file)
            
            # Get total number of pages
            num_pages = len(pdf_reader.pages)
            
            # Extract text from all pages
            text = ""
            for page_num in range(num_pages):
                # Get page object
                page = pdf_reader.pages[page_num]
                # Extract text from page
                text += page.extract_text()
                
            return text
            
    except Exception as e:
        print(f"Error reading PDF: {str(e)}")
        return None

# Example usage
if __name__ == "__main__":
    pdf_path = r"C:\Users\todd\Downloads\15620.pdf"  # Replace with your PDF file path
    pdf_text = read_pdf(pdf_path)
    
    if pdf_text:
        print("PDF content:")
        print(pdf_text)
    else:
        print("Failed to read PDF file")
