from fpdf import FPDF

WIDTH = 210
HEIGHT = 297
SIGN_LOCATION_Y = 243
LEFT_MARGIN = 25
RIGHT_MARGIN = 25
MARGIN = LEFT_MARGIN+RIGHT_MARGIN
REMAINING_WIDTH = WIDTH-MARGIN


class recommendation:
    def __init__(self, recommendation_data):
        self.recommendation_data = recommendation_data
        self.sub_list = []

    def add_sub_list(self, sub_list_data):
        self.sub_list.append(sub_list_data)


def create_report(patient_name, interp_date, study_date, patient_code, interp_dr, sex, dob, height, weight, bmi, recording_time, monitoring_time, ahi, odi, mean_spo2, min_spo2, mean_heart_rate, diagnosis, recommendations, age, lights_off_time, lights_on_time, bed_time, oai, cai):
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

    pdf.cell(w=(REMAINING_WIDTH)/2, h=4,
             txt=f'Patient Name: {patient_name}', align='L')
    pdf.cell(w=(REMAINING_WIDTH)/2, h=4,
             txt=f'Sex: {sex}', align='L', ln=1)
    pdf.cell(w=(REMAINING_WIDTH)/2, h=4,
             txt=f'Interp. Date: {interp_date}', align='L')
    pdf.cell(w=(REMAINING_WIDTH)/2, h=4,
             txt=f'DOB: {dob}', align='L', ln=1)
    pdf.cell(w=(REMAINING_WIDTH)/2, h=4,
             txt=f'Study Date: {study_date}', align='L')
    pdf.cell(w=(REMAINING_WIDTH)/2, h=4,
             txt=f'Height: {height} in.', align='L', ln=1)
    pdf.cell(w=(REMAINING_WIDTH)/2, h=4,
             txt=f'Patient Code: {patient_code}', align='L')
    pdf.cell(w=(REMAINING_WIDTH)/2, h=4,
             txt=f'Weight: {weight} lbs.', align='L', ln=1)
    pdf.cell(w=(REMAINING_WIDTH)/2, h=4,
             txt=f'Interp Physician: {interp_dr}', align='L')
    pdf.cell(w=(REMAINING_WIDTH)/2, h=4,
             txt=f'BMI: {bmi}', align='L', ln=1)
    pdf.ln(5)

    pdf.set_font(family='Arial', style='', size=9)
    pdf.multi_cell(
        w=0, h=4, txt='Test Sibel underwent a home sleep diagnostic study on 8/26/2019 investigating the possibility of obstructive sleep apnea. The study was conducted utilizing the Respironics Alice NightOne device. Raw data from the NightOne study was reviewed.')
    pdf.ln(5)

    pdf.cell(w=0, h=4, txt='Summary of Findings:', align='L', ln=1)
    pdf.ln(2)

    pdf.set_font(family='Arial', style='', size=10)
    pdf.cell(w=(REMAINING_WIDTH)/2, h=4,
             txt=f'Study Date: {study_date}', align='L')
    pdf.cell(w=(REMAINING_WIDTH)/2, h=4,
             txt=f'ODI: {odi}', align='L', ln=1)
    pdf.cell(w=(REMAINING_WIDTH)/2, h=4,
             txt=f'Recording Time (min): {recording_time}', align='L')
    pdf.cell(w=(REMAINING_WIDTH)/2, h=4,
             txt=f'Mean Sp02 Sat: {mean_spo2}%', align='L', ln=1)
    pdf.cell(w=(REMAINING_WIDTH)/2, h=4,
             txt=f'Monitoring Time (min): {monitoring_time}', align='L')
    pdf.cell(w=(REMAINING_WIDTH)/2, h=4,
             txt=f'Min. Sp02 Desat: {min_spo2}%', align='L', ln=1)
    pdf.cell(w=(REMAINING_WIDTH)/2, h=4,
             txt=f'AHI: {ahi}', align='L')
    pdf.cell(w=(REMAINING_WIDTH)/2, h=4,
             txt=f'Mean Heart Rate: {mean_heart_rate}', align='L', ln=1)
    pdf.ln(3)

    pdf.set_font(family='Arial', style='', size=9)
    pdf.multi_cell(
        w=0, h=4, txt='AHI=Apneas + Hypopneas per hour of sleep. All apneas and hypopneas must be at least 10 seconds in duration and have a minimum of 4% associated desaturation. AHI calculated using Remmers Respiratory Disturbance Index.ODI=Oxygen desaturation of at least 4% from baseline per hour of sleep')
    pdf.ln(5)

    pdf.cell(w=18, h=4,
             txt='Diagnosis: ', align='L')
    pdf.set_font(family='Arial', style='B', size=10)
    pdf.cell(w=(REMAINING_WIDTH-18), h=4,
             txt=f'{diagnosis}', align='L', ln=1)
    pdf.ln(5)

    pdf.set_font(family='Arial', style='', size=9)
    pdf.cell(w=0, h=4, txt='Recommendations: ', align='L')
    pdf.ln(4)

    for i in recommendations:
        pdf.cell(w=8, h=4,
                 txt='  -', align='L')
        pdf.multi_cell(w=(REMAINING_WIDTH-18), h=4,
                       txt=i.recommendation_data)
        for j in i.sub_list:
            pdf.cell(w=8, h=4, align='L')
            pdf.cell(w=8, h=4, txt='  -', align='L')
            pdf.multi_cell(w=(REMAINING_WIDTH-18), h=4, txt=j)
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

    # Second Page
    pdf.add_page()

    pdf.image('resources/philips-logo.png',
              x=LEFT_MARGIN, y=10, w=60, type='PNG')
    pdf.ln(15)

    pdf.set_font(family='Arial', style='B', size=20)
    pdf.cell(w=60, h=4)
    pdf.cell(w=120, h=10, txt='Sleep Test Report', align='C', ln=1)
    pdf.ln(5)

    pdf.set_font(family='Arial', style='B', size=10)  # Table Header
    pdf.set_draw_color(r=0, g=102, b=204)
    pdf.set_fill_color(r=213, g=227, b=187)
    pdf.cell(w=100, h=7, align='L', border=1, fill=True)
    pdf.cell(w=REMAINING_WIDTH-100, h=7,
             txt=f'Study Date: {study_date}', align='L', border=1, fill=True, ln=1)

    pdf.set_font(family='Arial', style='B', size=10)  # Row 1
    pdf.cell(w=20, h=5, txt='Patient', align='L', border=1)
    pdf.set_font(family='Arial', style='', size=10)
    pdf.cell(w=60, h=5, txt=f'{patient_name}', align='L', border=1)
    pdf.set_font(family='Arial', style='B', size=10)
    pdf.cell(w=20, h=5, txt='Recording', align='L', border=1)
    pdf.set_font(family='Arial', style='', size=10)
    pdf.cell(w=60, h=5, txt='Alice NightOne', align='L', border=1, ln=1)

    pdf.set_font(family='Arial', style='B', size=10)  # Row 2
    pdf.cell(w=20, h=5, txt='Sex', align='L', border=1)
    pdf.set_font(family='Arial', style='', size=10)
    pdf.cell(w=60, h=5, txt=f'{sex}', align='L', border=1)
    pdf.set_font(family='Arial', style='B', size=10)
    pdf.cell(w=20, h=5, txt='Height', align='L', border=1)
    pdf.set_font(family='Arial', style='', size=10)
    pdf.cell(w=60, h=5, txt=f'{height} in.', align='L', border=1, ln=1)

    pdf.set_font(family='Arial', style='B', size=10)  # Row 3
    pdf.cell(w=20, h=5, txt='DOB', align='L', border=1)
    pdf.set_font(family='Arial', style='', size=10)
    pdf.cell(w=60, h=5, txt=f'{dob}', align='L', border=1)
    pdf.set_font(family='Arial', style='B', size=10)
    pdf.cell(w=20, h=5, txt='Weight', align='L', border=1)
    pdf.set_font(family='Arial', style='', size=10)
    pdf.cell(w=60, h=5, txt=f'{weight} lbs.', align='L', border=1, ln=1)

    pdf.set_font(family='Arial', style='B', size=10)  # Row 4
    pdf.cell(w=20, h=5, txt='Age', align='L', border=1)
    pdf.set_font(family='Arial', style='', size=10)
    pdf.cell(w=60, h=5, txt=f'{age} years', align='L', border=1)
    pdf.set_font(family='Arial', style='B', size=10)
    pdf.cell(w=20, h=5, txt='BMI', align='L', border=1)
    pdf.set_font(family='Arial', style='', size=10)
    pdf.cell(w=60, h=5, txt=f'{bmi}', align='L', border=1, ln=1)
    pdf.ln(5)

    pdf.set_font(family='Arial', style='B', size=10)  # Table-2 Header
    pdf.cell(w=REMAINING_WIDTH, h=7, txt='Times and Durations',
             align='L', border=1, fill=True, ln=1)

    pdf.set_font(family='Arial', style='B', size=10)  # Row 1
    pdf.cell(w=40, h=5, txt='Lights off clock time', align='L', border=1)
    pdf.set_font(family='Arial', style='', size=10)
    pdf.cell(w=40, h=5, txt=f'{lights_off_time}', align='L', border=1)
    pdf.set_font(family='Arial', style='B', size=10)
    pdf.cell(w=40, h=5, txt='Total Time Recording', align='L', border=1)
    pdf.set_font(family='Arial', style='', size=10)
    pdf.cell(w=40, h=5, txt=f'{recording_time} minutes',
             align='L', border=1, ln=1)

    pdf.set_font(family='Arial', style='B', size=10)  # Row 2
    pdf.cell(w=40, h=5, txt='Lights on clock time', align='L', border=1)
    pdf.set_font(family='Arial', style='', size=10)
    pdf.cell(w=40, h=5, txt=f'{lights_on_time}', align='L', border=1)
    pdf.set_font(family='Arial', style='B', size=10)
    pdf.cell(w=40, h=5, txt='Time In Bed', align='L', border=1)
    pdf.set_font(family='Arial', style='', size=10)
    pdf.cell(w=40, h=5, txt=f'{bed_time} minutes',
             align='L', border=1, ln=1)

    pdf.set_font(family='Arial', style='B', size=10)  # Row 3
    pdf.cell(w=40, h=5, txt='', align='L', border=1)
    pdf.set_font(family='Arial', style='', size=10)
    pdf.cell(w=40, h=5, txt='', align='L', border=1)
    pdf.set_font(family='Arial', style='B', size=10)
    pdf.cell(w=40, h=5, txt='Monitoring Time', align='L', border=1)
    pdf.set_font(family='Arial', style='', size=10)
    pdf.cell(w=40, h=5, txt=f'{monitoring_time} minutes',
             align='L', border=1, ln=1)
    pdf.ln(5)

    pdf.set_font(family='Arial', style='B', size=10)  # Table-3 Header
    pdf.cell(w=REMAINING_WIDTH, h=7, txt='Device and Sensor Details',
             align='L', border=1, fill=True, ln=1)

    pdf.set_font(family='Arial', style='', size=10)  # Row 1
    pdf.multi_cell(
        w=REMAINING_WIDTH, h=4, txt='The study was recorded on a Philips Respironics Alice NightOne device using 1 RIP effort belt and a pressure based flow sensor. The heart rate is derived from the oximeter sensor and the snore signal is derived from the pressure sensor. The device also records body position and uses it to determine the monitoring time(sleep/wake periods).', align='', border=1)
    pdf.ln(5)

    pdf.set_font(family='Arial', style='B', size=10)  # Table-4 Header
    pdf.cell(w=REMAINING_WIDTH, h=7, txt='Summary',
             align='L', border=1, fill=True, ln=1)

    pdf.set_fill_color(r=250, g=191, b=143)
    pdf.cell(w=20, h=6, txt='AHI', align='C', border=1)  # Row 1
    pdf.cell(w=20, h=6, txt=f'{ahi}', align='C', border=1, fill=True)
    pdf.cell(w=20, h=6, txt='OAI', align='C', border=1)
    pdf.cell(w=20, h=6, txt=f'{oai}', align='C', border=1, fill=True)
    pdf.cell(w=20, h=6, txt='CAI', align='C', border=1)
    pdf.cell(w=20, h=6, txt=f'{cai}', align='C', border=1, fill=True)
    pdf.cell(w=20, h=6, txt='Min Desat', align='C', border=1)
    pdf.cell(w=20, h=6, txt=f'{min_spo2}',
             align='C', border=1, fill=True, ln=1)

    pdf.set_font(family='Arial', style='', size=8.5)
    pdf.set_text_color(r=107, g=107, b=107)
    pdf.multi_cell(
        w=REMAINING_WIDTH, h=4, txt='AHI is the number of respiratory events per hour. OAI is the number of obstructive apneas per hour. CAI is the number of central apneas per hour. Lowest Desat is the lowest blood oxygen level that lasted at least 2 seconds.', align='', )
    pdf.ln(5)

    pdf.set_text_color(r=0, g=0, b=0)  # Table 5 - Header
    pdf.set_fill_color(r=213, g=227, b=187)
    pdf.set_font(family='Arial', style='B', size=10)
    pdf.cell(w=REMAINING_WIDTH, h=7, txt='Respiratory Events',
             align='L', border=1, fill=True, ln=1)
    temp_y = pdf.get_y()

    pdf.set_font(family='Arial', style='B', size=8)  # Row 1
    pdf.cell(w=30, h=12, txt='', align='C', border=1)
    temp_x = pdf.get_x()
    pdf.multi_cell(w=15, h=6, txt='Index (#/hour)', align='C', border=1)
    pdf.set_y(temp_y)
    pdf.set_x(temp_x+15)
    temp_x = pdf.get_x()
    pdf.multi_cell(w=15, h=6, txt='Total # of Events', align='C', border=1)
    pdf.set_y(temp_y)
    pdf.set_x(temp_x+15)
    temp_x = pdf.get_x()
    pdf.multi_cell(w=15, h=6, txt='Mean Duration', align='C', border=1)
    pdf.set_y(temp_y)
    pdf.set_x(temp_x+15)
    temp_x = pdf.get_x()
    pdf.multi_cell(w=15, h=6, txt='Max Duration', align='C', border=1)
    pdf.set_y(temp_y)
    pdf.set_x(temp_x+15)
    pdf.cell(w=70, h=4, txt='# of Events by Position',
             align='C', border=1, ln=1)
    pdf.set_y(temp_y+4)
    pdf.set_x(temp_x+15)
    pdf.cell(w=14, h=8, txt='Supine', align='C', border=1)
    pdf.cell(w=14, h=8, txt='Prone', align='C', border=1)
    pdf.cell(w=14, h=8, txt='Left', align='C', border=1)
    pdf.cell(w=14, h=8, txt='Right', align='C', border=1)
    pdf.cell(w=14, h=8, txt='Up', align='C', border=1, ln=1)

    pdf.set_font(family='Arial', style='B', size=8)  # Row 2
    pdf.cell(w=30, h=6, txt='Central Apneas', align='L', border=1)
    pdf.set_font(family='Arial', style='', size=8)
    pdf.cell(w=15, h=6, txt='4.3', align='C', border=1)
    pdf.cell(w=15, h=6, txt='29', align='C', border=1)
    pdf.cell(w=15, h=6, txt='21.7', align='C', border=1)
    pdf.cell(w=15, h=6, txt='127', align='C', border=1)
    pdf.cell(w=14, h=6, txt='1', align='C', border=1)
    pdf.cell(w=14, h=6, txt='3', align='C', border=1)
    pdf.cell(w=14, h=6, txt='2', align='C', border=1)
    pdf.cell(w=14, h=6, txt='23', align='C', border=1)
    pdf.cell(w=14, h=6, txt='0', align='C', border=1, ln=1)

    pdf.set_font(family='Arial', style='B', size=8)  # Row 3
    pdf.cell(w=30, h=6, txt='Constructive Apneas', align='L', border=1)
    pdf.set_font(family='Arial', style='', size=8)
    pdf.cell(w=15, h=6, txt='4.3', align='C', border=1)
    pdf.cell(w=15, h=6, txt='29', align='C', border=1)
    pdf.cell(w=15, h=6, txt='21.7', align='C', border=1)
    pdf.cell(w=15, h=6, txt='127', align='C', border=1)
    pdf.cell(w=14, h=6, txt='1', align='C', border=1)
    pdf.cell(w=14, h=6, txt='3', align='C', border=1)
    pdf.cell(w=14, h=6, txt='2', align='C', border=1)
    pdf.cell(w=14, h=6, txt='23', align='C', border=1)
    pdf.cell(w=14, h=6, txt='0', align='C', border=1, ln=1)

    pdf.set_font(family='Arial', style='B', size=8)  # Row 4
    pdf.cell(w=30, h=6, txt='Mixed Apneas', align='L', border=1)
    pdf.set_font(family='Arial', style='', size=8)
    pdf.cell(w=15, h=6, txt='4.3', align='C', border=1)
    pdf.cell(w=15, h=6, txt='29', align='C', border=1)
    pdf.cell(w=15, h=6, txt='21.7', align='C', border=1)
    pdf.cell(w=15, h=6, txt='127', align='C', border=1)
    pdf.cell(w=14, h=6, txt='1', align='C', border=1)
    pdf.cell(w=14, h=6, txt='3', align='C', border=1)
    pdf.cell(w=14, h=6, txt='2', align='C', border=1)
    pdf.cell(w=14, h=6, txt='23', align='C', border=1)
    pdf.cell(w=14, h=6, txt='0', align='C', border=1, ln=1)

    pdf.set_font(family='Arial', style='B', size=8)  # Row 5
    pdf.cell(w=30, h=6, txt='Hypoapneas', align='L', border=1)
    pdf.set_font(family='Arial', style='', size=8)
    pdf.cell(w=15, h=6, txt='4.3', align='C', border=1)
    pdf.cell(w=15, h=6, txt='29', align='C', border=1)
    pdf.cell(w=15, h=6, txt='21.7', align='C', border=1)
    pdf.cell(w=15, h=6, txt='127', align='C', border=1)
    pdf.cell(w=14, h=6, txt='1', align='C', border=1)
    pdf.cell(w=14, h=6, txt='3', align='C', border=1)
    pdf.cell(w=14, h=6, txt='2', align='C', border=1)
    pdf.cell(w=14, h=6, txt='23', align='C', border=1)
    pdf.cell(w=14, h=6, txt='0', align='C', border=1, ln=1)

    pdf.set_font(family='Arial', style='B', size=8)  # Row 6
    pdf.cell(w=30, h=6, txt='RERAs', align='L', border=1)
    pdf.set_font(family='Arial', style='', size=8)
    pdf.cell(w=15, h=6, txt='4.3', align='C', border=1)
    pdf.cell(w=15, h=6, txt='29', align='C', border=1)
    pdf.cell(w=15, h=6, txt='21.7', align='C', border=1)
    pdf.cell(w=15, h=6, txt='127', align='C', border=1)
    pdf.cell(w=14, h=6, txt='1', align='C', border=1)
    pdf.cell(w=14, h=6, txt='3', align='C', border=1)
    pdf.cell(w=14, h=6, txt='2', align='C', border=1)
    pdf.cell(w=14, h=6, txt='23', align='C', border=1)
    pdf.cell(w=14, h=6, txt='0', align='C', border=1, ln=1)

    pdf.set_font(family='Arial', style='B', size=8)  # Row 7
    pdf.cell(w=30, h=6, txt='Total', align='L', border=1)
    pdf.set_font(family='Arial', style='', size=8)
    pdf.cell(w=15, h=6, txt='4.3', align='C', border=1)
    pdf.cell(w=15, h=6, txt='29', align='C', border=1)
    pdf.cell(w=15, h=6, txt='21.7', align='C', border=1)
    pdf.cell(w=15, h=6, txt='127', align='C', border=1)
    pdf.cell(w=14, h=6, txt='1', align='C', border=1)
    pdf.cell(w=14, h=6, txt='3', align='C', border=1)
    pdf.cell(w=14, h=6, txt='2', align='C', border=1)
    pdf.cell(w=14, h=6, txt='23', align='C', border=1)
    pdf.cell(w=14, h=6, txt='0', align='C', border=1, ln=1)

    pdf.set_font(family='Arial', style='B', size=8)  # Row 8
    pdf.cell(w=90, h=6, txt='Time in Position', align='L', border=1)
    pdf.set_font(family='Arial', style='', size=8)
    pdf.cell(w=14, h=6, txt='1', align='C', border=1)
    pdf.cell(w=14, h=6, txt='3', align='C', border=1)
    pdf.cell(w=14, h=6, txt='2', align='C', border=1)
    pdf.cell(w=14, h=6, txt='23', align='C', border=1)
    pdf.cell(w=14, h=6, txt='0', align='C', border=1, ln=1)

    pdf.set_font(family='Arial', style='B', size=8)  # Row 9
    pdf.cell(w=90, h=6, txt='Position', align='L', border=1)
    pdf.cell(w=14, h=6, txt='1', align='C', border=1)
    pdf.cell(w=14, h=6, txt='3', align='C', border=1)
    pdf.cell(w=14, h=6, txt='2', align='C', border=1)
    pdf.cell(w=14, h=6, txt='23', align='C', border=1)
    pdf.cell(w=14, h=6, txt='0', align='C', border=1, ln=1)

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
                  interp_dr='Chandra Matadeen-Ali, MD', sex='M', dob='10/23/1998', height=184, weight=160, bmi=21.3, recording_time=406.3, monitoring_time=400.8, ahi=35.2, odi=42.3, mean_spo2=92, min_spo2=74, mean_heart_rate=77.5, diagnosis='Severe Obstructive Sleep Apnea (G47.33)', recommendations=recommendation_list, age=22, lights_off_time="11:00:25 PM", lights_on_time="5:46:43 AM", bed_time=406.3, oai=15.3, cai=4.3)
