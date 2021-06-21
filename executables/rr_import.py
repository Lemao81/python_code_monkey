import cmd
import subprocess


class ImportCmd(cmd.Cmd):
    def __init__(self):
        super().__init__()
        self.executable = 'C:\\ProgramData\\RadioReport\\RadioReport.exe'
        self.prompt = '''
        CFind:
          StudyInstanceUid only:
            1 - Fachtan^Andreas
            2 - Knie^Hilde^
        
          AccessionNumber only:
            10 - Fachtan^Andreas
            11 - Knie^Hilde^
          
          PatientId + StudyInstanceUid:
            20 - Fachtan^Andreas
            21 - Knie^Hilde^
          
          PatientId + AccessionNumber:
            30 - Fachtan^Andreas
            31 - Knie^Hilde^
          
          PatientId + StudyInstanceUid + AccessionNumber:
            40 - Fachtan^Andreas
            41 - Knie^Hilde^
          
          PatientId only:
            50 - Fachtan^Andreas
            51 - Knie^Hilde^
            
          Missing required fields:
            60 - HEAD EXP2
        
        CMove:
          StudyInstanceUid only:
            100 - Fachtan^Andreas
            101 - Knie^Hilde^
            
        Eingabe (exit zum Beenden): '''

    def do_exit(self, _):
        print('Tschüss')
        return True

    def do_1(self, _):
        self.start_app('--studyInstanceUid=1.2.276.0.18.14.200.2.0.0.2.20210415.90634.95.48')

    def do_10(self, _):
        self.start_app('--accessionNumber=1344182')

    def do_20(self, _):
        self.start_app('--patientId=370142', '--studyInstanceUid=1.2.276.0.18.14.200.2.0.0.2.20210415.90634.95.48')

    def do_30(self, _):
        self.start_app('--patientId=370142', '--accessionNumber=1344182')

    def do_40(self, _):
        self.start_app('--patientId=370142', '--studyInstanceUid=1.2.276.0.18.14.200.2.0.0.2.20210415.90634.95.48', '--accessionNumber=1344182')

    def do_50(self, _):
        self.start_app('--patientId=370142')

    def do_60(self, _):
        self.start_app('--studyInstanceUid=1.3.46.670589.5.2.10.2156913941.892665384.993397')

    def start_app(self, *params):
        subprocess.run([self.executable, *params])


if __name__ == "__main__":
    ImportCmd().cmdloop()
