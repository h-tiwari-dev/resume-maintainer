from pdflatex import PDFLaTeX
import subprocess
import string


def has_git_changes(fileName: string):
    try:
        subprocess.check_output(["git", "diff", "--exit-code", "--", fileName])
        return False
    except subprocess.CalledProcessError:
        return True


def createPdf():
    pdfl = PDFLaTeX.from_texfile("resume.tex")
    pdfl.set_output_directory("./results")
    pdf, log, completed_process = pdfl.create_pdf(
        keep_pdf_file=True, keep_log_file=False
    )


if __name__ == "__main__":
    createPdf()
