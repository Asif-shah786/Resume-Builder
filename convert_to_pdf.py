from weasyprint import HTML, CSS
import os


def convert_html_to_pdf(html_path, output_path):
    """
    Convert HTML file to PDF with professional resume settings for single A4 page
    """
    # Define CSS for page layout
    css = CSS(
        string="""
        @page {
            size: A4;
            margin: 2.54cm;
        }
        body {
            font-family: 'Arial', sans-serif;
            font-size: 10pt;
            line-height: 1.3;
            margin: 0;
            padding: 0;
        }
        .section {
            margin-bottom: 12pt;
        }
        .job {
            margin-bottom: 8pt;
        }
        ul {
            margin: 4pt 0;
            padding-left: 20pt;
        }
        li {
            margin-bottom: 2pt;
        }
        .header {
            margin-bottom: 12pt;
        }
        .contact-info {
            font-size: 10pt;
        }
        .section-title {
            margin-bottom: 8pt;
        }
        .skills {
            margin: 5pt 0;
        }
        .skill-item {
            font-size: 10pt;
            margin: 2pt;
            padding: 3pt 8pt;
        }
    """
    )

    try:
        # Create WeasyPrint HTML object
        html = HTML(filename=html_path)

        # Convert to PDF with CSS
        html.write_pdf(output_path, stylesheets=[css])
        print(f"Successfully converted {html_path} to {output_path}")
    except Exception as e:
        print(f"Error converting to PDF: {str(e)}")


if __name__ == "__main__":
    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Define input and output file paths
    html_file = os.path.join(current_dir, "resume.html")
    output_pdf = os.path.join(current_dir, "Asif_Shah_Resume.pdf")

    # Convert the file
    convert_html_to_pdf(html_file, output_pdf)
