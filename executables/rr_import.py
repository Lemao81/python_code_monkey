import cmd
import subprocess


class ImportCmd(cmd.Cmd):
    def __init__(self):
        super().__init__()
        self.executable = 'C:\\ProgramData\\RadioReport\\RadioReport.exe'
        self.study = -1
        self.study_instance_uids = {
            1: '1.2.276.0.33.1.0.4.192.168.56.148.20200331.1192945.88622.2',
            2: '1.2.276.0.18.14.200.2.0.0.2.20210415.90634.95.48',
            3: '1.2.826.0.1.3680043.10.94.20210505100455',
            4: '1.3.6.1.4.1.24930.2.64834516866074.1587242',
            5: '1.2.276.0.18.14.200.2.0.0.2.20210420.155835.67.94',
            6: '1.3.46.670589.5.2.10.2156913941.892665384.993397',
            7: '1.3.6.1.4.1.24930.2.64870186785082.1744998',
            8: '1.2.276.0.33.1.0.4.192.168.56.148.20200323.1175751.86602.2'
        }
        self.accession_numbers = {
            1: 'KNI_0002',
            2: '1344182',
            3: 'KOB6DJV28C',
            4: 'SCH_0001',
            5: '1345229',
            6: '',
            7: '',
            8: 'LWS_0002'
        }
        self.patient_ids = {
            1: 'KNI0001',
            2: '370142',
            3: '21',
            4: 'SCH0001',
            5: '43549',
            6: '0009703828',
            7: 'PID_4711',
            8: 'LWS0001'
        }
        self.prompt_study()
        self.prompt_variant()

    def prompt_study(self):
        input_string = input('''
    Studie auswählen (Enter für Studie 1):
      1 - Knie^Routine Knie / Knie^Hilde^
      2 - MR LWS / Fachtan^Andreas
      3 - UNDEFINED / ROSE^RAPHAEL
      4 - Schulter_^Routine+ / Schulter^Peter^
      5 - MR Knie li. / Neubig^Detlef
      6 - HEAD EXP2 -> fehlende Pflichtfelder
      7 - Schulter_^Routine+ / Schulter^Sabine^
      8 - Wirbelsäule^Routine LWS / Wirbel-Säule^Lemmi^
    
    Eingabe: ''')

        if not input_string:
            input_string = '1'
        self.study = int(input_string)
        if self.study < 1 or self.study > 8:
            raise Exception('Ungültige Eingabe für Studie')

    def prompt_variant(self):
        self.prompt = '''
    Variante auswählen (exit zum Verlassen):
      1 - StudyInstanceUid only
      2 - AccessionNumber only
      3 - PatientId + StudyInstanceUid + AccessionNumber
      4 - PatientId + StudyInstanceUid
      5 - PatientId + AccessionNumber
      6 - PatientId only
    
    Eingabe: '''

    def do_1(self, _):
        self.start_app(f'--studyInstanceUid={self.get_study_instance_uid()}')

    def do_2(self, _):
        self.start_app(f'--accessionNumber={self.get_accession_number()}')

    def do_3(self, _):
        self.start_app(f'--patientId={self.get_patient_id()}', f'--studyInstanceUid={self.get_study_instance_uid()}',
                       f'--accessionNumber={self.get_accession_number()}')

    def do_4(self, _):
        self.start_app(f'--patientId={self.get_patient_id()}', f'--studyInstanceUid={self.get_study_instance_uid()}')

    def do_5(self, _):
        self.start_app(f'--patientId={self.get_patient_id()}', f'--accessionNumber={self.get_accession_number()}')

    def do_6(self, _):
        self.start_app(f'--patientId={self.get_patient_id()}')

    def do_exit(self, _):
        print('\nTschüss')
        return True

    def start_app(self, *params):
        subprocess.run([self.executable, *params])

    def get_study_instance_uid(self):
        return self.study_instance_uids[self.study]

    def get_accession_number(self):
        return self.accession_numbers[self.study]

    def get_patient_id(self):
        return self.patient_ids[self.study]


if __name__ == "__main__":
    ImportCmd().cmdloop()
