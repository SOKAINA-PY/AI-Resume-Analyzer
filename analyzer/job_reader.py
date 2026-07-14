from analyzer.pdf_reader import extract_text


def extract_job_description(pdf_file):
    """
    Extract text from the uploaded Job Description PDF.
    """
    return extract_text(pdf_file)