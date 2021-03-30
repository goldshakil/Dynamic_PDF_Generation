from fpdf import FPDF
from datetime import datetime, timedelta
import os

WIDTH = 210
HEIGHT = 297


def create_report(patient_name, interp_date, study_date, patient_code, interp_dr, sex, dob, height, weight, bmi, recording_time, monitoring_time, ahi, odi, mean_spo2, min_spo2, mean_heart_rate, diagnosis):
    pdf = FPDF()
    pdf.set_left_margin(margin=25)
    pdf.set_right_margin(margin=25)

    # First Page
    pdf.add_page()

    pdf.image('resources/logo.png',
              x=(WIDTH-150)/2, y=2, w=150, type='PNG')
    pdf.ln(20)

    pdf.set_font(family='Arial', style='B', size=10)
    pdf.multi_cell(
        w=0, h=4, txt='1060 S. Main St., Suite 301A\nSt. George, UT 84770\n(855) 276-3263', align='C')
    pdf.ln(5)

    pdf.set_font(family='Arial', style='', size=10)
    pdf.cell(w=0, h=4, txt='HOME SLEEP TEST ANALYSIS REPORT', align='L', ln=1)
    pdf.ln(5)

    pdf.cell(w=(WIDTH-2*25)/2, h=4,
             txt=f'Patient Name: {patient_name}', align='L')
    pdf.cell(w=(WIDTH-2*25)/2, h=4,
             txt=f'Sex: {sex}', align='L', ln=1)
    pdf.cell(w=(WIDTH-2*25)/2, h=4,
             txt=f'Interp. Date: {interp_date}', align='L')
    pdf.cell(w=(WIDTH-2*25)/2, h=4,
             txt=f'DOB: {dob}', align='L', ln=1)
    pdf.cell(w=(WIDTH-2*25)/2, h=4,
             txt=f'Study Date: {study_date}', align='L')
    pdf.cell(w=(WIDTH-2*25)/2, h=4,
             txt=f'Height: {height} in.', align='L', ln=1)
    pdf.cell(w=(WIDTH-2*25)/2, h=4,
             txt=f'Patient Code: {patient_code}', align='L')
    pdf.cell(w=(WIDTH-2*25)/2, h=4,
             txt=f'Weight: {weight} lbs.', align='L', ln=1)
    pdf.cell(w=(WIDTH-2*25)/2, h=4,
             txt=f'Interp Physician: {interp_dr}', align='L')
    pdf.cell(w=(WIDTH-2*25)/2, h=4,
             txt=f'BMI: {bmi}', align='L', ln=1)
    pdf.ln(5)

    pdf.set_font(family='Arial', style='', size=9)
    pdf.multi_cell(
        w=0, h=4, txt='Test Sibel underwent a home sleep diagnostic study on 8/26/2019 investigating the possibility of obstructive sleep apnea. The study was conducted utilizing the Respironics Alice NightOne device. Raw data from the NightOne study was reviewed.')
    pdf.ln(5)

    pdf.cell(w=0, h=4, txt='Summary of Findings:', align='L', ln=1)
    pdf.ln(2)

    pdf.set_font(family='Arial', style='', size=10)
    pdf.cell(w=(WIDTH-2*25)/2, h=4,
             txt=f'Study Date: {study_date}', align='L')
    pdf.cell(w=(WIDTH-2*25)/2, h=4,
             txt=f'ODI: {odi}', align='L', ln=1)
    pdf.cell(w=(WIDTH-2*25)/2, h=4,
             txt=f'Recording Time (min): {recording_time}', align='L')
    pdf.cell(w=(WIDTH-2*25)/2, h=4,
             txt=f'Mean Sp02 Sat: {mean_spo2}%', align='L', ln=1)
    pdf.cell(w=(WIDTH-2*25)/2, h=4,
             txt=f'Monitoring Time (min): {monitoring_time}', align='L')
    pdf.cell(w=(WIDTH-2*25)/2, h=4,
             txt=f'Min. Sp02 Desat: {min_spo2}%', align='L', ln=1)
    pdf.cell(w=(WIDTH-2*25)/2, h=4,
             txt=f'AHI: {ahi}', align='L')
    pdf.cell(w=(WIDTH-2*25)/2, h=4,
             txt=f'Mean Heart Rate: {mean_heart_rate}', align='L', ln=1)
    pdf.ln(3)

    pdf.set_font(family='Arial', style='', size=9)
    pdf.multi_cell(
        w=0, h=4, txt='AHI=Apneas + Hypopneas per hour of sleep. All apneas and hypopneas must be at least 10 seconds in duration and have a minimum of 4% associated desaturation. AHI calculated using Remmers Respiratory Disturbance Index.ODI=Oxygen desaturation of at least 4% from baseline per hour of sleep')
    pdf.ln(5)

    pdf.cell(w=18, h=4,
             txt='Diagnosis: ', align='L')
    pdf.set_font(family='Arial', style='B', size=10)
    pdf.cell(w=(WIDTH-2*25-18), h=4,
             txt=f'{diagnosis}', align='L', ln=1)

    # Second Page
    # Output
    pdf.output('sibel-report.pdf', 'F')


if __name__ == '__main__':
    create_report(patient_name='Dahab Shakeel', interp_date='9/3/2019', study_date='8/26/2019', patient_code='TS082619',
                  interp_dr='Chandra Matadeen-Ali, MD', sex='M', dob='10/23/1998', height=184, weight=72, bmi=21.3, recording_time=406.3, monitoring_time=400.8, ahi=35.2, odi=42.3, mean_spo2=92, min_spo2=74, mean_heart_rate=77.5, diagnosis='Severe Obstructive Sleep Apnea (G47.33)')
