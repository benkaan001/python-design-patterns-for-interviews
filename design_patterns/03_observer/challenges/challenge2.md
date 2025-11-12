# Challenge: Job Posting Alert System

## 📝 Scenario

You are developing the backend for a professional job board application. When a new job is successfully posted by a company, several different parts of your system need to react to this event, including sending alerts to users, updating internal analytics, and potentially triggering sponsored ads.

You must ensure that the core **Job Board** logic (the Subject) is completely decoupled from *how* these services react (the Observers). If you add a new service (like a machine learning recommendation engine), the `JobBoard` class should not need to be modified.

## 🚀 Your Task

Implement a system using the **Observer Pattern** to manage the publication of new job postings.

### Requirements:

1. **Product/Event Structure:** Define a simple class or dictionary structure for a `JobPost` containing `title`, `company`, and `salary` (string or float).
2. **Publisher (Subject):**
   * Define a class `JobBoard` that acts as the Concrete Subject.
   * It must manage a list of registered observers.
   * It must have a method `post_job(job: JobPost)` which updates its internal state (the latest job posted) and calls `notify_subscribers()`.
3. **Subscriber (Observer):**
   * Define an abstract class `JobSubscriber` with an abstract method `receive_update(job: JobPost) -> None`. (Use the  **Push Model** ).
4. **Concrete Subscribers (3 Types):**
   * `EmailAlerter`: Prints a confirmation email is sent: `"EmailAlerter: Sending job alert for '{title}' to all users."`
   * `AnalyticsTracker`: Prints a message indicating a database update: `"AnalyticsTracker: Logging new job posting data for {company}."`
   * `SponsorAdvertiser`: Reacts only to high-salary jobs: If `salary` is over $150,000, it prints `"SponsorAdvertiser: Activating ad campaign for high-value job: {title}."` (Otherwise, it prints a simple tracking message).
5. **Test Harness:** Write a usage block (`if __name__ == "__main__":`) that demonstrates:
   * Registering all three observers.
   * Posting a low-salary job.
   * Posting a high-salary job (triggering the `SponsorAdvertiser`).
   * Unsubscribing the `EmailAlerter`.
   * Posting another job (where the `EmailAlerter` is correctly ignored).

## 💡 Hints:

* You do not need to define separate abstract interfaces for Subject/Publisher this time, but the methods (`register`, `remove`, `notify`) are mandatory on the `JobBoard`.
* Ensure all three observers are correctly notified for standard posts, and that the `SponsorAdvertiser` applies its conditional logic.

Good luck!
