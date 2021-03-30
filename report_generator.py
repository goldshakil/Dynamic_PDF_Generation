from fpdf import FPDF

WIDTH = 210
HEIGHT = 297
SIGN_LOCATION_Y = 243


class recommendation:
    def __init__(self, recommendation_data):
        self.recommendation_data = recommendation_data
        self.sub_list = []

    def add_sub_list(self, sub_list_data):
        self.sub_list.append(sub_list_data)


def create_report(patient_name, interp_date, study_date, patient_code, interp_dr, sex, dob, height, weight, bmi, recording_time, monitoring_time, ahi, odi, mean_spo2, min_spo2, mean_heart_rate, diagnosis, recommendations):
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
    pdf.ln(5)

    pdf.set_font(family='Arial', style='', size=9)
    pdf.cell(w=0, h=4, txt='Recommendations: ', align='L')
    pdf.ln(4)

    for i in recommendations:
        pdf.cell(w=8, h=4,
                 txt='  -', align='L')
        pdf.multi_cell(w=(WIDTH-2*25-18), h=4,
                       txt=i.recommendation_data)
        for j in i.sub_list:
            pdf.cell(w=8, h=4, align='L')
            pdf.cell(w=8, h=4, txt='  -', align='L')
            pdf.multi_cell(w=(WIDTH-2*25-18), h=4, txt=j)
        pdf.ln(2)
    pdf.ln(2)

    pdf.multi_cell(
        w=0, h=4, txt='Clinical follow-up as deemed necessary would be appropriate. Patient should be advised on the long term consequences of OSA if left untreated, need for treatment, and close follow up. Retesting or follow up is recommended to ensure the apnea is controlled and the symptoms are relieved on the chosen therapy. ')
    pdf.ln(5)

    pdf.multi_cell(
        w=0, h=4, txt='Untreated obstructive sleep apnea is associated with hypertension, heart disease, stroke, daytime sleepiness, cognitive dysfunction, mood disorders and sudden death.')
    pdf.ln(5)

    pdf.ln(SIGN_LOCATION_Y-pdf.get_y())
    pdf.cell(w=50, h=4, txt="Sincerely,", align='L')
    pdf.image('resources/sign.png',
              x=20, y=SIGN_LOCATION_Y+5, w=60, type='PNG')
    pdf.ln(20)
    pdf.multi_cell(
        w=0, h=4, txt=f'Dr.{interp_dr}\nDiplomate ABIM-Sleep Medicine\nElectronically Signed')
    pdf.ln(5)

    # Second Page

    # Third Page

    # Output
    pdf.output('sibel-report.pdf', 'F')


if __name__ == '__main__':

    recommendation1 = recommendation('Consider nasal continuous positive airway pressure (CPAP) as the initial treatment choice for obstructive sleep apnea. If the patient chooses CPAP therapy, a nocturnal PSG with CPAP titration is recommended. As an alternative, an Auto PAP with pressure range 5-20 cmH20 with download is an option. Consider follow up overnight pulse oximetry test on Auto PAP therapy after OSA is controlled. Consider PAP interface (mask) fitted for patient comfort, heated humidification & PAP compliance monitoring (1month, 3 months & 12 months after PAP initiation).')

    recommendation2 = recommendation(
        'Positive airway pressure therapy (PAP) is the first line of treatment for patients with OSA. Alternative treatment for OSA in patients who cannot tolerate and have failed or refused CPAP therapy includes:')
    recommendation2.add_sub_list(
        'The patient may benefit from the use of a nocturnal mandibular repositioning appliance. If that line of therapy is to be pursued, the patient should be evaluated by a dentist trained in the treatment of sleep related breathing disorders.')
    recommendation2.add_sub_list(
        'An ENT consultation which may be useful to look for specific causes of obstruction and possible treatment options.')

    recommendation_list = []
    recommendation_list.append(recommendation1)
    recommendation_list.append(recommendation2)

    create_report(patient_name='Dahab Shakeel', interp_date='9/3/2019', study_date='8/26/2019', patient_code='TS082619',
                  interp_dr='Chandra Matadeen-Ali, MD', sex='M', dob='10/23/1998', height=184, weight=72, bmi=21.3, recording_time=406.3, monitoring_time=400.8, ahi=35.2, odi=42.3, mean_spo2=92, min_spo2=74, mean_heart_rate=77.5, diagnosis='Severe Obstructive Sleep Apnea (G47.33)', recommendations=recommendation_list)
