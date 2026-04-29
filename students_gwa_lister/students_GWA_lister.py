import random

with (open("./students_GWA.txt","w")) as studs_GWA:
    gwa_scores=["1.0","1.5","2.0","2.5","3.0","3.5","4.0"]
    studs_name=["Garen Crownguard", "Luxanna Crownguard", "Jericho Swain",
        "Jarro Lightfeather", "Ambessa Medarda", "Annie Hastur",
        "Cassiopeia Du Couteau", "Cecil B. Heimerdinger", "Irelia Lito",
        "Jarvan Lightshield", "Khada Jhin", "Katarina Du Couteau",
        "Caitlyn Kirraman", "Jayce Talis", "Sarah Fortune","Tobias Foxtrot",
        "Mel Medarda", "Renata Glasc", "Fiora Laurent","Ambessa Medarda"]
    for line in range(20):
        studs_GWA.write(f"{random.choice(studs_name)}, GWA: {random.choice(gwa_scores)}\n")