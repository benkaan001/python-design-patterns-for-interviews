# 02. Factory Method Pattern

## 🎯 Type

Creational Design Pattern

## 🤔 The "Why": Problem Solved

Imagine you're building a system that needs to create different types of objects, but the exact type of object to create isn't known until runtime, or you want to decouple the client code (the code that *uses* the objects) from the concrete classes it instantiates.

**Common Scenarios:**

* **Cross-Platform UI:** Creating OS-specific UI elements (buttons, checkboxes) without the client code knowing the concrete OS implementation.
* **Document Converters:** Generating different document types (PDF, Word, Spreadsheet) based on user input or configuration.
* **Notification System:** Sending notifications via different channels (Email, SMS, Push) where the dispatching logic is independent of the channel specifics.
* **Game Development:** Spawning different types of enemies or characters based on game level or player choice.

The naive approach would involve direct instantiation of concrete classes within the client code, often leading to:

* **Tight Coupling:** The client code becomes tightly coupled to specific concrete classes. Adding a new product type requires modifying the client. This violates the  **Open/Closed Principle** .
* **Lack of Flexibility:** It's hard to change the type of object created without modifying the client code.
* **Code Duplication:** Object creation logic might be duplicated across various parts of the application.

The Factory Method pattern solves this by **delegating the object creation process to subclasses** or dedicated "factory" methods, allowing the client code to work with an *interface* or *abstract class* rather than concrete implementations.

## 💡 The "What": Pattern Explanation

The Factory Method is a **creational design pattern** that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created. It's about letting a class defer instantiation to subclasses.

### Key Components:

1. **Product (Interface/Abstract Class):**
   * Declares the interface for the objects the factory method creates. All concrete products will implement this.
   * *Example:* `UIElement`, `Notification`.
2. **Concrete Product:**
   * Implements the `Product` interface. These are the actual objects being created.
   * *Example:* `WindowsButton`, `EmailNotification`.
3. **Creator (Abstract Class/Interface):**
   * Declares the abstract factory method, which returns an object of the `Product` type.
   * It might also define other concrete operations that use the factory method. This class doesn't know *which* concrete product it will create.
   * *Example:* `UIElementCreator`, `NotificationCreator`.
4. **Concrete Creator:**
   * Overrides the factory method to return an instance of a specific `Concrete Product`.
   * *Example:* `WindowsCreator`, `EmailNotificationCreator`.

### Benefits:

* **Loose Coupling:** The client code depends only on the `Product` and `Creator` interfaces, not on concrete classes. This means the client doesn't care *how* the product is created, just that it *is* a `Product`.
* **Extensibility (Open/Closed Principle):** You can introduce new `Concrete Product` types and new `Concrete Creator` types without modifying existing client code.
* **Centralized Creation Logic:** The logic for deciding which concrete product to instantiate is encapsulated within the `Concrete Creator`'s factory method, avoiding duplication in client code.
* **Improved Testability:** Concrete Products and Creators can be tested in isolation.

### When to Use / Avoid:

* **Use when:**
  * A class can't anticipate the class of objects it must create.
  * A class wants its subclasses to specify the objects it creates.
  * You want to avoid hard-coding application-specific classes into your code.
  * You need to provide a framework where users can extend it with their own product types.
* **Avoid when:**
  * The object creation process is simple and doesn't require abstraction.
  * You only have one type of product, and it's unlikely to change or have variants.

## 🐍 Initial Example (Python): Document Creator

Here's a simplified example of creating different types of documents, demonstrating the core components of the Factory Method pattern.

```py
from abc import ABC, abstractmethod

# 1. Product (Abstract Class)
class Document(ABC):
    @abstractmethod
    def display(self) -> str:
        pass

# 2. Concrete Products
class PDFDocument(Document):
    def display(self) -> str:
        return "Displaying PDF Document."

class WordDocument(Document):
    def display(self) -> str:
        return "Displaying Word Document."

class SpreadsheetDocument(Document):
    def display(self) -> str:
        return "Displaying Spreadsheet Document."

# 3. Creator (Abstract Class)
class DocumentCreator(ABC):
    @abstractmethod
    def create_document(self) -> Document:
        """The Factory Method: Abstract method to create a document."""
        pass

    def open_and_display_document(self) -> str:
        """
        An operation that uses the factory method.
        This method doesn't care about the concrete type of document,
        only that it's a Document.
        """
        document = self.create_document() # The factory method is called here
        result = f"Opening: {document.display()}"
        return result

# 4. Concrete Creators
class PDFCreator(DocumentCreator):
    def create_document(self) -> Document:
        return PDFDocument()

class WordCreator(DocumentCreator):
    def create_document(self) -> Document:
        return WordDocument()

class SpreadsheetCreator(DocumentCreator):
    def create_document(self) -> Document:
        return SpreadsheetDocument()

# --- Usage (Client Code) ---
def client_code(creator: DocumentCreator):
    """
    The client code works with an instance of a concrete creator,
    but it only expects it to implement the DocumentCreator interface.
    """
    print(f"Client: I'm not aware of the creator's class, but it works with '{creator.__class__.__name__}'.")
    print(f"{creator.open_and_display_document()}")

if __name__ == "__main__":
    print("App: Launching PDF application.")
    client_code(PDFCreator())

    print("\nApp: Launching Word application.")
    client_code(WordCreator())

    print("\nApp: Launching Spreadsheet application.")
    client_code(SpreadsheetCreator())

    # Adding a new document type doesn't require changing client_code()
    class PresentationDocument(Document):
        def display(self) -> str:
            return "Displaying Presentation Document."

    class PresentationCreator(DocumentCreator):
        def create_document(self) -> Document:
            return PresentationDocument()

    print("\nApp: Launching Presentation application (new feature, no client code change).")
    client_code(PresentationCreator())

```
