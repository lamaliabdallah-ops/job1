def time_to_text(minutes):
    heures = minutes // 60
    mins = minutes % 60
    print(f"{heures} heures et {mins} minutes")


time_to_text(150)  
time_to_text(50)
