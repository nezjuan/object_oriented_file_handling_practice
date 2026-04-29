import random
import os

class RandomStudentGenerator:
    def __init__(self, base_dir):
        self.base_dir = base_dir

    def student_gwa_txt(self):
        with open(os.path.join(self.base_dir, "students_GWA.txt"), "w") as studs_GWA:
            gwa_scores = ["1.0","1.5","2.0","2.5","3.0","3.5","4.0"]
            studs_name = ["Garen Crownguard","Luxanna Crownguard","Jericho Swain",
                "Jarno Lightfeather","Ambessa Medarda","Annie Hastur",
                "Cassiopeia Du Couteau","Cecil B. Heimerdinger","Irelia Lito",
                "Jarvan Lightshield","Khada Jhin","Katarina Du Couteau",
                "Caitlyn Kiramman","Jayce Tallis","Sarah Fortune","Tobias Foxtrot",
                "Mel Medarda","Renata Glasc","Fiora Laurent","Ambessa Medarda"]
            
            random.shuffle(studs_name)
            for name in studs_name:
                gwa = random.choice(gwa_scores)
                studs_GWA.write(f"{name} - GWA: {gwa}\n")