from abc import ABC, abstractmethod
from typing import List

# --- 1. Product/Event Structure ---
class JobPost:
    def __init__(self, title: str, company: str, salary: float) -> None:
        self._title: str = title
        self._company: str = company
        self._salary: float = salary

    @property
    def title(self) -> str:
        return self._title

    @property
    def company(self) -> str:
        return self._company

    @property
    def salary(self) -> float:
        return self._salary

# --- 3. Subscriber (Observer) Interface ---
class JobSubscriber(ABC):
    @abstractmethod
    def receive_update(self, job: JobPost) -> None:
        """Receives the JobPost event (Push Model)."""
        pass

# --- 2. Publisher (Subject) ---
class JobBoard:
    def __init__(self):
        self._observers: List[JobSubscriber] = []

    def register_observer(self, observer: JobSubscriber) -> None:
        if observer not in self._observers:
            self._observers.append(observer)
            print(f"[Board] Registered observer: {observer.__class__.__name__}")

    def remove_observer(self, observer: JobSubscriber) -> None:
        if observer in self._observers:
            self._observers.remove(observer)
            print(f"[Board] Removed observer: {observer.__class__.__name__}")

    def notify_subscribers(self, job: JobPost) -> None:
        print(f"\n[Board] Notifying subscribers about new job: {job.title} ({job.salary:.0f})")
        for observer in self._observers:
            observer.receive_update(job)

    def post_job(self, job: JobPost) -> None:
        """Updates state and triggers notification automatically."""
        self.notify_subscribers(job)

# --- 4. Concrete Subscribers ---
class EmailAlerter(JobSubscriber):
    def receive_update(self, job: JobPost) -> None:
        # Requirement: "EmailAlerter: Sending job alert for '{title}' to all users."
        print(f"EmailAlerter: Sending job alert for '{job.title}' to all users.")

class AnalyticsTracker(JobSubscriber):
    def receive_update(self, job: JobPost) -> None:
        # Requirement: "AnalyticsTracker: Logging new job posting data for {company}."
        print(f"AnalyticsTracker: Logging new job posting data for {job.company}.")

class SponsorAdvertiser(JobSubscriber):
    def receive_update(self, job: JobPost) -> None:
        salary_threshold = 150_000
        if job.salary > salary_threshold:
            # Requirement: High-salary alert
            print(f"SponsorAdvertiser: Activating ad campaign for high-value job: '{job.title}'.")
        else:
            # Requirement: Otherwise, prints a simple tracking message.
            print(f"SponsorAdvertiser: Tracking standard job post.")

# --- 5. Test Harness ---
if __name__ == "__main__":
    job_board = JobBoard()

    # Create observers
    email_alerter = EmailAlerter()
    analytics_tracker = AnalyticsTracker()
    sponsor_advertiser = SponsorAdvertiser()

    # Define jobs
    low_salary_job = JobPost(title="Junior Python Dev", company="Startup X", salary=95_000.00)
    high_salary_job = JobPost(title="Lead Architect", company="BigTech Corp", salary=180_000.00)
    mid_salary_job = JobPost(title="Data Scientist", company="Data Co", salary=125_000.00)

    # 1. Register all three observers
    print("\n--- PHASE 1: Registering All Observers ---")
    job_board.register_observer(email_alerter)
    job_board.register_observer(analytics_tracker)
    job_board.register_observer(sponsor_advertiser)

    # 2. Posting a low-salary job
    print("\n--- PHASE 2: Post Low-Salary Job (Test Standard Alert) ---")
    job_board.post_job(low_salary_job)

    # 3. Posting a high-salary job (triggering SponsorAdvertiser)
    print("\n--- PHASE 3: Post High-Salary Job (Test Conditional Alert) ---")
    job_board.post_job(high_salary_job)

    # 4. Unsubscribing the EmailAlerter
    print("\n--- PHASE 4: Unsubscribe Email Alerter ---")
    job_board.remove_observer(email_alerter)

    # 5. Posting another job (EmailAlerter should be ignored)
    print("\n--- PHASE 5: Post Mid-Salary Job (Verify Unsubscribe) ---")
    job_board.post_job(mid_salary_job)