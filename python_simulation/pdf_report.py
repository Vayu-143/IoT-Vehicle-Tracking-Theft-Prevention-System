from fpdf import FPDF
import pandas as pd


def generate_pdf():

    try:

        df = pd.read_csv(
            "data/vehicle_log.csv"
        )

        pdf = FPDF()

        pdf.add_page()

        pdf.set_font(
            "Arial",
            "B",
            14
        )

        pdf.cell(
            200,
            10,
            "Vehicle Tracking Report",
            ln=True,
            align="C"
        )

        pdf.ln(5)

        pdf.set_font(
            "Arial",
            size=8
        )

        for _, row in df.iterrows():

            line = (
                f"{row['timestamp']} | "
                f"{row['latitude']} | "
                f"{row['longitude']} | "
                f"{row['status']} | "
                f"{row['alert']}"
            )

            pdf.multi_cell(
                0,
                6,
                line
            )

        pdf.output(
            "outputs/vehicle_report.pdf"
        )

    except Exception as e:

        print(
            "PDF Error:",
            e
        )