
class Employee:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def send_email(self, subject, message, email):
        print(f"Sending email to {email}")
        print(f"Subject: {subject}")
        print(f"Message: {message}")

    def information(self, subject,message,  email):
        self.send_email(subject, message, email)

    def display_info():
        print(f"{self.name}  are emailul :  {self.email}")

class SalesManager(Employee):
    def __init__(self, name, email, sales_target):
        super().__init__(name, email)
        self.sales_target = sales_target

    def track_sales(self):
        print(f"{self.name} is tracking the target of {self.sales_target}")

    def information(self, coleague, subject, message, email):
        super().information(subject, message, email)
        print(f"Sales target for this quarter : {self.sales_target}")
        self.track_sales()

    def display_info(self):
        super().display_info()
        print(f"the sames should be {self.sales_target}")
        
class DataAnalyst(Employee):
    def __init__(self, name, email, analysis_tool):
        super().__init__(name, email)
        self.analysis_tool = analysis_tool

    def analyze_data(self):
        print(f"{self.name} is analyzing stuff with {self.analysis_tool}")

    def information(self, subject, message, email):
        super().send_email(subject, message, email)
        self.analyze_data()

class Intern(Employee):
    def __init__(self, name, email, project):
        super().__init__(name, email)
        self.project = project

    def work_on_progress(self):
        print(f"{self.name} is working on {self.project}")

    def information(self, subject, message, email):
        super().send_email(subject, message , email)
        print(f"Project assigned: {self.project}")
        self.work_on_progress()

class MarketingManager(Employee):
    def __init__(self, name, email, campaing_budget):
        super().__init__(name, email)
        self.camapaign_budget = campaing_budget
        

if __name__ == "__main__":
    analizator = DataAnalyst("jorj", "jorj@jorj.com", analysis_tool= "excel")
    analizator.analyze_data()
    analizator.send_email("write", "we writin'", "undeva@gmal.com")
    analizator.information("de munca", "avem de treaba", "undeva@gemai.com")


    the_intern = Intern("costel", "costica@jorj.com", "munca lui")
    the_intern.send_email("de munca", "avem de treaba", "undeva@gemai.com")
    the_intern.work_on_progress()
    the_intern.information("de munca", "avem de treaba", "undeva@gemai.com")

    manag = SalesManager("ghiorghe", "ghiorghe@jorj.com", 200)
    manag.information(analizator.name, "aicic e munca", "manca boss", email=analizator.email)