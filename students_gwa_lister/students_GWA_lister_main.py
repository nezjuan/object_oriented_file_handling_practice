from students_GWA_lister_function import RandomStudentGenerator
import os

base_dir = os.path.dirname(__file__)   # always the main script’s folder
generator = RandomStudentGenerator(base_dir)
generator.student_gwa_txt()

top_gwa = float("inf")
top_stud = None

with open(os.path.join(base_dir, "students_GWA.txt"), "r") as name_gwa:
    for line in name_gwa:
        name, gwa = line.strip().split(" - ")
        gwa = float(gwa.replace("GWA:", "").strip())
        if gwa < top_gwa:
            top_gwa = gwa
            top_stud = name.strip()

with open(os.path.join(base_dir, "honored_student.txt"), "w") as honored_one:
    honored_one.write(f"The Honored One: {top_stud}\nGeneral Weighted Average: {top_gwa}")